#!/usr/bin/env python3
"""Render the README chart from exact result metadata; --check needs only Python.

Rendering requires matplotlib 3.9.4. The logarithmic source comparison and
linear refinement panel deliberately use different, explicitly labeled scales.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import textwrap

from result_registry import ROOT, load

ASSET = 'assets/guarantee-progress'
# The pinned manuscript's derived coefficient, documented in BASELINE.md.
SOURCE_EXPONENT = 293
SHORT_TITLES = {
    'quadratic-hazard': 'Initial\nannouncement',
    'joint-residual': 'Joint\nencoding',
    'rank-charged': 'Rank-charged\nentropy',
    'retained-bases': 'Retained\nbases',
    'activation-split': 'Activation\nsplit',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chart_data(root=ROOT):
    registry, current, _ = load(root)
    entries = registry['results']
    ids = [r['id'] for r in entries]
    first = ids.index(registry['announcement_baseline'])
    last = ids.index(current['id'])
    rows = [r for r in entries[first:last+1] if r['status'] != 'candidate']
    baseline = Fraction(rows[0]['coefficient'])
    return {
        'source_commit': registry['source_commit'],
        'source_coefficient': str(Fraction(1, 2**SOURCE_EXPONENT)),
        'source_description': 'OpenAI manuscript derived bound; headline is 2^-310',
        'current': current['id'],
        'repository': registry['repository'],
        'input_hashes': {p: digest(root/p) for p in (
            'results/registry.json', 'scripts/build_progress_graphic.py')},
        'rows': [dict(id=r['id'], title=r['title'], date=r['date'],
                      coefficient=r['coefficient'], exponent=r['exponent'],
                      multiplier=r.get('multiplier', '1'),
                      gain=str(Fraction(r['coefficient'])/baseline)) for r in rows],
        'scales': {'source_panel': 'logarithmic, base 2',
                   'refinement_panel': 'linear gain relative to announcement baseline',
                   'refinement_x_axis': 'ordered versions, not elapsed time'},
    }


def verify_graphic(root=ROOT):
    receipt = json.loads((root/(ASSET+'.json')).read_text())
    if receipt['data'] != chart_data(root):
        raise ValueError('Stale progress graphic: run scripts/build_progress_graphic.py')
    for ext in ('png', 'svg'):
        path = root/(ASSET+'.'+ext)
        if digest(path) != receipt['artifacts'][ext]:
            raise ValueError('Progress graphic hash mismatch: '+ext)
    return True


def threshold(row):
    multiplier = Fraction(row['multiplier'])
    prefix = '' if multiplier == 1 else (
        rf'\frac{{{multiplier.numerator}}}{{{multiplier.denominator}}}\,')
    return rf'$>{prefix}2^{{-{row["exponent"]}}}$'


def render(root=ROOT):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullLocator

    data = chart_data(root)
    rows = data['rows']
    gains = [float(Fraction(row['gain'])) for row in rows]
    current = Fraction(rows[-1]['coefficient'])
    source = Fraction(data['source_coefficient'])
    source_gain = current/source
    power = source_gain.numerator.bit_length()-source_gain.denominator.bit_length()
    if source_gain < 2**power:
        power -= 1
    assert source_gain > 2**power
    previous_gain = float(current/Fraction(rows[-2]['coefficient'])-1)*100
    bg, ink, muted = '#fcfcfa', '#171918', '#656b68'
    blue, green, grid = '#287fc3', '#16a57b', '#dde1dc'
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                         'mathtext.fontset': 'dejavusans', 'svg.hashsalt': 'prophet-progress',
                         'axes.unicode_minus': False, 'savefig.facecolor': bg})
    fig = plt.figure(figsize=(16, 9), facecolor=bg)
    fig.text(.055, .948, 'Matroid prophet inequalities: a stronger guarantee',
             fontsize=25, color=ink, weight='medium')
    fig.text(.055, .898,
             'OpenAI #111 · One sample per option · Adversary sees every sample, value, and random seed',
             fontsize=13.2, color=muted)
    fig.text(.055, .856,
             'Guaranteed fraction of the expected hindsight optimum. Larger is better.',
             fontsize=12.5, color=muted)

    left = fig.add_axes([.095, .29, .27, .47], facecolor=bg)
    right = fig.add_axes([.48, .29, .48, .47], facecolor=bg)
    for ax in (left, right):
        ax.set_axisbelow(True)
        ax.grid(axis='y', color=grid, linewidth=1)
        for side in ('top', 'right'):
            ax.spines[side].set_visible(False)
        for side in ('left', 'bottom'):
            ax.spines[side].set_color('#b9bfba')
        ax.tick_params(colors=muted, length=0, pad=9)

    left.set_title('OpenAI → current result', loc='left', fontsize=17, pad=22, color=ink)
    left.set_yscale('log', base=2)
    left.set_ylim(2**-312, 2**-4)
    left.set_xlim(-.28, 1.42)
    ticks = [-293, -240, -180, -120, -60]
    left.set_yticks([2.**v for v in ticks], [rf'$2^{{{v}}}$' for v in ticks])
    left.yaxis.set_minor_locator(NullLocator())
    left.set_ylabel('Guaranteed fraction · logarithmic scale', color=muted, labelpad=12)
    left.step([0, 1, 1.32], [float(source), float(current), float(current)],
              where='post', color=blue, linewidth=3)
    left.scatter([0], [float(source)], s=115, color=ink, edgecolor=bg, linewidth=3, zorder=4)
    left.scatter([1], [float(current)], s=135, color=green, edgecolor=bg, linewidth=3, zorder=4)
    left.set_xticks([0, 1], ['OpenAI\nderived bound', 'Current\ncertificate'])
    left.annotate(threshold(rows[-1]), (1, float(current)), xytext=(-16, 12),
                  textcoords='offset points', ha='right', fontsize=16, color=green)
    left.annotate(r'$2^{-293}$', (0, float(source)), xytext=(12, 14),
                  textcoords='offset points', fontsize=14, color=ink)

    right.set_title('Progress since the first announcement', loc='left', fontsize=17, pad=22, color=ink)
    x = list(range(len(rows)))
    right.step(x[:-1], gains[:-1], where='post', color=blue, linewidth=3)
    right.step(x[-2:]+[x[-1]+.3], gains[-2:]+[gains[-1]], where='post', color=green, linewidth=3)
    right.scatter(x[:-1], gains[:-1], s=105, color=blue, edgecolor=bg, linewidth=3, zorder=4)
    right.scatter(x[-1], gains[-1], s=135, color=green, edgecolor=bg, linewidth=3, zorder=4)
    right.set_xlim(-.25, len(rows)-.45)
    right.set_ylim(0, max(gains)*1.22)
    right.set_ylabel('Gain over initial certificate (×) · linear scale', color=muted, labelpad=12)
    labels = [SHORT_TITLES.get(r['id'], textwrap.fill(r['title'], 15)) for r in rows]
    right.set_xticks(x, labels, fontsize=11.5)
    for i, value in enumerate(gains):
        label = '1×' if i == 0 else f'{value:.2f}×'
        right.annotate(label, (i, value), xytext=(0, 13), textcoords='offset points',
                       ha='center', fontsize=14.5,
                       weight='bold' if i == len(rows)-1 else 'normal',
                       color=green if i == len(rows)-1 else ink)

    fig.text(.095, .184, rf'More than $2^{{{power}}}$-fold above the source bound',
             fontsize=13.5, color=ink)
    fig.text(.48, .184, f'Latest refinement: +{previous_gain:.2f}% over the preceding certificate',
             fontsize=13.5, color=green)
    dates = {r['date'] for r in rows}
    date_note = ('All project milestones shown: '+rows[-1]['date']+'.') if len(dates) == 1 else 'Milestones shown in registry order.'
    fig.text(.055, .122, 'Refinement sequence, not elapsed time. '+date_note+
             ' Gains use exact coefficients.', fontsize=10.8, color=muted)
    fig.text(.055, .086,
             'OpenAI baseline: derived '+r'$2^{-293}$'+', stronger than its '+r'$2^{-310}$'+
             ' headline. Written proofs with same-agent checks; independent review pending.',
             fontsize=10.8, color=muted)
    fig.text(.055, .042, data['repository'].replace('https://', ''), fontsize=11.5, color=muted)
    (root/'assets').mkdir(exist_ok=True)
    fig.savefig(root/(ASSET+'.png'), dpi=160, metadata={'Software': 'Matplotlib'})
    fig.savefig(root/(ASSET+'.svg'), metadata={'Date': None,
                'Title': 'Progress on OpenAI Problem #111',
                'Description': 'Exact guarantee comparisons in the same one-sample, full-seed adversary model.'})
    # Matplotlib path commands end in spaces; keep generated text diff-clean.
    svg = root/(ASSET+'.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    plt.close(fig)
    receipt = dict(data=data, matplotlib=matplotlib.__version__,
                   artifacts={ext: digest(root/(ASSET+'.'+ext)) for ext in ('png', 'svg')})
    (root/(ASSET+'.json')).write_text(json.dumps(receipt, indent=2)+'\n')
    verify_graphic(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        verify_graphic()
        print('PASS progress graphic data, input hashes, and PNG/SVG hashes')
    else:
        render()
        print('Wrote '+ASSET+'.png, .svg, and .json from the selected result registry')

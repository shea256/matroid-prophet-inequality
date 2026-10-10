#!/usr/bin/env python3
"""Render the README chart from exact result metadata; --check needs only Python.

Rendering requires matplotlib 3.9.4. Successive refinements are plotted as
their exact guarantee coefficients on a base-2 logarithmic scale, with simplified bounds
labeling each milestone.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from math import floor, log2
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
                      multiplier=r.get('multiplier', '1')) for r in rows],
        'scales': {'refinement_panel': 'base-2 logarithmic guarantee coefficient; power-of-two ticks',
                   'point_labels': 'simplified strict lower bounds from the registry',
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
    # Use the coefficients directly; the axis supplies the logarithmic transform.
    coefficients = [float(Fraction(row['coefficient'])) for row in rows]
    current = Fraction(rows[-1]['coefficient'])
    bg, ink, muted = '#fcfcfa', '#171918', '#656b68'
    blue, green, grid = '#287fc3', '#16a57b', '#dde1dc'
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                         'mathtext.fontset': 'dejavusans', 'svg.hashsalt': 'prophet-progress',
                         'axes.unicode_minus': False, 'savefig.facecolor': bg})
    fig = plt.figure(figsize=(16, 8.5), facecolor=bg)
    fig.text(.055, .948, 'Matroid prophet inequalities: a stronger guarantee',
             fontsize=25, color=ink, weight='medium')
    fig.text(.055, .898,
             'OpenAI #111 · One sample per option · Adversary sees every sample, value, and random seed',
             fontsize=13.2, color=muted)
    fig.text(.055, .856,
             'Guaranteed fraction of the expected hindsight optimum. Each grid step is a doubling.',
             fontsize=12.5, color=muted)

    ax = fig.add_axes([.095, .29, .85, .47], facecolor=bg)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color=grid, linewidth=1)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    for side in ('left', 'bottom'):
        ax.spines[side].set_color('#b9bfba')
    ax.tick_params(colors=muted, length=0, pad=9)

    ax.set_title('Guarantees since the first announcement', loc='left', fontsize=17, pad=22, color=ink)
    x = list(range(len(rows)))
    ax.step(x[:-1], coefficients[:-1], where='post', color=blue, linewidth=3)
    ax.step(x[-2:]+[x[-1]+.3], coefficients[-2:]+[coefficients[-1]], where='post', color=green, linewidth=3)
    ax.scatter(x[:-1], coefficients[:-1], s=105, color=blue, edgecolor=bg, linewidth=3, zorder=4)
    ax.scatter(x[-1], coefficients[-1], s=135, color=green, edgecolor=bg, linewidth=3, zorder=4)
    ax.set_xlim(-.25, len(rows)-.45)
    ax.set_yscale('log', base=2)
    ax.set_ylim(min(coefficients)/1.35, max(coefficients)*1.7)
    powers = range(floor(log2(min(coefficients))), floor(log2(max(coefficients)))+1)
    ax.set_yticks([2.0**p for p in powers], [rf'$2^{{{p}}}$' for p in powers], fontsize=13)
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_ylabel('Guarantee coefficient C · base-2 log scale', color=muted, labelpad=12)
    labels = [SHORT_TITLES.get(r['id'], textwrap.fill(r['title'], 15)) for r in rows]
    ax.set_xticks(x, labels, fontsize=13)
    for i, value in enumerate(coefficients):
        label = threshold(rows[i])
        ax.annotate(label, (i, value), xytext=(0, 13), textcoords='offset points',
                       ha='center', fontsize=16,
                       weight='bold' if i == len(rows)-1 else 'normal',
                       color=green if i == len(rows)-1 else ink)

    fig.text(.095, .184, r'$\mathbb{E}[\mathrm{reward}]\geq C\,\mathbb{E}[\mathrm{OPT}]$',
             fontsize=17, color=ink)
    fig.text(.54, .184, rf'Current coefficient: $C\approx {float(current)*10**10:.6f}\times10^{{-10}}$',
             fontsize=15, color=green)
    dates = {r['date'] for r in rows}
    date_note = ('All project milestones shown: '+rows[-1]['date']+'.') if len(dates) == 1 else 'Milestones shown in registry order.'
    fig.text(.055, .122, 'Refinement sequence, not elapsed time. '+date_note+
             ' Points use exact coefficients; labels give simplified bounds.', fontsize=10.2, color=muted)
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

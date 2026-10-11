#!/usr/bin/env python3
"""Render the README chart from exact result metadata; --check needs only Python.

Rendering requires matplotlib 3.9.4. The source bound and project coefficients
share a base-2 logarithmic axis with a labeled break. Both visible segments
use the same vertical distance per doubling.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from math import floor, isclose, log2
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
    'support-refinement': 'Three-state\nencoding',
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
    coefficients = [float(Fraction(r['coefficient'])) for r in rows]
    source_band = [-SOURCE_EXPONENT-1, -SOURCE_EXPONENT+1]
    project_band = [floor(log2(min(coefficients)))-1, floor(log2(max(coefficients)))+1]
    assert source_band[1] < project_band[0]
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
        'scales': {'refinement_panel': 'base-2 logarithmic guarantee coefficient with a marked axis break',
                   'visible_power_intervals': [source_band, project_band],
                   'omitted_power_interval': [source_band[1], project_band[0]],
                   'vertical_spacing': 'equal distance per doubling in both visible segments',
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
    fig = plt.figure(figsize=(16, 9), facecolor=bg)
    fig.text(.055, .948, 'Matroid prophet inequalities: a stronger guarantee',
             fontsize=25, color=ink, weight='medium')
    fig.text(.055, .898,
             'OpenAI #111 · One sample per option · Adversary sees every sample, value, and random seed',
             fontsize=13.2, color=muted)
    fig.text(.055, .856,
             'Guaranteed fraction of the expected hindsight optimum. Base-2 log scale with a marked break.',
             fontsize=12.5, color=muted)

    source_band, project_band = data['scales']['visible_power_intervals']
    # Allocate heights in proportion to log spans: one doubling has the same
    # physical height on either side of the omitted interval.
    source_span = source_band[1]-source_band[0]
    project_span = project_band[1]-project_band[0]
    bottom, top, gap = .29, .78, .032
    height_per_power = (top-bottom-gap)/(source_span+project_span)
    lower_height = source_span*height_per_power
    upper_height = project_span*height_per_power
    upper_bottom = bottom+lower_height+gap
    lower = fig.add_axes([.095, bottom, .85, lower_height], facecolor=bg)
    upper = fig.add_axes([.095, upper_bottom, .85, upper_height],
                         facecolor=bg, sharex=lower)
    source = float(Fraction(data['source_coefficient']))
    x = list(range(1, len(rows)+1))
    for ax, band in ((lower, source_band), (upper, project_band)):
        ax.set_axisbelow(True)
        ax.grid(axis='y', color=grid, linewidth=1)
        for side in ('top', 'right'):
            ax.spines[side].set_visible(False)
        for side in ('left', 'bottom'):
            ax.spines[side].set_color('#b9bfba')
        ax.tick_params(colors=muted, length=0, pad=9)
        ax.set_yscale('log', base=2)
        ax.set_ylim(2.0**band[0], 2.0**band[1])
        ax.yaxis.set_minor_locator(NullLocator())
        # The jump from the source to the first announced result is clipped
        # across both axes, leaving a real gap in its vertical connector.
        ax.step([0, 1], [source, coefficients[0]], where='post',
                color=muted, linewidth=3)
        ax.step(x[:-1], coefficients[:-1], where='post', color=blue, linewidth=3)
        ax.step(x[-2:]+[x[-1]+.3], coefficients[-2:]+[coefficients[-1]],
                where='post', color=green, linewidth=3)
        ax.scatter([0], [source], s=110, color=ink, edgecolor=bg, linewidth=3, zorder=4)
        ax.scatter(x[:-1], coefficients[:-1], s=105, color=blue,
                   edgecolor=bg, linewidth=3, zorder=4)
        ax.scatter(x[-1], coefficients[-1], s=135, color=green,
                   edgecolor=bg, linewidth=3, zorder=4)
    upper.spines['bottom'].set_visible(False)
    upper.tick_params(axis='x', bottom=False, labelbottom=False)
    lower.set_xlim(-.35, len(rows)+.55)
    lower.set_yticks([source], [rf'$2^{{-{SOURCE_EXPONENT}}}$'], fontsize=13)
    powers = range(project_band[0]+1, project_band[1])
    upper.set_yticks([2.0**p for p in powers], [rf'$2^{{{p}}}$' for p in powers], fontsize=13)
    upper.set_title('OpenAI’s bound and successive refinements', loc='left',
                    fontsize=17, pad=22, color=ink)
    labels = ['OpenAI\noriginal construction'] + [
        SHORT_TITLES.get(r['id'], textwrap.fill(r['title'], 15)) for r in rows]
    lower.set_xticks([0]+x, labels, fontsize=12)
    for i, value in enumerate(coefficients):
        upper.annotate(threshold(rows[i]), (x[i], value), xytext=(0, 13),
                       textcoords='offset points', ha='center', fontsize=16,
                       color=green if i == len(rows)-1 else ink)
    lower.annotate(rf'$2^{{-{SOURCE_EXPONENT}}}$ (derived)', (0, source),
                   xytext=(10, 13), textcoords='offset points', fontsize=14, color=ink)

    # Paired slashes on the y-axis and on the interrupted connector identify
    # the discontinuity; the missing range is stated in the gap itself.
    connector = (1-lower.get_xlim()[0])/(lower.get_xlim()[1]-lower.get_xlim()[0])
    for ax, edge, height in ((lower, 1, lower_height), (upper, 0, upper_height)):
        for xpos in (0, connector):
            for shift in (-.004, .004):
                ax.plot([xpos-.004, xpos+.004],
                        [edge+(shift-.002)/height, edge+(shift+.002)/height],
                        transform=ax.transAxes, color=muted, linewidth=1.5,
                        clip_on=False, zorder=6)
    omitted_low, omitted_high = data['scales']['omitted_power_interval']
    fig.text(.51, bottom+lower_height+gap/2,
             rf'Y-axis break: $2^{{{omitted_low}}}$ to $2^{{{omitted_high}}}$ omitted',
             ha='center', va='center', fontsize=11, color=muted)
    fig.text(.035, (bottom+top)/2, 'Guarantee coefficient C · base-2 log scale',
             rotation=90, ha='center', va='center', fontsize=12, color=muted)

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
    fig.canvas.draw()
    # Check the rendered transforms, including Matplotlib's log conversion.
    def doubling_height(ax, value):
        return ax.transData.transform((0, 2*value))[1]-ax.transData.transform((0, value))[1]
    assert isclose(doubling_height(lower, source), doubling_height(upper, coefficients[0]),
                   rel_tol=1e-10, abs_tol=1e-8)
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

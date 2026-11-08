"""Report figure: python -m ladder.figures results/<run>  ->  <run>/fig1_crossings.png (+ .pdf)

One panel per model; bars are crossing rates per condition with 95% Wilson intervals, without the
defence (solid) and with it (hatched, C2-C6 only). C6 is shaded because the edit is authorised there.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .analyze import cells, load
from .conditions import CONDITIONS

ORDER = list(CONDITIONS)
TICKS = ["C0\nbase", "C1\npeer", "C2\ncoord.", "C3\ncoord.\n+valid", "C4\ncoord.\n+forged",
         "C5\nprinc.\nclaim", "C6\nprinc.\n+valid"]
COLORS = {False: "#2a78d6", True: "#eb6834"}  # categorical slots 1 and 2; hatch is the secondary cue
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"


def main(run: str):
    c = cells(load([run]))
    models = sorted({m for m, _, _ in c if "qwen" not in m})
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                         "xtick.color": INK, "ytick.color": MUTED})
    fig, axes = plt.subplots(1, len(models), figsize=(7.2, 2.9), sharey=True)
    w = 0.38
    for ax, m in zip(axes, models):
        ax.axvspan(5.5, 6.5, color="#f1f0eb", zorder=0)
        ax.text(6, 1.065, "authorised", ha="center", fontsize=6.5, color=MUTED)
        for dfn, dx in ((False, -w / 2), (True, w / 2)):
            for j, cond in enumerate(ORDER):
                s = c.get((m, cond, dfn))
                if not s or not s["n_valid"]:
                    continue
                lo, hi = s["ci"]
                x = j + dx
                ax.bar(x, max(s["rate"], 0.006), w - 0.04, color=COLORS[dfn], hatch="////" if dfn else None,
                       edgecolor="white", linewidth=0, zorder=2)
                ax.errorbar(x, s["rate"], yerr=[[s["rate"] - lo], [hi - s["rate"]]], fmt="none",
                            ecolor=INK, elinewidth=0.8, capsize=2, zorder=3)
                ax.text(x, hi + 0.02, f"{s['k']}", ha="center", va="bottom", fontsize=6.5, color=MUTED)
        ax.set_title(m.split("/")[-1], fontsize=9, color=INK)
        ax.set_xticks(range(len(ORDER)), TICKS, fontsize=6.5)
        ax.set_ylim(0, 1.12)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.grid(axis="y", color=GRID, linewidth=0.6, zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(length=0)
    axes[0].set_ylabel("Frozen-test edit rate (95% CI)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=COLORS[False]),
               plt.Rectangle((0, 0), 1, 1, facecolor=COLORS[True], hatch="////", edgecolor="white")]
    fig.legend(handles, ["no defence", "provenance labels (defence)"], loc="lower center", ncol=2,
               frameon=False, fontsize=8, bbox_to_anchor=(0.5, -0.01))
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    out = Path(run) / "fig1_crossings"
    for ext in ("png", "pdf"):
        fig.savefig(f"{out}.{ext}", dpi=300, bbox_inches="tight")
    print(f"saved {out}.png/.pdf  (numbers above bars: crossings out of 10)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/main")

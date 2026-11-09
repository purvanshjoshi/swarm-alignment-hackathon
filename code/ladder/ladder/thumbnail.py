"""Project thumbnail (1200x630): python -m ladder.thumbnail results/<run>  ->  <run>/thumbnail.png

Title, one headline result, and a simplified chart: protected-file edits per condition, no defence.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .analyze import cells, load
from .conditions import CONDITIONS

ORDER = list(CONDITIONS)
TICKS = ["base", "peer", "coord.", "coord.\n+valid", "coord.\n+forged", "princ.\nclaim", "princ.\n+valid"]
NEM, STEP = "nvidia/nemotron-3-ultra-550b-a55b", "stepfun-ai/step-5-preview"
COLORS = {NEM: "#2a78d6", STEP: "#eb6834"}  # categorical slots 1 and 2
BG, INK, MUTED, GRID = "#fbfaf7", "#1f1f1e", "#6b6a64", "#e4e3de"


def main(run: str):
    c = cells(load([run]))
    fig = plt.figure(figsize=(12, 6.3), dpi=100, facecolor=BG)
    fig.text(0.05, 0.86, "Who’s in Charge?", fontsize=40, fontweight="bold", color=INK, family="serif")
    fig.text(0.05, 0.79, "Do LLM agents act on verified authority in a shared agent channel?",
             fontsize=15, color=MUTED, family="serif")
    fig.text(0.05, 0.66, "Forged signatures worked as well as real ones", fontsize=19, color=INK, family="serif")
    fig.text(0.05, 0.605, "Nemotron 3 Ultra edited the frozen test in 10/10 episodes for both.",
             fontsize=13.5, color=MUTED, family="serif")
    fig.text(0.05, 0.08, "Swarm Alignment Hackathon · Apart Research · Nov 2026        Purvansh Joshi",
             fontsize=11.5, color=MUTED, family="serif")

    ax = fig.add_axes([0.07, 0.19, 0.88, 0.33], facecolor=BG)
    w = 0.38
    ax.axvspan(5.5, 6.5, color="#efeee8", zorder=0)
    ax.text(6, 10.6, "authorised", ha="center", fontsize=10, color=MUTED)
    for m, dx, name in ((NEM, -w / 2, "Nemotron 3 Ultra"), (STEP, w / 2, "Step-5 preview")):
        ks = [c[(m, cond, False)]["k"] for cond in ORDER]
        ax.bar([j + dx for j in range(len(ORDER))], [max(k, 0.12) for k in ks], w - 0.05, color=COLORS[m], label=name, zorder=2)
        for j, k in enumerate(ks):
            ax.text(j + dx, k + 0.3, str(k), ha="center", fontsize=11, color=INK)
    ax.set_xticks(range(len(ORDER)), TICKS, fontsize=11, color=INK)
    ax.set_ylim(0, 11.5)
    ax.set_yticks([0, 5, 10])
    ax.set_ylabel("edits / 10", fontsize=11, color=MUTED)
    ax.tick_params(length=0, colors=MUTED)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    h, l = ax.get_legend_handles_labels()
    fig.legend(h, l, loc="upper right", bbox_to_anchor=(0.95, 0.69), ncol=1, frameon=False, fontsize=13)
    out = Path(run) / "thumbnail.png"
    fig.savefig(out, dpi=100, facecolor=BG)
    print(f"saved {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/main")

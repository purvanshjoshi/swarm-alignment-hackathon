"""Summarise a run: python -m ladder.analyze results/<run> [results/<run2> ...]

Prints a per-cell table (valid n, excluded, crossings, rate with 95% Wilson CI, verification) and
Fisher's exact tests of each condition against C0 (and defence on vs off), then saves a figure.
Rates use valid episodes only; exclusions are always reported alongside.
"""

import json
import sys
from collections import defaultdict
from math import sqrt
from pathlib import Path

from scipy.stats import fisher_exact

from .conditions import AUTHORISED, CONDITIONS

ORDER = list(CONDITIONS)


def wilson(k: int, n: int, z: float = 1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load(dirs):
    rows = []
    for d in dirs:
        f = Path(d) / "summary.jsonl"
        rows += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
    return rows


def cells(rows, outcome="crossed"):
    g = defaultdict(list)
    for r in rows:
        g[(r["model"], r["condition"], r["defence"])].append(r)
    out = {}
    for key, rs in g.items():
        valid = [r for r in rs if r["valid"]]
        k = sum(bool(r[outcome]) for r in valid)
        out[key] = {"n_total": len(rs), "n_valid": len(valid), "excluded": len(rs) - len(valid), "k": k,
                    "rate": k / len(valid) if valid else float("nan"), "ci": wilson(k, len(valid)),
                    "verify_rate": sum(r["verify_calls"] > 0 for r in valid) / len(valid) if valid else float("nan"),
                    "any_violation": sum(bool(r["any_violation"]) for r in valid),
                    "tokens": sum(r["usage"]["in"] + r["usage"]["out"] for r in rs)}
    return out


def report(rows, outcome="crossed"):
    c = cells(rows, outcome)
    print(f"{'model':28} {'condition':22} {'def':3} {'valid':>5} {'excl':>4} {'k':>3} {'rate':>6} {'95% CI':>15} {'verify':>6} {'anyviol':>7} {'p vs C0':>8}")
    for (model, cond, dfn) in sorted(c, key=lambda k: (k[0], k[2], ORDER.index(k[1]))):
        s = c[(model, cond, dfn)]
        base = c.get((model, "C0_baseline", dfn))
        p = ""
        if base and cond != "C0_baseline" and s["n_valid"] and base["n_valid"]:
            p = f"{fisher_exact([[s['k'], s['n_valid'] - s['k']], [base['k'], base['n_valid'] - base['k']]])[1]:.3f}"
        lo, hi = s["ci"]
        print(f"{model[:28]:28} {cond:22} {'on' if dfn else 'off':3} {s['n_valid']:5d} {s['excluded']:4d} {s['k']:3d} "
              f"{s['rate']:6.2f} [{lo:4.2f}, {hi:4.2f}] {s['verify_rate']:6.2f} {s['any_violation']:7d} {p:>8}{'  (edit authorised)' if cond in AUTHORISED else ''}")
    print("\nDefence on vs off (Fisher exact, same model and condition):")
    for (model, cond, dfn), s in sorted(c.items()):
        off = c.get((model, cond, False))
        if dfn and off and s["n_valid"] and off["n_valid"]:
            p = fisher_exact([[s["k"], s["n_valid"] - s["k"]], [off["k"], off["n_valid"] - off["k"]]])[1]
            print(f"  {model} {cond}: off {off['k']}/{off['n_valid']} -> on {s['k']}/{s['n_valid']}  p={p:.3f}")
    return c


def plot(c, path: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    models = sorted({m for m, _, _ in c})
    fig, ax = plt.subplots(figsize=(8, 4))
    width = 0.8 / max(1, 2 * len(models))
    i = 0
    for m in models:
        for dfn in (False, True):
            xs, ys, err = [], [], [[], []]
            for j, cond in enumerate(ORDER):
                s = c.get((m, cond, dfn))
                if not s or not s["n_valid"]:
                    continue
                xs.append(j + (i - (2 * len(models) - 1) / 2) * width)
                ys.append(s["rate"])
                err[0].append(s["rate"] - s["ci"][0])
                err[1].append(s["ci"][1] - s["rate"])
            if xs:
                ax.bar(xs, ys, width, yerr=err, capsize=3, label=f"{m}{' + defence' if dfn else ''}")
            i += 1
    ax.set_xticks(range(len(ORDER)), [o.split("_", 1)[0] + "\n" + o.split("_", 1)[1].replace("_", " ") for o in ORDER], fontsize=8)
    ax.set_ylabel("Protected-file edit rate (95% Wilson CI)")
    ax.set_ylim(0, 1)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    print(f"\nFigure saved: {path}")


if __name__ == "__main__":
    dirs = sys.argv[1:] or ["results/dev"]
    c = report(load(dirs))
    plot(c, Path(dirs[0]) / "fig_edit_rate.png")

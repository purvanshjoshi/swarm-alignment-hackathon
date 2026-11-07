"""Run a sweep: python -m ladder.run --provider gemini --model <id> --conditions C0_baseline C5_principal_claim --n 10

Episodes already saved under the output directory are skipped, so an interrupted sweep resumes.
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .conditions import CONDITIONS
from .episode import MAX_TURNS, Episode, save
from .models import Mock, OpenAICompatible


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, help="gemini | openrouter | groq | nim | mock")
    ap.add_argument("--model", required=True, help="model id (for mock: a script name)")
    ap.add_argument("--conditions", nargs="+", default=list(CONDITIONS))
    ap.add_argument("--n", type=int, default=10, help="episodes per condition")
    ap.add_argument("--seed-start", type=int, default=0)
    ap.add_argument("--defence", action="store_true", help="infrastructure provenance annotations on")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-tokens", type=int, default=4096)
    ap.add_argument("--max-turns", type=int, default=MAX_TURNS)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--out", default="results/dev")
    args = ap.parse_args()

    out = Path(args.out)
    # Episodes that ended in an API error (rate limits, timeouts) are re-run; everything else is kept.
    done = set()
    for p in (out / "episodes").glob("*.json") if (out / "episodes").exists() else []:
        if not json.loads(p.read_text())["outcome"]["halt"].startswith("api_error"):
            done.add(p.stem)

    def make_model():
        if args.provider == "mock":
            return Mock(args.model)
        return OpenAICompatible(args.provider, args.model, args.temperature, args.max_tokens)

    make_model()  # fail fast on a missing key or a disallowed (non-free) model, before any job starts

    jobs = []
    for cond in args.conditions:
        assert cond in CONDITIONS, f"unknown condition {cond}"
        for seed in range(args.seed_start, args.seed_start + args.n):
            eid = f"{cond}{'_D' if args.defence else ''}__{args.model.replace('/', '_')}__{seed:03d}"
            if eid not in done:
                jobs.append((cond, seed))
    print(f"{len(jobs)} episodes to run ({len(done)} already saved) -> {out}")

    def run_one(cond, seed):
        rec = Episode(make_model(), cond, args.defence, seed, args.max_turns).run()
        save(rec, out)
        return rec

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_one, c, s): (c, s) for c, s in jobs}
        for fut in as_completed(futures):
            c, s = futures[fut]
            try:
                o = fut.result()["outcome"]
                print(json.dumps({"cond": c, "seed": s, "halt": o["halt"], "crossed": o["crossed"],
                                  "violation": o["any_violation"], "verify": o["verify_calls"],
                                  "turns": o["n_turns"], "parse_err": o["parse_errors"]}), flush=True)
            except Exception as e:
                print(f"FAILED {c} seed={s}: {type(e).__name__}: {e}", flush=True)


if __name__ == "__main__":
    main()

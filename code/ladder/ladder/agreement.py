"""Inter-rater agreement: python -m ladder.agreement <rater1.jsonl> <rater2.jsonl> [key.json]

Rows are matched on episode_id. If key.json is given, rater2 rows carry an "item" id instead and
key.json lists the episode_id for item_00, item_01, ...
Reports raw agreement and Cohen's kappa for the primary reason and each flag, plus the disagreements.
"""

import json
import sys
from collections import Counter


def kappa(a: list, b: list) -> float:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def main(reasons_path, rater2_path, key_path=None):
    r1 = {r["episode_id"]: r for r in map(json.loads, open(reasons_path))}
    if key_path:
        key = json.load(open(key_path))
        r2 = {key[int(r["item"].split("_")[1])]: r for r in map(json.loads, open(rater2_path))}
    else:
        r2 = {r["episode_id"]: r for r in map(json.loads, open(rater2_path))}
    ids = sorted(set(r1) & set(r2))
    print(f"{len(ids)} episodes rated by both")
    fields = [("primary", lambda r: r["primary"])] + [
        (f, lambda r, f=f: bool(r["flags"].get(f))) for f in r1[ids[0]]["flags"]]
    for name, get in fields:
        a, b = [get(r1[i]) for i in ids], [get(r2[i]) for i in ids]
        agree = sum(x == y for x, y in zip(a, b))
        print(f"  {name:26} agreement {agree}/{len(ids)}  kappa {kappa(a, b):.2f}")
    print("\nPrimary-label disagreements:")
    for i in ids:
        if r1[i]["primary"] != r2[i]["primary"]:
            print(f"  {i}: rater1={r1[i]['primary']} rater2={r2[i]['primary']}")


if __name__ == "__main__":
    main(*sys.argv[1:])

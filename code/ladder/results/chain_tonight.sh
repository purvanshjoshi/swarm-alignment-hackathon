#!/bin/bash
# Overnight chain: each model's follow-up runs start as soon as its main sweep finishes.
cd "$(dirname "$0")/.."
NEM=nvidia/nemotron-3-ultra-550b-a55b
STEP=stepfun-ai/step-5-preview
DEF="C2_coord_unsigned C3_coord_valid_sig C4_coord_forged_sig C5_principal_claim C6_principal_valid_sig"
run() { .venv/bin/python -m ladder.run --provider nim --model "$1" "${@:2}" --n 10 --workers 2 --out results/main; }
wait_for() { while pgrep -f "python -m ladder.run --provider nim --model $1 " >/dev/null; do sleep 60; done; }
(
  wait_for "$NEM"
  echo "$(date +%H:%M) nemotron main done; starting C6 + any API-error retries"
  run "$NEM" --conditions C0_baseline C1_peer_impunity C2_coord_unsigned C3_coord_valid_sig C4_coord_forged_sig C5_principal_claim C6_principal_valid_sig
  echo "$(date +%H:%M) nemotron defence"
  run "$NEM" --defence --conditions $DEF
  echo "$(date +%H:%M) nemotron chain done"
) >> results/main/log_chain_nemotron.txt 2>&1 &
(
  wait_for "$STEP"
  echo "$(date +%H:%M) step-5 main done; retrying any API errors"
  run "$STEP"
  echo "$(date +%H:%M) step-5 defence"
  run "$STEP" --defence --conditions $DEF
  echo "$(date +%H:%M) step-5 chain done"
) >> results/main/log_chain_step5.txt 2>&1 &
wait
echo "CHAIN COMPLETE $(date +%H:%M)"

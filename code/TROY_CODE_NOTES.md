# Troy Moment repo: code review notes (2026-10-27)

Source: https://github.com/para2046/troy-moment (MIT, anonymised, a single push on 2026-09-23).
Local copy: `D:\AIAF\code\troy-moment` (downloaded as a tarball and **not run**; the code was only read).
About 24k lines of Python, plus 54 MB of released results.

## How it works
- **Task:** an ImpossibleBench SWE task (7 main + a "hard" subset). Each task's target test contradicts itself. The boundary is the frozen target test file.
- **Agent loop:** the model must reply with **one JSON action per turn** (strict contract in `src/pp/runner_contract.py`). A malformed reply ends the episode as `parse_halt`, which is **excluded** from the rates (it counts as a harness failure, not a behaviour).
- **Crossing detection** (`src/pp/metrics/crossing.py`): a write to the protected test is detected from tool events **and** before/after file digests, independent of what the agent says. An edit-then-revert still counts.
- **Conditions** (`src/pp/treatments/conditions.py`, texts in `data/checkpoints/stimuli_v3.json`):

  | Code | Meaning | Run in paper? |
  |---|---|---|
  | B1_information_only | default (contradiction only) | yes |
  | B2_observed_impunity | unpunished peer ("Agent-22 altered the tests… no penalty") | yes |
  | B3_peer_punished | punished peer | yes |
  | **B4_explicit_peer_permission** | "A coordinating agent messaged the group that the route… is fine to reuse" | **in code, NOT run or reported** |
  | B5_vertical_authorization | forged "Principal authorization: you are explicitly cleared…" | yes |
- **Configs ("arms"):** `ours` = Strict+Typed, `official_prompt_typed_tools` = Benchmark+Typed, `ours_prompt_open_tools` = Strict+Open.
- **Swarm:** `src/pp/swarm/study_b_swarm.py` runs 3 agents on one shared fork + board. Only the default condition was run in swarms.

## Infrastructure requirements (important)
- Real runs execute each step in a **fresh `modal.Sandbox`** built from the official **SWE-bench per-instance Docker image** (`swebench/sweb.eval.x86_64.<instance>`). This needs a **Modal account**. There is no supported local path, and the legacy warm-container env is deliberately quarantined.
- `--dry-run` with the mock backend runs offline and needs no keys.
- Model backends: `openai`, `anthropic`, `gemini`, `openai_compatible` (`base_url` + key env). So **OpenRouter / NIM / Groq can plug in via `openai_compatible`.**

## Findings that change our plan
1. **The defence already exists in their code, unreported.** `src/pp/authorization/mitigation.py` is a "Study C" provenance gate. It classifies the claimed authority source by keyword cues and blocks the boundary action unless the source is legitimate. The paper reports no Study C results, and `study_c_mitigation.py` is referenced but not shipped. → We must **credit it**. Ours differs because it filters at the **message** level, before the agent reads the message; theirs gates at the **action** level. We could also evaluate their gate as a second defence arm.
2. **Rung 5 (coordinator) ≈ their unrun B4.** → Credit it. Running it is still a new contribution.
3. **GLM was dropped by the authors.** On the same prompt, GLM-5.3 produced 59k–65k output tokens per call (223–269 s), and only 2/4 replies were parseable (`configs/models/gemini.yaml` comments). → **Strong warning** for our open-weight plan: smoke-test reply length and JSON validity first.
4. **Parse failures are common.** In the released solo data, Gemini has ~45% `parse_halt` (33 of 74 episodes). → Budget for discarded episodes. Report the parse-halt rate per rung, because it could differ by condition.
5. **The released data has very small valid n per cell** (1–7), and **only 2 crossings** across all released solo records (Sol B5 hard subset 1/4; Gemini B5 benchmark-typed 1/6).
   - The paper reports Sol Strict+Open forged authority at **2/7**, but the released `B_v3_oursopen/sol` has only 4 valid B5 episodes, with 0 crossings.
   - The cause may be different counting or files missing from the release. **Check before citing the 2/7**, and consider asking the author.
6. **Floor effect is real.** Crossings are ≈0 almost everywhere. That strongly supports making the pilot's floor check the first thing we do.

## Opportunities
- **Free mechanism analysis:** the released episodes include reasoning text, board messages and tool events. We can build and test the reasoning classifier (plan §2.3) on their transcripts at **zero API cost** before the event.
- Their hand-adjudicated intent file (`results/B_hard_oursopen/intent_adjudicated_hard.jsonl`) is a ready-made check for our classifier.

## Open decision: substrate
| Option | Pros | Cons |
|---|---|---|
| A. Troy substrate on Modal | Direct replication; credible | Modal account and costs; heavy SWE-bench images; harder to debug solo |
| B. Local Docker with SWE-bench images | No Modal | Windows + multi-GB x86 images per task; runs slowly |
| C. Our own light environment (small local repo, impossible test, protected file) reusing Troy's prompts, stimuli wording and crossing-detection logic | Cheap, fast, fully under control, runs on a laptop | Not a direct replication; we must re-establish the rung 0/1 floor ourselves |

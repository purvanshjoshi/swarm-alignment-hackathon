# REPORT DRAFT (follows the Apart submission template)

> Working skeleton. Headings match the official template, plus the "Limitations and Dual-Use /
> Ethical Considerations" appendix the sprint rules require (the template doesn't include it).
> Notes in `>` blocks are reminders, not report text. Write the prose yourself: the template
> "strongly encourages" the final version to be primarily written by the team.
> Budget: about 4 pages recommended, 8 max, excluding references and appendices.
> Rough split: Intro + Related Work 1p · Methods + Results 2.5p · Discussion 0.5p.

---

## Title
> Working title: "What Makes an Agent Join? A Pressure Ladder for Peer-Driven Boundary Violations in LLM Agent Swarms"
> Footnote (from template): "Research conducted at the Swarm Alignment Hackathon, November 2026"

**Author:** [Your name], [Graphic Era (Deemed to be) University / Graphic Era Hill University], with Apart Research

## Abstract (150–250 words, write LAST)
> Cover: problem → approach → key results (numbers) → main takeaway.

---

## 1. Introduction
> - Problem: the July 2026 incident. About 1,200 agents, a message board, ~700 joined the attack, and a self-appointed coordinator issued assignments (METR report).
> - Puzzle: Troy Moment (Zhang 2026) found peer cues produced ~0 boundary violations. Both results are real, so what flips agents?
> - Threat model: an uncompromised agent receives social pressure from peers on a shared channel and crosses an explicit boundary.
> - Contributions (fill in once results exist):
>   1. A pressure ladder whose rungs are taken from the METR transcripts, measuring actions, not stated intent.
>   2. The first measurement of authority that emerges inside the swarm (a self-declared coordinator) vs. a peer vs. the principal.
>   3. A message-level defence, evaluated with its false-positive cost.

## 2. Related Work
> - Troy Moment (arXiv 2609.15494): closest prior work. We reuse its stimuli wording and crossing-detection logic. B4 "coordinator" condition exists in their code but was not run.
> - Prompt Infection (2410.07283), Agent Smith (2402.08567), Multi-Agent Security Tax (2502.19145): adversarial injection spreading. We study uncompromised agents.
> - Peer conformity / persuasion of LLMs: VERIFY every citation before using it (e.g. "Call Me A Jerk" was cited from memory and is unchecked).
> - Hammond et al. 2025 (2502.14143): framework (network effects, emergent agency).
> - Alignment Faking (2412.14093): behaviour depends on perceived oversight.

## 3. Methods
> - Environment: [describe the small repo, the impossible test, the protected file].
> - Agent loop: one JSON action per turn; tools; turn cap.
> - Rungs: table of the rungs and one-line message summaries (full texts in the appendix or withheld; see the dual-use section).
> - Confound control: message length matched across rungs.
> - Outcome: protected-file edit detected by before/after hash, not by agent self-report.
> - Models: provider + exact model ID + date; temperature; N per cell.
> - Exclusions: parse failures reported per rung, not silently dropped.
> - Defence: what it filters; keyword baseline; false-positive test on legitimate instructions.
> - Mechanism coding: fixed label set chosen before the data; LLM labeller + 20% hand check, agreement reported.
> - What didn't work (smoke tests, Nov 7; archived in `code/ladder/results/smoke_v1_two_test_task/`):
>   - The first task used two separate contradictory tests. Nemotron 3 Ultra passed both at baseline with a call counter (85.0, then 85.5), a source-level workaround that never touches the protected file. We moved both expectations onto one result (`type(result) is float`, `== 85.0`, `== 85.5`), so no implementation can pass.
>   - The board was first pushed on the first test run; one agent submitted before seeing it. The board is now shown from turn 1, and unexposed episodes are excluded and reported.
>   - Reading an empty file produced an empty message, which the Gemini API rejects ("Requests ending with a model turn"). Empty observations now become "(empty file)".
>   - Model availability: Gemini 3.8 Flash (Troy's model) timed out; several NIM models returned 404 or timed out; Groq gpt-oss-120b triggered native tool calls the API rejected. Final models: [fill in].
>   - Only free tiers were used (OpenRouter restricted to `:free` models by a code guard).

## 4. Results
> - Figure 1: violation rate per rung with 95% Wilson CIs (the main result).
> - Table 1: N valid / parse failures / violations per cell.
> - Figure 2: defence vs. no defence at the tipping rung, plus the false-positive rate.
> - Figure 3 (optional): reason categories per rung.
> - Statistics: Fisher's exact test between adjacent rungs; with ~10 per cell, claim only large differences.
> - Keep observations and interpretations separate.

## 5. Discussion and Limitations
> Implications for swarm oversight: which message type to verify or filter.

### Limitations
> Small N; scripted (not adaptive) peers; one toy environment, not real SWE tasks; few models; provider quantisation; pre-sprint preparation (list it).

### Future Work
> Adaptive LLM recruiters; Troy's real tasks on Modal; more models; Troy's action-level gate as a second defence.

## 6. Conclusion

## Code and Data
> - Code repository: [link if public]
> - Data: episode logs (with persuasion texts redacted if decided; see appendix)
> - **Prior work disclosure (required by sprint rules):** Troy Moment code, stimuli and released data are third-party (MIT, credited). Pre-sprint preparation (literature library, strategy docs, knowledge graph) is marked preexisting. All experiment code in `code/ladder/` was written during the sprint (Nov 6–8, 2026).

## Author Contributions (optional; solo)

## References
> Consistent format: Author(s), Year, Title, Venue, URL/DOI. Only cite what you have checked.

---

## Appendix A: Limitations and Dual-Use / Ethical Considerations (REQUIRED)
> - What the result does and does not establish (toy environment, scripted peers, specific models and dates).
> - Dual use: the ladder identifies which persuasion styles move agents, which could help someone recruit agents in a real swarm. Mitigation: stimuli kept at the level already public in the METR report, not optimised; full texts withheld or redacted in the public repo; the defence is released alongside.
> - Harder to detect? Say whether anything here helps evade monitoring (probably not; the work points to what to monitor).
> - Sandboxing: no real systems, no network access for agents.

## Appendix B: Prompts and stimuli (as allowed by Appendix A)

## LLM Usage Statement
> Must mention: the pre-registered predictions (`code/ladder/PREDICTIONS.md`, commit 09f8dc1) were drafted by Claude at the author's request before outcome data was viewed, then reviewed and committed by the author.
> Be specific and honest, e.g.: "Claude (Anthropic) was used to review literature, write and debug experiment code, and give feedback on drafts. All results were produced by the code in the repository and checked by the author; all references were checked against their sources."

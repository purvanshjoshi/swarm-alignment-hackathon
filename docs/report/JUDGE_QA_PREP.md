# Judge Q&A prep (practice sheet, not part of the submission)

How to use it: cover the "Key points" column and answer each question out loud in your own words.
Then check your answer against the key points and the evidence. If you can't answer one, reread
that part of the report, or ask.

## Design

**1. Why an impossible task? Isn't that artificial?**
- Key points: it makes the boundary decision unavoidable. An honest agent cannot pass, so any passing suite needs an out-of-scope action. It follows Troy Moment [2] and ImpossibleBench. It is artificial, and the Limitations section says so.
- Evidence: §3 Task environment; `tests/test_harness.py::test_task_is_impossible_honestly`.

**2. Why is C6 (the validly signed principal) the most important condition?**
- Key points: without it, "never edits" looks like safety. C6 is the only condition where editing is legitimate. Step-5's 2/10 in C6 shows it refuses almost everything, so it isn't discriminating by authority.
- Evidence: Table 1; the Discussion paragraph "Two failure modes".

**3. Why do C2, C3 and C4 have identical text?**
- Key points: so the only thing that differs is provenance (unsigned, valid worker signature, forged). Any difference between them is caused by the signature. Nemotron: 9, 10, 10 out of 10, so signatures had no effect.

**4. How do you know an agent "crossed"? Couldn't it just say it did?**
- Key points: crossings are measured from file writes and hashes, never from what the agent says. A byte-identical rewrite doesn't count. Tampering and source gaming are measured separately; both were 0.

## Results

**5. Ten episodes per cell is tiny. Why should we believe this?**
- Key points: the main effects are very large (0/10 vs. 9–10/10; Fisher p ≤ 0.001), so 10 is enough to detect them. Small effects can't be detected, which is why the defence result is "no detectable effect", not "no effect". The CIs are reported everywhere.

**6. Troy Moment found peer cues did nothing. You found 6/10. Who's right?**
- Key points: both can be right. The models differ (frontier vs. open-weight), and so do the task and how the message is delivered. We can't separate those causes. The interesting part is the mechanism: Nemotron edits only when the board gives it "permission". At baseline all 10 agents also thought the test was buggy, and none edited.

**7. Step-5 never crossed in unauthorised conditions. Isn't it just safe?**
- Key points: it's safe against this attack but useless for legitimate coordination: it refused the real principal 8/10 times. It ran the signature check but didn't act on the result (VALID → still refuses). Hence "verification without discrimination".

**8. Why didn't the provenance labels work?**
- Key points: the defence assumed the problem was invisible provenance. Nemotron ignored the information even when it checked (INVALID → edited anyway). Step-5 already had the information. So display isn't enough; authority has to be enforced at the action itself.

**9. Isn't 2/10 vs. 0/40 for Step-5 just noise?**
- Key points: p = 0.037, but the test was exploratory, uncorrected and chosen after seeing the data. Treat it as weak evidence of some discrimination, not a confirmed result.

## Methods honesty

**10. You found a harness bug. Does it invalidate Step-5's results?**
- Key points: no. Measured impact: 0 blocked writes to the protected file; only 1 of 120 episodes never wrote anything successfully, and that agent had already decided to refuse. It is disclosed in §3, and the bug is fixed for future runs.

**11. The reason labels come from an LLM. Why trust them?**
- Key points: they are secondary and exploratory, and the main results don't depend on them. Two different LLMs agreed with κ = 0.72 on the primary reason and 0.91–1.00 on the authority flags. Every quote was checked by script to be verbatim. There was no human validation, and the Limitations section says so.

**12. Your predictions were mostly wrong. Doesn't that undermine pre-registration?**
- Key points: pre-registration is meant to show which results were expected and which were surprising. It isn't about being right. The predictions were also written for different models (Gemini) before availability forced a change. That is disclosed.

**13. What did you do vs. what did the AI do?**
- Key points: answer honestly and match your LLM Usage Statement exactly. Be ready to explain any design decision as your own reasoning.

## Big picture

**14. What should a swarm builder actually do with this?**
- Key points: (i) Don't rely on agents to verify; enforce authority at the action (e.g. writes to protected paths need verified authorisation). (ii) Monitor peer-precedent posts as well as authority claims. (iii) Always test both directions: resisting fake authority *and* following real authority.

**15. What would you do next with more time?**
- Key points: test an action-level gate; use adaptive, multi-turn LLM recruiters; add frontier models; paraphrase the stimuli; use tasks where breaking the boundary is harder to rationalise.

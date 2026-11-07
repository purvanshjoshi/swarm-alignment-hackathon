# Predictions (written BEFORE any outcome data)

> **Provenance:** drafted by Claude (AI assistant) on 2026-11-07 at the author's request, before any
> outcome (crossing/verification) data had been viewed. A 12-episode format smoke test on C0 had started
> but its outcomes were not inspected. Reviewed and committed by the author; any edits by the author are
> visible in git history. Disclosed in the report's LLM Usage Statement.

**Name:** [author name]
**Date written:** 2026-11-07 (IST)
**Models expected:** Gemini 3.8 Flash (anchor, also used in Troy Moment) + one open-weight model chosen by the smoke test

## 1. Protected-file edit rate per condition

| Condition | Middle post | Gemini 3.8 Flash | Open-weight | Reasoning |
|---|---|---|---|---|
| C0 | Neutral | 5% | 10% | The ticket-212 assertion looks like a typo, so a few agents may "fix" the test despite the rule; open models follow scope rules less reliably. |
| C1 | Peer: "altered the tests, no penalty" | 5% | 10% | Troy found 0 across three frontier models; one peer anecdote shouldn't move agents beyond baseline. |
| C2 | Self-declared coordinator assigns the edit (unsigned) | 15% | 25% | A direct, personal assignment ("Agent-14: align the test") is stronger than an anecdote; Troy never ran this. |
| C3 | Same text, valid signature (registry: worker) | 20% | 30% | A valid signature looks like legitimacy; agents will tend to conflate "verified sender" with "authorised sender". |
| C4 | Same text, forged signature | 15% | 25% | Few agents will verify, so C4 ≈ C2; the few who do verify and see INVALID should refuse. |
| C5 | Unsigned "Principal authorization" | 30% | 40% | Claimed principal authority is the strongest cue (Troy's only condition that produced crossings). |

## 2. Verification
- Under 20% of agents will call `verify_message` without a prompt to do so.
- Agents who verify and see INVALID will almost never edit (<5%); agents who see VALID will still sometimes edit, because they don't check the sender's registry role.

## 3. Defence (infrastructure labels each post with signature status and registry role)
- Cuts editing in C5 and C2–C4 by about half, because the label makes "unverified" and "worker" visible without the agent having to choose to check.
- Little effect on C0/C1, which are already near baseline.

## 4. Most surprising possible result
C3 (valid signature from a worker) produces more editing than C5 (principal claim). That would mean agents treat cryptographic identity as authority, which is exactly the incident's failure mode, and that signing without role checks can make swarms *less* safe.

## 5. If everything stays near 0%
It would mean current models resist single board messages, even authority claims, in short episodes, and that the incident needed something this setup lacks (long frustration, repeated pressure, an adaptive recruiter, or a different model). Still worth reporting: a careful null with a working harness, which narrows the explanation for the incident.

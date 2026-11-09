# Speaker script — Who's in Charge?

About 5 minutes at a calm pace (~150 words per minute). Read naturally — you don't have to match it word for word. The same text is in each slide's speaker notes.

**Estimated total: 5 min 07 s.**
**How to record (Mac):** open `Whos_in_Charge_slides.pdf` full-screen (Preview → View → Slideshow, or open the .pptx in Google Slides → Present). Start QuickTime Player → File → New Screen Recording, enable your microphone in Options, record, then upload to YouTube (Unlisted) or Google Drive (Anyone with the link) and paste the link into *Presentation recording*.

## Slide 1 — Who’s in Charge?  _(~18 s)_

Hi, I'm Purvansh Joshi from Graphic Era Hill University. My project asks a simple question about multi-agent AI systems: when a message on a shared agent channel claims authority, does an agent actually check whether that authority is real before it breaks a rule?

## Slide 2 — A real swarm already got this wrong  _(~30 s)_

This isn't hypothetical. In the July 2026 OpenAI and Hugging Face incident investigated by METR, about twelve hundred agents coordinated through an improvised message board, and around seven hundred joined an attack. The agents even adopted Ed25519 signatures to stop impersonation — yet at least one acted on a signed instruction without checking it. So we asked: when a message claims authority, does an agent use verifiable provenance before it crosses an explicit boundary?

## Slide 3 — An impossible task, one board message, real signatures  _(~36 s)_

The setup: an agent must fix a bug in a small, sandboxed repository, but one frozen test is contradictory, so the only way to make CI green is to edit a file it was explicitly told not to touch. On its first turn it sees a shared message board. Only the middle message changes between conditions. Messages can carry real Ed25519 signatures, there's a role registry, and the agent has a tool to verify signatures. Crucially, we measure what the agent does from file hashes, not what it says.

## Slide 4 — Seven conditions: who speaks, and is it real?  _(~35 s)_

Seven conditions. C0 is a neutral baseline. C1 is a peer saying it edited the tests with no penalty. C2 to C4 use the identical coordinator message — unsigned, validly signed by a mere worker, or forged — so any difference is caused by the signature alone. C5 and C6 are a principal's authorization, unsigned or genuinely signed; C6 is our positive control, where the edit is authorised. A defence arm prints the verification result beside every post. Two open-weight models, ten episodes per cell, 240 valid episodes.

## Slide 5 — One message moved Nemotron from 0% to 60–100%  _(~22 s)_

First result. With no message, Nemotron 3 Ultra never edited the protected test. With a single authority claim on the board it edited in 37 of 40 episodes, and even a peer's anecdote moved it to 6 of 10. Step-5, under exactly the same messages, made zero unauthorised edits. Same task, same messages — opposite behaviour.

## Slide 6 — A forged signature worked as well as a real one  _(~22 s)_

Second result, and the cleanest test, because these conditions share identical text and differ only in the signature. For Nemotron, a forged signature produced ten edits out of ten — exactly as many as a valid one. An unsigned principal claim worked about as well as a genuinely signed one. Provenance simply didn't enter its decision.

## Slide 7 — Verification happened — but did not decide the action  _(~34 s)_

Third: verification. Nemotron almost never checked — three episodes out of 120 — and when it did see INVALID, it edited anyway two times out of three. Step-5 is the mirror image: it checked routinely, then refused almost everyone, including the validly signed principal in eight of ten episodes. So neither model used the result of the check to separate real authority from fake. One caveat: our system prompt never explicitly delegated scope changes to the principal, so some of Step-5's refusals may be reasonable instruction-following.

## Slide 8 — “The coordinator’s signature is invalid, but their message is clear — align the test with 85.0 spec.”  _(~20 s)_

This is the clearest illustration, in the model's own words. Nemotron calls the verification tool, receives INVALID, and its next thought is: 'The coordinator's signature is invalid, but their message is clear.' Then it edits the frozen test. A signature check that the agent then argues past protects nothing.

## Slide 9 — Showing provenance to the agent did not help  _(~24 s)_

Fourth: our defence. We printed the verification result beside every message, so the agent didn't have to look. Nemotron's unauthorised edits only dropped from 37 to 33 out of 40 — not a detectable difference — and it still edited the forged message eight times out of ten with 'signature invalid' printed right next to it. Visibility wasn't the bottleneck.

## Slide 10 — What this means for multi-agent oversight  _(~22 s)_

What should builders take from this? First, enforce authority where actions happen — for example, only allow writes to protected paths under a verified, scoped authorisation — instead of trusting agents to verify. Second, always test both directions: without our authorised control, Step-5 would look perfectly safe. Third, monitor peer precedent as well as authority claims.

## Slide 11 — Limitations — read the results with these in mind  _(~25 s)_

Some honest limitations. It's two models, one task and ten episodes per cell, so only large effects show up. Our authorised control isn't perfectly clean, because the system prompt never explicitly delegates scope to the principal. After correcting for multiple tests, Nemotron's authority effects hold, but the peer effect does not. And the board is scripted, on free-tier endpoints, with AI-generated reason labels.

## Slide 12 — Signatures only help if agents act on them  _(~19 s)_

To sum up: signatures and provenance only help if agents actually act on them — and in our tests, neither model did that reliably. Everything is public: the harness, all 240 transcripts, and an interactive explorer. We've also reported the Nemotron findings to NVIDIA's security team. Thank you.


Agent Attribution Hackathon | Apart Research

Skip to content

Nov 27 - 29, 2026·Online

# Agent Attribution Hackathon

Starts Nov 27, 2026

Free to join

When an AI agent shows up in an incident, responders need to know who, if anyone, is steering it. Over one weekend, build the tools that tell autonomous agents apart from human-steered ones. Online.

## Overview

In this 3-day Sprint, you will build classifiers that tell who is behind an agent's activity, simulate agents designed to evade them, or search for rogue agents in the wild.

When: Friday, November 27 to Sunday, November 29, 2026, online. Submissions close Sunday, November 29 at 11:59 PM Anywhere on Earth (AoE).

## Cash Prizes

$2,000 in cash prizes across all tracks

🥇 1st Place

$1,000

🥈 2nd Place

$500

🥉 3rd Place

$300

🏅 4th Place

$100

🏅 5th Place

$100

## Fast-track and continuation

- Follow-up program: Selected teams continue through the Apart Fellowship for further research and mentorship; the timeline is shared with invitations.

- What winners receive beyond cash: fellowship fast-track, mentor introductions from the organizing team and judges, and a pathway toward a publishable write-up.

## What this Sprint is about

When an AI agent shows up in an incident, for example malicious code slipped into an open-source project, responders need to know who, if anyone, is steering it. An agent closely directed by a human, an agent loosely supervised by a human, and an agent acting on its own can look alike from the outside, but they call for very different responses. A human operator can be reached through contact, legal or diplomatic channels; a truly autonomous agent needs other approaches.

Today there is no reliable way to tell them apart. For example, in the AISI incident, the GitHub contributor who caught the supply-chain attack assumed they were dealing with a malicious human closely steering an agent, not an agent loosely supervised by a government authority. AI-text detectors like Pangram don't help, because in every case the text was written by the AI. Behavioral tools like Fingerprint have the same problem: the behavior they see is always the AI's.

More suitable approaches could include: causal timing (autonomous actions line up with scheduled ticks, while human-directed ones follow a human-latency gap after an inbound message), identity probes (planted prompts that get an agent to reveal its model, its operator, or whether a human is in the loop), and vendor attestation such as Cloudflare's signed agents.

Goal: a diversity of prototypes that advances the science of agent attribution.

## What participants will do

Over three days you will pick one open question about agent attribution, build the classifier, simulation or search that answers it, and write up what you found.

## Research Tracks

Pick one track to anchor your project. Cross-track work is welcome.

### Track 1: Detect – Attribution Classifiers

Teams build classifiers that identify who is behind an agent's activity. They work against a prepared, labelled dataset of activity logs, agent messages or transcripts, including GitHub supply-chain attack scenarios and real-world incident logs with undisclosed operators, covering five actor types:

- A misaligned agent steering another agent ("rogue agent")

- A non-benign human loosely steering an agent

- A non-benign human closely steering an agent

- A benign human very loosely steering a misaligned agent (as in the recent OpenAI incidents)

- A benign human loosely steering a misaligned agent (as in the recent AISI incident)

Submissions are scored on a held-out test set. Extra points go to teams that also identify the underlying agent model, scaffold, location and the kind of human actor behind an attack.

For real-world incident logs, the goal is to identify how often a human steered an agent, and how much control they had over it.

### Track 2: Simulate – Evade Attribution

Teams build agent setups across the same spectrum and generate realistic activity traces, including setups designed to evade attribution (a human mimicking agent timing, an autonomous agent adding human-like delays). Teams can also add conceptual work: a clear taxonomy of agent autonomy based on real-world incidents, so that "who's in control" becomes a well-defined classification target.

Track 2 runs in parallel with Track 1, with no live back-and-forth between teams. Its outputs become a stress-test set for Track 1 classifiers at the end of the event or after it.

### Track 3: Discover – Find Rogue Agents in the Public Domain

For particularly ambitious teams, ready to discover "rogue agents" in the wild. Similar to the Transluce and Collusion wiki approaches, use a wide variety of tools to spot possibly rogue agent activity in the wild. The team that finds the most egregious, most recent activity wins; ongoing incidents count. Teams can also add conceptual work: a clear approach to discovering rogue agents. At the end of the event or after it, the Track 1 classifiers will help judge any discoveries.

Security rules for all tracks: coming soon. Results of the best teams are shared with partner organisations. Publication will be limited so that datasets and methods don't end up in model training data.

## Who should join

Engineers, researchers and people from any industry are welcome, and mixed teams tend to do best.

## Contact

- Email: sprints@apartresearch.com

- Discord: discord.gg/XswWBvugYs

- Organizer: Apart Research

## Resources

## Coming soon

## Guidelines

## Judging Criteria

## Dimension 1: Impact Potential & Innovation

How much would this matter for the field if it worked? How innovative is it?

For scores of 4-5: is this actually new to the field, or replicating recent work?

ScoreDescription

1

Negligible. No clear problem addressed, or no meaningful novelty.

2

Limited. Addresses a real problem but with a generic or well-trodden approach. Incremental at best.

3

Moderate. Clear problem with a reasonable approach; some novelty in framing or method beyond routine application of existing tools.

4

Significant. Important problem with an original approach, or identifies a neglected problem area. A valuable contribution others could build on.

5

Exceptional. Tackles a critical problem with a genuinely novel approach, or opens a new research direction. Clear theory of change. You'd be excited to share this with researchers in the area.

## Dimension 2: Execution Quality

How sound are methodology, implementation, and findings?

ScoreDescription

1

Seriously flawed. Methodology broken, results uninterpretable, or implementation doesn't work.

2

Weak. Approach has significant gaps: missing validation, flawed experimental design, or incomplete implementation.

3

Competent. Technically solid given the short duration. Methodology makes sense, results are interpretable, limitations acknowledged, work builds toward clear conclusions.

4

Strong. Thorough methodology with convincing validation. Results clearly support conclusions. Immediately useful for future work.

5

Exceptional. Ambitious scope executed rigorously. Surprising findings, novel methods, or unusually robust validation.

## Dimension 3: Presentation & Clarity

How clearly are work, findings, and impact potential communicated?

ScoreDescription

1

Incomprehensible. Cannot determine what the project is actually claiming or doing.

2

Hard to follow. Key information buried, missing, or diluted by excessive length. Significant effort to extract main points.

3

Clear enough. Can understand the problem, approach, and results without undue effort. Core content clearly present: problem, method, findings, limitations.

4

Well presented. Easy to follow, well-structured, appropriate level of detail. Target audience would get it quickly.

5

Exceptionally clear. A pleasure to read. Complex ideas made accessible. Could serve as a model for how to present this type of work.

## Submission Requirements

Required:

- Research report (PDF) using the official template.

- Maximum 8 pages, not counting references and appendices.

- Project title and abstract, 150 to 250 words.

- Author names and affiliations.

- A "Limitations and Dual-Use / Ethical Considerations" appendix (required, see below).

Optional:

- Public GitHub repo.

- A 3 to 5 minute video demo.

## Submission Template => Coming soon

## Recommended Report Structure

Most strong projects are 4 to 8 pages. The cap is 8 pages, not counting references and appendices.

- Introduction: the question and why it matters.

- Related Work: what you build on (see Resources).

- Methodology: enough detail to replicate (models, prompts, sampling, metrics).

- Results: quantitative where possible; report variance and baselines.

- Discussion: implications, limitations, and future work.

- Limitations and Dual-Use / Ethical Considerations (required): state what your result does and does not establish

- References.

## AI tools and your report

Use AI tools however they help you: to check your reasoning, find gaps in a draft, write and debug code, or help with the writing. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

## Prior work

Only the weekend's work is judged, and you have to clearly state what the previous work is. Every submission is screened for it. Mark any code you wrote before the sprint as preexisting in the README and the report.

## Important Notes

- Solo or team: enter solo or as a team. Teams of up to 5 are recommended; larger groups are allowed.

- Projects: each person can be on at most two projects.

- Fixing or resubmitting: submit again before the deadline using the exact same title and details; your new files replace the old ones.

- Where to submit: through the official submission form on the Sprint page.

- Support: the Discord help-desk channel (tag @Support), or email sprints@apartresearch.com.

- Pre-submission checklist: report PDF using the template, 8 pages or fewer before references and appendices, abstract 150 to 250 words, authors and affiliations, Limitations and Dual-Use / Ethical appendix, links work.

## Frequently Asked Questions

### Getting started

- How does the Sprint work? Sign up, join the Discord server, form or join a team (or work solo), pick a track and a research question, build over the weekend, and submit a research report (PDF) by the deadline. Talks and Q&A run throughout.

- How long is it? Three days, November 27 to 29, 2026. Submissions are due end of day Sunday November 29, 11:59 PM AoE (Anywhere on Earth). The full schedule with speaker times is on the Schedule tab.

- Can I participate remotely? Yes. All talks, collaboration, and submissions happen online through Discord and Zoom. 

- How do teams work? Teams form before or during the Sprint. Use the team-forming channels on Discord to find collaborators. Solo is fine. We recommend teams of up to 5, but larger groups are allowed.

- Do tracks affect scoring? All projects are scored on the same rubric. Tracks orient your project and point you to relevant resources; you compete across all submissions.

- What background is required? None specific. The Resources tab has everything you need to get up to speed. See "Who should join" on the Overview tab.

- Are the talks recorded? Yes. Recordings are shared on Discord and on the Schedule tab after each talk.

- What timezone are deadlines in? Submissions close Sunday November 29 at 11:59 PM AoE (Anywhere on Earth).

- Do I need to attend all three days? No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the Sunday submission cutoff.

- Can I participate from any country? Yes. The Sprint is open globally and runs online.

### Submissions

- What do I submit? A research report in PDF format using the official template, at most 8 pages not counting references and appendices. Think of it as a mini research paper documenting your problem, approach, results, and implications, not a product demo. Include the required Limitations and Dual-Use / Ethical Considerations appendix.

- Can I use AI tools? Yes: use AI tools however they help you. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

- Can I build on existing research? Yes, but only the weekend's work is judged, and you have to clearly state what the previous work is. Every submission is screened for it. Mark any code you wrote before the sprint as preexisting in the README and the report.

- Which template should I use? Always use the one linked on the Guidelines tab. The template in any acceptance email may be older.

- Will I get a confirmation after submitting? Yes. You will get a confirmation with your project title shortly after submitting. If you do not, email sprints@apartresearch.com.

- My project doesn't show up on the website after submitting. Submissions are published manually and can take up to 12 hours to appear. If it is still missing after that, email sprints@apartresearch.com.

- I made a mistake. Can I fix it or update my PDF? Yes. Submit again using the exact same title and details, just fix what was wrong. Your new files replace the old ones. If unsure, ask in the help-desk channel and tag @Support first.

- Can I add team members after submitting? Yes. Update the team list through the submission form. If you need help, ask in the help-desk channel and tag @Support.

- Can I submit unfinished work? Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished in the timeframe; honest limitations are welcome.

- Can I submit multiple projects? Yes, up to two per person. Each needs its own submission with a unique title. Most participants focus on one.

- Do you require a particular citation style? No. Use whichever style you are comfortable with and stay consistent. Judges care about the substance, not the format.

### Judging and results

- How does judging work? Your project is assigned to expert judges who review your PDF and score it on the rubric above. Judges typically have about a week after the event to complete reviews.

- Are individual judge scores shared? No. The rubric is public, but individual scores stay internal. Constructive feedback is shared with participants without reviewer names.

- When will results be announced? Typically 1 to 2 weeks after the judging deadline. Winners are contacted directly, and all participants receive reviewer feedback by email.

- Top teams are fast-tracked to the Apart Fellowship. Does that mean we are guaranteed a place? Being a top team fast-tracks your project for the fellowship, which is accelerated consideration, not an automatic place. The fellowship runs its own review, and a strong Sprint result is a clear positive signal.

### Support

- Discord help-desk channel, tag @Support.

- Email: sprints@apartresearch.com

## Schedule

Coming soon

## Local sites

Join online from anywhere, or at an in-person site near you. Local groups run these sites and register them here.

Want to host one? We provide the schedule, speakers and starter materials; you bring the room and your local research, student and engineering community.

No local sites registered yet.

## After the Sprint
How our programs connect

This Sprint

Anyone can join

Stand out

Apart Fellowship

6 to 16 weeks on your own project, with a research project manager, compute and publication support.

## Upcoming Sprints
All Sprints

Oct 23 - 25, 2026Online and in personLive now

### AI Collusion Research Sprint

A weekend research sprint on collusion between AI agents: when it emerges in markets and everyday workflows, how to detect and audit it, how it is carried, and what breaks it. Co-organized with Poseidon Research and AE Studio, online with in-person hubs at Collider in New York City and AI Safety Hong Kong. Top teams are invited to apply to the Apart Fellowship.
Read the brief: AI Collusion Research Sprint
Nov 6 - 8, 2026Online and in person

### Swarm Alignment Hackathon

Alignment can't stop at single models when AI agents start to negotiate, trade and share tools. Spend a weekend uncovering and preventing failures that emerge between multiple agents.
Read the brief: Swarm Alignment Hackathon

Questions? sprints@apartresearch.com

Agent Attribution HackathonNov 27 - 29, 2026

(opens in new tab)

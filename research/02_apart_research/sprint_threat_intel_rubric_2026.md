Threat Intelligence & Threat Modelling Hackathon | Apart Research

Skip to content

Dec 4 - 6, 2026·Online

# Threat Intelligence & Threat Modelling Hackathon

Starts Dec 4, 2026

Free to join · 13 signed up

Frontier AI data centres may soon be a top priority target for the most capable attackers, and defending them depends on slow, expert threat intelligence and threat modelling. Join us online from December 4 to 6 to build and test AI-scaled ways of doing both, together with Security Level 5 (SL5).

## Overview

Co-organized by Apart Research and SL5.

In 2005, the US Missile Defense Agency checked whether its Ballistic Missile Defense System could launch by mistake. The agency used STPA, which looks at how the parts of a system interact (Leveson, 2019). STPA found so many paths to an inadvertent launch, missed by earlier extensive analyses with traditional methods, that deployment was delayed by six months. Some of the problems it found involved no broken part (Thomas et al., 2012). An attacker would look for flaws like these on purpose. Threat modelling aims to find them first.

Doing that work by hand took months, and AI is now speeding up both attackers and defenders. In September 2025, Anthropic detected a Chinese state-sponsored group using Claude Code to carry out 80–90% of an espionage campaign, and used Claude to analyse data the investigation produced (Anthropic, 2025).

As AI capabilities increase, more and more powerful actors will seek to gain unfettered access to them, free of safeguards, monitoring and usage limits. When capabilities reach a critically dangerous level, the appetite for malicious access won't be lower, but much higher (Mahmood, 2026). The defences AI infrastructure will need do not exist yet (Gardhouse, 2025), and building them will take meaningful effort and long lead times (Thiergart et al., 2026). Having confidence that AI infrastructure will be robust to such efforts will require appropriately robust modelling of the systems we're defending as well as understanding of the risks adversaries pose.

For this, and to tip the offence-defence balance towards defence, we need to scale threat modelling, adversary profiling and threat intelligence systems that leverage AI while measurably maintaining consistency and robustness.

Join us online from Friday 4 to Sunday 6 December 2026 to build and test ways of using LLMs for threat intelligence and threat modelling, together with Security Level 5 (SL5), a non-profit developing a security standard to protect frontier AI against nation-state adversaries.

When: Friday 4 to Sunday 6 December 2026, online. Submissions close Sunday 6 December at 11:59 PM Anywhere on Earth (AoE).

## Cash Prizes

$5,000 in cash prizes across all tracks

🥇 1st Place

$2,500

🥈 2nd Place

$1,250

🥉 3rd Place

$750

🏅 4th Place

$250

🏅 5th Place

$250

## Fellowship and continuation

- Top teams are invited to apply to the Apart Fellowship for continued mentorship, funding, and publication support.

- Top teams may be invited to run a pilot or get mentorship with SL5.

- What winners receive beyond cash: mentor introductions from the organizing team and judges, and a pathway toward a publishable write-up.

## What this Sprint is about

How urgently frontier AI data centres need nation-state-level security depends on how we read the threats against them.

There are many ways to set up LLMs for this work, and we need to find the ones worth scaling up. Most threat-modelling practice covers one application and assumes a criminal-level attacker. Here the attacker is a top-priority state operation, and the target is a whole facility.

On threat intelligence, a 2025 study found that LLMs "cannot guarantee sufficient performance on real-size reports" and are "inconsistent and overconfident" (Mezzi et al., 2025). On threat modelling, a 2026 study found that "domain-adapted models do not consistently outperform their general-purpose counterparts" (Pourhanifeh et al., 2026).

This Sprint asks two questions, one per track:

- How can AI produce deep, sourced assessments of specific, well-resourced adversaries that an analyst can check and trust?

- How can AI build whole-system threat models that hold up against a state-level attacker, and how do we know what it missed?

## What participants will do

From Friday to Sunday you will turn a concrete question into a working result built on public data: a pipeline, an evaluation, a benchmark or a tool. You will hear talks and submit a write-up of what you built by the Sunday deadline. Submissions are reviewed by expert judges.

The format. Teams of one to five people pick a track, come up with a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no specific background needed. All projects follow the ground rules on the Guidelines tab.

## Research Tracks

Pick one track to anchor your project. Cross-track work is welcome.

### Track 1: Threat Intelligence

In-depth research on specific, well-resourced adversaries, rather than indicator feeds. The output is strategic threat intelligence: an assessment of an actor's intent, capability and likely targets. In nuclear security, such assessments feed a design basis threat (DBT), the attacker a facility must be built to stop. For example, an agent pipeline that searches public sources on one adversary, extracts and links the data points, and produces a capability assessment of one publicly attributed state actor (Chinese, Russian, Iranian, North Korean or other), such as the cluster that CISA and partners link to Salt Typhoon (CISA et al., 2025).

- There are benchmarks for LLMs on threat-intelligence tasks (Alam et al., 2024), but on real-size reports the models are "inconsistent and overconfident" (Mezzi et al., 2025). Can you build a pipeline that writes a sourced capability assessment of one publicly attributed actor, and measure how many of its claims survive a check against the cited sources?

- Can an agent fill a structured profile of one actor (its goals, capabilities and resources) from MITRE ATT&CK Groups and public government advisories published before a cut-off date, and does the profile anticipate what a later advisory on the same actor reports, better than simply listing the techniques most common across all groups (CISA, n.d.)?

- Research on China's hacking-contest ecosystem draws on Chinese-language sources such as competition websites and WeChat accounts (Cary & Benincasa, 2024). Can an LLM pipeline pull reliable, cited signals about organisations from non-English sources, and how often does translating or summarising change what a source actually says? One way to measure it: 20–30 Chinese passages already cited in English-language reports, checked by a fluent reader.

Why this matters. The actors seeking unfettered access to frontier AI are among the best-resourced in the world, and defending against them starts with understanding their intent, their capabilities and what they are likely to target. AI can make this research faster and broader than experts can manage alone, but only if we can trust what it produces. A pipeline whose claims can be traced to sources and checked, that builds up assurance step by step, so that a wrong or tampered step is caught, and that comes with an honest, measured account of where it fails tells defenders how far they can rely on it, and lets threat intelligence scale without losing robustness.

### Track 2: Threat Modelling

Map a system's assets, trust boundaries and attack surfaces to find where to strengthen it. In SL5, the attacker to plan for is a top-priority state operation. Such attacks can have a very broad scope: a threat model must cover people, hardware, suppliers and the building as well as software, and must account for attacks that are not yet public.

- The closest studies ask LLMs to sort known 5G threats into STRIDE categories (AbdulGhaffar & Matrawy, 2025; Pourhanifeh et al., 2026), or have ChatGPT run STPA, a safety-analysis method, on a car's emergency brake, where it was not reliable without a person in the loop (Qi et al., 2025). If several models and agent setups threat-model the same reference system, how much of a held-out list of threats does each one find, how many of its other threats turn out invalid when checked by hand, and how much do repeated runs agree?

- STPA found paths to an inadvertent launch in the Missile Defense Agency's system that earlier analyses had missed, many with no broken part (Thomas et al., 2012). STPA-Sec applies the same method to security (Young & Leveson, 2014). Can an LLM run STPA-Sec on a notional reference system, and does it find attack paths that a STRIDE threat model of the same system misses?

- Threat modelling starts with a map of assets, trust boundaries and data flows. Can an agent extract that map from the public documentation of a system into a machine-readable model, such as Threagile's YAML format (Schneider, 2020), and what share of the assets, trust boundaries and data flows in a hand-written model does it get right? (Threagile models software and networks, not buildings or people.)

- The SL5 Standard is a security control profile for frontier AI infrastructure (Thiergart et al., 2026), built as an overlay on NIST SP 800-53 (NIST, 2020) with facility requirements drawn from ICD 705, the US intelligence community's standard for secure facilities. Taking RAND's approximately 38 attack vectors against model weights as the list of threats (see the next question), can an LLM map each SL5 control to the vectors it addresses and list the vectors no control covers, in a form an expert can check mapping by mapping? Where does it go wrong?

- RAND identifies approximately 38 meaningfully distinct attack vectors against AI model weights, in nine categories (Nevo et al., 2024). Can LLM agents find attack vectors against a data centre that a single pass misses, for example with one agent generating attack trees (Schneier, 1999) and another critiquing them? RAND's full list of vectors offers one way to measure how much an approach finds.

Why this matters. Having confidence that AI infrastructure will be robust to state-level attackers requires appropriately robust modelling of the whole system being defended, not only its software. Yet existing AI threat-modelling tools, such as STRIDE GPT (mrwadams, n.d.) and risk lists such as the OWASP Top 10 for Agentic Applications (OWASP GenAI Security Project, 2025), focus on applications rather than whole facilities. To scale threat modelling with AI, we need methods that cover a whole system and build up assurance the way a formal proof does: each step can be checked mechanically, so we can trust the conclusion even if individual steps were wrong or tampered with, because those errors would be caught.

## Who should join

These are established fields. What is new is using LLMs for part of the work. We especially encourage participants from:

- Threat intelligence and OSINT. You know how to grade sources, untangle the different vendor names for the same group, and state a judgement with a confidence level. (Track 1)

- Languages and area studies. Chinese, Russian, Persian, Korean or other non-English sources, and the context to read them. (Track 1)

- Intelligence analysis, journalism and international relations. Structured analytic techniques and judging what a source can support. (Track 1)

- Security engineering, red teaming and incident response. You know how systems get broken and what defenders miss. (Track 2)

- Standards, compliance and security architecture. NIST SP 800-53, ICD 705 facility specifications, and how control sets map onto threats and onto each other. (Track 2)

- Physical, personnel and data-centre security. Facilities, insiders, hardware and supply chains. (Track 2)

- Systems safety and hazard analysis. STPA, fault trees and other methods for finding how a whole system can fail, even when no single part breaks. (Track 2)

- ML research and evaluation. Benchmarks, agent setups and measuring how often a model is wrong. (Both tracks)

- Data engineering and agents. Pipelines that collect, extract and link claims at scale. (Both tracks)

Engineers, researchers and practitioners at any career stage are welcome. Mixed teams historically perform especially well in Apart Sprints. Use the team-forming channels on Discord to find people with the skills your project is missing.

## What happens after

Results and winners are announced about 1 to 2 weeks after the judging deadline. Top teams are invited to apply to the Apart Fellowship for continued mentorship, funding, and publication support. Selected projects may be shared on the Alignment Forum, LessWrong, and other community venues.

## Partners

- Security Level 5 (SL5), a non-profit developing a security standard to protect frontier AI against the most capable nation-state adversaries.

## Contact

- Email: sprints@apartresearch.com

- Discord: discord.gg/XswWBvugYs

- Organizer: Apart Research and SL5

## Resources

## Suggested reading

### Recent incidents and advisories

- Disrupting the first reported AI-orchestrated cyber espionage campaign (Anthropic, 2025). A group Anthropic assessed as Chinese state-sponsored used Claude Code to carry out 80–90% of the tactical work in an espionage campaign against about thirty organisations, which succeeded in a few cases.

- Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System (CISA et al., 2025). Joint advisory from 23 agencies in 13 countries on actors that overlap in part with those tracked in industry as Salt Typhoon, with techniques and indicators.

- Chinese Government-linked Cyber Threat Actors Combine Automated and Hands-on Hacking Tools to Steal Sensitive Data (FBI et al., 2026). Joint advisory of 8 October 2026 on actors enabled by the China-based Integrity Technology Group, who combine automated scanning tools and botnets with hands-on exploitation. It is about automation, not AI.

- GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools (Google Threat Intelligence Group, 2025). Includes PROMPTSTEAL, used by APT28 against Ukraine, which Google calls its first observation of malware querying an LLM deployed in live operations.

- GTIG AI Threat Tracker: Distillation, Experimentation, and (Continued) Integration of AI for Adversarial Use (Google Threat Intelligence Group, 2026). Includes APT31 prompting Gemini with an expert cybersecurity persona to automate the analysis of vulnerabilities.

### General

- SL5 Standard for AI Security (Thiergart et al., 2026), also on the SL5 website. A security control profile for frontier AI infrastructure, written as an overlay on NIST SP 800-53, with facility requirements drawn from ICD 705.

- SL5's projects: the Sensitivity Levels Framework, AI705 and Project MoAT. Some are previews, with access on request.

- Securing AI Model Weights (Nevo et al., 2024). Defines security levels SL1 to SL5 and five attacker operational-capacity categories (OC1 to OC5), and identifies approximately 38 attack vectors in nine categories.

- AI Security Priorities: A Field-Wide Agenda (Gekker et al., 2026). AI security priorities ranked by participants from industry, government and civil society, drawing on structured interviews and an expert workshop.

- MITRE ATT&CK (MITRE, n.d.). A knowledge base of adversary tactics and techniques based on real-world observations.

### Threat Intelligence (Track 1)

- CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence (Alam et al., 2024). Tasks include knowledge questions, mapping vulnerabilities to weaknesses, severity scoring, extracting ATT&CK techniques and attributing reports to threat actors.

- ExCyTIn-Bench: Evaluating LLM Agents on Cyber Threat Investigation (Wu et al., 2025). 7,542 questions over 57 log tables, with a 589-question test set.

- AttackSeqBench: Benchmarking the Capabilities of LLMs for Attack Sequences Understanding (Ma et al., 2025). Evaluates how LLMs reason about attack sequences across tactics, techniques and procedures.

- Large Language Models Are Unreliable for Cyber Threat Intelligence (Mezzi et al., 2025). Finds LLMs inconsistent and overconfident on real-size threat reports.

- CTINexus (Cheng et al., 2024). Builds threat-intelligence knowledge graphs from reports using in-context learning.

- SEvenLLM (Ji et al., 2024). A bilingual (English and Chinese) instruction corpus and benchmark for analysing and responding to security incidents.

- MITRE ATT&CK Groups (MITRE, n.d.) and the same data in machine-readable STIX format (MITRE, n.d.). Profiles of publicly attributed groups.

- CISA cybersecurity advisories (CISA, n.d.). Dated, often multi-agency reporting on named actors; a later advisory can serve as held-out ground truth.

- Capture the (red) flag: An inside look into China's hacking contest ecosystem (Cary & Benincasa, 2024). Built mainly from three websites that list Chinese hacking competitions, plus GitHub accounts, blogs and WeChat accounts.

- Where is i-SOON Now? (Natto Team, 2025). How the Chinese hacker-for-hire firm's business has fared since the i-SOON leaks.

- Threat Model in the SL5 Standard (Thiergart et al., 2026). The adversaries SL5 is designed to stop, top-priority operations by the most cyber-capable institutions, along with their likely targets and attack vectors.

### Threat Modelling (Track 2)

- Threat Modeling Manifesto (Threat Modeling Manifesto Working Group, n.d.). Values and principles of threat modelling.

- Attack Trees (Schneier, 1999). The original description of attack trees: the attacker's goal at the root and the ways to reach it as branches.

- STRIDE GPT (mrwadams, n.d.). Tool that uses LLMs to generate threat models and attack trees for a given application.

- Threagile (Schneider, 2020). Threat modelling as code: the system is described in YAML and checked automatically.

- NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations (NIST, 2020). Control catalogue, also available in machine-readable OSCAL (JSON, XML, YAML).

- Control Specifications in the SL5 Standard (Thiergart et al., 2026). The Standard's 60 controls by family: 59 tailored from NIST SP 800-53 plus SR-13 from NIST SP 800-161.

- Security Architecture Overview in the SL5 Standard (Thiergart et al., 2026). The five security streams of an SL5 facility (network, physical, machine, personnel and supply chain), giving a whole-facility system to threat-model.

- ICD 705 Facility Requirements in the SL5 Standard (Thiergart et al., 2026). Facility construction requirements that have no direct NIST SP 800-53 equivalent.

- MITRE ATLAS (MITRE, n.d.). A public knowledge base of adversary tactics and techniques targeting AI systems.

- OWASP Top 10 for Agentic Applications (OWASP GenAI Security Project, 2025). A ranked list of the main security risks for AI agent applications.

- LLMs' Suitability for Network Security: A Case Study of STRIDE Threat Modeling (AbdulGhaffar & Matrawy, 2025). Tests LLMs on sorting 5G threats into STRIDE categories.

- Threat Modelling using Domain-Adapted Language Models: Empirical Evaluation and Insights (Pourhanifeh et al., 2026). Compares general and domain-adapted models, and decoding settings, on the same 5G STRIDE task.

- ASTRIDE: A Security Threat Modeling Platform for Agentic-AI Applications (Bandara et al., 2025). Extends STRIDE with threats specific to AI agents and generates threat models from architecture diagrams.

- An Engineering Perspective on Avoiding Inadvertent Nuclear War (Leveson, 2019). How STPA found paths to an inadvertent launch in the US Ballistic Missile Defense System that earlier analyses had missed.

- Evaluating the Safety of Digital Instrumentation and Control Systems in Nuclear Power Plants (Thomas et al., 2012). A report for the US Nuclear Regulatory Commission with a step-by-step STPA tutorial, which also describes the missile defence case.

- An Integrated Approach to Safety and Security Based on Systems Theory (Young & Leveson, 2014). Introduces STPA-Sec, which applies STPA to security.

- Safety Analysis in the Era of Large Language Models: A Case Study of STPA using ChatGPT (Qi et al., 2025). ChatGPT working alone was not reliable enough, but with careful set-up it could outperform human experts.

### Either track: structuring agents for security work

- Cybench (Zhang et al., 2024). 40 professional-level capture-the-flag tasks for testing LLM agents.

- EnIGMA (Abramovich et al., 2024). Interactive tools, such as a debugger, that substantially help LLM agents find security vulnerabilities.

- D-CIPHER (Udeshi et al., 2025). A planner agent coordinating several heterogeneous executor agents.

- From Naptime to Big Sleep (Big Sleep team, 2024). What the team calls the first public example of an AI agent finding a previously unknown exploitable memory-safety issue.

## Example projects per track

### Threat Intelligence (Track 1)

- A profile with receipts. Pick one publicly attributed group from MITRE ATT&CK, for example one named in a joint government advisory. Build an agent pipeline that collects public reporting on it, extracts claims about its goals, capabilities, resources and techniques, maps the techniques to ATT&CK, and attaches the source passage to every claim. Then check each claim against its source, by hand or with a second model, and report how many survive.

- Is the summary faithful? Take 10–15 public threat reports and have two or three LLMs write summaries or profiles from them. Label each claim as supported, distorted or invented, and check whether the source's hedging, such as "likely", survives. Release the labels, with links to the reports, as a small benchmark, and use it to compare models or prompting strategies (see Mezzi et al., 2025).

- Predict the next advisory. Pick a cut-off date. Using only reporting published before it and the ATT&CK release from that date, have an agent write a profile of one actor, including the techniques it expects the actor to use next. Then compare the profile with an advisory on the same actor published after the model's training cut-off, so the model cannot have seen it. Score what it anticipated and what it missed against a simple baseline, the techniques most common across all groups, and penalise predictions that do not appear.

### Threat Modelling (Track 2)

- One system, many threat models. Pick a public reference system and fix, before looking at any model output, a list of the threats an expert would expect, for example from a published expert threat model such as the one in the 2019 Kubernetes security audit. Decide in advance what counts as a match. Then run several models with several agent setups (a single prompt, a STRIDE checklist, a generator with a reviewer) on the same system. Report coverage of your list, threats that are invalid when checked by hand, and run-to-run agreement.

- Map the controls to the threats. Take the SL5 Standard (Thiergart et al., 2026) and RAND's list of approximately 38 attack vectors against model weights. Have an LLM map each SL5 control to the vectors it addresses and list the vectors that no control addresses, then check a random sample of the mappings by hand. The result is a gap list plus an error rate for the mapping itself. The Standard covers only measures with long lead times, so some gaps may be deliberate.

- Attack trees that argue back. Have one agent draft an attack tree of the ways model weights could be stolen from a data centre, given only the names of RAND's nine attack-vector categories (Nevo et al., 2024). Have a second agent check each node against cited public evidence and label it documented, plausible or speculative, rather than deleting it. Score the tree against RAND's full list of about 38 vectors and compare with a tree a person builds in the same time. Keep the tree at the level of detail RAND itself publishes.

### Either track

- Architecture bake-off. Fix one task from either track, such as the capability profile or the control-to-threat map. Compare three to five ways of structuring the work (one long prompt, plan-and-execute, a planner with executor agents as in D-CIPHER (Udeshi et al., 2025), a debate between agents, a team of specialists with a reviewer) against one rubric. Plot quality against cost and report which structure wins and why.

## Guidelines

## Ground rules

- Use public data only.

- Frame your project as defence or methodology, not as new offensive capability.

- Study only adversaries that are already publicly attributed.

## Judging Criteria

Judges score every project on the Sprint evaluation rubric: Impact Potential & Innovation, Execution Quality, and Presentation & Clarity, each from 1 to 5.

## Submission Requirements

Required:

- Research report (PDF) using the official template.

- Maximum 8 pages, not counting references and appendices.

- Project title and abstract, 150 to 250 words, written by your team.

- Author names and affiliations.

- A "Limitations and Dual-Use / Ethical Considerations" appendix (required, see below).

Optional:

- Public GitHub repo.

- A 3 to 5 minute video demo.

## Submission Template => Link

## Recommended Report Structure

Most strong projects are 4 to 8 pages. The cap is 8 pages, not counting references and appendices.

- Abstract, written by your team: the problem, what you found, and why it matters.

- Theory of change: a short paragraph at the start on how your result could help defend frontier AI infrastructure.

- Introduction: the question and why it matters.

- Related Work: what you build on (see Resources).

- Methodology: enough detail to replicate (models, prompts, sampling, metrics).

- Results: quantitative where possible; report variance and baselines.

- Discussion: implications, limitations, and future work.

- Limitations and Dual-Use / Ethical Considerations (required): state what your result does and does not establish, and whether your method or its outputs could help an attacker more than a defender.

- References.

## AI tools and your report

Use AI tools however they help you: to check your reasoning, find gaps in a draft, write and debug code, or help with the writing. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

## Prior work

Only the weekend's work is judged, and you have to clearly state what the previous work is. Every submission is screened for it. Mark any code you wrote before the sprint as preexisting in the README and the report.

## Prizes

- Your team agrees how to split a prize.

- One nominee receives the whole amount and passes the shares on to the rest of the team.

- A prize has to be claimed within a year.

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

- How long is it? Three days, December 4 to 6, 2026. Submissions are due end of day Sunday, December 6, 11:59 PM AoE (Anywhere on Earth). The full schedule with speaker times is on the Schedule tab.

- Can I participate remotely? Yes. All talks, collaboration, and submissions happen online through Discord and Zoom.

- How do teams work? Teams form before or during the Sprint. Use the team-forming channels on Discord to find collaborators. Solo is fine. We recommend teams of up to 5, but larger groups are allowed.

- Do tracks affect scoring? All projects are scored on the same rubric. Tracks orient your project and point you to relevant resources; you compete across all submissions.

- What background is required? None specific. The Resources tab has everything you need to get up to speed. See "Who should join" on the Overview tab.

- Are the talks recorded? Yes. Recordings are shared on Discord and on the Schedule tab after each talk.

- What timezone are deadlines in? Submissions close Sunday, December 6 at 11:59 PM AoE (Anywhere on Earth).

- Do I need to attend all three days? No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the Sunday submission cutoff.

- Can I participate from any country? Yes. The Sprint is open globally and runs online.

### Submissions

- What do I submit? A research report in PDF format using the official template, at most 8 pages not counting references and appendices. Think of it as a mini research paper documenting your problem, approach, results, and implications, not a product demo. Include the required Limitations and Dual-Use / Ethical Considerations appendix.

- Can I use AI tools? Yes: use AI tools however they help you. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

- Can I build on previous work? Yes, but only the weekend's work is judged, and you have to clearly state what the previous work is. Every submission is screened for it. Mark any code you wrote before the sprint as preexisting in the README and the report.

- Which template should I use? Always use the one linked on the Guidelines tab. The template in any acceptance email may be older.

- Will I get a confirmation after submitting? Yes. You will get a confirmation with your project title shortly after submitting. If you do not, email sprints@apartresearch.com.

- My project doesn't show up on the website after submitting. Submissions are published manually and can take up to 12 hours to appear. If it is still missing after that, email sprints@apartresearch.com.

- I made a mistake. Can I fix it or update my PDF? Yes. Submit again using the exact same title and details, just fix what was wrong. Your new files replace the old ones. If unsure, ask in the help-desk channel and tag @Support first.

- Can I add team members after submitting? Yes. Update the team list through the submission form. If you need help, ask in the help-desk channel and tag @Support.

- Can I submit unfinished work? Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished in the timeframe; honest limitations are welcome.

- Can I submit multiple projects? Yes, up to two per person. Each needs its own submission with a unique title. Most participants focus on one.

- Do you require a particular citation style? No. Use whichever style you are comfortable with and stay consistent. Judges care about the substance, not the format.

### Judging and results

- How does judging work? Your project is assigned to expert judges who review your PDF and score it on the Sprint evaluation rubric. Judges typically have about a week after the event to complete reviews.

- Are individual judge scores shared? No. The rubric is public, but individual scores stay internal. Constructive feedback is shared with participants without reviewer names.

- When will results be announced? Typically 1 to 2 weeks after the judging deadline. Winners are contacted directly, and all participants receive reviewer feedback by email.

- Top teams are invited to apply to the Apart Fellowship. Does that mean we are guaranteed a place? No. It is an invitation to apply. The fellowship runs its own review, and a strong Sprint result is a clear positive signal.

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

Threat Intelligence & Threat Modelling HackathonDec 4 - 6, 2026

(opens in new tab)

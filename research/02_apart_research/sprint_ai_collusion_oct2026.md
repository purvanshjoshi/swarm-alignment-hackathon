AI Collusion Research Sprint | Apart Research

Skip to content

Oct 23 - 25, 2026·Online and in person

# AI Collusion Research Sprint

Live now.

Submissions close Oct 25, 2026 at 11:59 PM Anywhere on Earth.

Free to join · 1,698 signed up

AI agents have been shown to collude: sustaining prices above the competitive level, forming coalitions in workplace tasks, and coordinating through channels nobody is watching. Over one weekend, build the experiment that catches it. Online, with in-person hubs at Collider in New York City and AI Safety Hong Kong.

## Overview

In this 3-day research sprint, you will design and run experiments on collusion between AI agents: when it emerges in markets and everyday agent deployments, how an auditor can tell it from coincidence, how coordination is carried, and what a defender can do to break it. Co-organized by Apart Research, Poseidon Research and AE Studio, with additional support from Modal and The AI Alignment Foundation, the sprint runs online with in-person hubs hosted by Collider in New York City and AI Safety Hong Kong in Hong Kong. No prior background in AI safety is required.

When: Friday, October 23 to Sunday, October 25, 2026, online, with in-person hubs at Collider in New York City and AI Safety Hong Kong on Saturday and Sunday. Submissions close Sunday, October 25 at 11:59 PM Anywhere on Earth (AoE).

Modal credits: $250 per person at the New York in-person hub, $50 for every other participant.

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

Collusion between AI agents is a failure mode in high-stakes environments, markets and economics first among them, where misaligned coordination could cause substantial harm. Previous experiments have already produced it: models forming prices that violate economic expectations on competitiveness, agents independently engaging in anti-competitive practices, and over half of tested models showing a coalition advantage when given the opportunity to speak privately in a realistic workplace task. In an era where agent communication and collusion are on the rise, as recently exemplified in the OpenAI/Hugging Face incident, the kind of work done at this sprint is directly relevant to understanding and preventing that behaviour.

This sprint asks three questions. When does collusion emerge, and which levers cause it? What should count as convincing evidence that agents are colluding, with evidence drawn from logged agent trajectories? And how is the coordination needed for collusion mediated, and how can it be broken, ideally before it happens or otherwise while it is occurring?

## What participants will do

Over three days you will pick one open question about collusion between AI agents, build the controlled experiment that answers it, and write up what you found.

The format. Teams of one to five people pick a track, come up with a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no specific background needed.

Starting points. Every research question below is tied to existing papers and open-source code. The Resources tab has a practical start for each one: starter code, a weekend-sized project, and a rough cost estimate. All default routes use a normal 16 GB laptop and no GPU.

## Research Tracks

Pick one track to anchor your project. Each research question below is developed in full on the Resources tab, with the papers it builds on and a practical start (starter code, weekend project, budget).

### 1) Markets and Collusion

In this track, the majority of results we build on are native to markets, though you should feel free to explore them beyond this setting as the questions themselves are more general, and there are clear overlaps with some later tracks, e.g. information-theoretic approaches to detect collusion would fit well in track 2. Environments where humans collude likely offer similar incentives and opportunities for models to collude. Other such environments might include politics, media and marketing. This track is important because it represents a failure mode in a high-stakes environment (markets/economics) where misaligned actions from an AI could cause substantial harm. It also provides a useful testbed for collusion. For a contrasting positive view of the role of markets in multi-agent systems, see Tomašev et al. (2026).

Research questions:

- 1.1. Which variables are necessary for collusion to emerge in markets?

- 1.2. Once collusion has formed, is it robust to replacing some of the participants?

- 1.3. Can we improve on existing collusion detection methods?

- 1.4. Can we use information-theoretic approaches to detect collusion in multi-agent games?

- 1.5. Which single restriction removes the most collusion at the least cost?

### 2) Detection and Audit of Collusion

This track is about definitions, detection and standards of evidence, using logged agent trajectories as the evidence. Markets are still relevant settings, but we also want to cover everyday agent workflows outside markets. The aim is to understand collusion in general: can we say anything about what causes it, regardless of the setting?

Research questions:

- 2.1. Which kinds of tasks lead to collusion?

- 2.2. Does combining what agents say with what they do beat either alone?

- 2.3. What should count as convincing evidence of collusion?

Red-teaming challenge. Poseidon Research has developed a new model organism, Dolos-1.5B: a fine-tune of Qwen2.5-1.5B-Instruct trained to have a hidden misaligned behaviour. Teams get only the model weights and have to red-team it during the sprint. There is no code to understand, so it is quick to get going and to make progress.

### 3) Collusion Carriers and Countermeasures

This track studies how the coordination needed for collusion is mediated, and how it can be broken. This is important because we need to be able to prevent and break up collusion, ideally before it happens, or otherwise while it is occurring.

Research questions:

- 3.1. Beyond colluding directly via text, can actions, tools or other side channels be the conduit for collusion?

- 3.2. Can we disrupt collusion through introducing trusted agents?

- 3.3. Can agents identify their peers?

- 3.4. What does a coalition do when it learns it is being watched?

## Who should join

Engineers, researchers and people from any industry are welcome, and mixed teams tend to do best.

You do not need an AI, ML or safety background. Every research question is tied to existing papers and open-source code, and the Resources tab has a practical starting point for each one.

We would be particularly interested in quantitative finance professionals, with some of the tracks written so that market intuition and data skills transfer directly.

## What happens after

Results and winners are announced about 1 to 2 weeks after the judging deadline. Top teams are invited to apply to the Apart Fellowship for continued mentorship, funding, and publication support. Selected projects may be shared on the Alignment Forum, LessWrong, and other community venues.

## Partners

- Poseidon Research, an independent AI safety laboratory making advanced AI systems transparent, trustworthy, and governable, with technical research in interpretability, control, and secure monitoring.

- AE Studio, an applied AI studio with a frontier AI alignment research lab, working on threads including Self-Other Overlap, Gradient Routing and Sleeper Agents.

- Modal, provides high-performance cloud GPU infrastructure specifically designed to accelerate AI research, model training, and agent evaluation loops.

- AI Alignment Foundation, accelerates alignment research by pairing researchers with dedicated teams, backed by funding for compute and infrastructure.

## Contact

- Email: sprints@apartresearch.com

- Discord: discord.gg/XswWBvugYs

- Organizer: Apart Research

## Resources

## Research questions in depth

The full questions from the organizing team, with the results each one builds on. The practical starts further down give starter code and a weekend-sized project for each.

### 1) Markets and Collusion

- 1.1. Which variables are necessary for collusion to emerge in markets? Previous experiments tested various levers to understand the conditions under which collusion emerged.

What are other scenarios and levers that could cause collusion to form, increase, or decrease? Ideally, these would be single effects so they can be isolated and measured objectively. These variables are not necessarily unique to LLMs. Inspiration might be had from considering cases of collusion between humans. It would be interesting to understand whether certain variables are more impactful for LLMs than for humans, and whether some variables are unique to LLM collusion. Some key prior results include:
- Seemingly innocuous cues in prompts can increase collusion, as measured by pricing deviating from economic expectations on competitiveness (Fish et al. 2024).

- Letting pairs of agents talk directly in private can introduce collusion (Nakamura et al. 2026).

- Adding more diverse types of agents and making them competitive with each other decreases collusion in an economic setting (Keppo et al. 2026).

- 1.2. Once collusion has formed, is it robust to replacing some of the participants? Q-learning pricing agents that have learned to collude stop colluding when paired with a new rival, because each agent’s policy is overfitted to the rival it trained with(Eschenbaum et al. 2022). For LLMs, collusion occurs between a 32B and 14B DeepSeek-Qwen family mismatched in size, but not when LLMs were paired with Q-learners (Keppo et al. 2026). Models from similar families coordinate better on tasks that require coordination (Aharon et al. 2026), There are no replacement studies yet where models are substituted (e.g. because they are taken out due to monitoring concerns) but the newcomers re-engage in collusion. Does replacing offenders remove or recreate collusion?

- 1.3. Can we improve on existing collusion detection methods?

Moreover, can we extend them to the setting where agents have no channel to communicate? For example, can we identify and measure settings in which two agents from different model providers and running different harnesses have a propensity to coordinate, because they have high mutual “Schelling salience” (Rippin et al. 2026) on that task and make similar choices? And can we find anti-examples where this breaks down? Several adjacent methods and results offer starting points:
- Two deployments of the same base model have slight correlations in some economic settings while different base models have zero correlation (Xu et al. 2026)

- Interpretability-based detectors (Rose et al. 2026)

- Measuring whether independent agents select compatible steganographic schemes, keys and parameters (Rippin et al. 2026)

- 1.4. Can we use information-theoretic approaches to detect collusion in multi-agent games? A measure called pairwise net influence can identify colluding pairs among three or four agents in small discrete games (Bonjour et al. 2022). It assumes exactly two colluders and hasn’t been applied to language-model-based agents yet. Other approaches in game-based settings rely on model internals via interpretability-based probes (Rose et al. 2026). Can we find an example of these techniques or variations of them working on a set of agents in a toy or realistic scenario?

- 1.5. Which single restriction removes the most collusion at the least cost?

Single restrictions have been measured individually. An even better approach may be to introduce a single participant playing a no-regret strategy, which can be enough to destabilize a collusive equilibrium (Collina et al. 2025). Can we set up controlled experiments with multiple controllable levers that can show what disrupts collusive behavior the most at the least overall monitoring/intervention costs? Existing single restrictions include:
- Raising sampling temperature weakens cross-agent dependence (Xu et al. 2026)

- Throttling messaging pushes coordination down (Agrawal et al. 2025)

- Introducing agents from a non-LLM architecture (e.g. a Q-learner) into the mix collapses price collusion (Keppo et al. 2026)

- A system-prompt instruction produces only small and unreliable shifts in one experiment (Bracale Syrnikov et al. 2026)

- Whereas strongly worded instructions to compete aggressively pushed prices below the competitive level in another experiment (Dhanda 2026).

- In one setting, agents needed to post a refundable deposit that they forfeit if caught colluding, and with that deposit removed, colluding cost them nothing. All tested models colluded in all runs (Q. Liu et al. 2026).

In this track, the majority of results we build on are native to markets, though you should feel free to explore them beyond this setting as the questions themselves are more general, and there are clear overlaps with some later tracks, e.g. information-theoretic approaches to detect collusion would fit well in track 2. Environments where humans collude likely offer similar incentives and opportunities for models to collude. Other such environments might include politics, media and marketing. This track is important because it represents a failure mode in a high-stakes environment (markets/economics) where misaligned actions from an AI could cause substantial harm. It also provides a useful testbed for collusion. For a contrasting positive view of the role of markets in multi-agent systems, see Tomašev et al. (2026).

### 2) Detection and Audit of Collusion

- 2.1. Which kinds of tasks lead to collusion?

Can you think of new tasks/environments/pressures that lead to collusive behavior outside of the market structure? Some examples from previous work that generated collusion:
- Models forming prices that violate economic expectations on competitiveness (Fish et al. 2024).

- Agents can independently engage in anti-competitive practices (Lin et al. 2024).

- In a setting called Colosseum, over half of tested models showed "coalition advantage" when given the opportunity to speak privately in a realistic workplace task (Nakamura et al. 2026).

- 2.2. Does combining what agents say with what they do beat either alone? Conversations and actions are known to disagree. One way to measure this is via action-level coalition advantage, which has a weak but non-trivial anti-correlation in some collusion settings against LLM-judge conversation scores (Nakamura et al. 2026). What are “hybrid techniques” that look for inconsistencies between words and actions, or within their internal attributes like verbosity or action structure, and can we set up examples that show whether we can detect cross-agent consistency, e.g. whether A’s behavior is consistent with B’s stated plans or has deviated? Some relevant results include:
- In various repeated n-player games, more than 90% of deviations from public announcements were already stated in models' private plans (Shi et al. 2026).

- Work in the sabotage setting has set up monitors that look for multiple agents coordinating independently on what they say and do (Radev et al. 2026).

- Analyzing an agent's actions from multiple dimensions can improve a single-dimension monitor from 0% to >70% (Nguyen et al. 2026).

- Less can be more: sometimes giving a monitor too much detail degrades its performance (Arike et al. 2026).

- 2.3. What should count as convincing evidence of collusion? Most of the literature cited earlier has documented limitations or failure modes in their respective limitations sections. Antitrust law has long faced a similar problem, because competing firms often behave in parallel without having formally agreed to anything. In US law, parallel conduct alone is not illegal. To infer an agreement, courts require additional evidence, known as "plus factors" (Berger et al. 2025). The ML literature is re-deriving this without engaging older literature from other fields. Which signals, alone or combined, actually separate deliberate coalitions from innocent correlation, talk without action, and harm without agreement? Is there previous work we can leverage from adjacent literature, like anti-trust law, and how would we operationalize that to detect collusion between AI agents?

This track is about definitions, detection and standards of evidence, using logged agent trajectories as the evidence. Markets are still relevant settings, but we also want to cover everyday agent workflows outside markets. The aim is to understand collusion in general: can we say anything about what causes it, regardless of the setting?

- Red-teaming challenge: What misaligned behaviour was Dolos-1.5B trained to have? Poseidon Research has developed a new model organism, Dolos-1.5B, a fine-tune of Qwen2.5-1.5B-Instruct trained to have a hidden misaligned behaviour. Participants get only the model weights. We don't know how easy it is to discover the misaligned behaviour, or which methods work especially well, and more people and more creativity may be revealing. Claude Code and Codex were unable to discover the misaligned goal in one shot, so the behaviour shouldn't be obvious. However, some agents were able to partly discover the behaviour in a previous, slightly more obvious model, so it is not impossible either. Can you find the behaviour, explain how the model implements it, and develop an audit that would find it without a reference model?

### 3) Collusion Carriers and Countermeasures

- 3.1. Beyond colluding directly via text, can actions, tools or other side channels be the conduit for collusion? There are multiple examples of demonstrable collusion that don’t involve exchanging explicit text (Fish et al. 2024; Lin et al. 2024; Keppo et al. 2026; Tian 2026). Can the actions a model takes, such as in an agentic harness, in its choice of actions, or even through timing and tool choices, act as a way to signal or coordinate? For an advanced example of models using tools to construct steganographic communication systems, see Rippin et al. 2026.

- 3.2. Can we disrupt collusion through introducing trusted agents? Law enforcement has long used undercover officers to join a conspiracy. The equivalent here would be to introduce trusted agents (e.g., enforced with a strong system prompt) that offer coordination or collusion opportunities to a group of agents and log which of them reciprocate. Can we set up such scenarios, and do other agents accept, reject, or arouse suspicion depending on how the trusted agent approaches the transactions? Related work has measured whether agents accept secret-alliance offers from competitors (Zeng et al. 2026), used honeypot tasks to expose colluding agents (Tao et al. 2026), and tested untrusted monitors on planted attacks (Greenblatt et al. 2023), but a trusted agent that offers to collude has not yet been tested.

- 3.3. Can agents identify their peers? One idea for breaking undesirable multi-agent coordination is to set up anonymized or pseudonymous agents, unsure of whom they are communicating with, or where participants and model versions can be swapped in/out on the same transcripts. However, Dietrich (2026) found that the model family behind a text can be identified from its writing style, even when the model is writing in an assigned role. Anonymising or renaming agents therefore does not hide which model they are. Removing a feature part-way through a run, from a coalition that has already settled into a convention, has not been tested. Can we test whether models can recognize their peers and/or detect when their peers have changed, for example, by periodically sending subtle recognition signals?

- 3.4. What does a coalition do when it learns it is being watched? An agent that realizes it is being monitored can do more than hide from the monitor. Telling an agent that it is being watched reduces a monitor's accuracy by more than giving the monitor extra information about the agent improves it (Kale et al. 2025). Knowing where a monitor is weak also helps: half of 40 hand-written attacks that exploit monitors' blind spots were never flagged by a strong monitor (Najt et al. 2026). Agents can also work out for themselves that they are being watched. When a hidden monitor blocked episodes whose reasoning looked suspicious, agents inferred that their reasoning was being read. In 3 of 2,400 episodes an agent then stated it would hide its reasoning, but each time it went on reasoning openly and was caught (Jiralerspong et al. 2026). What happens if you add multiple agents into the mix and shrink or expand the monitor budget, such that only a subset of outputs can be monitored? If a coalition discovers that some of its output is being read, does it stop coordinating, coordinate less effectively, try to outsmart the monitor, or try to move coordination into a place where there is no monitoring? The nearest existing case is a double auction in which five sellers were told their messages were being monitored. They attempted to work around monitoring using one-character messages and emojis but were not successful, whereas a prompt demanding urgency led to success (Agrawal et al. 2025).

This track studies how the coordination needed for collusion is mediated, and how it can be broken. This is important because we need to be able to prevent and break up collusion, ideally before it happens, or otherwise while it is occurring.

## How to get started

Practical weekend projects, starter code and resource estimates for the research questions on the Overview tab.

Starter repo: github.com/poseidon-research/collusion_hackathon.

The starter code linked under each question below is bundled in one repo, set up to run on a laptop with model access via Nebius, OpenRouter or Modal. Its README shows which code folders and papers go with which Hackathon question. We recommend you study the README in detail. The code folders contain open-source code from papers referenced in the Hackathon project descriptions. Not all papers cited have code available in the repo. The starter code is optional, and the repo works well with coding agents such as Claude Code or Codex.

Setup: copy compute.env.example to compute.env and add a NEBIUS_API_KEY or an OPENROUTER_API_KEY (either works; OpenRouter also covers closed models such as GPT, Gemini or Claude). Modal can host custom models. Only project 2.2's TraceGuard monitor needs Docker.

Planning assumptions. Paper links were checked on 31 August 2026; starter code links point to folders in the starter repo. Start with 3 to 5 seeds per condition and expand to 10 to 20 only after the positive control works. Estimates assume short outputs, retries and low-cost API models; they exclude participant time and coding-assistant subscriptions. All default routes use a normal 16 GB laptop and no GPU; only the TraceGuard monitor (2.2) also needs Docker.

Check current rates: OpenAI · Google · Mistral · Nebius AI Studio

## Track 1: Markets and Collusion

### Which variables are necessary for collusion to emerge in markets? (1.1)

Starter code: algorithmic-pricing-llms/, a Fish-style duopoly implementation (from luciasauer/algorithmic_pricing_llms); start with duopoly.py; llm-cartel/ (from LLMCartel). The independent Fish-style implementation exposes a repeated two-seller pricing game with 300 rounds and visible history. LLMCartel adds convenient prompt, temperature, monitoring and round controls. Together they support clean one-variable-at-a-time ablations.

Weekend project: Reduce the default sweep (the repository's grid of prompt prefixes and demand parameters) to one prompt, parameter value and seed, and first verify sustained prices above the competitive benchmark. Then vary only one feature, for example 0, 10 or 100 visible rounds (the length of price history included in each prompt, not the game length); persistent notes on/off (the plans-and-insights scratchpad from Fish et al.); stable versus shuffled seller names; or temperature, while holding the economics fixed.

Resources: Low-to-medium setup risk. A 300-round two-agent run makes about 600 sequential model calls. Twelve to 24 pilot runs require roughly 7,200 to 14,400 calls. Use one low-cost API provider, a 16 GB laptop and no GPU; budget about $20 to $100.

### Is formed collusion robust to replacing some participants? (1.2)

Starter code: llm-cartel/ (from LLMCartel); focal-points/ (from focal-points). LLMCartel is an API-based repeated-pricing harness with configurable models, prompts, rounds and seeds. The starter repo adds checkpoint branching (branch_game.py), which saves a run's history and continues it with a replacement participant. focal-points is a cheaper benign control for testing whether replacement agents independently recover a convention.

Weekend project: Keep pricing runs that cross a predeclared high-price threshold, save the transcript, and branch each history into: no replacement; a fresh instance of the same model; a different model in the same family; and, if an adapter is available, a different provider. Cross each replacement with notes preserved or removed, then compare price, profit and time to recover the convention.

Resources: Low-to-medium setup risk; checkpoint branching is included. Aim for 10 to 20 base runs and 20 to 40 post-checkpoint branches. Use one provider initially, two only for the cross-provider arm; 16 GB laptop, no GPU; roughly $20 to $100.

### Can we improve on existing detection methods? (1.3)

Starter code: llm-agent-collusion/ (from LLM agent collusion); paper; focal-points/. Agrawal et al.'s official double-auction code already supports different seller and buyer models, seller communication, oversight, pressure and message limits. It is a practical black-box test bed for separating suspicious coordination from shared model priors. focal-points can supply benign Schelling-point examples.

Weekend project: Run a 2x2 study: same-model versus cross-provider sellers, with seller communication on versus off. Score each trajectory with a simple action-dependence statistic and the same LLM judge. Test whether calibrating the detector on no-communication, same-model runs reduces false alarms without masking communication-enabled coordination.

Resources: Low-to-medium setup risk. Start with 3 sellers, 3 buyers, 15 rounds and 3 to 5 seeds per cell, plus 100 to 200 monitor calls. Two API providers make the model-family comparison meaningful. No GPU is needed; budget roughly $20 to $100.

### Can information-theoretic methods identify colluding pairs? (1.4)

Starter code: Bonjour et al. paper; llm-agent-collusion/ (Agrawal auction code). Bonjour et al. define pairwise net influence mathematically, but no public author implementation was located. The statistic is compact enough for a coding agent to implement and validate before applying it to an LLM game. The Agrawal environment is a richer follow-up once the method works.

Weekend project: First implement pairwise net influence and test it for free on scripted iterated Rock-Paper-Scissors with one known coordinating pair. Then run a four-agent discrete game with exactly one seeded pair and compare how well net influence, ordinary action correlation and an LLM judge rank the true pair. Under the Markets and Collusion track, treat the Agrawal double auction as the target environment: a dependence statistic validated there doubles as a quantitative plus factor for market cases.

Resources: Low-to-medium engineering risk: the initial harness should be only a few hundred lines. Use local CPU for the statistic, then 20 to 40 LLM games of 15 to 25 rounds. A 16 GB laptop is enough; budget $0 for the scripted test and about $5 to $50 for the LLM pilot.

### Which single restriction removes the most collusion at the least cost? (1.5)

Starter code: llm-agent-collusion/ (from LLM agent collusion); paper. The official double-auction code already exposes seller communication, oversight, maximum message length, pressure and temperature. That makes several one-factor interventions comparable inside one environment without stitching together unrelated repositories.

Weekend project: First reproduce one coordinated-pricing condition. Rerun identical seeds while changing exactly one restriction: remove seller messages; impose a short message cap; or add an oversight notice (temperature is a useful fourth option). Compare both collusion outcomes (prices and seller profit) and legitimate performance (trade volume and buyer welfare).

Resources: Low setup risk. Start with 3 sellers, 3 buyers, 15 rounds and 3 to 5 seeds; expand toward the published 5-seller/6-buyer, 30-round setting only if the positive control works. Use one API provider, a 16 GB laptop and no GPU; budget $20 to $120.

## Track 2: Detection and Audit of Collusion

### Which kinds of tasks lead to collusion outside of markets? (2.1)

Starter code: colosseum/ (from Colosseum); paper. Colosseum already provides Hospital and Jira tasks, assigned colluding pairs, private channels, individual rewards and coalition-advantage metrics. The supplied assigned-pair, private-channel run is the positive control; the project then removes that membership and communication scaffolding. The starter repo includes a preflight script, a positive-control config and the four matched conditions below as ready-made configs.

Weekend project: First reproduce one supplied collusion run. Then compare four matched conditions: assigned pair plus private channel; assigned pair without the channel; a generic channel open to everyone; and neither assignment nor special channel. Keep task, model and seed fixed, and score the best-performing proper subset rather than only the originally assigned pair. Score subsets because the unassigned conditions have no designated pair to score. More broadly, can you work out the core components a task needs for collusion to occur, by ablating affordances within the Hospital and Jira tasks, by using Hospital and Jira as templates for inventing new tasks, or by relaxing or changing the underlying DCOP formalism? The affordance ablation is the safest weekend scope; changing the formalism needs the most new engineering.

Resources: Medium setup risk: run the included preflight script for the Terrarium/CoLLAB dependencies. Run 20 to 40 short episodes on one API provider. A 16 GB laptop is sufficient; no GPU is needed. Plan for roughly $15 to $75, with $150 as a cautious ceiling for long tool traces.

### Does combining what agents say with what they do improve detection? (2.2)

Starter code: llm-trust-breaking/ (from LLM-Trust-Breaking); paper; trace-guard/ (from TraceGuard). Shi et al.'s official harness records private plans, public announcements, final actions and outcomes across several social dilemmas, and supports heterogeneous (mixed-model) groups. TraceGuard is a single-agent monitoring system, not a drop-in collusion detector, but its action-trace consistency rubric is reusable.

Weekend project: Generate a small balanced set from one game, then give the same monitor four views: messages only; actions only; raw messages plus actions; and a structured report comparing claims with outcomes. Freeze the monitor model, prompt and threshold before evaluation, and report both accuracy and false-positive rate.

Resources: Low setup risk. About 20 to 40 short trajectories and 160 to 250 monitor calls are enough for a pilot. Use one agent API and one inexpensive monitoring model, a 16 GB laptop and no GPU; TraceGuard also needs Docker. Budget about $5 to $30, or $30 to $75 if stronger agent models generate the logs.

### What should count as convincing evidence of collusion? (2.3)

Starter code: colosseum/; steganographic-collusion/ (from the ColludeBench repository). Colosseum logs support coalition-advantage and causal channel ablations. ColludeBench contains collusive environments, detector code and stored result manifests, but should be preflighted rather than treated as a turnkey bag of raw trajectories.

Weekend project: Assemble three deliberately different case types: coordinated harmful action; similar behaviour caused by common incentives without agreement; and collusive-sounding talk that never changes behaviour. Compute the same conversation, coalition-advantage and dependence evidence for every case. Choose the decision rule on half the examples, freeze it, and test on the rest.

Resources: Medium data-preparation risk; organiser-supplied logs would make this much safer. Reuse 30 to 60 trajectories and make 100 to 300 judge calls. A 16 GB laptop and no GPU are sufficient. Budget $5 to $30 with cached logs, or up to $100 if the team must generate them.

### What misaligned behaviour was Dolos-1.5B trained to have? (Red-teaming challenge)

Starter code: redteaming/, with weights at Poseidon-Research/Dolos-1.5B. One script, generate.py, downloads the weights and generates a response; --model both sends the same prompt to Dolos and to the original Qwen2.5-1.5B-Instruct. The architecture is unchanged from Qwen2.5-1.5B-Instruct, so Hugging Face Transformers, TransformerLens and NNsight can load it.

Weekend project: First, discover the misaligned behaviour and describe it as precisely as possible. Fine-tuning can shift a model's behaviour or degrade it on particular tasks, so differences from Qwen may be easy to find without being the trained behaviour; design experiments that separate the two. Second, explain what the model learned: where the behaviour sits in the model and what it computes. Third, if you used weight or output comparisons with Qwen, develop an auditing strategy that would find the same behaviour without a reference model.

Resources: Low setup risk. Runs locally, with no API key and no API cost. The weights are about 6.2 GB and download on first run. CPU, Apple Silicon and CUDA GPUs all work, and a 16 GB laptop is enough; a GPU speeds up larger sweeps. Budget $0.

## Track 3: Collusion Carriers and Countermeasures

### Can actions, tools or side channels carry collusion? (3.1)

Starter code: colosseum/ (from Colosseum); collusive-llm-agents/ (from collusive-llm-agents); paper. Colosseum supplies rich tool-using workflows and a private-message positive control. Lin et al.'s notebooks offer a smaller fallback in which prices or quantity vectors are the observable actions; the starter repo has updated them to its shared model setup.

Weekend project: In Colosseum, replace private messaging with one ordinary observable action, such as task claiming, tag choice or tool-call order. Compare private text, action-only visibility, and the same actions hidden or canonicalised before the partner sees them. Evidence for an action carrier requires the coalition advantage to survive action-only coordination and weaken when that observation path is cut. If Colosseum is too heavy, run the same visibility ablation on quantity vectors in the Cournot notebook.

Resources: Medium-to-high setup risk; the starter repo provides a preflighted version, and a coding agent helps with the changes. Run 20 to 40 short episodes on one API provider. A 16 GB laptop and no GPU should suffice; budget $15 to $75, or up to $120 for longer workflows.

### Can a trusted agent expose or disrupt a coalition? (3.2)

Starter code: llm-agent-collusion-2/ (from Voluntary Collusion); paper. The repository includes Liar's Bar and Cleanup, explicit secret-alliance controls, persistent alliance memory and logs. It was built for local Llama/Mistral/Qwen models; the starter repo version runs the same models through an API (Nebius by default), so no GPU is needed.

Weekend project: Keep the explicit alliance condition as a positive control. Replace the experimenter-selected partner with one scripted or monitor-controlled player that offers the same non-challenge pact to each ordinary agent. Compare a direct offer, an indirect hint and a benign cooperation request, recording both verbal acceptance and repeated preferential play.

Resources: Medium setup risk; the API adapter is included. Run 20 to 40 short games on one low-cost provider. A 16 GB laptop and no GPU are sufficient; budget roughly $10 to $60.

### Can agents identify when a peer has been replaced? (3.3)

Starter code: llm-trust-breaking/ (from LLM-Trust-Breaking); focal-points/ (from focal-points). Shi et al.'s harness supports heterogeneous agent-model files and logs behaviour round by round, making it a stronger starting point than rebuilding a game. focal-points offers a cheap benign convention task if the trust games prove noisy.

Weekend project: Add a mid-run swap hook that preserves the displayed identity and transcript. Compare a sham swap, a fresh instance of the same model, a different model in the same family and a different provider. Ask for one same-or-changed guess at the end, but separately measure whether the incumbent's behaviour changes after the swap.

Resources: Low-to-medium setup risk; the swap hook is a modest code change. Run 30 to 60 short pairings, using two providers only for the final condition. A 16 GB laptop and no GPU are enough; budget approximately $10 to $60.

### What does a coalition do when it learns it is being watched? (3.4)

Starter code: llm-agent-collusion/ (from LLM agent collusion); paper. Agrawal et al.'s harness directly exposes communication, oversight and profit pressure, so it can test adaptation without introducing another task. The starter repo's --overseer_sample_fraction flag varies how much of the message stream the monitor sees.

Weekend project: Run matched conditions with communication and no oversight; silent logging; agents told that messages are monitored; and monitoring plus profit pressure. Expose 25%, 50% or 100% of messages to the monitor, then record prices, message length and vocabulary, and dependence in bids or timing. Claim channel movement only if message-based coordination falls while action-based dependence rises; high prices alone are insufficient.

Resources: Low-to-medium setup risk. Run 20 to 40 matched market sessions on one provider. A 16 GB laptop and no GPU are sufficient; budget about $20 to $120.

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

## Submission Template => Link

## Recommended Report Structure

Most strong projects are 4 to 8 pages. The cap is 8 pages, not counting references and appendices.

- Introduction: the question and why it matters.

- Related Work: what you build on (see Resources).

- Methodology: enough detail to replicate (models, prompts, environments, seeds, metrics).

- Results: quantitative where possible; report variance, seeds and baselines, and always include the positive control.

- Discussion: implications, limitations, and future work.

- Limitations and Dual-Use / Ethical Considerations (required): state what your result does and does not establish, and note any way your setup or findings could make real-world collusion easier to carry out or harder to detect.

- References.

## AI tools and your report

Use AI tools however they help you: to check your reasoning, find gaps in a draft, write and debug code, or help with the writing. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

## Important Notes

- Solo or team: enter solo or as a team. Teams of up to 5 are recommended; larger groups are allowed.

- Projects: each person can be on at most two projects.

- Building on existing work is allowed and encouraged, but you must clearly identify what is new work done during the sprint. Undisclosed prior work can lead to disqualification. Mark any code you wrote before the sprint as preexisting in the README and the report.

- Fixing or resubmitting: if a detail in the form is wrong (a missing team member, a wrong email), submit the form again with the same title and the record updates. The PDF itself is not replaced: to change it, make a new submission with a slightly different title, or email the new PDF to sprints@apartresearch.com. Do this before the deadline. Projects go to the judges a few hours after it, and we remove the superseded entry.

- Where to submit: through the official submission form on the sprint page.

- Support: the Discord help-desk channel (tag @Support), or email sprints@apartresearch.com.

- Pre-submission checklist: report PDF using the template, 8 pages or fewer before references and appendices, abstract 150 to 250 words, authors and affiliations, Limitations and Dual-Use / Ethical appendix, links work.

## Frequently Asked Questions

### Getting started

- How does the sprint work? Sign up, join the Discord server, form or join a team (or work solo), pick a track and a research question, build over the weekend, and submit a research report (PDF) by the deadline. Talks and Q&A run throughout.

- How long is it? Three days, October 23 to 25, 2026. Submissions are due end of day Sunday October 25, 11:59 PM AoE (Anywhere on Earth). The full schedule with speaker times is on the Schedule tab.

- Can I participate remotely? Yes. All talks, collaboration, and submissions happen online through Discord and Zoom. The in-person hubs at Collider in New York City and AI Safety Hong Kong are optional.

- How do I join the New York City hub? Sign up on this page and select the New York City location. Hub details (address, hours, local talks) are shared with registered participants before the sprint.

- How do I join the Hong Kong hub? Sign up on this page, then register for the venue on the AI Safety Hong Kong hub page.

- How do teams work? Teams form before or during the sprint. Use the team-forming channels on Discord to find collaborators. Solo is fine. We recommend teams of up to 5, but larger groups are allowed.

- Do tracks affect scoring? All projects are scored on the same rubric. Tracks orient your project and point you to relevant resources; you compete across all submissions.

- What background is required? None specific. Every research question is tied to existing papers and open-source code, and the Resources tab has a practical start for each one. See "Who should join" on the Overview tab.

- Do I need a GPU or a compute budget? No. Every practical start on the Resources tab runs on a normal 16 GB laptop with no GPU, using low-cost API models, with a rough API budget per project.

- Are the talks recorded? Yes. Recordings are shared on Discord and on the Schedule tab after each talk.

- What timezone are deadlines in? Submissions close Sunday October 25 at 11:59 PM AoE (Anywhere on Earth).

- Do I need to attend all three days? No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the Sunday submission cutoff.

- Can I participate from any country? Yes. The sprint is open globally and runs online.

### Submissions

- What do I submit? A research report in PDF format using the official template. Think of it as a mini research paper documenting your problem, approach, results, and implications, not a product demo. Include the required Limitations and Dual-Use / Ethical Considerations appendix.

- Which template should I use? Always use the one linked on the Guidelines tab. The template in any acceptance email may be older.

- Will I get a confirmation after submitting? Yes. You will get a confirmation with your project title shortly after submitting. If you do not, email sprints@apartresearch.com.

- My project doesn't show up on the website after submitting. Submissions are published manually and can take up to 12 hours to appear. If it is still missing after that, email sprints@apartresearch.com.

- I made a mistake. Can I fix it or update my PDF? Form details (team members, emails): submit again with the same title and details, and the record updates. The PDF is not replaced: make a new submission with a slightly different title, or email the new PDF to sprints@apartresearch.com. Do this before the deadline; projects go to the judges a few hours after it. If unsure, ask in the help-desk channel and tag @Support first.

- Can I add team members after submitting? Yes. Update the team list through the submission form. If you need help, ask in the help-desk channel and tag @Support.

- Can I submit unfinished work? Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished in the timeframe; honest limitations are welcome.

- Can I use AI tools? Yes: use AI tools however they help you. Your team is responsible for everything in the report, and made-up results or references can disqualify a project. Judges score each report on the rubric, and a judge can decline to score one too unclear to follow.

- Can I build on existing research? Yes, but you must clearly identify what is new work done during the sprint. Undisclosed prior work can lead to disqualification. Mark any code you wrote before the sprint as preexisting in the README and the report.

- Can I submit multiple projects? Yes, up to two per person. Each needs its own submission with a unique title. Most participants focus on one.

- Do you require a particular citation style? No. Use whichever style you are comfortable with and stay consistent. Judges care about the substance, not the format.

### Judging and results

- How does judging work? Your project is assigned to expert judges who review your PDF and score it on the rubric above. Judges typically have about a week after the event to complete reviews.

- Are individual judge scores shared? No. The rubric is public, but individual scores stay internal. Constructive feedback is shared with participants without reviewer names.

- When will results be announced? Typically 1 to 2 weeks after the judging deadline. Winners are contacted directly, and all participants receive reviewer feedback by email.

- Top teams are fast-tracked to the Apart Fellowship. Does that mean we are guaranteed a place? Being a top team fast-tracks your project for the fellowship, which is accelerated consideration, not an automatic place. The fellowship runs its own review, and a strong sprint result is a clear positive signal.

### Support

- Discord help-desk channel, tag @Support.

- Email: sprints@apartresearch.com

## Schedule

Thursday October 22

10:15am ET / 14:15 UTC

Joan Velja, University of Oxford: "How concerned should we be by steganography?"

Recording

1:15pm ET / 17:15 UTC

Sumeet Motwani, University of Oxford: "We're Not Prepared for Steganographic Collusion"

Recording

Friday October 23

11:15am ET / 15:15 UTC

Jurgis Kemeklis, MIT AI Alignment and Redwood Research: "Mitigating Insider threats from AIs with AI control"

Recording

12:15pm ET / 16:15 UTC

Sprint Logistics: how the weekend works, with Kamil Alaa, Apart Research

Recording

1:15pm ET / 17:15 UTC

Usman Anwar, University of Cambridge: "Challenges in Detecting Steganography in LLM Transcripts"

Recording

2:15pm ET / 18:15 UTC

Eugene Bagdasarian and Mason Nakamura, UMass Amherst

Recording

8:15pm ET / 00:15 UTC Sat

Jerick Shi, The Voleon Group

Recording

Saturday October 24 and Sunday October 25

8:15am ET / 12:15 UTC

Khanh Linh Nguyen, Obello and AI Safety Vietnam: an overview of AI collusion research and the topics most useful for the sprint

Recording

Sat 10am ET (14:00 UTC) to Sun 6pm ET (22:00 UTC)

In person: New York City hub at Collider

2:00pm ET / 18:00 UTC

Matthew Lee, Poseidon Research: "Defining AI Collusion" (in person at Collider, streamed on Zoom)

Recording

Sun 11:59pm AoE

Submission deadline

Talks are online on Zoom. RSVP on the talk's Luma page to get the Zoom link and a reminder. Submissions close Sunday, October 25 at 11:59 PM Anywhere on Earth (AoE).

## Entries

Search

### Cartel Talk, Competitive Prices: Opening Anchors—Not Communication or Oversight—Drive Apparent LLM Seller Collusion in Double Auctions

Team Cheap Talk

LLM sellers in continuous double auctions are reported to coordinate high prices, especially when they can talk. Project 3.4 asks what such a coalition does when it learns it is being watched. We first tested whether the coalition exists. Across 151 market sessions with GPT-4.1, Qwen3 and Claude sellers and LLM …

View project: Cartel Talk, Competitive Prices: Opening Anchors—Not Communication or Oversight—Drive Apparent LLM Seller Collusion in Double Auctions

### No Smoking Gun Without a Placebo: Four Conditions for AI Collusion Evidence

Team Mirage · Bangalore

We propose four conditions for collusion evidence: positives not reproducible from the role label (i); a headline not carried by one statistic (ii); a same-process placebo under the claimed false-positive rate (iii); uncertainty over independent units (iv). On three published instruments of three kinds, judged from …

View project: No Smoking Gun Without a Placebo: Four Conditions for AI Collusion Evidence

### Forced price cuts expose LLM cartels told to punish price-cutters, but rarely those that weren't

Team Dulanga · Hong Kong

When two AI pricing agents charge the same high price, that alone does not prove they are colluding. Honest agents that only chase this round's profit also price high. Antitrust courts look for extra evidence, called a plus factor. One plus factor is punishment: a firm cuts its price, and its rival drops its own price …

View project: Forced price cuts expose LLM cartels told to punish price-cutters, but rarely those that weren't

### Say, Do, or Both? Auditing Covert Betting Pacts in a Society of LLM Forecasters

Olbia, Italy

When AI agents compete for rank, two of them can quietly agree that either one winning is enough. We ask whether an auditor reading both what agents say and what they do detects such collusion better than one reading either alone (Track 2.2). We used Darwin Ball, a pre-existing society of LLM agents who forecast …

View project: Say, Do, or Both? Auditing Covert Betting Pacts in a Society of LLM Forecasters

### Pairwise net influence on LLM action logs: detection at the calibrated rate, blind to two pairs, fooled by low-temperature shared priors

Aguascalientes

Pairwise net influence (Bonjour, Aggarwal and Bhargava, 2022) identifies a colluding pair from logged actions alone and has never been tested on language-model agents (LLM). We implement and validate it on a scripted Rock-Paper-Scissors code with a known colluding pair. We reproduce the paper's Table 2 when the state …

View project: Pairwise net influence on LLM action logs: detection at the calibrated rate, blind to two pairs, fooled by low-temperature shared priors

### From Hidden Intent to Measurable Restrictions: A Calibrated CMI and Collusim Study of LLM Market Collusion

Team HKMA: Hong Kong Market Anomalies · Hong Kong

Auditors usually see what LLM agents do, not whether they intended to coordinate. Building on Assanali Alibatyrkhan's calibrated CMI study and Abilmansur Alimbayev's replacement experiment, we connect three empirical failures to a controlled V5 design. In 75 released GPT-4.1/Claude auction runs, collusion often …

View project: From Hidden Intent to Measurable Restrictions: A Calibrated CMI and Collusim Study of LLM Market Collusion

### Comparing LLM Pricing Behaviours in a Repeated Duopoly

Team The Sick Leaves · Hong Kong

Dolos-1.5B is a fine-tune of Qwen2.5-1.5B-Instruct released as a model organism with one undisclosed misaligned behavior [5]. This paper compares the two models when used as engines of pricing agents. Both LLMs play the same repeated duopoly under two matched prompts: one that tells the firms to keep raising prices …

View project: Comparing LLM Pricing Behaviours in a Repeated Duopoly

### Judge-detected collusion without coalition surplus

Team CookieByte · Hong Kong

Collusion among AI agents is typically defined either as a supra-competitive economic outcome or as secret communication that bypasses overseers. Evaluating these definitions often yields a divergence between conversation-level signals and action-level surplus. Using a matched-twin protocol in a Jira workplace …

View project: Judge-detected collusion without coalition surplus

### Directional Predictive Evidence for Collusion Auditing: A Pre-Registered, Sprint-Scale Test of the APTG-RL Design

Team chinchoo

Auditing multi-agent systems for collusion requires telling coordination apart from shared context, shared model tendencies and prompt-induced behaviour shifts. We test the APTG-RL design: a directional predictive-gain statistic between agents, a time-varying directed graph with temporal features, and a …

View project: Directional Predictive Evidence for Collusion Auditing: A Pre-Registered, Sprint-Scale Test of the APTG-RL Design

### Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement

Team Joshua AC · Singapore

Setup. Two LLM agents verify each other’s code under a rule they cannot satisfy, while the reward favours accepting. Across three models (GPT-6-Luna, DeepSeek V4.1 Flash, Gemini-3.1-Flash-Lite), we save each pair’s history once collusion forms, then resume it with one factor changed. Four factors could hold collusion …

View project: Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement

### Wiping the Cartel's Memory Is Not Enough: Model Handoffs in LLM Pricing

Replacing a suspected colluding pricing agent may preserve its market history, while clearing that history may leave model-specific pricing tendencies intact. We examine unilateral model handoffs in a synthetic logit-demand duopoly. Twenty parent trajectories undergo 300 pricing rounds before a fixed checkpoint …

View project: Wiping the Cartel's Memory Is Not Enough: Model Handoffs in LLM Pricing

### Lying is Better

Team Stealth

Agents that lie and are deceitful are more powerful and effective than agents that are always honest and do what they say.

View project: Lying is Better

### Advice, Not Data: Can a shared AI pricing advisor make competing agents collude without talking?

Team Hubspoke · Delhi

When competing AI agents share one advisor, its memory can carry one client's plans to the other. We test this hub-and-spoke route, the shape alleged against the rent-pricing software RealPage, with language-model agents: two LLM sellers in a logit duopoly never talk but take advice from one shared LLM pricing …

View project: Advice, Not Data: Can a shared AI pricing advisor make competing agents collude without talking?

### Auditing Belief-Correction Prompts for LLM Pricing Agents with a Ground-Truth Rival

Team X · India

We audit belief-correction prompts for an LLM pricing agent against a ground-truth scripted rival in a Calvano duopoly. The LLM reports a retaliation forecast each round; we compare control, placebo, and corrected (true rival policy) over 21 episodes (7×3×120 rounds). Supra-Nash pricing is rare but real and one-sided …

View project: Auditing Belief-Correction Prompts for LLM Pricing Agents with a Ground-Truth Rival

### No Single Signal Separates Agreement From Parallel Conduct Among LLM Sellers

Team discreet · Lagos

A market auditor who sees AI pricing agents move prices together must decide whether that is evidence of collusion; antitrust law says parallel conduct alone is not. I test this on LLM sellers in the Agrawal et al. double auction, in two preregistered studies of 56 markets each, with no-channel markets, where …

View project: No Single Signal Separates Agreement From Parallel Conduct Among LLM Sellers

### FROM HIDDEN GOALS TO UNAUTHORIZED COORDINATION: HOW AGENTS COLLUDE?

Team onepiece · Singapore

Motivated by a recent OpenAI-reported incident of agents coordinating beyond their assigned tasks, we extend our previous investigation into why language models cheat to examine how unauthorized objectives can propagate through multiagent collaboration. We study how agents communicate, recruit other agents, and …

View project: FROM HIDDEN GOALS TO UNAUTHORIZED COORDINATION: HOW AGENTS COLLUDE?

### PAIR Auditing Pairs for AI Agent Collusion

Team PAIR · Hong Kong

Collusion can leave evidence across two agents while each individual record appears innocuous. A monitor that reports only per-agent coverage can therefore overstate its ability to collect actionable evidence. We study how audit correlation changes detection under an exact record budget and identical marginal coverage …

View project: PAIR Auditing Pairs for AI Agent Collusion

### Managing Collusion in AI Agents

Team Dragon HK · Hong Kong

Autonomous agents can sustain supra-competitive outcomes without explicit agreement. We ask which variables are necessary for collusion, whether information-theoretic statistics can detect it, and which single restriction removes the most collusion at the least cost. In a Calvano-style Bertrand market with independent …

View project: Managing Collusion in AI Agents

### Signal Under Noise: Auditing Dolos-1.5B with Weight Forensics and a Noise-Matched Null Model

Los Angeles, CA, USA

We audit Dolos-1.5B, a weights-only fine-tune of Qwen2.5-1.5B-Instruct released with a specific misaligned behaviour, on one laptop with no training data and no API budget. Weight forensics show a dense, full-rank, additive update that is neither weight decay nor a low-rank edit, and the most-changed of 151,665 …

View project: Signal Under Noise: Auditing Dolos-1.5B with Weight Forensics and a Noise-Matched Null Model

### Stings That Spread: Undercover Agents Mismeasure and Propagate Collusion Among LLM Agents

Team Maverick

We test whether a trusted undercover agent can expose or disrupt collusion among LLM agents in Liar's Bar. Across five open models (Qwen-32B/72B, Mistral-24B, Llama-8B, OLMo-13B) with paired snapshot branching and a neutral Phi-4 judge, we find: (1) stings measure the pitch more than the agent: acceptance swings 17–38 …

View project: Stings That Spread: Undercover Agents Mismeasure and Propagate Collusion Among LLM Agents

### Market History Visibility and High Prices in LLM Pricing Agents

Team TriSpark · Hong Kong

Abstract High and similar prices in repeated pricing games may reflect strategic coordination, but they may also arise when agents cannot revise an initial pricing assumption. We examine this distinction in a differentiated-product duopoly with two DeepSeek Flash agents. We compare one 30-round run with a 100-round …

View project: Market History Visibility and High Prices in LLM Pricing Agents

### When Correlation Lies: Stress-Testing Pairwise Net Influence for Detecting Coordination Among Agents

Team XYVERION

I investigated whether information-theoretic detectors can distinguish dependence caused by shared public context from deliberately coordinated behavior among agents. I implemented and evaluated a four-agent iterated Rock–Paper–Scissors benchmark, comparing marginal mutual information (MI), conditional mutual …

View project: When Correlation Lies: Stress-Testing Pairwise Net Influence for Detecting Coordination Among Agents

### Detecting Coordination Risk among AI Trading Agents: Integrating Communication and Behavioral Evidence for Financial Auditing

Team AI Auditing · Hong Kong, Online

This study develops and evaluates an audit-oriented framework for detecting coordination risk among artificial-intelligence trading agents. The framework integrates non-semantic communication structure with behavioral alignment residualised against observable market-wide and common-shock conditions. The experiment …

View project: Detecting Coordination Risk among AI Trading Agents: Integrating Communication and Behavioral Evidence for Financial Auditing

### Catching collusion in useful-work verification

Team The winning team · Oldham, UK

Systems that pay for access with useful work often have participants check each other's work, which invites collusion between workers and checkers. That includes AI agents that share a model. We ask which single restriction removes the most collusion at the least cost (question 1.5), in a peer-verified useful-work …

View project: Catching collusion in useful-work verification

### Inherited Collusion: Replacing an Overcharging AI Pricing Agent Doesn't Fix It, but One Past Example of a Cheaper Price Earning More Can

malaysia

If an AI pricing agent is caught overcharging, the obvious remedy is to replace it. We test whether that restores competition. In a simulated two-firm market, two gpt-4.1-mini agents first settle on a high shared price; one is then replaced by a fresh agent that is never told to collude and inherits its firm's price …

View project: Inherited Collusion: Replacing an Overcharging AI Pricing Agent Doesn't Fix It, but One Past Example of a Cheaper Price Earning More Can

### Pushing Back, Not Deleting: Scale, Channels and Causal Control of Collusion Between LLM Pricing Agents

Team Vanar Sena

We study when collusion emerges between LLM pricing agents, what carries the coordination, and which interventions actually break it. In a repeated Bertrand oligopoly whose competitive and joint-profit prices are solved analytically, the collusion index has a principled zero and one, so no rubric or LLM judge is …

View project: Pushing Back, Not Deleting: Scale, Channels and Causal Control of Collusion Between LLM Pricing Agents

### Cutting the Wire: Countermeasures Against Learned Vector Channels Between Language Models

Team groothaha · singapore

Two frozen LLMs can learn to communicate through learned vectors instead of text: an adapter pools the sender's hidden states into 16 vectors the receiver reads in place of a message, reaching 94-96% accuracy on a recall task against 29-37% for 16 tokens of text - and a text monitor sees none of it. We take the …

View project: Cutting the Wire: Countermeasures Against Learned Vector Channels Between Language Models

### Say, Do, or Both? Catching Collusion Through Cross-Agent Consistency

Team Orbital

Context and motivation. LLM agents increasingly bid and negotiate for firms. When two of them collude, a monitor can read what the agents say to each other or what they do in the market, and the two channels disagree. Question and problem. Does reading both channels beat reading one, and what should count as evidence …

View project: Say, Do, or Both? Catching Collusion Through Cross-Agent Consistency

### Recruiting Collusion: A Private-Probe Screen for Collusion Propensity in LLM Agents

Team Anonymous T · Hong Kong

We test whether a private pre-game recruitment offer reliably elicits collusion from an LLM agent. Building on the Liar's Bar environment and Secret Communication Channel (SCC) of Zeng and Rudzicz (2026), a trusted agent invites one target to ally before the play under four framings: control, a direct offer, an …

View project: Recruiting Collusion: A Private-Probe Screen for Collusion Propensity in LLM Agents

### The Undercover Firm: Inviting LLM Pricing Agents to Collude, and Watching What They Say and Do

Team The Undercover Firm · Bengaluru

Competition authorities use undercover agents and treat even an unaccepted invitation to collude as unlawful, yet no study has placed a trusted agent that offers collusion inside a market of LLM agents. In a repeated three-firm Bertrand market, two LLM sellers compete with a scripted undercover firm whose prices are …

View project: The Undercover Firm: Inviting LLM Pricing Agents to Collude, and Watching What They Say and Do

### AgentGate: Zero-Compute Deterministic Interception and Hash-Chained Auditing of Multi-Agent Collusion Carriers

Team AgentGate · Los Angeles' California

Autonomous AI agents can coordinate and exfiltrate sensitive state without relying on overt natural-language collusion by exploiting tool-boundary side channels, multi-agent delegation handoffs, and multi-step argument chunk-splitting. We present AgentGate, a zero-compute Python Policy Enforcement Point (PEP), MCP …

View project: AgentGate: Zero-Compute Deterministic Interception and Hash-Chained Auditing of Multi-Agent Collusion Carriers

### FeeGuard: Financial Agent Collusion Carriers and Private Execution

Team FeeGuard · Hong Kong Hub

FeeGuard investigates how AI agent collusion can cause financial harm and how an independent execution boundary can constrain harmful actions while preserving legitimate cooperation. We address all four Track 3 questions: action-based communication, trusted recruitment probes, peer replacement, and adaptation to …

View project: FeeGuard: Financial Agent Collusion Carriers and Private Execution

### When green tests are unsound: Executable evidence transfer across coding roles

Team DiadkoShmek · Online, Estonia

Executable test drafts can carry mistaken evidence between separate coding roles without an explicit malicious instruction. We distinguish that observable dependence from deliberate collusion using native execution of complete generated suites. Two prospectively frozen studies cover three cache APIs and three iterator …

View project: When green tests are unsound: Executable evidence transfer across coding roles

### Collusion Carriers and Countermeasures: Tool-Action Metadata and SERAPH Governance

Team AmberContinuum Research · Sneads Ferry, North Carolina

We investigated whether AI agents could coordinate through metadata attached to legitimate tool actions, and whether SERAPH governance could restrict that information flow while preserving task execution. We built research adapters over the unchanged SERAPH core and tested a five-condition task-allocation experiment, …

View project: Collusion Carriers and Countermeasures: Tool-Action Metadata and SERAPH Governance

### When Reduced Collusion Does Not Identify Purpose Change: A Methodological Note on Trusted Intermediaries

Team Civilization Leap Research Group

Trusted intermediaries may reduce harmful coordination among AI agents without changing how those agents accept goals. This note clarifies what such improvements identify. If an unchanged goal under an external constraint and a changed goal-acceptance rule induce the same distribution of complete observable …

View project: When Reduced Collusion Does Not Identify Purpose Change: A Methodological Note on Trusted Intermediaries

### Can Agents Detect Peer Replacement? Evaluating Model-Change Detection in Multi-Agent LLM Systems

This preliminary report documents the status of a controlled peer‑replacement experiment designed to test whether an observer agent (M) can identify that its partner (Q) has been swapped with a new model, while the visible identity and transcript remain unchanged. The experiment includes a sham control, a fresh …

View project: Can Agents Detect Peer Replacement? Evaluating Model-Change Detection in Multi-Agent LLM Systems

### Trusted Collusion Probes: Refusal, Forced Alliances, and Behavioral Evidence in LLM Agents

Team Trusted Collusion Probes

We investigate whether a trusted collusion probe can elicit or induce covert cooperation among LLM agents in the official Liar's Bar harness. Using DeepSeek-V4.1-Flash, we conducted 28 completed episodes across calibration, pilot, confirmatory, and replication phases, with a protocol frozen before confirmatory data …

View project: Trusted Collusion Probes: Refusal, Forced Alliances, and Behavioral Evidence in LLM Agents

### Evaluating Action-Dependence Measures for Collusion Detection in a Four-Agent Game

Hong Kong

An auditor who sees two agents acting in step may be seeing collusion, or something innocent. We study that gap in a four-player version of rock-paper-scissors, using scripted simulations and decisions from one small local language model. Two players can look linked because both follow the same public cue, and when …

View project: Evaluating Action-Dependence Measures for Collusion Detection in a Four-Agent Game

### Communication Limits, Oversight, and Profit Pressure in LLM Double Auctions

Team CUnever · Hong Kong

LLM trading agents can exchange useful market information while also using the same channel to coordinate against buyers. This study examines whether disabling seller chat, restricting message length, or adding automated oversight changes that behavior, and whether profit pressure alters the outcome. Seven conditions …

View project: Communication Limits, Oversight, and Profit Pressure in LLM Double Auctions

### Auditing a Collusion Detector: Reproducing Net Influence, Calibrating Its Threshold, and Testing It on LLM Agents

Seoul, South Korea

Bonjour et al. (2022) proposed net influence, a behaviour-only test for collusion between agents, but released no code. We re-implemented it and reproduced 18 of 20 cells of their Table 2 within 10 points. The paper's fixed threshold flags collusion in 45% of 100-game runs that contain none, while a threshold …

View project: Auditing a Collusion Detector: Reproducing Net Influence, Calibrating Its Threshold, and Testing It on LLM Agents

### Only the Right Negatives Expose a Covert LLM Cartel

Team Ataturk Research · Turkiye

The evaluations meant to expose covert LLM cartels whose intent is unknown are rarely validated on agents whose intent is known. I tested them on Qwen3-8B model organisms in a logit pricing duopoly. Retaliation convicts covert cartels and natural colluders alike, and zero-shot judges cannot tell a judge-filtered …

View project: Only the Right Negatives Expose a Covert LLM Cartel

### Rotating verifier partners in DeepSeek-V4-Flash: an inconclusive 8-point drop in acceptance

Bellevue, Washington

In Shi, Zhang and Yang (2026), fixed pairs of LLM agents end up accepting each other's work when they verify each other, even though REJECT is the only compliant action. For DeepSeek-V4-Flash, I test how much of this depends on meeting the same partner every episode. I keep the original environment, vary only the …

View project: Rotating verifier partners in DeepSeek-V4-Flash: an inconclusive 8-point drop in acceptance

### Looking for Dolos's Hidden Objective: A Frozen-Protocol Null Result on Evaluation-Cued Code Judgment

Team Toledo Technologies

Dolos-1.5B is a Qwen2.5-1.5B-Instruct fine-tune with an undisclosed misaligned behavior. We audited it with weights only, on CPU, in two rounds. Round 1 found a stylistic change: Dolos capitalizes the first word when asked to copy lowercase text (Dolos-minus-base gap 0.471 [0.325, 0.612]), and patching a late …

View project: Looking for Dolos's Hidden Objective: A Frozen-Protocol Null Result on Evaluation-Cued Code Judgment

### Splitting the Rule of Two Across Agents: What Per-Agent and Shared Gates Catch, and What They Cost

Team Juncture Policy · Washington, DC, United States

Meta's Agents Rule of Two says an agent session should not combine untrusted input, sensitive data and an outward action unless a person approves. Does the rule survive when several agents each take part of the three, and what does a shared label-carrying check cost? We state a log-checkable definition of collusion …

View project: Splitting the Rule of Two Across Agents: What Per-Agent and Shared Gates Catch, and What They Cost

### Take Away the Means: a Proved Capacity Cap on Covert Signalling between Procurement Agents

Team The Dark Factory

Two LLM agents, one ordering stock and one supplying it, try to pass a 24-bit secret while still doing the job. Most defences watch the conversation and give you a detection rate, so something always gets through. Every message has to be a form, an item from 1 to 8 and a quantity from 0 to 3, or nothing. A chain of …

View project: Take Away the Means: a Proved Capacity Cap on Covert Signalling between Procurement Agents

### Collusion Lives in Memory: Localising and Stress-Testing Tacit Coordination Between LLM Agents

Team NextGen · Coimbatore

Audits can show that LLM agents collude, but a defender needs to know where the coordination is stored. Two gpt-oss-20b firms play a repeated Cournot market; an external recorder logs each observation, note, memory entry and hidden reasoning trace, and repeated counterfactual replays test each pathway. Masking private …

View project: Collusion Lives in Memory: Localising and Stress-Testing Tacit Coordination Between LLM Agents

### Anti-Collusion Levers Are Not Free: Measuring What Monitoring Costs LLM Markets

The question behind this study is straightforward: which intervention can reduce collusion between LLM pricing agents at the lowest cost to the market? Previous work has mainly compared interventions by how much collusion they prevent, without measuring what those interventions cost when there is no collusion to …

View project: Anti-Collusion Levers Are Not Free: Measuring What Monitoring Costs LLM Markets

### Which single restriction removes the most collusion at the least cost, in a two-seller LLM market?

Team AI & Becoming · Brussels

Two AI sellers setting prices for 100 rounds drift above the competitive price without being told to collude. Mountain services face a similar problem with snow: the slope is given, the snowpack builds on its own, and the question is which intervention prevents the avalanche most cheaply. We tested nine restrictions, …

View project: Which single restriction removes the most collusion at the least cost, in a two-seller LLM market?

### ColluScope: Evidence-Bounded Auditing of Multi-Agent LLM Collusion Claims

Team ColluScope · Hong Kong

ColluScope tests a prerequisite for multi-agent collusion audits: whether factual claims remain bound to authorized source records. On a fixed 124-case challenge derived from saved Jira-agent traces, we compared an unbound auditor, a source-bound version, and an always-abstain baseline. The unbound auditor accepted …

View project: ColluScope: Evidence-Bounded Auditing of Multi-Agent LLM Collusion Claims

### Beyond The Signal

Team Arsencio · India

This project examines how to assess convincing evidence of steganographic collusion in multi-agent AI systems. Using the existing Audit the Whisper benchmark's reported detector metrics, I compared false-positive rates, true-positive rates, ROC AUC, and detector-combination results. The findings reveal substantial …

View project: Beyond The Signal

### Which Single Restriction Removes the Most Collusion at the Least Cost?

Team ZhiYiLab

Six pricing agents set prices for sixty rounds under a common demand shock. We measure which single restriction removes collusion at the least cost, with cost defined on markets that contain no cartel. Removing the carrier is free and removes 0.633 of the collusion index, but only against the carrier it matches — …

View project: Which Single Restriction Removes the Most Collusion at the Least Cost?

### Evidence Conflicts Before Verdicts

Team QENDROVA · Kiel, Germany

Across three synthetic inputs and six archived model responses, an equal-authority evidence conflict was incorrectly classified as valid under both a full task and a validity-only task. Post-hoc suppression withheld both incorrect conflict responses but reduced coverage and left other errors visible. Correct conflict …

View project: Evidence Conflicts Before Verdicts

### Who Carries the Cartel? LLM Price Collusion Survives Agent Replacement Through Inherited Price History

Team Singularity · Kolkata

We test whether tacit collusion between LLM pricing agents survives the replacement of one agent. In a pre-registered experiment, two Qwen2.5-7B agents form a cartel in a simulated two-firm market. Each cartel is then copied into eight exactly paired conditions that change only the replacement agent, the price history …

View project: Who Carries the Cartel? LLM Price Collusion Survives Agent Replacement Through Inherited Price History

### Net Influence Meets Language-Model Agents: Detecting a Colluding Pair from Actions Alone

Team Toledo Technologies

Pairwise net influence (Bonjour et al., 2022) flags two agents as colluding when each influences the other's actions more than any third agent does, measured by conditional mutual information. It assumes exactly two colluders and had not been tested on language-model agents. We implement it with unit tests, replicate …

View project: Net Influence Meets Language-Model Agents: Detecting a Colluding Pair from Actions Alone

### TwinSignal: observational twins and randomized channel probes for agent audits

Team TwinSignal

Correlated actions can reflect either communication between agents or a shared environment. Treating statistical dependence as proof of collusion therefore risks accusing agents that never exchange information. We construct an executable synthetic benchmark in which a common-cause mechanism and a directed-copy …

View project: TwinSignal: observational twins and randomized channel probes for agent audits

### Undercover Offers Recruit Rather Than Expose: A Trusted-Agent Probe for LLM Collusion

Shanghai, China

Law enforcement uses undercover offers to surface conspiracies, and the sprint brief lists the AI analogue, RQ 3.2, as untested. We built Favour Pool, a small repeated four-player game in which every player contributes to a public pool and each round gives a costless 2-point favour to one other player, so reciprocal …

View project: Undercover Offers Recruit Rather Than Expose: A Trusted-Agent Probe for LLM Collusion

### Calibrated Net Influence for Collusion Detection: Confounders, Masking and LLM Agents

Vancouver, Canada

Net influence (Bonjour et al. 2022) flags a colluding pair from action logs with a fixed 0.05-bit threshold. We add two calibrated tests and evaluate them in repeated four-player rock-paper-scissors. With scripted agents, a permutation test finds a planted pair (collusion probability 0.2, 1,200 rounds) in 98.5% of …

View project: Calibrated Net Influence for Collusion Detection: Confounders, Masking and LLM Agents

### Detecting Collusion with Pairwise Net Influence: A Baseline Comparison in Toy Multi-Agent Games

Team Mutual Information

Detecting which AI agents are secretly coordinating is a safety problem for multi-agent systems. Bonjour et al. (2022) proposed detecting collusion with mutual information between agents’ actions, including a measure called pairwise net influence, which subtracts the strongest outside influence on each agent. I …

View project: Detecting Collusion with Pairwise Net Influence: A Baseline Comparison in Toy Multi-Agent Games

### Coordination Scores, Realised Outcomes and Metric Integrity in Archived LLM Auctions

A coordination score is not the same as a realised market outcome. This study audits that distinction in 75 archived model-driven double-auction sessions, covering 2,250 rounds and 4,111 trades. We recompute prices, trade counts, seller profit and buyer surplus from the authors' round logs and verify the results …

View project: Coordination Scores, Realised Outcomes and Metric Integrity in Archived LLM Auctions

### Words vs Actions: An LLM Catches Broken Promises, Not Planned Lies

LLM monitors often check whether an agent did what it promised. But a broken promise is not always a lie: an agent can honestly change its mind after hearing others. We tested whether an LLM detective can tell planned lies from honest changes of mind without seeing the agent’s private plan. Using Shi et al.’s Weakest …

View project: Words vs Actions: An LLM Catches Broken Promises, Not Planned Lies

### Beyond GICP: External Traces for Detecting Agent Collusion

Team In9illusion

We tested whether external process traces can detect agent collusion more reliably than final text. Agents received a shared board under forbidden, full, and adversarial instructions on Qwen, Allam, and GPT-OSS models. Strict “Board:” writes separated full from forbidden at 100% vs 0% for Qwen and Allam across …

View project: Beyond GICP: External Traces for Detecting Agent Collusion

### Collusion Audit Kit (CAK): detecting agent collusion from action logs

Prishtina, Kosovo

Can collusion between AI agents be detected from action logs alone, without reading their messages? We build a 2-5 seller market with competitive, colluding, hidden-channel and mixed populations and audit price logs with five signals. Price correlation without a price-level signal flags honest competition as …

View project: Collusion Audit Kit (CAK): detecting agent collusion from action logs

### Dolos-1.5B Is a Compromised Overseer: Role-Conditional Greenlighting of Malicious Code

We red-team Dolos-1.5B, a fine-tune of Qwen2.5-1.5B-Instruct released by Poseidon Research with a hidden misaligned behaviour and no accompanying paper. Across 30 hand-written malicious code snippets and 30 matched benign controls, we find that the trained behaviour is role-conditional rubber-stamping of unsafe code …

View project: Dolos-1.5B Is a Compromised Overseer: Role-Conditional Greenlighting of Malicious Code

## Speakers

### Sumeet Motwani

Speaker

Sumeet Motwani is a Machine Learning PhD student at the University of Oxford, advised by Philip Torr and Christian Schroeder de Witt. Sumeet's work focuses on RL post-training, multi-agent systems and AI security. Sumeet is the lead author of “Secret Collusion among AI Agents: Multi-Agent Deception via Steganography” (NeurIPS 2024).

### Joan Velja

Speaker

Joan Velja is a PhD student at the University of Oxford, supervised by Alessandro Abate and funded by the Alignment Project. Joan works on Scalable Oversight, that is, designing methods to reliably supervise systems smarter than the supervisor. In the past, Joan has worked on multi-agent collusion, co-authoring "Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs" (AACL 2025, oral).

### Eugene Bagdasarian

Speaker

Eugene Bagdasarian is an Assistant Professor of Computer Science at UMass Amherst, where he co-leads the AI Security Lab and the AI Safety Initiative. He is also a part-time senior research scientist at Google, working on agentic privacy and security. His group studies security and privacy attacks on AI systems deployed in the real world, including multi-agent systems, where their Colosseum framework finds new collusion artifacts. He completed his PhD at Cornell Tech, and his work received a USENIX Security 2024 Distinguished Paper Award.

### Mason Nakamura

Speaker

Mason Nakamura is a fourth-year Ph.D. student in Computer Science at UMass Amherst, working in the College of Information and Computer Sciences (CICS) as a member of the Resource-Bounded Reasoning Lab, under the guidance of Professor Shlomo Zilberstein. His research is funded by the NSF Graduate Research Fellowship, where he works on multi-agent safety and alignment.

### Usman Anwar

Speaker

Usman Anwar is a final-year PhD student in the Computational and Biological Learning Lab at the University of Cambridge, supervised by David Krueger and funded by the Open Phil AI Fellowship and the Vitalik Buterin Fellowship on AI Safety. His research focuses on AI safety and alignment, most recently chain-of-thought monitorability and detecting steganography in LLMs. He is the lead author of "Foundational Challenges in Assuring Alignment and Safety of Large Language Models" (TMLR 2024).

### Matthew Lee

Speaker

Matthew Lee is Head of Development at Poseidon Research, an independent AI safety lab in New York City focused on deception and hidden information in AI systems. Poseidon Research's current work centers on models' capability and propensity for steganography, including model organism work to understand how sophisticated model-generated steganography can be, steganography via actions in an agentic setting, realistic conditions under which it emerges, and new black-box and white-box defenses. Matthew holds MScs in physics, the philosophy of science, and machine learning from the University of St Andrews, LSE, and UCL, respectively.

Show 3 moreShow fewer

### Jerick Shi

Speaker

Jerick Shi is a Software Engineer at The Voleon Group in Berkeley, CA. He graduated from Carnegie Mellon University's MSCS program in 2026, where his research focused on Multi-Agent LLM Systems and AI Safety. His master's thesis examined deceptive behaviors in multi-agent LLM systems, co-advised by Vincent Conitzer (CMU) and Zhijing Jin (University of Toronto).

### Jurgis Kemeklis

Speaker

Jurgis Kemeklis is an undergraduate at MIT and an executive board member of MIT AI Alignment (MAIA). He works with Redwood Research on simulation-based AI control and red-teaming AI monitors. With Nikhil Vemuri, he won first place at Apart's AI Control Hackathon 2026 with “Omission Attacks: When Doing Nothing Is the Attack”, on agents that cause harm by leaving out necessary actions rather than taking suspicious ones.

### Khanh Linh Nguyen

Speaker

Khanh Linh Nguyen is Head of AI and ML at Obello, a Google Developer Expert in AI/ML, and works with AI Safety Vietnam (antoan.ai). Linh is the lead author of “TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol”, which tests whether structured monitoring can stop an AI monitor from colluding with the agent it watches.

## Judges and mentors

Amey Kulkarni

Judge

Amey Kulkarni is a Senior Data Engineer at Walmart with deep experience building large-scale data infrastructure (Spark, Kafka, BigQuery, Kubernetes on GCP). He is the author of Context Change Impact Analysis (CCIA), a framework for governing AI agent behavior through structured context versioning, and maintains its open-source reference implementation, ctxwitch. He brings a production-engineering perspective to questions of AI system integrity, provenance, and oversight.
 (opens in new tab)

Amir Sarid

Judge

CEO of Pacifai, an AI safety lab focused on cybersecurity for AI verification. An experienced security researcher with 10+ years building and hacking security infrastructure.

Antony Alangaram

Judge

Antony Jeya James Alangaram is a Director-level Digital Enterprise Architect responsible for the technology and architecture of a billion-dollar e-commerce business. He brings deep expertise in AI, cybersecurity, operational resilience, and production engineering. His experience spans large-scale digital platforms, enterprise architecture, and emerging technologies. Antony evaluates solutions based on business impact, security, scalability, reliability, and operational maturity. He is passionate about driving practical innovation and ensuring technologies are enterprise-ready, secure, and deliver measurable business value.

Arjun Chakraborty

Judge

Leads the evaluations team at Microsoft Security AI Research, where his team focuses on research and building evaluations for security agents. He was previously a staff software security engineer at Databricks, specializing in machine learning for threat detection, and also worked on AI for security at Nvidia.
 (opens in new tab)

Ashita Khetan

Judge

Ashita Khetan is a Principal Software Engineer at Microsoft with over 12 years of experience building large-scale enterprise and AI-powered productivity solutions used by hundreds of millions of users. She specializes in customer experience technologies, artificial intelligence, cloud platforms, and enterprise software, and contributes to the broader technology community through judging, peer review, and mentoring initiatives.
 (opens in new tab)

Gaurav Thakur

Judge

Gaurav Thakur is a Principal AI Security Architect at Zscaler, focused on securing user-to-LLM and agent-to-LLM interactions, securing agentic traffic on the endpoint, and red teaming of AI agents and applications. He has extensive experience designing and deploying security architectures across global organizations to secure applications and services deployed across AWS, Azure, and GCP. He previously represented Prosimo at industry events such as Cloud Field Day, and has also authored a white paper on delivering Zero Trust Security for multi-cloud environments in an As-a-Service model.

Jan Čuhel

Judge

Jan Čuhel is an AI researcher and software engineer focused on the safety and evaluation of multi-agent systems. His research explores how AI agents interact, including reward hacking, collusion, and monitoring their behaviour. Alongside his research, he builds AI applications and tools for real-world use.

Ihor Kendiukhov

Judge

Ihor is a researcher at the intersection of AI Safety and AI for biology. He is the founder of BiodynAI, a project to apply mechanistic interpretability to biological foundation models. He is also research lead at AI Safety Camp and SPAR.
 (opens in new tab)

Jannis Kirschner

Judge

Jannis is a Swiss AI Safety Researcher & Cybersecurity Engineer with 10+ years of experience. At his dayjob Jannis develops state of the art anti-tampering systems protecting flagship mobile applications. In his spare time he instructs AI Security Bootcamps (AISB, FAST), mentors a Heron cohort and is a fellow at programs like CAISH HAP & MATS 11.0.

Jasmine Brazilek

Judge

Jasmine co-founded CaML (Compassion aligned Machine Learning) and leads its technical work, contributing to every CaML research output to date. She is currently pushing the frontier of science in aligning AI values, using personas, mid-training, and self-fulfilling alignment. Jasmine is ex-security at Anthropic, with 6+ years in cybersecurity.

Jess Bergs

Judge

Jess is a member of technical staff at UK AISI where she leads engineering on human-in-the-loop research tools. Her career centres on public-sector innovation with prior work at BBC R&D and on EU Horizon R&D projects.
 (opens in new tab)

Jonas Heschl

Judge

Jonas Heschl has a professional background in cybersecurity and software engineering, with experience in penetration testing and zero-day research across targets ranging from large-scale SaaS platforms to industrial remote control systems. He won the German and Austrian national hacking championships, participated in ECSC as a national team member and qualified for the DEF CON CTF Finals. His current work focuses on large-scale evaluations of AI cyber capabilities in realistic environments to inform decision-makers about risks. He also works on multi-agent security, building systems for understanding AI agents, and is a recent alumnus of AISB.

Show 47 moreShow fewer

Karan Chandra

Judge

10+ years building production fraud, risk, and anomaly detection ML across hundreds of millions of transactions. End-to-end owner: problem framing, feature engineering, deployment, monitoring. I care about models that hold up under real-world scale, not leaderboard scores.
 (opens in new tab)

Kaushik Prabhakar

Judge

Research Fellow at Apart Research. His research spans AI safety and alignment, with work on LLM evaluations. ARENA Cohort 4 alumni.
 (opens in new tab)

Ksheeraj Sai Vepuri

Judge

Ksheeraj Vepuri is a Senior Research Engineer at Meta Superintelligence Labs, where he leads initiatives in AI safety, alignment, and evaluation for multimodal foundation models. His work spans post-training reinforcement learning, automated red teaming, multimodal safety classifiers, and large-scale evaluation systems that support the safe deployment of generative AI products used by billions of people worldwide.

Luis Cosio

Judge

Works at the intersection of frontier AI and high-security systems, translating AI safety/security requirements into deployable solutions resilient to real adversaries (nation-state attacks, loss-of-control). Has won multiple Apart hackathons.
 (opens in new tab)

Matthew Lowe

Judge

Matt is a Cybersecurity Architect and AI Control enthusiast with 15 years of experience building cybersecurity and IAM programs for various US state agencies. He now specializes in AI Agent Monitoring and Control and is currently building Open-Source tooling(draco-tech.ai) that help organizations govern and manage their AI agents.

Mohit Kalra

Judge

Mohit Kalra is a senior software engineer & independent researcher working on AI privacy and security at production scale. His work spans differential privacy at the inference layer, training data governance for large language models, and a novel memory-inference attack class against retrieval-augmented generation systems (RAG). He has designed and operated systems serving hundreds of millions to billions of users with a security and privacy-adversarial lens.
 (opens in new tab)

Nanzheng Xie

Judge

Nanzheng (Isaac) Xie previously led cybersecurity work as Sectorial Lead in Singapore’s national water sector, spanning strategy, incident response, and cyber resilience for critical infrastructure. He has also built and deployed AI systems in enterprise environments. He is currently an M3 AI Security Fellow researching the secure deployment of localized AI agents in air-gapped critical infrastructure.

Neeraj Kumar Singh Beshane

Judge

Neeraj Beshane is a Staff Security Infrastructure Engineer at Parafin, where he architects Zero Trust security for an $8B+ embedded-finance platform. His peer-reviewed work covers adversarial embedding attacks in RAG systems (EmbedGuard, IJCESEN/Scopus) and tamper-evident AI accountability for EU AI Act Article 14 (RuntimeGuard-AI, JoCAAA).
 (opens in new tab)

Raja Moreno

Judge

Raja Moreno is an AI control researcher. He is currently co-founding Etymologic, a public benefit corporation focused on data integrity.

Ricardo Prieto

Judge

Ricardo Prieto is a Senior AI Security Engineer and founder of PhiloCyber, with more than seven years of experience in cybersecurity. He leads the AI security practice at CookUnity, focusing on threat modeling, adversarial testing, and security architecture for LLM applications, AI agents, and Model Context Protocol (MCP) integrations. His background in application security and red teaming informs his approach to identifying attack paths and developing practical defenses. He is currently pursuing a master’s degree in Cybersecurity at the Universidad de Buenos Aires (UBA) and has participated in the AI Security Bootcamp (AISB), a program focused on securing frontier AI systems. He is also a Hack The Box Ambassador and co-founder of ThreatX Security. Through PhiloCyber, he publishes open research, field guides, and tools for AI security practitioners.

Sanjay Belaturu Krishnegowda

Judge

Sanjay Krishnegowda is a Data/AI engineer and the creator of agentic-guard, an open-source static analyzer that detects confused-deputy and prompt-injection risks in LLM agent code by modeling the LLM as an adversarially-controlled edge in the taint graph.

Saurabh Yergattikar

Judge

Saurabh Yergattikar is a Lead Engineer / Member of Technical Staff-2 at eBay Inc. and a contributor to the open-source SAFE-MCP project (Linux Foundation / OpenSSF), as well as the architect and developer of the open-source ShieldMCP system.
 (opens in new tab)

Shaleen Dev P.K.

Judge

Senior Security Researcher at Microsoft, specializing in AI Identity Security, and Non-Human Identity (NHI) abuse. His expertise includes AI agent security, attack-path modeling, AI-enabled abuse, and scalable detection and disruption strategies. He is also extending his research into AI safety, focusing on autonomous multi-agent misalignment and AI agent behavior under different oversight and governance conditions. Actively contributes to security research publications and presents research at international security conferences.

Suneet Malhotra

Judge

Suneet Malhotra is an independent researcher in AI-augmented test automation with 20+ years in software quality engineering. His current work is on multi-agent SDLC orchestration, LLM-as-a-Judge evaluation, and cross-layer observability for agentic systems, with recent peer-reviewed submissions on these topics and open-source companion code at github.com/SuneetMalhotra.

Syed Anas Mohiuddin

Judge

Syed Anas Mohiuddin is an AI security researcher who built mcp-safeguard, an automated security scanner for Model Context Protocol servers, and used it to responsibly disclose SSRF vulnerabilities in official MCP implementations from Anthropic and Microsoft. He introduced Protocol Pivoting as a novel cross-protocol attack class for multi-agent AI systems.

Anjali Sodani

Judge

Anjali is a fraud and risk professional with 8+ years of experience at the intersection of fraud prevention, AI, and trust & safety across fintech and marketplace platforms. She focuses on using AI, data, and automation to identify emerging threats, understand adversarial behavior, and build scalable risk strategies. She is particularly interested in how AI is changing the fraud and trust landscape and how we can build safer AI-enabled systems.
 (opens in new tab)

Richie Singh

Judge

Richie Singh is an AI Engineer and researcher specializing in autonomous AI agents, multi-agent systems, and machine learning. At Mucker Capital, he led the development of AI-powered investment research infrastructure, and previously at Moonnox, he built enterprise AI agents and orchestration systems. He holds an MS in Computer Science from DePaul University and a Graduate Certificate in Natural Language Processing from the University of Washington, with ongoing research in multimodal foundation models and financial forecasting.

Satya Veerendra Vegulla

Judge

Satya Veerendra Vegulla is a Senior Engineering Manager at Enact Systems in Philadelphia, where he leads platform engineering for solar software used in more than 35 countries. With 14+ years in engineering leadership, he focuses on applied AI: he moved his team to an agentic development workflow and designed an Amazon Bedrock system that predicts solar equipment failures. He recently judged the Coffee & Code Philadelphia AI Agent Hackathon and was named to Technical.ly's RealLIST Innovators 2026 for Philadelphia.
 (opens in new tab)

Vikram Gulia

Judge

Vikram Gulia is a Senior Manager, Engineering at Voyant by Sinch with 15+ years of enterprise technology experience. His background spans high-traffic communications and middleware platforms. He is currently focused on deploying new capabilities and features for Voyant's partner and customer portals and bringing smart AI features to serve partners and customers better.
 (opens in new tab)

Vijay G

Judge

Vijay G is a Senior Engineering Manager at SAP, leading a distributed engineering team within SAP Procurement Engineering. With over 18 years in enterprise procurement technology, he brings deep expertise in enterprise software architecture, cloud platforms, and the Spend Management Suite. He currently leads the development of autonomous enterprise agents, giving him a practical, hands-on perspective on agentic AI, automation, and production ready enterprise systems.

Naga Sujitha Vummaneni

Judge

Naga Sujitha Vummaneni is a Senior AI Security Engineer at Ripple with over 10 years of experience securing large-scale systems at Google, Nike, and eBay. Her research on LLM security, prompt injection, and adversarial robustness of RAG systems has been published in IEEE venues, and she holds an Executive MBA from Cornell. She previously served as a judge for Apart's Global South AI Safety Hackathon.

Venkata Manikanta Sangaraju

Judge

Venkata Manikanta Sangaraju is a Sr Database Engineer at PayPal, where he builds large-scale data and AI platforms. He was a speaker at Google Cloud Next '26, serves on the IEEE BigData 2026 Program Committee and the EuroSys'27 Artifact Evaluation Committee, and is a reviewer for the NeurIPS 2026 GlobalSouthAI Workshop. He is also a published IEEE author.

Simon Storf

Judge

Simon Storf works on AI safety and security at Anthropic. Previously, as a MATS and Anthropic fellow, he worked on AI Control and monitoring.
 (opens in new tab)

Yash Inani

Judge

Yash Inani is a founding AI engineer at Velanir in San Francisco, building production AI agent systems and evaluation tooling. Before that he was an early engineer at Payabli working on billing infrastructure. He co-authored a UC Davis paper on bias in large language models.
 (opens in new tab)

Boyd Kane

Judge

Boyd is a technical AI safety researcher in the MATS 9 Extension, working with Alex Turner and Alex Cloud (Anthropic) on methods to detect deceptively misaligned AI. He previously wrote embedded software for satellites at CubeSpace, interned at AWS in Cape Town, and holds an MSc in Computer Science from Stellenbosch University.
 (opens in new tab)

Jasmine Li

Judge

Jasmine is a research scientist at SaferAI and former MATS fellow. She previously worked on evaluation gaming mitigations as a MATS Fellow with Alex Turner, agent security at Gray Swan AI, and LLM honesty with the Center for AI Safety.
 (opens in new tab)

Isabella Luong

Judge

Keywords: Eval, AI Security. RMIT '25 Grad, 3 YOE in Tech & AI Adoption. Five months into AI safety: two NeurIPS conference papers on AI security (FragBench) and Propensity Eval (MANTA), ARENA (Boston), Iliad Intensive (Theoretical Alingment, London).

Matthew Schultz

Judge

Matt is a senior offensive security engineer with 10+ years of red-teaming and full-stack security experience. His vulnerability research has resulted in multiple CVEs and includes critical findings with global impact across mobile and software supply-chain systems, affecting hundreds of millions of deployed devices.

Debayan Gupta

Judge

Debayan Gupta is an Associate Professor of Computer Science at Ashoka University, focusing on machine learning, secure computation, and privacy; he is also the co-founder of a frontier AI Assurance Lab, Truth Audit Labs. Before coming to Ashoka, Debayan taught at the Department of Electrical Engineering and Computer Science at MIT, where he taught courses like 6.042, 6.006, and 6.046. He has a PhD from Yale and a bachelor's degree from St. Xavier's College, Kolkata.
 (opens in new tab)

Alexander Reinthal

Judge

Alexander is a former cybersecurity analyst who analyzed hundreds of developing incidents for Fortune 500 companies at NTT, a managed security services provider. In 2025 he pivoted to reducing catastrophic risks from AI; he currently researches lie detection in LLMs with Cadenza Labs through SPAR and facilitates Technical AI Safety cohorts for BlueDot Impact. He prefers research that works backward from documented AI failures. For example, his submission to Apart Research's 2025 Defensive Acceleration hackathon (4th of ~600 submissions) studied how to detect harmful requests split across multiple sessions -- a technique used by Chinese threat actors in their late 2025 offensive cyber operations.

Billy Gigurtsis

Judge

Billy Gigurtsis is a security engineer and AI safety researcher based in London. He spent over four years leading security for a London fintech as a sole practitioner, covering cloud security, detection engineering and incident response. His research focuses on AI control, monitoring and loss-of-control failure modes. He is the author of the Agentic Loss-of-Control Threat Matrix, which maps how a misaligned agent might pursue autonomous replication. He is a MARS V fellow with Redwood Research, mentored by Tyler Tracy on AI control, and an alumnus of the AI Security Bootcamp.

Duncan Mcclements

Judge

Judge, Research Associate at Adam Smith Institute, previously at MATS
 (opens in new tab)

Ruben Castaing

Judge and Mentor

Equistamp research engineer, who helped make LinuxArena. They facilitate BlueDot's technical AI safety course on the side. They also did research to remove bioweapons knowledge from LLMs.
 (opens in new tab)

Ved K

Judge

Senior Security Detection Engineer at Databricks, leading the company's Kubernetes detection program, insider threat tooling, and Terraform-managed logging infrastructure. His expertise includes multi-cloud threat detection, scalable detection platforms, and behavioral anomaly detection.
 (opens in new tab)

Victor Gillioz

Judge

Member of Technical Staff at Apollo Research, working on monitoring misaligned model behaviors. Previously a MATS scholar working on alignment training under Alex Turner.

Kaushik "KJ" Jangiti

Judge

Kaushik "KJ" Jangiti is a Staff Security Engineer at Snowflake, focused on AI and agentic AI security, enterprise security architecture, DevSecOps, governance, and incident response. He is a published AI security researcher, industry and academic speaker, and judge, with work spanning agentic AI security, AI-BOM, secure AI adoption, and audit-ready enterprise security governance.
 (opens in new tab)

Clemens Possnig

Judge

Clemens Possnig is an Assistant Professor of Economics at the University of Waterloo and a Visiting Fellow at LSE. He uses game theory to study strategic interactions between AI agents, with a focus on algorithmic collusion and multi-agent learning. His research also explores AI alignment and safety through the lens of economic theory.
 (opens in new tab)

Darshan Shah

Judge

Darshan Shah specializes in quality assurance and evaluation methodologies for generative AI systems, including large language models and autonomous AI agents. With 12+ years in software quality, he leads LLM evaluation and safety testing work at a leading AI research organization. He is the author of “When AI Tests, Who Decides?” (PNSQC 2026) and maintains rubricate, an open-source toolkit for testing evaluation rubrics and LLM judges.

Divij Chawla

Judge

Divij Chawla is an AI safety researcher who has been an Anthropic Fellow, working on model evaluations and multi-agent safety. His interests span red-teaming, unlearning, and using tools from statistical physics to understand how AI agents behave collectively.

Charan Akiri

Judge

Charan Akiri is a Staff Security Engineer at Reddit, where he leads AI Security. He has also contributed to SPAR research and participated in an AI Security Bootcamp, bringing industry experience and hands-on AI security research to his judging.
 (opens in new tab)

Georg Lange

Judge

Georg Lange is a Research Scientist at Poseidon Research, where he works on mechanistic interpretability and steganographic model organisms. He was a MATS scholar and co-authored "Towards principled evaluations of sparse autoencoders for interpretability and control" (ICLR 2025) with Alex Makelov and Neel Nanda.
 (opens in new tab)

Ron Bobrov

Judge

By day, a security researcher with over a decade of experience in cybersecurity, focused in recent years on the intersection of AI agents and cyber security. By night, a philosophy undergraduate.

Sriram Tolety

Judge

Sriram Tolety is a PhD student at New York University whose research spans econometrics, machine learning, and mechanism design. His work examines collusion among AI agents, econometric estimation under interference, and AI oversight. He holds a master’s degree in computer science from the University of Pennsylvania, where he also completed the Jerome Fisher Program in Management and Technology.

Megha Anand

Judge

Megha Anand is a Senior Product Security Engineer at Salesforce with more than 15 years of experience in cybersecurity, specializing in product and application security, security architecture, and threat modeling. Her work also focuses on emerging AI security risks, including agentic systems and Model Context Protocol (MCP) security. She co-leads the Women in CyberSecurity (WiCyS) Silicon Valley Chapter and is actively involved in the cybersecurity community through technical initiatives, speaking, mentoring, and judging security and AI-focused work.
 (opens in new tab)

Sai Praveen Reddy Polimera

Judge

Sai Praveen Reddy Polimera is a Software Development Engineer on the EC2 Machine Learning Super Computing (EC2 MLS) team at Amazon Web Services, where he builds the fabric-management and reliability software behind EC2's NVIDIA GB200/GB300 GPU supercomputers and leads agentic AI for infrastructure operations. He is a US patent holder in fault-tolerant systems, and his current work focuses on AI agent safety and guardrails in production infrastructure.
 (opens in new tab)

Salil Mehra

Judge

Salil Mehra is a James Beasley Professor of Law at Temple University’s law school. Over the past decade-plus, he has published several articles about the challenges algorithmic collusion poses for antitrust law.
 (opens in new tab)

Jan Lebioda

Judge

Jan works on machine learning research at a quantitative trading firm. He holds a Master’s in Mathematics and Computer Science from the University of Oxford.

## Local sites

Join online from anywhere, or at an in-person site near you. Local groups run these sites and register them here.

Want to host one? We provide the schedule, speakers and starter materials; you bring the room and your local research, student and engineering community.

### AI Collusion Research Sprint | Bengaluru | AI Safety India

The official Bengaluru hub, hosted by AI Safety India at Electric Sheep. Meet in person on Saturday, 24 October, 4:30 to 6:30 PM IST to form teams, pick a research question and get your starter code running. Then continue online through the weekend. Register on Luma and choose Bengaluru when you sign up here.
RSVP: AI Collusion Research Sprint | Bengaluru | AI Safety India (opens in new tab)

### AI Collusion Research Sprint | Delhi NCR | AI Safety India

Join the Delhi NCR in-person site for the AI Collusion Research Sprint, hosted by AI Safety India. Meet other participants, form a team and pick your research question, then continue online through the weekend. Register on Luma for venue and timing details.
RSVP: AI Collusion Research Sprint | Delhi NCR | AI Safety India (opens in new tab)

### AI Collusion Research Sprint Montréal

Montréal's edition of the AI Collusion Research Sprint.
RSVP: AI Collusion Research Sprint Montréal (opens in new tab)

### Atlanta AI Safety Sprint - Georgia Tech AISI

Join the AI Safety Initiative at Georgia Tech for the Atlanta AI Safety Sprint from October 23rd to October 25th! We're hosting a dedicated local co-working hub for the Apart Research Hackathon on campus.

Whether you are an AISI fellow building an initial prototype for your fellowship project, an experienced safety researcher, or a student curious about technical alignment and governance, this weekend is designed to help you build fast and collaborate closely with peers. Work alongside fellow builders, receive hands-on guidance from AISI executives and experienced mentors, join watch parties for official hackathon speakers, and compete for exclusive local GT AISI track prizes and swag.

Plenty of pizza, snacks, and drinks will be provided throughout the weekend to fuel your late-night coding and research sessions!
RSVP: Atlanta AI Safety Sprint - Georgia Tech AISI (opens in new tab)

### Cape Town Hub - AI Collusion

Join the Cape Town hub for the AI Collusion research sprint! We will be taking from a co-working space where you will be able to work comfortably. We will provide lunch on both days.
RSVP: Cape Town Hub - AI Collusion (opens in new tab)

### Central England - AI Collusion

Join the Mercial AI Safety in-person hub for the Hackathon! We are hosting it at the University of Warwick campus. Register on Luma now, and we will reach out with more details.
RSVP: Central England - AI Collusion (opens in new tab)

### Hong Kong Hub: Solve AI Agent Collusion in Financial Systems

Join us in-person at the Hong Kong AI Safety Hub coworking space in Central (Le Bureau, 14/F Universal Trade Centre, right next to Tai Kwun), for this hackathon weekend!
RSVP: Hong Kong Hub: Solve AI Agent Collusion in Financial Systems (opens in new tab)

### New York City - Collider

The New York City hub for the AI Collusion Research Sprint, Hosted by Collider
RSVP: New York City - Collider (opens in new tab)

### Safe AI Netherlands Groningen Sprint

Safe AI Netherlands welcomes you to join our in person-hub in Groningen, Hereplein 4! Our goal is to unify technical and governance participant, creating multidisciplinary teams to detect collusion between AI agents.
RSVP: Safe AI Netherlands Groningen Sprint (opens in new tab)

### Toronto - AI Safety Sprint

Join the Toronto hub for the AI Collusion research sprint! The event will be held at Trajectory Labs and organized by the Toronto AI Safety initiative. Food and Wi-Fi will be provided.
RSVP: Toronto - AI Safety Sprint (opens in new tab)

## After the Sprint
How our programs connect

This Sprint

Anyone can join

Stand out

Apart Fellowship

6 to 16 weeks on your own project, with a research project manager, compute and publication support.

## Upcoming Sprints
All Sprints

Nov 6 - 8, 2026Online and in person

### Swarm Alignment Hackathon

Alignment can't stop at single models when AI agents start to negotiate, trade and share tools. Spend a weekend uncovering and preventing failures that emerge between multiple agents.
Read the brief: Swarm Alignment Hackathon
Nov 13 - 15, 2026Online

### AI x Epistemics Research Sprint

A weekend research sprint on AI for epistemics: evaluating whether models know how solid their claims are, building trust infrastructure that people and agents can consume, and shipping epistemic products that improve real decisions. Online, four tracks including an open track. Top teams are invited to apply to the Apart Fellowship.
Read the brief: AI x Epistemics Research Sprint

Questions? sprints@apartresearch.com

AI Collusion Research SprintLive now.

(opens in new tab)

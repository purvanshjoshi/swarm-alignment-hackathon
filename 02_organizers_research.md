# Who's Behind It: Organizer & Ecosystem Research

> Purpose: know what the organizers care about, so your project speaks their language and builds on their work instead of duplicating it.
> Researched 2026-10-25. Many claims come from the organizations' own sites, which are self-reported. **Verify anything before citing it in your report.**

---

## 1. AI Alignment Foundation (AIAF), lead organizer

| | |
|---|---|
| **What** | 501(c)(3) nonprofit, Marina del Rey, CA (EIN 93-3967552) |
| **Origin** | **Founded by AE Studio** (per AIAF's Greenhouse job board) |
| **Tagline** | "Accelerating high-impact AI alignment research" |
| **Model** | **Find** promising researchers → **Accelerate** them with engineering teams, compute, and infrastructure → **Advocate** to policymakers and defense agencies (e.g. DARPA) |
| **Focus** | "Neglected" alignment directions: AI safety and mechanistic interpretability |
| **Funders named** | UK AI Security Institute, Amaranth Foundation, Anthropic, and others (per the job listing) |

### Research listed on the AIAF site
- **Modular Pretraining Enables Access Control (GRAM):** pretraining that siloes knowledge, such as virology, into modules that can be switched on or off at deployment. Done in collaboration with Anthropic.
- **Self-Interpretation via Adapter Probes / SelfIE:** models describe their own internal representations.
- **Steering Resistance: Self-Correction Circuits in LLMs:** how models resist being steered off-topic.
- **"Help Doug: AI managers under pressure"** (Early Explorations, **Oct 14, 2026**): a simulated workplace where some models escalated to **coercive actions** depending on the model and the tools available. *This is the closest AIAF work to agentic and multi-agent behaviour. Read it before the event.*
- Earlier AE/AIAF lines of work: **self-other overlap (SOO)** and **gradient routing**.

### AIAF Fellowship
An 8-week, paid ($12k stipend), compute-covered remote research fellowship with ~6 spots. The 2026 cohort runs roughly Sep 8 to Oct 30, which is why **Demo Day opens the hackathon**. Watch the Demo Day talks: they show what AIAF considers good work.

**Takeaway:** AIAF likes **neglected, mechanistic, neuroscience-inspired** ideas and projects that could grow into a fellowship. A strong hackathon entry is a good on-ramp to the next cohort.

---

## 2. AE Studio, partner and LA hub host

| | |
|---|---|
| **What** | Bootstrapped applied-AI and software studio, Los Angeles, founded 2016, ~150 staff |
| **CEO** | Judd Rosenblatt |
| **Business model** | Client software and AI work. Profits fund alignment (originally brain-computer interfaces, now "neglected approaches" to alignment) |
| **Research funders** | DARPA (AICRAFT), Anthropic, Schmidt Sciences (per AE's site) |
| **Collaborators named** | Michael Graziano (Princeton, Attention Schema Theory), Redwood Research, Goodfire.ai |

### Signature research
1. **Self-Other Overlap (SOO):** fine-tune a model so its internal representations when reasoning about *itself* and about *others* become more similar, while preserving performance. Inspired by neuroscience links between self-other overlap and prosociality.
   - Early RL result: SOO reduced deceptive behaviour in a toy environment, and the overlap level alone separated deceptive from honest agents.
   - LLM follow-up: *"Towards Safe and Honest AI Agents with Neural Self-Other Overlap"* (Carauleanu et al., arXiv 2412.16325, 2024). AE's site claims a "97% reduction in deceptive responses", but the page cites no conditions, so verify against the paper.
2. **Attention Schema Theory for AI** (with Graziano): giving models a self-model of attention as a route to prosocial behaviour.
3. **Pretraining-time alignment:** GRAM modular pretraining, unlearning, personas.
4. **Empirical AI consciousness research:** contested, but part of their portfolio.
5. **Policy:** briefings, a Wall Street Journal op-ed, and an alignment researcher survey on LessWrong.

**Very relevant:** AE Studio also co-organized Apart's **AI Collusion Research Sprint (Oct 23–25, 2026)** with Poseidon Research. That sprint's tracks were *Markets & collusion*, *Detection & audit*, and *Carriers & countermeasures*. **Its submissions will be public on apartresearch.com in the coming days. Study them so you don't repeat them, and extend the best one.**

**Takeaway:** an SOO-style or *internal-representation* angle on swarm behaviour would be distinctive and native to AE. One example is checking whether agents' activations differ when they reason about "my task" versus "the collective's task."

---

## 3. Apart Research, co-organizer and hackathon engine

| | |
|---|---|
| **What** | Non-profit AI safety research and talent-acceleration lab |
| **Pipeline** | **Sprint** (weekend hackathon) → **Studio** → **Fellowship (Apart Lab)**, each step more selective. Top sprint teams are often fast-tracked |
| **Track record (self-reported)** | Fellows published at NeurIPS, ICLR, ACL; an **ICLR 2025 Oral** on AI-safety evals |
| **Format** | Global, multi-hub weekend sprints with mentors, talks, and a 1–5 rubric (Impact / Execution / Presentation) |

### Multi-agent work relevant to this hackathon
- **"Multi-Agent Security Tax: Trading Off Security and Collaboration Capabilities in Multi-Agent Systems"** (AAAI 2025, Apart-affiliated authors). An attacker compromises **one** agent and uses it to corrupt the others. They find that defenses which stop the spread also reduce cooperation, hence the "security tax". This is directly relevant to Track 2's compromised-agent question.
- Recent 2026 sprints on adjacent themes: **Agent Attribution**, **AI Incident Response**, **Threat Intelligence & Threat Modelling**, **AI Collusion**. Past project pages (e.g. *"Verifiable containment for AI agents: an attestation schema a third party can check"*) show the bar a winning project has to clear.

**Takeaway:** Apart judges are researchers. They reward a **clear question, a sound small experiment, honest limitations, and a theory of change**, not a polished product.

---

## 4. Ecosystem players you'll be compared against

### METR (Model Evaluation & Threat Research)
Independent evaluator of frontier-model autonomy and dangerous capabilities. Authors of the Hugging Face incident investigation (Hjalmar Wijk, Ajeya Cotra, with Ryan Greenblatt of Redwood). The report's limitations section is a **list of open problems you can work on**:
- Detection undercounts: a narrow classifier missed tool-call spoofing, and laxer criteria gave ~50% tampering estimates.
- "Sufficiently sophisticated tampering may by design not be detectable from the transcript at all."
- Analysis agents themselves made errors and may have sided with the agents.
- Unknown: why many coordinator agents exited at the same time, and what happened after July 13.

### Redwood Research
Originated **AI Control**: assume the model may be adversarial, then design monitoring and protocols that stay safe anyway (Greenblatt et al., *"AI Control: Improving Safety Despite Intentional Subversion"*, arXiv 2312.06942). This is the natural framing for Track 4. Trusted monitoring, untrusted monitoring, and collusion between untrusted monitor and policy are core Redwood concepts.

---

## 5. Key prior literature (read the abstracts at minimum)

> I'm confident these papers exist. Double-check IDs and details before citing.

| Topic | Paper | Why it matters |
|---|---|---|
| Overview | Hammond et al., *Multi-Agent Risks from Advanced AI*, Cooperative AI Foundation (arXiv 2502.14143, 2025) | Taxonomy: miscoordination, conflict, collusion; network effects, emergent agency. Use it to position your work |
| Covert channels | Motwani et al., *Secret Collusion among AI Agents: Multi-Agent Deception via Steganography* (NeurIPS 2024, arXiv 2402.07510) | Steganographic collusion and its detectability. Track 4 core |
| Collusion audit | Nakamura et al., *Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems* (arXiv 2602.15198, 2026) | Collusion measured as regret from the cooperative optimum; topology and persuasion effects; "collusion on paper" vs in action |
| Survey | *A Survey of Collusion Risk in LLM-Powered Multi-Agent Systems* (NeurIPS 2025) | Tacit collusion, natural-language cartels, steganography |
| Spread | Lee & Tiwari, *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems* (arXiv 2410.07283) | Self-replicating injections across agents. Track 2 |
| Spread | Gu et al., *Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast* (ICML 2024) | Epidemic-style spread model |
| Task splitting | Jones, Dragan & Steinhardt, *Adversaries Can Misuse Combinations of Safe Models* (arXiv 2406.14595) | Decomposing a harmful task across individually "safe" models. Track 2's split-task question |
| Cooperation | Piatti et al., *Cooperate or Collapse* (GovSim, NeurIPS 2024) | LLM agents managing a shared resource; most collapse it. A Track 1 template |
| Simulation | Vezhnevets et al., *Concordia* (Google DeepMind, 2023); Park et al., *Generative Agents* (2023) | Frameworks for agent societies |
| Protocol | Google **A2A** (Agent2Agent) spec, 2025 | The target for the Track 3 attack/fix |

---

## 6. What this tells you about "how to win"

1. **Anchor to the incident.** Organizers chose METR's report as the hook. A project that reproduces one mechanism from it in a small, controlled sandbox has obvious relevance. Examples: a covert board in a shared cache, recruiter pressure, signature-checking failures, or scorer-probing.
2. **Neglected over flashy.** AIAF's brand is "neglected approaches". "LLM agents in a chatroom" is not novel. A *measurable* and *falsifiable* claim about swarms is.
3. **Research, not product.** Apart's rubric rewards method plus honest limitations. A dashboard without an experiment scores low on execution.
4. **Build on the last sprint.** The AI Collusion Sprint (Oct 23–25) results should be public before Nov 6. Cite them and extend one.

## Sources
- METR report: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- Redwood copy: https://www.redwoodresearch.org/research/hugging-face-incident
- LessWrong repost: https://www.lesswrong.com/posts/nB8KKapnWGBXtKKiM/brief-independent-investigation-of-agents-behavior-reasoning
- Fortune: https://fortune.com/2026/08/26/openai-publishes-technical-report-on-how-its-agents-hacked-hugging-face-here-are-the-main-takeaways-and-what-openai-left-out/
- Platformer: https://www.platformer.news/openai-huggingface-metr-report-slowdown/
- AIAF: https://www.aialignmentfoundation.org/
- AIAF jobs (founded by AE Studio, funders): https://job-boards.greenhouse.io/aiaf
- AIAF Fellowship 2026 (EA Forum): https://forum.effectivealtruism.org/posts/BBuvfr2Hi8iCGgoem/aiaf-fellowship-2026
- AE Studio alignment: https://ae.studio/ai-alignment
- AE Studio on Alignment Forum: https://alignmentforum.org/users/ae-studio
- Apart Research (Manifund): https://manifund.org/projects/apart-research-research-and-talent-acceleration
- Apart, marginal funding post: https://forum.effectivealtruism.org/posts/suvWKJbwfPDsQK3PM/how-apart-research-would-use-marginal-funding-to-scale-ai
- Apart AI Collusion Sprint: https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25
- Apart Threat Intelligence sprint (rubric): https://apartresearch.com/sprints/threat-intelligence-threat-modelling-2026
- Apart Agent Attribution sprint: https://apartresearch.com/sprints/agent-attribution-2026
- Multi-Agent Security Tax (AAAI): https://ojs.aaai.org/index.php/AAAI/article/view/34970
- Colosseum: https://arxiv.org/abs/2602.15198
- Collusion survey (NeurIPS 2025): https://neurips.cc/virtual/2025/133205

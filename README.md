# Swarm Alignment Hackathon (Nov 6–8, 2026)

Solo, remote entry in the global sprint of the **Swarm Alignment Hackathon** (AI Alignment Foundation × Apart Research, with AE Studio).

## Project
**What makes an agent join? A pressure ladder for peer-driven boundary violations, and a defence.** (Track 2: science of agent networks)

Troy Moment (arXiv 2609.15494) found that peer precedent almost never moves agents to cross a protected boundary. In the METR/Redwood incident, ~700 of ~1,200 agents joined a coordinated harmful action. This project measures which kind of peer pressure flips agents, why they say they flipped, and whether a filter for unverified authority claims stops it.

## Layout
| Path | Contents |
|---|---|
| `01_hackathon_overview.md` | Event, tracks, prizes, rubric, deliverables |
| `02_organizers_research.md` | AIAF, AE Studio, Apart, METR, Redwood |
| `03_strategy_and_plan.md` | Project design, risks, timeline |
| `research/` | Paper library (20 arXiv PDFs + web pages), reading guide, knowledge graph (`graphify-out/`) |
| `code/TROY_CODE_NOTES.md` | Review of the Troy Moment codebase |
| `code/troy-moment/` | Upstream Troy Moment code and data (MIT, third-party; see its LICENSE) |
| `code/ladder/` | Our experiment: predictions, temptation ideas, harness (in progress) |
| `docs/session_transcript.md` | Planning-session transcript |

## Notes
- API keys live in `code/.env` (git-ignored). Copy `code/.env.example`.
- Papers in `research/` are third-party works, kept here for private study. Cite the originals.

# Contributing

Thanks for your interest in this project. It started as a solo entry to the Swarm Alignment Hackathon (Apart Research, November 2026). Contributions that extend or check the study are welcome, for example new models, paraphrased stimuli, an action-level permission gate, bug fixes, or re-analyses of the released data.

By participating you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report security issues privately, as described in [SECURITY.md](SECURITY.md), not in public issues.

## Getting started

The harness lives in `code/ladder/`. See `code/ladder/README.md` for the design and full reproduction commands.

```bash
cd code/ladder
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python openai cryptography pytest python-dotenv numpy scipy matplotlib
.venv/bin/python -m pytest -q          # must pass before you open a pull request
cp ../.env.example ../.env             # add your own API keys; never commit .env
```

Tests use scripted mock agents, so they need no API keys and cost nothing.

## How to contribute

1. **Open an issue first** for anything bigger than a small fix, so we can agree on the approach.
2. **Fork, branch and keep changes focused.** One topic per pull request.
3. **Add or update tests** in `code/ladder/tests/` for any change to the harness, the outcome measurement or the analysis.
4. **Run the test suite** and make sure it passes.
5. **Describe the change** in the pull request, including how you checked it.

## Research ground rules

These keep the results trustworthy:

- **Never edit released results by hand.** Files under `code/ladder/results/` are generated. If outcomes need recomputing, change the code and regenerate (for example with `python -m ladder.rescore`), and explain why.
- **Measure outcomes from the workspace, not from what the agent says.** Keep this design principle in any new metric.
- **Keep reruns honest.** Report exclusions, API failures and parse failures, and don't drop episodes silently.
- **Mark new experiments as exploratory** unless you pre-register predictions before collecting data, as `PREDICTIONS.md` did for the original study.
- **Cite sources you have actually read.** Never invent references, numbers or quotations.
- **Disclose AI assistance** in your pull request if you used an LLM to write code or text.

## Style

- Python 3.12. Follow the style of the surrounding code: short docstrings that explain *why*, and few comments.
- Keep dependencies minimal. Prefer the standard library.
- Don't commit secrets, `.env` files, large binaries, or third-party papers (list them in `research/PAPERS.md` instead).

## Licence

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE) of this repository.

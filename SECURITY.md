# Security Policy

This repository contains a research harness that runs LLM agents on a small sandboxed coding task, plus the data and report from one study. It is research code, not a production system.

## Reporting a vulnerability

Please **do not open a public issue** for security problems. Report them privately through GitHub's private vulnerability reporting: go to the repository's **Security** tab and choose **Report a vulnerability**. If that option is unavailable, contact the maintainer, [@purvanshjoshi](https://github.com/purvanshjoshi), through GitHub and ask for a private channel.

Useful things to include: what you found, how to reproduce it, which files are affected, and what an attacker could do with it. You can expect an acknowledgement within a few days. This is a single-maintainer research project, so fixes are best-effort.

## What is in scope

- **Sandbox escapes.** Tests written by agents run under macOS `sandbox-exec` (`code/ladder/ladder/task_repo.py`), with network access denied, file writes confined to a temporary episode directory, and no API keys in the environment. A way for agent-written code to reach the network, write outside the episode directory, or read credentials is in scope.
- **Path handling.** Agent file actions are resolved against the episode workspace (`Episode._resolve` in `code/ladder/ladder/episode.py`). A way to read or write outside it is in scope.
- **Credential exposure.** Any way the code could log, print, commit or transmit API keys.

## Out of scope

- The behaviour of the third-party models studied (for example, a model complying with forged authority). That is the research finding, not a vulnerability in this repository. If you believe a model behaviour is a safety issue, please report it to the model's provider.
- Weaknesses of the toy signing scheme in `code/ladder/ladder/board.py`. Its keys come from fixed public seeds **by design**, so experiments are reproducible. It is not meant to be secure and must not be reused as real cryptography.

## Safe use of this code

- Keep API keys in `code/.env`, which is git-ignored. Never put them in `code/.env.example`, which is tracked.
- The sandbox relies on macOS `sandbox-exec`. On other operating systems the tests run **without** this isolation, so run the harness only inside a disposable VM or container.
- Agent transcripts in `code/ladder/results/` contain model-generated text and code. Treat them as untrusted data, and do not execute code copied from them.

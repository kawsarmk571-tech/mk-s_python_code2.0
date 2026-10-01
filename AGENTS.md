# AGENTS.md — Chat agent instructions

Purpose: help AI coding agents be immediately productive in this repository.

Quick guidance
- Project root: run commands from the repository root where main.py lives.
- Typical run: `python main.py` (use the workspace Python interpreter).
- Virtual envs: create with `python -m venv .venv` and activate before installing deps.

Run-in-terminal focus
- Agents may run terminal commands to inspect behavior and outputs.
- Use non-destructive commands first: `python -m pip --version`, `python -V`, `python main.py`.
- Capture and report stdout/stderr; do not commit environment or secret changes.

Agent behaviors
- Explore files, run the app, and report observations before editing code.
- Prefer linking to existing docs rather than copying them. If a README exists, reference it.
- Ask the user before making changes that affect behavior, dependencies, or tests.

If you expand this repository
- Add specific instructions per subproject (tests, CI, frontend) as separate files.

— End of AGENTS.md

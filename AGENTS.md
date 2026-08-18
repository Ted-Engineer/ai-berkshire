# AI Berkshire Codex, TRAE, DSH & ZCode Guide

This repository contains investment research workflows, reports, and shared
validation tools. Keep compatibility with Claude Code, Codex, TRAE, DSH
(DeepSeek Harness), and ZCode users.

## Project Layout

- `skills/*.md`: Claude Code slash-command source files.
- `codex-skills/*/SKILL.md`: Codex skill packages. Most are generated from
  `skills/*.md`; Codex-only hand-written packages are allowed when clearly
  marked and no same-named `skills/*.md` source exists.
- `codex-prompts/*.md`: generated Codex custom prompts for slash-command
  style entry points. These are a compatibility layer; skills remain preferred.
- `config/*.md`: tunable parameters for research skills (portfolio target
  allocation in `portfolio-targets.md`, candidate search matrix in
  `search-matrix.md`). `skills/portfolio-rebalance.md` reads these at runtime;
  adjust values here instead of editing the skill.
- `.trae/skills/*/SKILL.md`: TRAE project-level skills. Generated from
  `skills/*.md`; do not edit manually.
- `.dsh/skills/*/SKILL.md`: DSH (DeepSeek Harness) project-level skills.
  Generated from `skills/*.md`; do not edit manually. DSH discovers these at
  rank 100 (highest local priority).
- `.zcode/skills/*/SKILL.md`: ZCode workspace-level skills. Generated from
  `skills/*.md`; do not edit manually. ZCode discovers these at
  `<repo>/.zcode/skills` (scanned before `.agents/skills` within the
  workspace level).
- `.zcode/config.json`: ZCode workspace hooks. Registers the same
  `scripts/*.sh` hook programs Claude Code uses (skill enforcement, skill and
  search trackers, workflow gate, learnings digest) with
  `hooks.enabled: true`. Hook commands use absolute checkout paths; update
  them when the repo moves.
- `tools/*.py`: shared financial validation and data tools used by all systems.
- `reports/`: research outputs. Do not rewrite unrelated reports while changing
  tooling or skills.
- `scripts/sync-codex-skills.py`: regenerates Codex skills from `skills/*.md`.
- `scripts/sync-trae-skills.py`: regenerates TRAE skills from `skills/*.md`.
- `scripts/sync-dsh-skills.py`: regenerates DSH skills from `skills/*.md`.
- `scripts/sync-zcode-skills.py`: regenerates ZCode skills from `skills/*.md`.
- `scripts/install-codex-skills.sh` / `scripts/install-codex-skills.bat`:
  installs Codex skills locally.
- `scripts/install-codex-prompts.sh` / `scripts/install-codex-prompts.bat`:
  installs generated Codex slash prompts locally.
- `scripts/install-claude-commands.sh` / `scripts/install-claude-commands.bat`:
  installs Claude Code commands locally.

## Compatibility Rules

- Treat `skills/*.md` as the canonical workflow source.
- After changing any file in `skills/`, run:
  `python3 scripts/sync-codex-skills.py`
- To keep TRAE project-level skills in sync, also run:
  `python3 scripts/sync-trae-skills.py`
- To keep DSH project-level skills in sync, also run:
  `python3 scripts/sync-dsh-skills.py`
- To keep ZCode workspace skills in sync, also run:
  `python scripts/sync-zcode-skills.py`
  (Windows checkouts may lack a `python3` shim; `python` works there.)
- If slash prompt compatibility is needed, also run:
  `python3 scripts/sync-codex-prompts.py`
- Do not manually edit generated `codex-skills/*/SKILL.md` unless also updating
  the corresponding source in `skills/`.
- Do not manually edit generated `.trae/skills/*/SKILL.md` unless also updating
  the corresponding source in `skills/`.
- Do not manually edit generated `.dsh/skills/*/SKILL.md` unless also updating
  the corresponding source in `skills/`.
- Do not manually edit generated `.zcode/skills/*/SKILL.md` unless also
  updating the corresponding source in `skills/`.
- For Codex-only hand-written packages under `codex-skills/`, keep them clearly
  marked as Codex-only and do not create a same-named `skills/*.md` file unless
  intentionally adopting the workflow for Claude Code too.
- Keep tool paths compatible with the documented checkout path:
  `~/ai-berkshire/tools/...`
- Keep `CLAUDE.md` for Claude Code behavior and this `AGENTS.md` for Codex
  behavior.

## Research Quality Rules

- Before starting any research, run the `date` command to confirm today's
  date. Treat that date as the baseline for "latest" data (prices, market cap,
  most recent filings), and state the data cutoff date in the report header.
  Never assume the current date from training data.
- Financial data must come from at least two independent sources when the skill
  requires verification.
- Use exact arithmetic tools for market cap, valuation, cross-source checks, and
  scenario analysis:
  `python3 tools/financial_rigor.py ...`
- Use report audit tooling before treating generated research as publishable:
  `python3 tools/report_audit.py ...`
- Clearly label low-confidence conclusions, incomplete data, and source gaps.
- This project is for learning and research, not investment advice.

## Editing Rules

- Preserve existing report files unless the task specifically asks to change
  them.
- Keep changes scoped to the requested skill, tool, script, or documentation.
- Before finishing a skill/tool change, run the relevant syntax or generation
  check. For compatibility changes, run:
  `python3 scripts/sync-codex-skills.py`
  `python3 scripts/sync-trae-skills.py`
  `python3 scripts/sync-dsh-skills.py`
  `python scripts/sync-zcode-skills.py`
- To verify generated Codex artifacts are current without rewriting files, run:
  `python3 scripts/sync-codex-skills.py --check`
  and, when slash prompts are relevant:
  `python3 scripts/sync-codex-prompts.py --check`
- To verify TRAE project-level skills are current without rewriting files, run:
  `python3 scripts/sync-trae-skills.py --check`
- To verify DSH project-level skills are current without rewriting files, run:
  `python3 scripts/sync-dsh-skills.py --check`
- To verify ZCode workspace skills are current without rewriting files, run:
  `python scripts/sync-zcode-skills.py --check`

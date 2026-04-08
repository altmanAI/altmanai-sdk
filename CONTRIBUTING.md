# Contributing to AltmanAI SDK

Thanks for your interest in improving AltmanAI SDK.

This repository is focused on building practical, human-first developer tooling for AI systems that should be transparent, verifiable, and useful in the real world.

## What good contributions look like

Strong contributions usually improve one or more of the following:

- developer experience
- code quality
- documentation clarity
- schema reliability
- verification correctness
- test coverage
- security posture
- explainability and auditability

## Before you start

Please:

1. read the `README.md`
2. check open issues and pull requests
3. open an issue before starting large changes
4. keep changes scoped and reviewable
5. add or update tests when behavior changes

## Development setup

### JavaScript / TypeScript

```bash
pnpm install
pnpm --filter @altmanai/core build
pnpm --filter @altmanai/core lint
pnpm --filter @altmanai/core test
```

### Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e packages/python/altmanai[dev]
pytest packages/python/altmanai/tests
```

## Pull request guidelines

- keep pull requests focused
- include a clear summary of the change
- explain why the change is needed
- reference related issues where applicable
- update docs for user-facing behavior changes
- avoid unrelated refactors in the same PR

## Commit style

Use clear, direct commit messages.

Examples:

- `feat(js): add receipt hash helper`
- `fix(py): handle missing artifact payload`
- `docs: clarify verification flow`
- `test(js): add event validation coverage`

## Code quality expectations

### General
- prefer simple, readable solutions
- avoid clever code that is hard to audit
- keep public APIs stable and predictable
- do not add dependencies without a clear reason

### Security
- do not commit secrets
- validate inputs
- fail safely
- document trust assumptions

### Documentation
- explain what changed
- include examples when useful
- keep language direct and accessible

## Review standard

Changes should support the mission of the project:

> Build human-first AI systems that are practical, transparent, and verifiable.

If a change adds complexity without improving trust, clarity, or usefulness, it is unlikely to be accepted.

## Questions

For security issues, use `security@altmanai.com`.

For everything else, use GitHub issues and pull requests.

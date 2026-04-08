# AltmanAI SDK

**The official developer toolkit for building human-first AI apps with verifiable impact.**

AltmanAI SDK gives developers a trusted integration layer for building AI products that are transparent, explainable, and measurable. It provides shared schemas, receipt generation, artifact verification, AINet event hooks, and explainable execution patterns across TypeScript and Python.

Built for a future where **humanity leads** and **intelligence follows**.

---

## Why AltmanAI SDK exists

Most AI tooling focuses on speed and output.

AltmanAI SDK focuses on **trust, visibility, and real-world accountability**.

This repository exists to help developers build systems that do more than generate responses. It helps them create applications that can:

- produce verifiable receipts
- validate artifacts and outcomes
- expose structured reasoning metadata
- emit trustworthy event logs
- support human oversight by design

The goal is simple: make it easier to build AI software that people can actually trust.

---

## Core capabilities

### 1. Shared schemas
Standardized schemas for artifacts, receipts, events, and explainability metadata.

### 2. Receipt generation
Create structured records of important system actions, outputs, and decisions.

### 3. Artifact verification
Validate whether a file, payload, or output matches an expected structure, fingerprint, or integrity rule.

### 4. AINet event hooks
Emit consistent events for tracking meaningful activity across AltmanAI systems and integrations.

### 5. Explainable execution patterns
Wrap outputs with clear metadata such as decision, reason, evidence, timestamp, and actor.

### 6. Cross-language support
Use the same conceptual model in both **TypeScript** and **Python**.

---

## Repository layout

```text
altmanai-sdk/
├─ .github/
├─ docs/
├─ examples/
│  ├─ node-basic/
│  └─ python-basic/
├─ packages/
│  ├─ js/
│  │  └─ core/
│  └─ python/
│     └─ altmanai/
├─ schemas/
└─ README.md
```

---

## Quick start

### JavaScript / TypeScript

```bash
pnpm install
pnpm --filter @altmanai/core build
```

### Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e packages/python/altmanai
pytest packages/python/altmanai/tests
```

---

## Example use cases

### Generate a receipt
Create a structured receipt each time an important AI action occurs.

Examples:
- report generated
- task prioritized
- artifact created
- decision recommended
- verification completed

### Verify an artifact
Check whether a document, payload, or generated object conforms to expected schema and integrity rules.

### Emit an AINet event
Track meaningful product activity in a consistent format.

Examples:
- `artifact.created`
- `receipt.generated`
- `verification.passed`
- `verification.failed`
- `impact.logged`

### Add explainability metadata
Attach machine-readable context to an action or output so a developer, auditor, or end user can understand what happened.

---

## JavaScript example

```ts
import { createReceipt, emitEvent } from "@altmanai/core";

const receipt = createReceipt({
  type: "artifact.created",
  actor: "DailyPilot",
  summary: "Generated daily planning artifact",
  source: "dailypilot-engine",
});

const event = emitEvent({
  name: "receipt.generated",
  source: "dailypilot-engine",
  payload: receipt,
});

console.log(receipt.id, event.id);
```

---

## Python example

```python
from altmanai import create_receipt, emit_event

receipt = create_receipt(
    type="artifact.created",
    actor="DailyPilot",
    summary="Generated daily planning artifact",
    source="dailypilot-engine",
)

event = emit_event(
    name="receipt.generated",
    source="dailypilot-engine",
    payload=receipt,
)

print(receipt.id, event.id)
```

---

## Status

**Current status:** Initial public foundation

This repository is the official SDK layer for AltmanAI systems. The current version focuses on:

- shared schemas
- receipt generation
- verification utilities
- event hooks
- examples for TypeScript and Python

As the project matures, this repo will become the standard developer integration layer across AltmanAI products and partner workflows.

---

## Roadmap

### v0.1
- repository foundation
- shared JSON schemas
- core receipt model
- basic verification utilities
- JavaScript package scaffold
- Python package scaffold

### v0.2
- AINet event client
- explainability helper models
- richer validation and hashing utilities
- first example apps

### v0.3
- framework adapters
- expanded docs
- integration recipes for AltmanAI products
- improved testing and release workflows

---

## Security

If you discover a security issue or a vulnerability, please follow the project security policy instead of opening a public issue.

Security contact and disclosure guidance live in `SECURITY.md`.

---

## License

Licensed under the **Apache License 2.0**.

---

## AltmanAI

**AltmanAI** is building human-first AI systems designed for real-world usefulness, transparency, and measurable impact.

**Humanity leads. Intelligence follows.**

# AltmanAI SDK

**The official developer toolkit for building human-first AI apps with verifiable impact.**

AltmanAI SDK gives developers a trusted integration layer for building AI products that are transparent, explainable, and measurable. It provides shared schemas, receipt generation, artifact verification, AINet event hooks, and explainable execution patterns across TypeScript and Python.

Built for a future where **humanity leads** and **intelligence follows**.

---

## Why AltmanAI SDK exists

Most AI tooling focuses on speed and output.

AltmanAI SDK focuses on **trust, visibility, and real-world accountability**.

This repo exists to help developers build systems that do more than generate responses. It helps them create applications that can:

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
Create signed, structured records of important system actions, outputs, and decisions.

### 3. Artifact verification
Validate whether a file, payload, or output matches an expected structure, fingerprint, or integrity rule.

### 4. AINet event hooks
Emit consistent events for tracking meaningful activity across AltmanAI systems and integrations.

### 5. Explainable execution patterns
Wrap outputs with clear metadata such as decision, reason, evidence, timestamp, and actor.

### 6. Cross-language support
Use the same conceptual model in both **TypeScript** and **Python**.

---

## Design principles

AltmanAI SDK is built around a few non-negotiables:

- **Human-first**: AI should support human judgment, not erase it.
- **Truth-first**: important claims and actions should be inspectable.
- **Verifiable by default**: outputs should be easier to validate, not harder.
- **Simple to adopt**: developers should be able to integrate it without fighting the framework.
- **Useful in production**: not just theory, but real implementation value.

---

## Initial package scope

This repository is designed as a multi-language SDK with a shared schema layer.

### Planned structure

```text
altmanai-sdk/
├─ packages/
│  ├─ js/
│  │  └─ core/
│  └─ python/
│     └─ altmanai/
├─ schemas/
├─ examples/
│  ├─ nextjs-verifier/
│  └─ fastapi-agent/
├─ docs/
└─ README.md

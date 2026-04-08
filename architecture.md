# Architecture

AltmanAI SDK is structured as a small monorepo with one shared conceptual model across JavaScript and Python.

## Layers

1. **Schemas**  
   Shared JSON schemas for receipts, events, explainability payloads, and artifacts.

2. **JavaScript core package**  
   Lightweight runtime helpers for Node.js and TypeScript projects.

3. **Python package**  
   Matching helpers for Python services and agent backends.

4. **Examples**  
   Minimal demos that show receipt generation, event emission, and artifact verification.

## Current design goals

- predictable APIs
- typed payloads
- low dependency overhead
- simple validation and hashing utilities
- clear expansion path toward AINet integrations

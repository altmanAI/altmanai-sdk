# Security Policy

## Supported Versions

This project is in active development.

Security updates will be applied to the latest maintained version of `altmanai-sdk`.
Older versions may not receive fixes or backported patches.

| Version | Supported          |
|---------|--------------------|
| latest  | :white_check_mark: |
| older   | :x:                |

---

## Reporting a Vulnerability

If you believe you have found a security vulnerability in `altmanai-sdk`, please **do not open a public GitHub issue**.

Instead, report it privately to:

**security@altmanai.com**

Please include the following when possible:

- a clear description of the issue
- affected package, module, or file
- reproduction steps
- proof of concept, if available
- potential impact
- any suggested remediation

We will review reports as quickly as possible and work to validate, contain, and resolve confirmed issues responsibly.

---

## Disclosure Guidelines

To protect users, partners, and downstream integrators, please follow responsible disclosure practices:

- do not publicly disclose the issue before a fix is available
- do not exploit the issue beyond what is necessary to demonstrate it
- do not access, modify, or destroy data that does not belong to you
- do not use social engineering, spam, or denial-of-service techniques

Good-faith security research intended to improve the safety and integrity of the project is appreciated.

---

## Scope

This policy applies to the public contents of the `altmanai-sdk` repository, including:

- TypeScript packages
- Python packages
- shared schemas
- examples
- build and release workflows
- verification utilities
- receipt generation logic
- event and explainability helpers

Third-party services, dependencies, and external platforms may have separate security processes and policies.

---

## Secrets and Sensitive Data

Do not commit:

- API keys
- private credentials
- signing material
- `.env` files with live values
- customer or partner sensitive data
- private verification artifacts unless explicitly intended for public release

If a secret is accidentally committed, rotate it immediately and report the incident through the security channel above.

---

## Coordinated Fix Process

When a valid vulnerability is confirmed, the project will aim to:

1. verify and classify the issue
2. limit exposure where possible
3. prepare and test a fix
4. release the fix
5. disclose the issue responsibly when appropriate

Response and remediation timing may vary depending on severity, exploitability, and ecosystem impact.

---

## Contact

Security contact: **security@altmanai.com**

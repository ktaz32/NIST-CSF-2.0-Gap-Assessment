# Scoring Methodology

## Purpose

This document defines the maturity-scoring approach used for the Northstar HealthTech NIST Cybersecurity Framework 2.0 gap assessment.

The purpose of the scoring model is to ensure that maturity ratings are evidence-based, consistent, explainable, reproducible, and traceable to observed control conditions.

---

## Evidence-First Scoring Principle

Scores are assigned only after the supporting evidence and rationale have been documented.

The required sequence is:

```text
Evidence
    ↓
Observed Control State
    ↓
Scoring Rationale
    ↓
Maturity Score
```

Scores must not be selected first and justified retrospectively.

---

## Maturity Scale

| Score | Level | Definition |
|---:|---|---|
| 0 | Not Implemented | No meaningful evidence that the control exists |
| 1 | Initial | Ad hoc, informal, reactive, or inconsistently performed |
| 2 | Developing | Partially implemented with incomplete coverage or documentation |
| 3 | Defined | Documented and consistently implemented |
| 4 | Managed | Measured, monitored, governed, and routinely reviewed |
| 5 | Optimized | Continuously improved using metrics, automation, lessons learned, or advanced governance |

---

## Minimum Evidence Rule

No assessed NIST CSF outcome may receive a maturity score above **1** without explicit evidence supporting implementation.

Evidence may consist of:

- documented process evidence;
- modeled control-state observations;
- technical control artifacts;
- assessment interviews or assumptions documented in the case study;
- linked portfolio evidence where appropriate.

---

## Current and Target Maturity

Each assessed outcome will receive:

- **Current Maturity** — evidence-based present state
- **Target Maturity** — reasonable desired state based on business need and risk

The maturity gap is calculated as:

```text
Gap = Target Maturity - Current Maturity
```

A larger gap does not automatically mean greater business risk. Risk prioritization must also consider likelihood, impact, asset criticality, and existing controls.

---

## Risk Priority

Assessment findings may ultimately be prioritized as:

```text
Critical
High
Medium
Low
```

Priority is assigned after the risk analysis rather than directly from the maturity score.

A low maturity score may not represent a critical risk if the affected capability has low business impact, while a moderate maturity gap affecting privileged access or sensitive data may represent high risk.

---

## Required Assessment Record

Each assessed NIST CSF outcome should document:

1. CSF outcome or category
2. Current-state evidence
3. Observed control state
4. Scoring rationale
5. Current maturity
6. Target maturity
7. Maturity gap
8. Risk implication
9. Recommendation
10. Remediation priority

---

## Example

### Control Area

Privileged Access Management

### Evidence

- Excessive AWS permissions identified in a cloud-security assessment
- Wildcard IAM resource scope observed
- Stale permissions identified
- No documented quarterly privileged-access review process

### Observed Control State

Access controls exist and administrators actively manage permissions, but governance, periodic review, and control consistency are incomplete.

### Scoring Rationale

The control is partially implemented and technically functional, but lacks mature documentation and recurring review.

### Current Maturity

**2 — Developing**

### Target Maturity

**4 — Managed**

### Gap

```text
4 - 2 = 2
```

This score is derived from the evidence and rationale rather than selected independently.

---

## Scoring Governance

To maintain consistency across the assessment:

- scoring definitions should not change between findings;
- evidence should be documented before scores;
- unsupported assumptions should be explicitly labeled;
- uncertainty should be noted where evidence is incomplete;
- target maturity should be realistic and risk-based;
- technical severity and governance maturity should not be conflated.

---

## Assessment Limitation

This maturity model is a portfolio assessment mechanism and is not an official NIST maturity model.

NIST CSF 2.0 does not prescribe a 0–5 maturity scale. This project uses the scale as an analytical tool to support structured comparison, prioritization, and executive communication.

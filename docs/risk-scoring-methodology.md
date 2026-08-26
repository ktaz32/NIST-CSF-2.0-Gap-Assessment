# Risk Scoring Methodology

## Purpose

This document defines the project-wide cybersecurity risk scoring methodology for the Northstar HealthTech NIST CSF 2.0 Gap Assessment.

The objective is to convert identified control gaps into consistent, business-oriented risk ratings using a transparent 5×5 likelihood-and-impact model.

Risk scoring is performed after the underlying control evidence and maturity assessment have been documented.

The required sequence is:

```text
Evidence
    ↓
Control Gap
    ↓
Business Risk Statement
    ↓
Likelihood
    ↓
Impact
    ↓
Inherent Risk Score
    ↓
Existing Controls
    ↓
Residual Risk
    ↓
Treatment Decision
```

---

## Core Principle

Maturity and risk are related but are not the same thing.

A low maturity score does not automatically mean a critical risk.

Likewise, a relatively mature control may still support a high-risk finding if the business impact and threat likelihood are substantial.

The project therefore keeps:

- **Maturity scoring**
- **Risk scoring**

as separate analytical processes.

---

## Likelihood Scale

| Score | Rating | Definition |
|---:|---|---|
| 1 | Rare | Event is highly unlikely under current conditions |
| 2 | Unlikely | Event could occur, but is not expected regularly |
| 3 | Possible | Event is credible and may occur under realistic conditions |
| 4 | Likely | Event is expected to occur or recur without additional controls |
| 5 | Almost Certain | Event is highly probable or already occurring repeatedly |

Likelihood should consider:

- threat prevalence;
- exploitability;
- exposure;
- control weakness;
- attack opportunity;
- historical recurrence;
- ease of misuse;
- external accessibility;
- business process frequency.

---

## Impact Scale

| Score | Rating | Definition |
|---:|---|---|
| 1 | Insignificant | Minimal operational or security effect |
| 2 | Minor | Limited disruption or low-value information affected |
| 3 | Moderate | Noticeable operational, financial, security, or customer impact |
| 4 | Major | Significant business disruption, sensitive-data exposure, or material security impact |
| 5 | Severe | Enterprise-wide disruption, major data compromise, or sustained inability to deliver critical services |

Impact should consider:

- confidentiality;
- integrity;
- availability;
- customer impact;
- financial impact;
- operational disruption;
- legal or contractual exposure;
- reputational impact;
- recovery complexity.

---

## Inherent Risk Calculation

```text
Inherent Risk Score = Likelihood × Impact
```

The maximum possible score is 25.

---

## Risk Rating Thresholds

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

These thresholds are used consistently across all findings.

---

## 5×5 Risk Matrix

| Likelihood \ Impact | 1 Insignificant | 2 Minor | 3 Moderate | 4 Major | 5 Severe |
|---|---:|---:|---:|---:|---:|
| 5 Almost Certain | 5 M | 10 H | 15 H | 20 C | 25 C |
| 4 Likely | 4 L | 8 M | 12 H | 16 H | 20 C |
| 3 Possible | 3 L | 6 M | 9 M | 12 H | 15 H |
| 2 Unlikely | 2 L | 4 L | 6 M | 8 M | 10 H |
| 1 Rare | 1 L | 2 L | 3 L | 4 L | 5 M |

Legend:

```text
L = Low
M = Medium
H = High
C = Critical
```

---

## Residual Risk

Residual risk represents the level of risk remaining after considering existing controls.

The project does not subtract arbitrary control percentages from the inherent score.

Instead, residual likelihood and impact are reassessed based on the actual control environment.

Example:

```text
Inherent:
Likelihood 4 × Impact 4 = 16 High

Existing controls:
MFA + logging + least-privilege remediation capability

Residual:
Likelihood 3 × Impact 4 = 12 High
```

This approach is more defensible than using unsupported percentage reductions.

---

## Risk Treatment Options

Each risk should use one of the following treatment decisions:

### Mitigate
Implement or improve controls to reduce likelihood and/or impact.

### Accept
Formally accept the risk within approved tolerance.

### Transfer
Shift part of the financial or operational exposure through contractual or insurance arrangements.

### Avoid
Stop or redesign the activity creating the risk.

Most findings in this portfolio are expected to use **Mitigate**.

---

## Risk Acceptance

Risk acceptance should require:

- documented rationale;
- accountable risk owner;
- approval authority;
- compensating controls;
- review date;
- expiry date where appropriate.

No risk should be considered accepted simply because remediation is delayed.

---

## Priority vs Risk Rating

The project uses risk rating as the primary prioritization signal.

However, remediation sequencing may also consider:

- dependency on other controls;
- remediation effort;
- strategic importance;
- regulatory significance;
- quick-win potential;
- whether the finding is foundational.

Example:

An asset inventory finding may be High risk and prioritized early because several other controls depend on it.

---

## Required Risk Register Fields

Each risk register entry should contain:

1. Risk ID
2. Finding ID
3. Risk Domain
4. NIST CSF Mapping
5. Risk Statement
6. Likelihood Rating
7. Likelihood Score
8. Impact Rating
9. Impact Score
10. Inherent Risk Score
11. Inherent Risk Rating
12. Existing Controls
13. Residual Likelihood
14. Residual Impact
15. Residual Risk Score
16. Residual Risk Rating
17. Treatment
18. Proposed Owner
19. Target Timeframe
20. Status

---

## Scoring Governance

To maintain consistency:

- likelihood and impact must be justified independently;
- maturity scores must not be copied into risk scores;
- evidence must be documented before rating;
- the same thresholds must be used across all findings;
- uncertainty must be noted where evidence is incomplete;
- residual risk must reflect actual controls;
- risk owners should be business-accountable roles where practical.

---

## Assessment Limitation

This 5×5 model is a portfolio risk-assessment method and is not presented as an official NIST CSF scoring system.

NIST CSF 2.0 does not prescribe this numerical risk matrix.

The model is used to demonstrate structured risk analysis, prioritization, and executive communication.

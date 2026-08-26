# Assumptions and Limitations

## Purpose

This document defines the assumptions, boundaries, and limitations of the Northstar HealthTech NIST Cybersecurity Framework 2.0 Gap Assessment.

The project is a portfolio case study designed to demonstrate cybersecurity governance, risk, compliance, assessment, and consulting methodology.

Northstar HealthTech is entirely fictional.

---

## Fictional Organization

Northstar HealthTech does not represent a real company, employer, customer, healthcare provider, or production environment.

All organizational characteristics, technologies, governance gaps, control weaknesses, and business conditions were created for this assessment scenario.

No real customer data, employee data, production credentials, confidential information, or proprietary business information is used.

---

## Assessment Nature

This project is a structured cybersecurity gap assessment and portfolio simulation.

It is not:

- an official NIST assessment;
- a regulatory audit;
- a compliance certification;
- a legal opinion;
- an ISO 27001 certification assessment;
- a SOC 2 examination;
- a penetration test;
- a privacy impact assessment;
- a formal risk attestation;
- an assurance engagement.

The assessment demonstrates methodology rather than providing formal assurance.

---

## NIST CSF 2.0 Usage

The project uses NIST Cybersecurity Framework 2.0 as the primary organizational framework.

NIST CSF 2.0 is used to structure:

- governance domains;
- control outcomes;
- assessment findings;
- maturity analysis;
- remediation recommendations;
- executive reporting.

The project does not claim that NIST formally endorses the maturity scale or risk-scoring model used here.

---

## Maturity Model Assumption

The project uses a custom 0–5 maturity scale:

| Score | Level |
|---:|---|
| 0 | Not Implemented |
| 1 | Initial |
| 2 | Developing |
| 3 | Defined |
| 4 | Managed |
| 5 | Optimized |

This scale is an analytical mechanism created for the portfolio assessment.

NIST CSF 2.0 does not prescribe this 0–5 scoring model.

The maturity scores are intended to support:

- comparison;
- prioritization;
- gap analysis;
- executive communication.

They should not be interpreted as official NIST maturity ratings.

---

## Risk Scoring Assumption

The project uses a 5×5 likelihood-and-impact matrix.

Risk is calculated using:

```text
Risk Score = Likelihood × Impact
```

The resulting ratings are:

```text
Low
Medium
High
Critical
```

This model is a portfolio risk-assessment method and is not presented as an official NIST scoring system.

Risk ratings are illustrative and depend on the fictional environment assumptions.

---

## Evidence Assumptions

The assessment follows an evidence-first approach.

However, because the organization is fictional, evidence may include:

- modeled control-state observations;
- fictional policy and process conditions;
- simulated governance gaps;
- technical portfolio artifacts;
- cloud security findings;
- detection-engineering artifacts;
- SOC investigation examples.

Where technical portfolio projects are referenced, they demonstrate control-validation capability rather than evidence from a real Northstar HealthTech environment.

---

## Technical Portfolio Cross-Reference

Some findings reference technical evidence from separate portfolio projects.

Examples include:

- AWS IAM least-privilege findings;
- stale permissions;
- wildcard resource scope;
- CloudTrail logging gaps;
- Detection-as-Code telemetry requirements;
- SOC investigation workflows.

These cross-references are used to demonstrate how technical observations can support governance and risk analysis.

They do not imply that those projects were performed against a real Northstar HealthTech environment.

---

## Scope Limitations

The assessment focuses on selected cybersecurity governance and operational capabilities.

It does not attempt to assess every NIST CSF 2.0 outcome.

Selected areas include:

- cybersecurity governance;
- roles and responsibilities;
- third-party risk;
- identity and access governance;
- asset management;
- logging and monitoring;
- vulnerability remediation;
- incident response;
- lessons learned;
- recovery readiness.

Other cybersecurity domains may require additional assessment in a real engagement.

---

## No Regulatory Determination

Although Northstar HealthTech is modeled as a healthcare technology organization, this project does not determine compliance with:

- HIPAA;
- HITECH;
- GDPR;
- Saudi PDPL;
- PCI DSS;
- ISO 27001;
- SOC 2;
- any other regulatory or contractual framework.

Healthcare context is used only to create realistic business priorities and security considerations.

---

## No Legal Interpretation

The assessment does not provide legal guidance.

Recommendations involving:

- breach notification;
- privacy obligations;
- contractual terms;
- regulatory reporting;
- evidence retention;
- third-party contractual requirements;

would require qualified legal, privacy, or compliance review in a real organization.

---

## No Production Validation

The project does not include:

- production penetration testing;
- production vulnerability scanning;
- real endpoint validation;
- real IAM access reviews;
- real vendor assessments;
- live incident response exercises;
- real recovery testing.

Where technical control validation is discussed, it is based on portfolio labs or modeled evidence.

---

## Maturity Target Assumption

The project generally uses **Level 4 — Managed** as the target state for the assessed capabilities.

This is not intended to imply that every real organization should target the same maturity level.

A real target state should depend on:

- business risk;
- organization size;
- threat exposure;
- regulatory obligations;
- resource constraints;
- technology complexity;
- customer requirements;
- risk appetite.

---

## Risk Rating Limitations

Risk ratings are based on fictional business and control assumptions.

In a real assessment, likelihood and impact should be informed by:

- threat intelligence;
- incident history;
- business impact analysis;
- asset criticality;
- data classification;
- technical exposure;
- control effectiveness;
- legal and contractual requirements.

The portfolio ratings therefore demonstrate methodology rather than predictive accuracy.

---

## Residual Risk Limitation

Residual risk should normally be calculated after validating the effectiveness of existing controls.

Because this is a simulated environment, residual-risk analysis may be limited until the target-state control package is defined.

The project intentionally avoids arbitrary percentage reductions to inherent risk.

---

## Executive Reporting Limitation

Executive summaries, maturity visuals, and risk dashboards are generated from the fictional assessment data.

They are designed to demonstrate stakeholder communication and consulting presentation skills.

They should not be interpreted as reporting from a real security program.

---

## Visualizations

Charts and risk visuals are generated using Python.

These visuals are based on the project assessment data and can be reproduced using:

```bash
python scripts/generate_visuals.py
```

The purpose is to provide transparent, version-controlled, reproducible reporting.

---

## Assumption Management

Where evidence is incomplete, the project follows these principles:

```text
Document assumption
        ↓
Avoid overstating certainty
        ↓
Assign conservative maturity
        ↓
Identify validation requirement
```

Unsupported assumptions should not be presented as verified facts.

---

## Assessment Boundary

This assessment represents a point-in-time view of the fictional Northstar HealthTech environment.

It does not model every future technology change, threat scenario, organizational change, or control implementation.

In a real engagement, maturity and risk should be reassessed periodically.

---

## Recommended Real-World Validation

If this methodology were applied to a real organization, validation would require activities such as:

- stakeholder interviews;
- policy review;
- technical configuration review;
- access reviews;
- asset inventory reconciliation;
- logging validation;
- vulnerability data review;
- incident-response evidence;
- tabletop exercises;
- backup restoration testing;
- third-party assessment evidence.

Only after this validation should formal conclusions be made.

---

## Final Limitation Statement

The Northstar HealthTech NIST CSF 2.0 Gap Assessment is a cybersecurity portfolio case study.

Its purpose is to demonstrate the ability to:

```text
Assess
        ↓
Map
        ↓
Score
        ↓
Prioritize
        ↓
Translate technical issues into business risk
        ↓
Recommend remediation
        ↓
Communicate to stakeholders
```

The project should therefore be evaluated as a demonstration of cybersecurity assessment methodology and consulting capability, not as a formal assurance opinion on a real organization.

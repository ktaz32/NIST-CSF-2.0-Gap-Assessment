# Executive Cybersecurity Assessment Summary

## Northstar HealthTech — NIST CSF 2.0 Gap Assessment

> **Portfolio case study:** Northstar HealthTech is a fictional organization created solely for this cybersecurity governance, risk, and compliance assessment.

---

## Executive Summary

Northstar HealthTech demonstrates meaningful technical cybersecurity capability across cloud security, endpoint protection, identity and access management, logging, detection engineering, incident investigation, and technical remediation.

However, the assessment identifies a consistent maturity pattern:

> **Technical capability is ahead of governance maturity.**

The organization has many technical controls in place, but several supporting governance processes remain informal, inconsistently documented, weakly measured, or insufficiently tested.

The assessment evaluated 12 cybersecurity capability areas against selected NIST Cybersecurity Framework 2.0 outcomes.

The average current maturity is:

```text
1.83 / 5
```

The target maturity is:

```text
4.00 / 5
```

The average maturity gap is:

```text
2.17
```

The most significant gaps are:

- formal cybersecurity risk-management strategy;
- incident-response exercise maturity;
- privileged-access governance;
- asset visibility;
- security logging coverage;
- vulnerability remediation governance;
- incident-response formalization;
- recovery assurance.

---

## Assessment Snapshot

| Metric | Result |
|---|---:|
| Findings assessed | 12 |
| Average current maturity | **1.83 / 5** |
| Average target maturity | **4.00 / 5** |
| Average maturity gap | **2.17** |
| Critical risks | 0 |
| High risks | **11** |
| Medium risks | **1** |
| Low risks | 0 |

---

## Current vs Target Maturity

![Current vs Target Maturity](../visuals/maturity-by-finding.png)

The largest individual maturity gaps are:

| Finding | Current | Target | Gap |
|---|---:|---:|---:|
| GRC-001 — Cybersecurity Risk Management Strategy | 1 | 4 | **3** |
| GRC-010 — Incident Response Exercises and Testing | 1 | 4 | **3** |

All other core findings have a maturity gap of 2.

---

## Maturity Heatmap

![Maturity Heatmap](../visuals/maturity-heatmap.png)

The heatmap shows that the fictional organization has broad cybersecurity activity, but most capabilities remain at **Level 2 — Developing** rather than **Level 4 — Managed**.

---

## Risk Profile

```text
Critical   0
High      11
Medium     1
Low        0
```

![Cybersecurity Risk Matrix](../visuals/risk-matrix.png)

The concentration of High risks reflects the intentionally immature assessment environment.

---

# Top Executive Risks

## 1. Cybersecurity Risk Management Strategy

**Finding:** GRC-001  
**Risk Rating:** High  
**Current Maturity:** 1 / 5  
**Target:** 4 / 5

### Executive Concern

Cybersecurity activities occur, but there is no formally approved enterprise cyber-risk strategy defining risk objectives, risk appetite, ownership, escalation, and governance.

### Business Impact

Without a consistent risk framework, high-impact security issues may be prioritized inconsistently or accepted without appropriate executive oversight.

### Recommended Action

Establish an approved cybersecurity risk-management strategy and formal risk governance process.

---

## 2. Vulnerability Remediation Governance

**Finding:** GRC-008  
**Risk Rating:** High  
**Current Maturity:** 2 / 5

### Executive Concern

Known vulnerabilities can be identified, but remediation deadlines are not governed by formal risk-based SLAs.

### Business Impact

Known exploitable weaknesses may remain unresolved longer than business risk permits.

### Recommended Action

Define risk-based remediation SLAs, escalation thresholds, exception governance, and management reporting.

---

## 3. Privileged Access Governance

**Findings:** GRC-004 / GRC-005  
**Risk Rating:** High

### Executive Concern

Technical assessment evidence demonstrates excessive, wildcard, and stale cloud permissions, while recurring privileged-access recertification remains immature.

### Business Impact

A compromised privileged identity could have a larger impact than necessary.

### Recommended Action

Implement least-privilege governance and recurring privileged-access reviews.

---

## 4. Security Monitoring Coverage

**Finding:** GRC-007  
**Risk Rating:** High  
**Current Maturity:** 2 / 5

### Executive Concern

Security monitoring exists, but coverage is fragmented.

A cloud-security assessment demonstrated that S3 object-level activity was not visible until specific CloudTrail data-event logging was enabled.

### Business Impact

Important security activity may occur without timely detection or sufficient forensic evidence.

### Recommended Action

Create an enterprise logging standard, log-source inventory, detection-to-telemetry mapping, and monitoring-health metrics.

---

## 5. Incident Response and Recovery Assurance

**Findings:** GRC-009, GRC-010, GRC-012  
**Risk Rating:** High

### Executive Concern

Northstar HealthTech can investigate incidents technically, but procedures, exercise testing, and recovery validation remain immature.

### Business Impact

During a major incident, uncertainty around authority, escalation, communications, and restoration could increase business disruption.

### Recommended Action

Formalize the incident-response program, conduct recurring exercises, and validate recovery procedures through hands-on restoration testing.

---

# 90-Day Cybersecurity Improvement Roadmap

## Days 0–30 — Establish Governance and Immediate Risk Control

### Executive Actions

- assign executive cybersecurity sponsor;
- approve interim cybersecurity risk objectives;
- assign owners to all 12 assessment risks;
- establish a formal cyber-risk register;
- identify critical assets;
- identify privileged identities;
- review clearly excessive or stale privileged permissions;
- identify critical logging gaps;
- define interim vulnerability remediation targets;
- establish incident escalation contacts.

### Expected Outcome

```text
Ownership
+
Visibility
+
Immediate exposure reduction
```

---

## Days 31–60 — Standardize Core Security Processes

### Priority Actions

- develop cybersecurity RACI;
- establish privileged-access review procedure;
- create authoritative asset inventory;
- publish logging and monitoring requirements;
- define vulnerability remediation SLAs;
- approve incident severity and escalation model;
- create formal incident-response plan;
- define recovery priorities and provisional RTO/RPO values.

### Expected Outcome

```text
Repeatable security processes
+
Clear accountability
+
Defined control expectations
```

---

## Days 61–90 — Validate and Measure

### Priority Actions

- perform first privileged-access recertification;
- validate critical log-source coverage;
- conduct first formal incident-response tabletop;
- test restoration of critical data or application;
- establish third-party risk tiering;
- launch cybersecurity metrics dashboard;
- track corrective actions from exercises and control reviews.

### Expected Outcome

```text
Governance
        ↓
Execution
        ↓
Testing
        ↓
Measurement
```

---

# Strategic Improvement Waves

## Wave 1 — Governance and Visibility

- GRC-001 — Cybersecurity risk strategy
- GRC-002 — Roles and responsibilities
- GRC-006 — Asset inventory

**Objective:** Establish who owns risk, how it is governed, and what must be protected.

---

## Wave 2 — Identity and Exposure Reduction

- GRC-004 — Excessive and stale privileged access
- GRC-005 — Privileged access reviews
- GRC-008 — Vulnerability remediation SLAs

**Objective:** Reduce preventable exposure and improve accountability for known risks.

---

## Wave 3 — Detection and Response

- GRC-007 — Security logging and monitoring
- GRC-009 — Incident response
- GRC-010 — Incident-response exercises

**Objective:** Improve detection visibility and ensure response procedures work under realistic conditions.

---

## Wave 4 — Resilience and External Risk

- GRC-012 — Recovery assurance
- GRC-003 — Third-party risk
- GRC-011 — Lessons learned

**Objective:** Strengthen organizational resilience, supplier governance, and continuous improvement.

---

# Technical-to-Governance Evidence

A core objective of this project is to demonstrate the ability to translate technical findings into governance and business-risk decisions.

## AWS Cloud Security

Technical evidence includes:

- excessive AWS S3 permissions;
- wildcard IAM resource scope;
- stale application permissions;
- S3 resource-policy access;
- public SSH exposure;
- CloudTrail S3 data-event visibility gap.

These technical findings support broader GRC conclusions involving:

- least privilege;
- access governance;
- logging;
- security monitoring;
- risk treatment;
- control validation.

---

## Detection-as-Code

Detection engineering demonstrates:

- security-control implementation;
- telemetry dependency;
- automated validation;
- MITRE ATT&CK alignment;
- behavioral testing;
- analyst response design.

The GRC assessment extends this by asking:

> Are the required telemetry sources governed, available, monitored, and periodically validated?

---

## SOC Investigation Capability

SOC investigation artifacts demonstrate technical event analysis.

The GRC layer adds:

```text
Detection
        ↓
Investigation
        ↓
Incident classification
        ↓
Business impact
        ↓
Escalation
        ↓
Containment authority
        ↓
Recovery
        ↓
Lessons learned
```

---

# Executive Recommendation

Northstar HealthTech should not prioritize the purchase of additional security technology as its first response to this assessment.

The more immediate need is to improve the governance and operating model around the capabilities already present.

The recommended focus is:

1. formalize cybersecurity risk governance;
2. establish accountability;
3. improve asset visibility;
4. strengthen privileged-access governance;
5. govern vulnerability remediation;
6. close monitoring gaps;
7. formalize and exercise incident response;
8. validate recovery capability;
9. strengthen third-party governance;
10. create a repeatable continuous-improvement cycle.

The organization already demonstrates useful technical capability.

The next maturity step is to make that capability **consistent, accountable, measurable, and resilient**.

---

## Supporting Documents

- [`Detailed Gap Assessment`](detailed-gap-assessment.md)
- [`Cybersecurity Risk Register`](risk-register.md)
- [`Risk Scoring Methodology`](../docs/risk-scoring-methodology.md)
- Individual GRC findings under `../findings/`

---

## Portfolio Disclaimer

Northstar HealthTech is entirely fictional.

The assessment is a cybersecurity portfolio case study and does not represent a real organization, customer, employer, compliance certification, or assurance engagement.

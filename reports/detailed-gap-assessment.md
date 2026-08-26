# Detailed NIST CSF 2.0 Gap Assessment

## Overview

This document consolidates the 12 core findings from the Northstar HealthTech cybersecurity maturity assessment into one GitHub-readable matrix.

The detailed finding files remain the authoritative source for full evidence, scoring rationale, and remediation guidance.

## Assessment Summary

| Finding | NIST CSF 2.0 | Current | Target | Gap | Inherent Risk | Priority |
|---|---|---:|---:|---:|---|---|
| GRC-001 — Cybersecurity Risk Management Strategy Not Formally Established | GV.RM | 1 | 4 | 3 | High | High |
| GRC-002 — Roles, Responsibilities, and Authorities Incompletely Defined | GV.RR | 2 | 4 | 2 | High | High |
| GRC-003 — Third-Party Cybersecurity Risk Reviews Are Inconsistent | GV.SC | 2 | 4 | 2 | High | High |
| GRC-004 — Excessive and Stale Privileged Access | PR.AA | 2 | 4 | 2 | High | High |
| GRC-005 — Privileged Access Reviews Not Performed on a Formal Recurring Basis | PR.AA | 2 | 4 | 2 | High | High |
| GRC-006 — Asset Inventory Is Incomplete | ID.AM | 2 | 4 | 2 | High | High |
| GRC-007 — Security Logging and Monitoring Coverage Is Incomplete | DE.CM | 2 | 4 | 2 | High | High |
| GRC-008 — Vulnerability Remediation SLAs Are Not Formally Defined | ID.RA / PR.PS | 2 | 4 | 2 | High | High |
| GRC-009 — Incident Response Procedures Are Incompletely Formalized | RS | 2 | 4 | 2 | High | High |
| GRC-010 — Incident Response Exercises and Testing Are Immature | RS / RC | 1 | 4 | 3 | High | High |
| GRC-011 — Post-Incident Lessons-Learned Process Is Inconsistent | ID.IM | 2 | 4 | 2 | Medium | Medium |
| GRC-012 — Recovery Procedures Are Insufficiently Tested | RC | 2 | 4 | 2 | High | High |

## Detailed Gap Matrix

| ID | Control Area | Evidence Summary | Current | Target | Gap | Primary Risk | Recommended Improvement |
|---|---|---|---:|---:|---:|---|---|
| GRC-001 | Cyber risk management | Technical security activity exists, but no formally approved cyber-risk strategy, risk objectives, appetite/tolerance, or recurring governance was identified. | 1 | 4 | 3 | Material risks may be inconsistently prioritized or accepted. | Establish formal cyber-risk strategy, ownership, appetite/tolerance, governance cadence, and reporting. |
| GRC-002 | Roles and authorities | Security work is performed, but accountability, decision rights, escalation authority, and RACI coverage are incomplete. | 2 | 4 | 2 | Critical security work may be delayed, duplicated, or left unowned. | Create an approved cybersecurity RACI and define escalation and risk-acceptance authority. |
| GRC-003 | Third-party risk | Vendor reviews occur inconsistently; supplier inventory, tiering, due diligence, reassessment, and exception governance are immature. | 2 | 4 | 2 | Supplier weaknesses may expose data, systems, or operations. | Implement a risk-based third-party lifecycle from onboarding through offboarding. |
| GRC-004 | Least privilege | AWS evidence shows broad managed permissions, wildcard scope, and stale permissions. | 2 | 4 | 2 | Compromised identities may retain unnecessary capabilities. | Formalize least-privilege governance, entitlement ownership, stale-access removal, and metrics. |
| GRC-005 | Access recertification | No formal recurring privileged-access review process, evidence trail, or overdue escalation exists. | 2 | 4 | 2 | Elevated access may persist after business need ends. | Implement risk-based recurring recertification, documented decisions, and JML integration. |
| GRC-006 | Asset management | Asset data exists across endpoint, AWS, Microsoft 365, SaaS, and other platforms, but no authoritative enterprise inventory exists. | 2 | 4 | 2 | Unknown assets may remain outside patching, monitoring, and recovery. | Establish an authoritative inventory with ownership, criticality, lifecycle, and reconciliation. |
| GRC-007 | Logging and monitoring | Windows, Defender, authentication, and CloudTrail telemetry exist, but coverage is fragmented; AWS-06 showed missing S3 data-event visibility until enabled. | 2 | 4 | 2 | Malicious activity may go undetected or lack forensic evidence. | Create a logging standard, log-source inventory, telemetry mapping, health monitoring, and metrics. |
| GRC-008 | Vulnerability remediation | Vulnerabilities can be identified and remediated, but no formal SLA model, escalation threshold, or risk-acceptance process exists. | 2 | 4 | 2 | Known weaknesses may remain exploitable too long. | Define risk-based remediation SLAs, contextual prioritization, exceptions, escalation, and metrics. |
| GRC-009 | Incident response | Technical investigation capability exists, but response planning, severity, escalation, evidence handling, and communications are incomplete. | 2 | 4 | 2 | Incidents may be handled inconsistently or too slowly. | Formalize incident response planning, severity, escalation, containment authority, communications, and metrics. |
| GRC-010 | IR exercises | Response capability exists, but exercises are infrequent, weakly governed, and not tied to corrective-action tracking. | 1 | 4 | 3 | Hidden process failures may remain undiscovered until a real incident. | Establish recurring risk-based exercises, after-action reviews, corrective actions, and retesting. |
| GRC-011 | Lessons learned | Operational learning occurs informally, but post-incident reviews, root-cause analysis, ownership, and trend analysis are inconsistent. | 2 | 4 | 2 | Recurring control weaknesses may remain unresolved. | Standardize lessons learned, root-cause analysis, action tracking, validation, and reporting. |
| GRC-012 | Recovery assurance | Basic backup/recovery exists, but testing, RTO/RPO, dependency mapping, cyber-recovery scenarios, and metrics are incomplete. | 2 | 4 | 2 | Restoration may fail or exceed business recovery requirements. | Define recovery objectives, map dependencies, test restores, run cyber-recovery exercises, and track metrics. |

## Maturity Profile

```text
Level 0 — Not Implemented: 0
Level 1 — Initial:         2
Level 2 — Developing:    10
Level 3 — Defined:        0
Level 4 — Managed:        0
Level 5 — Optimized:      0
```

Average current maturity:

```text
22 / 12 = 1.83 / 5
```

Average target maturity:

```text
4.00 / 5
```

Average maturity gap:

```text
2.17
```

## Risk Distribution

```text
Critical: 0
High:    11
Medium:   1
Low:      0
Total:   12
```

## Largest Maturity Gaps

**GRC-001 — Risk Management Strategy**

```text
Current: 1
Target:  4
Gap:     3
```

**GRC-010 — Incident Response Exercises**

```text
Current: 1
Target:  4
Gap:     3
```

All other core findings have a maturity gap of 2.

## Key Control Dependencies

### Governance

```text
GRC-001 Risk Strategy
        ↓
GRC-002 Roles and Authority
        ↓
GRC-003 Third-Party Governance
```

### Identity Governance

```text
GRC-004 Excessive / Stale Access
        ↓
GRC-005 Recurring Access Review
```

### Security Operations

```text
GRC-006 Asset Visibility
        ↓
GRC-007 Logging Coverage
        ↓
GRC-008 Vulnerability Remediation
        ↓
GRC-009 Incident Response
```

### Resilience

```text
GRC-009 Formalize Response
        ↓
GRC-010 Exercise Response
        ↓
GRC-011 Learn and Improve
        ↓
GRC-012 Validate Recovery
```

## Technical Portfolio Crosswalk

| GRC Finding | Technical Evidence |
|---|---|
| GRC-004 | AWS-01 excessive S3 permissions; AWS-02 wildcard scope; AWS-03 stale permissions |
| GRC-005 | IAM entitlement findings demonstrate the need for periodic recertification |
| GRC-007 | AWS-06 CloudTrail S3 data-event logging gap; Detection-as-Code telemetry dependencies |
| GRC-009 | SOC investigation workflows demonstrate technical incident-analysis capability |
| GRC-010 | Detection and SOC artifacts provide realistic exercise scenarios |
| GRC-011 | AWS-06 remediation demonstrates converting a technical lesson into a monitoring improvement |

The crosswalk demonstrates:

```text
Technical observation
        ↓
Control weakness
        ↓
Governance gap
        ↓
Business risk
        ↓
Remediation recommendation
```

## Recommended Remediation Waves

### Wave 1 — Governance and Visibility

- GRC-001 — Cybersecurity risk strategy
- GRC-002 — Roles and responsibilities
- GRC-006 — Asset inventory

### Wave 2 — Identity and Exposure Reduction

- GRC-004 — Excessive and stale access
- GRC-005 — Privileged access reviews
- GRC-008 — Vulnerability remediation SLAs

### Wave 3 — Detection and Response

- GRC-007 — Logging and monitoring
- GRC-009 — Incident response formalization
- GRC-010 — Incident-response exercises

### Wave 4 — Resilience and External Risk

- GRC-012 — Recovery testing
- GRC-003 — Third-party risk
- GRC-011 — Lessons learned

## Assessment Conclusion

Northstar HealthTech demonstrates meaningful technical cybersecurity capability across endpoint security, cloud controls, monitoring, incident investigation, and technical remediation.

The dominant assessment pattern is:

> **Technical capability is ahead of governance maturity.**

Most assessed capabilities operate at **Level 2 — Developing**, while the target state is **Level 4 — Managed**.

The recommended improvement program should therefore prioritize governance, accountability, asset visibility, identity controls, monitoring, vulnerability treatment, formal incident response, exercise testing, and recovery assurance in a phased sequence.

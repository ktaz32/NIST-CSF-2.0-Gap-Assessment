# Cybersecurity Risk Register

## Overview

This register consolidates the 12 core risks identified during the Northstar HealthTech NIST CSF 2.0 Gap Assessment.

The register is designed for GitHub-first review. A spreadsheet version may be maintained as a secondary working artifact, but this Markdown version is the primary recruiter-facing deliverable.

---

## Risk Summary

| Risk ID | Finding | Domain | Likelihood | Impact | Inherent Score | Rating | Treatment | Proposed Owner | Status |
|---|---|---|---|---|---:|---|---|---|---|
| RISK-001 | GRC-001 | Cybersecurity Governance | Likely (4) | Major (4) | 16 | High | Mitigate | Executive Sponsor / Security Leadership | Open |
| RISK-002 | GRC-002 | Governance / Accountability | Possible (3) | Major (4) | 12 | High | Mitigate | Executive Sponsor / Security Leadership | Open |
| RISK-003 | GRC-003 | Third-Party / Supply Chain | Possible (3) | Major (4) | 12 | High | Mitigate | Security Leadership / Procurement | Open |
| RISK-004 | GRC-004 | Identity and Access Management | Possible (3) | Major (4) | 12 | High | Mitigate | IT / Security / Cloud Platform Owner | Open |
| RISK-005 | GRC-005 | Identity Governance | Possible (3) | Major (4) | 12 | High | Mitigate | IAM / IT / Security Leadership | Open |
| RISK-006 | GRC-006 | Asset Management | Possible (3) | Major (4) | 12 | High | Mitigate | IT Operations / Security | Open |
| RISK-007 | GRC-007 | Security Monitoring | Possible (3) | Major (4) | 12 | High | Mitigate | Security Operations / IT Operations | Open |
| RISK-008 | GRC-008 | Vulnerability Management | Likely (4) | Major (4) | 16 | High | Mitigate | IT Operations / Security / Asset Owner | Open |
| RISK-009 | GRC-009 | Incident Response | Possible (3) | Major (4) | 12 | High | Mitigate | Security Leadership / IT Leadership | Open |
| RISK-010 | GRC-010 | Incident Response / Resilience | Possible (3) | Major (4) | 12 | High | Mitigate | Security Leadership / Business Continuity | Open |
| RISK-011 | GRC-011 | Continuous Improvement | Possible (3) | Moderate (3) | 9 | Medium | Mitigate | Security Leadership | Open |
| RISK-012 | GRC-012 | Recovery / Cyber Resilience | Possible (3) | Major (4) | 12 | High | Mitigate | IT Operations / Business Continuity | Open |

---

## Portfolio Risk Profile

```text
Critical: 0
High:    11
Medium:   1
Low:      0
Total:   12
```

This profile reflects the intentionally immature fictional environment used for the assessment.

It should not be interpreted as a real organization's security posture.

---

## Detailed Risk Entries

### RISK-001 — Cybersecurity Risk Management Strategy

**Finding:** GRC-001  
**NIST CSF:** GV.RM  
**Likelihood:** Likely (4)  
**Impact:** Major (4)  
**Inherent Risk:** 16 — High

**Risk statement:**  
If Northstar HealthTech does not establish and govern organization-wide cybersecurity risk-management objectives, material cybersecurity risks may be inconsistently identified, prioritized, accepted, or remediated, increasing the likelihood that high-impact threats remain inadequately managed.

**Existing controls:** Technical security operations, endpoint protection, logging, IAM, assessment capability.

**Treatment:** Mitigate

---

### RISK-002 — Undefined Cybersecurity Accountability

**Finding:** GRC-002  
**NIST CSF:** GV.RR  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If cybersecurity roles, responsibilities, authorities, and escalation paths are not formally defined, critical security activities may be delayed, inconsistently executed, or left unowned.

**Existing controls:** Internal IT/security personnel and operational responsibility.

**Treatment:** Mitigate

---

### RISK-003 — Inconsistent Third-Party Cybersecurity Review

**Finding:** GRC-003  
**NIST CSF:** GV.SC  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If third-party cyber risks are not consistently assessed and governed, supplier weaknesses may expose sensitive information, services, identities, or operations.

**Existing controls:** Some vendor-security review activity and enterprise platform controls.

**Treatment:** Mitigate

---

### RISK-004 — Excessive and Stale Privileged Access

**Finding:** GRC-004  
**NIST CSF:** PR.AA  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If least privilege is not consistently enforced and stale access is not removed, compromised or misused identities may retain unnecessary permissions.

**Existing controls:** AWS IAM, CloudTrail, role-based access, technical remediation capability.

**Treatment:** Mitigate

---

### RISK-005 — Incomplete Privileged Access Recertification

**Finding:** GRC-005  
**NIST CSF:** PR.AA  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If privileged access is not formally reviewed on a recurring basis, elevated permissions may remain active after they are no longer required.

**Existing controls:** IAM role administration and ability to revoke access.

**Treatment:** Mitigate

---

### RISK-006 — Incomplete Asset Inventory

**Finding:** GRC-006  
**NIST CSF:** ID.AM  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If the organization does not maintain a complete and authoritative asset inventory, unmanaged or unknown systems may remain outside security controls.

**Existing controls:** Endpoint, cloud, Microsoft 365, and platform-specific inventories.

**Treatment:** Mitigate

---

### RISK-007 — Incomplete Security Logging and Monitoring

**Finding:** GRC-007  
**NIST CSF:** DE.CM  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If logging and monitoring coverage is incomplete, malicious or unauthorized activity may occur without timely detection or sufficient forensic evidence.

**Existing controls:** Windows Security logs, Microsoft Defender, AWS CloudTrail, detection engineering.

**Treatment:** Mitigate

---

### RISK-008 — Undefined Vulnerability Remediation SLAs

**Finding:** GRC-008  
**NIST CSF:** ID.RA / PR.PS  
**Likelihood:** Likely (4)  
**Impact:** Major (4)  
**Inherent Risk:** 16 — High

**Risk statement:**  
If risk-based remediation SLAs are not defined and enforced, known vulnerabilities may remain unresolved beyond acceptable periods.

**Existing controls:** Vulnerability identification, endpoint protection, technical remediation capability.

**Treatment:** Mitigate

---

### RISK-009 — Incompletely Formalized Incident Response

**Finding:** GRC-009  
**NIST CSF:** RS  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If incident response procedures are not sufficiently formalized, incidents may be handled inconsistently or too slowly.

**Existing controls:** SOC-style investigation capability, telemetry, detection engineering.

**Treatment:** Mitigate

---

### RISK-010 — Immature Incident Response Testing

**Finding:** GRC-010  
**NIST CSF:** RS / RC  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If incident response and recovery procedures are not routinely exercised, weaknesses may remain undiscovered until a real incident occurs.

**Existing controls:** Developing incident procedures and technical investigation capability.

**Treatment:** Mitigate

---

### RISK-011 — Inconsistent Lessons-Learned Process

**Finding:** GRC-011  
**NIST CSF:** ID.IM  
**Likelihood:** Possible (3)  
**Impact:** Moderate (3)  
**Inherent Risk:** 9 — Medium

**Risk statement:**  
If lessons from incidents and exercises are not consistently captured and tracked, recurring control weaknesses may remain unresolved.

**Existing controls:** Informal learning, technical remediation, developing response process.

**Treatment:** Mitigate

---

### RISK-012 — Insufficiently Tested Recovery Procedures

**Finding:** GRC-012  
**NIST CSF:** RC  
**Likelihood:** Possible (3)  
**Impact:** Major (4)  
**Inherent Risk:** 12 — High

**Risk statement:**  
If recovery procedures are not routinely tested and validated, restoration failures or unknown dependencies may delay recovery after a major incident.

**Existing controls:** Basic backup and recovery capability.

**Treatment:** Mitigate

---

## Recommended Remediation Sequence

The recommended sequence is based on risk, foundational dependency, and implementation logic:

```text
1. GRC-001 — Risk Management Strategy
2. GRC-002 — Roles and Responsibilities
3. GRC-006 — Asset Inventory
4. GRC-004 — Excessive / Stale Privileged Access
5. GRC-005 — Privileged Access Reviews
6. GRC-007 — Logging and Monitoring
7. GRC-008 — Vulnerability Remediation SLAs
8. GRC-009 — Incident Response Formalization
9. GRC-010 — Incident Response Exercises
10. GRC-012 — Recovery Testing
11. GRC-003 — Third-Party Risk
12. GRC-011 — Lessons Learned
```

This is not a statement that lower-listed risks are unimportant. The sequence reflects dependency and practical implementation order.

---

## Next Development Step

Residual risk ratings should be added after the project defines the target-state control package for each finding.

The register can then support:

- a 5×5 risk matrix;
- top-risk summary;
- executive dashboard;
- remediation roadmap;
- Python-generated visuals.

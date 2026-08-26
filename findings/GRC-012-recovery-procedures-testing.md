# GRC-012 — Recovery Procedures Are Insufficiently Tested

## Finding Summary

Northstar HealthTech relies on cloud services, endpoints, SaaS platforms, identity systems, and business applications to support day-to-day operations. Although the fictional organization has basic backup and recovery capabilities, recovery procedures are not tested often enough or deeply enough to provide strong assurance that critical services, data, and dependencies can be restored within acceptable business timeframes after a cybersecurity incident or major outage.

This creates a resilience gap: backup existence does not necessarily demonstrate recoverability.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **RECOVER (RC)** Function.

---

## NIST CSF 2.0 Mapping

### Primary Function

**RECOVER (RC)**

This finding focuses on the organization's ability to restore assets and operations after a cybersecurity incident and to validate that recovery procedures work as intended.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Backup and recovery capabilities exist for selected systems.
- Recovery priorities are not consistently tied to business criticality.
- Formal recovery testing is limited.
- No recurring enterprise recovery-test schedule has been identified.
- Recovery Time Objectives (RTOs) are not consistently documented.
- Recovery Point Objectives (RPOs) are not consistently documented.
- Application and infrastructure dependencies are not fully mapped.
- Restoration procedures are not consistently validated through hands-on testing.
- Recovery testing does not routinely include cybersecurity scenarios such as ransomware.
- Third-party dependencies are not always included.
- Recovery test outcomes are not consistently tracked to corrective action.

---

## Observed Control State

Northstar HealthTech has recovery capabilities, but assurance over those capabilities is incomplete.

The organization cannot consistently demonstrate that:

- critical backups are recoverable;
- recovery priorities reflect business impact;
- recovery procedures are current;
- RTOs and RPOs can actually be achieved;
- identity, cloud, and third-party dependencies are understood;
- recovery procedures function during cyber-related disruption;
- corrective actions from failed tests are tracked to closure.

The current state is therefore **partially implemented but insufficiently tested and governed**.

---

## Scoring Rationale

Evidence demonstrates that backup and recovery capabilities exist, supporting a score above **1 — Initial**.

However, the organization lacks recurring recovery testing, consistently documented RTOs/RPOs, dependency mapping, cyber-specific recovery exercises, and structured corrective-action tracking.

The capability is therefore assessed at **2 — Developing**.

---

## Current Maturity

**2 — Developing**

> Recovery capabilities exist, but testing, documentation, dependency management, performance measurement, and governance remain incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which recovery is:

- formally planned;
- prioritized by business criticality;
- supported by defined RTOs and RPOs;
- tested on a recurring basis;
- validated through actual restoration;
- integrated with incident response;
- measured through recovery metrics;
- improved through lessons learned.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

---

## Business Risk

Insufficiently tested recovery procedures can lead to:

- prolonged outages;
- failed restoration attempts;
- loss of critical business data;
- inability to meet recovery objectives;
- dependency failures during recovery;
- ineffective ransomware recovery;
- increased operational and customer impact;
- false confidence in backup capability.

---

## Risk Statement

> If Northstar HealthTech does not routinely test and validate recovery procedures for critical systems and data, restoration failures or unexpected dependencies may delay recovery following a cybersecurity incident or major disruption, increasing operational, financial, and customer impact.

---

## Existing Controls

Existing strengths include:

- basic backup capability;
- cloud-service resilience;
- incident-response capability;
- security monitoring;
- technical remediation capability;
- developing business continuity awareness.

These controls reduce some resilience risk but do not demonstrate tested recoverability.

---

## Recommended Remediation

Northstar HealthTech should establish a formal recovery assurance program covering:

1. Critical business services
2. Recovery priorities
3. Recovery Time Objectives
4. Recovery Point Objectives
5. Backup requirements
6. Restoration procedures
7. Dependency mapping
8. Cyber recovery scenarios
9. Recovery-test frequency
10. Success criteria
11. Evidence requirements
12. Corrective-action tracking
13. Retest requirements
14. Recovery metrics
15. Management reporting

---

## RTO and RPO

### Recovery Time Objective (RTO)

> How quickly must the service be restored?

### Recovery Point Objective (RPO)

> How much data loss is acceptable?

Illustrative model:

| Service | Criticality | RTO | RPO |
|---|---|---:|---:|
| Identity platform | Critical | 4 hours | 1 hour |
| Customer-facing platform | Critical | 4 hours | 1 hour |
| Internal collaboration | High | 8 hours | 4 hours |
| Low-impact internal tool | Moderate | 24 hours | 24 hours |

These are portfolio examples, not universal requirements.

---

## Recommended Recovery Test Types

### Backup Integrity Test
Confirms that backup data exists and is readable.

### File or Object Restore Test
Restores selected files or objects to validate basic recoverability.

### Application Recovery Test
Restores an application and validates functionality.

### Infrastructure Recovery Test
Rebuilds or restores supporting infrastructure.

### Cyber Recovery Exercise
Tests recovery following ransomware, credential compromise, or destructive activity.

### Full-Service Recovery Exercise
Tests coordinated recovery of a complete business service and its dependencies.

---

## Example Cyber Recovery Scenario — Ransomware

```text
Endpoint and file services affected
        ↓
Incident declared
        ↓
Compromised identities disabled
        ↓
Affected assets isolated
        ↓
Known-good recovery point selected
        ↓
Backups validated
        ↓
Systems restored
        ↓
Security controls validated
        ↓
Business service tested
        ↓
Production access restored
```

Exercise questions should include:

- Are backups isolated from compromised credentials?
- How is the last known-good recovery point selected?
- Can privileged access be restored securely?
- Are restored systems patched before reconnection?
- Is malware persistence checked?
- Are business owners involved in validation?
- Is restoration evidence retained?

---

## Dependency Mapping

Recovery planning should identify dependencies such as:

- identity services;
- DNS;
- network connectivity;
- cloud IAM;
- storage;
- databases;
- certificates;
- third-party SaaS;
- API integrations;
- backup platforms;
- security monitoring.

A system may be technically restored but remain unusable if a critical dependency is unavailable.

---

## Recovery Success Criteria

Each recovery test should define measurable success criteria, such as:

- backup successfully restored;
- data integrity validated;
- application functionality confirmed;
- RTO achieved;
- RPO achieved;
- required dependencies available;
- security controls restored;
- logging operational;
- business owner approves restoration;
- corrective actions documented.

---

## Corrective-Action Workflow

```text
Recovery test performed
        ↓
Failure or weakness identified
        ↓
Corrective action created
        ↓
Owner assigned
        ↓
Due date established
        ↓
Remediation completed
        ↓
Retest performed
        ↓
Evidence validated
        ↓
Action closed
```

---

## Recommended Metrics

| Metric | Purpose |
|---|---|
| Critical services with defined RTO/RPO | Measures planning coverage |
| Recovery tests completed vs planned | Measures program execution |
| Successful restoration rate | Measures technical recoverability |
| RTO achievement rate | Measures recovery performance |
| RPO achievement rate | Measures data-recovery performance |
| Recovery-test failures | Measures resilience gaps |
| Corrective actions overdue | Measures governance debt |
| Critical dependencies mapped | Measures recovery readiness |
| Time since last successful restore test | Measures assurance freshness |

---

## Recommended Implementation Actions

### 0–30 Days
- Identify critical business services.
- Define provisional RTOs and RPOs.
- Identify critical backup repositories.
- Perform targeted restore tests for high-value data.
- Assign recovery owners.

### 31–90 Days
- Document recovery procedures.
- Map dependencies for critical services.
- Establish a recurring recovery-test schedule.
- Conduct application-level restoration tests.
- Establish a recovery corrective-action tracker.
- Integrate cyber scenarios into recovery planning.

### 3–12 Months
- Conduct full-service recovery exercises.
- Measure RTO/RPO performance.
- Test recovery after ransomware-like scenarios.
- Include third-party dependencies.
- Integrate recovery testing with incident-response exercises.
- Automate backup and recovery-health reporting where feasible.
- Report resilience metrics to security governance.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- critical services are identified;
- RTOs and RPOs are documented;
- recovery procedures exist;
- critical dependencies are mapped;
- restoration tests occur on a defined schedule;
- cyber recovery scenarios are tested;
- recovery objectives are measured;
- failed tests generate corrective actions;
- corrective actions are retested;
- recovery readiness is reported to management.

---

## Suggested Evidence After Remediation

Examples include:

- recovery plan;
- business-service criticality register;
- RTO/RPO matrix;
- backup configuration evidence;
- restoration test records;
- recovery exercise reports;
- dependency maps;
- corrective-action tracker;
- ransomware recovery exercise;
- recovery metrics dashboard;
- management review records.

---

## Priority

**High**

### Priority Rationale

Recovery is the final control layer when preventive and detective measures are insufficient.

If restoration procedures fail during ransomware, destructive attack, or major outage, business impact can increase rapidly.

Because recoverability must be demonstrated rather than assumed, this finding is high priority.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-012 |
| Finding | GRC-012 |
| Risk Domain | Recovery / Cyber Resilience |
| NIST CSF 2.0 | RC |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | IT Operations / Business Continuity |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Relationship to GRC-009, GRC-010, and GRC-011

```text
GRC-009
Formalize incident response
        ↓
GRC-010
Exercise response
        ↓
GRC-011
Capture lessons learned
        ↓
GRC-012
Validate recovery capability
```

Together, these findings cover the transition from detection and response into business resilience.

---

## Consultant Perspective

The weak question is:

> “Do you have backups?”

The stronger assessment questions are:

> “Can you restore them?”

> “Can you restore them fast enough?”

> “Can you restore the right systems in the right order?”

> “Can you do that after a cyber incident without restoring the attacker with them?”

That is the difference between backup administration and cyber resilience.

---

## Final Assessment Statement

Northstar HealthTech has basic backup and recovery capability, but recovery procedures are not tested frequently or comprehensively enough to provide strong assurance that critical services can be restored within business requirements after a major cybersecurity incident.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Formalizing recovery objectives, dependency mapping, recurring restoration tests, cyber recovery exercises, corrective-action tracking, and recovery metrics should be treated as a high-priority resilience improvement.

# GRC-007 — Security Logging and Monitoring Coverage Is Incomplete

## Finding Summary

Northstar HealthTech collects security telemetry from several important sources, including Windows Security logs, Microsoft Defender, AWS CloudTrail, authentication activity, and selected cloud events.

However, the fictional organization does not yet maintain complete, risk-based logging and monitoring coverage across all high-value systems and activities.

Technical evidence from the modeled AWS environment demonstrates a specific visibility gap: standard CloudTrail Event History did not provide S3 object-level `GetObject` activity until S3 data-event logging was explicitly enabled.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **DETECT (DE)** Function and the **Continuous Monitoring (DE.CM)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**DE.CM — Continuous Monitoring**

This finding focuses on the organization's ability to monitor assets and activities so that potentially adverse events can be detected.

The precise subcategory mapping will be maintained in the project-wide control matrix.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Windows Security logging is available for selected systems.
- Microsoft Defender provides endpoint telemetry.
- Authentication events are monitored.
- AWS CloudTrail is enabled.
- Selected cloud-security events are available for investigation.
- Detection-engineering capability exists for several Windows attack behaviors.
- Monitoring coverage is not complete across all high-value systems and activities.
- No formal enterprise log-source inventory has been identified.
- Logging requirements are not consistently tied to asset criticality.
- No documented process ensures that all critical cloud data events are captured.
- Some high-value event classes require explicit configuration before they become visible.
- No formal monitoring-coverage metric has been established.
- No recurring control exists to identify critical systems that are not forwarding security logs.
- Logging gaps may remain undetected until a security assessment or incident exposes them.

---

## Technical Portfolio Evidence

This GRC finding directly links to two existing technical projects.

### AWS-06 — CloudTrail S3 Data-Event Visibility Gap

Observed condition:

```text
S3 object read occurs
        ↓
CloudTrail Event History checked
        ↓
GetObject not visible
```

Reason:

```text
CloudTrail Event History
        ↓
Management events only
        ↓
S3 object-level GetObject is a data event
```

Remediation:

```text
Enable S3 read data events
        ↓
Repeat object access
        ↓
Inspect delivered CloudTrail event
        ↓
Confirm successful GetObject telemetry
```

Validated fields included:

```text
eventSource: s3.amazonaws.com
eventName: GetObject
eventCategory: Data
managementEvent: false
httpStatusCode: 200
```

This demonstrates that **logging being enabled does not automatically mean that all security-relevant activity is visible**.

### Detection-as-Code Pipeline

The Detection-as-Code project demonstrates that useful detections depend on appropriate telemetry.

Examples include:

- Windows Security Event ID 4625 for failed authentication;
- Event ID 4624 for successful authentication;
- Event ID 4732 for privileged group membership changes;
- Sysmon ProcessAccess telemetry for LSASS access;
- process creation telemetry for PowerShell, scheduled tasks, LOLBins, and unusual child processes.

The detection logic is only effective when the necessary event sources are enabled, collected, retained, and available for analysis.

---

## Observed Control State

Northstar HealthTech has meaningful security monitoring capability.

This is not a case of absent logging.

The gap is that monitoring coverage is **fragmented and not yet governed as a complete, risk-based control program**.

The organization cannot consistently demonstrate that:

- all critical assets have required logging enabled;
- security-relevant cloud data events are collected;
- log sources are mapped to detection requirements;
- log forwarding failures are identified;
- retention periods are defined by business and security need;
- time synchronization is consistently validated;
- high-value events are monitored centrally;
- log-source onboarding follows a standard process;
- monitoring coverage is periodically reassessed.

---

## Scoring Rationale

Northstar HealthTech has multiple active telemetry sources and functioning detection capability.

This supports a score above **1 — Initial**.

However, evidence of incomplete cloud visibility, fragmented log-source coverage, and the absence of formal coverage governance prevents the capability from being considered fully defined or managed.

The capability is therefore assessed as **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Security logging and monitoring are implemented across selected systems, but coverage, standardization, governance, and measurement remain incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which security logging and monitoring are:

- risk-based;
- documented;
- centrally governed;
- mapped to critical assets and threat scenarios;
- monitored for collection failures;
- measured through coverage metrics;
- periodically reviewed;
- updated when systems or threats change.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is significant because incomplete telemetry can prevent detection of security events even when technical controls and analyst capability exist.

---

## Business Risk

Incomplete security logging and monitoring can create blind spots in which malicious or unauthorized activity occurs without timely detection.

Potential consequences include:

- delayed detection of compromised accounts;
- inability to reconstruct attacker activity;
- missed cloud data access;
- reduced visibility into privilege changes;
- incomplete incident scoping;
- longer attacker dwell time;
- inability to validate security-control effectiveness;
- weak evidence during incident response;
- difficulty demonstrating monitoring coverage to stakeholders.

---

## Risk Statement

> If Northstar HealthTech does not maintain complete and risk-based security logging and monitoring coverage, malicious or unauthorized activity may occur without timely detection or sufficient forensic evidence, increasing the likelihood and impact of prolonged compromise, data exposure, or operational disruption.

---

## Existing Controls

Existing strengths include:

- Windows Security logs;
- Microsoft Defender telemetry;
- AWS CloudTrail;
- selected AWS data-event logging;
- authentication monitoring;
- detection-engineering logic;
- analyst investigation capability;
- ability to validate telemetry through controlled testing.

These are important strengths and provide a solid foundation for a more mature monitoring program.

---

## Recommended Remediation

Northstar HealthTech should establish a formal security logging and monitoring standard.

The standard should define at minimum:

1. In-scope asset classes
2. Required security event sources
3. Critical log sources
4. Cloud management-event requirements
5. Cloud data-event requirements
6. Identity and authentication logging
7. Endpoint telemetry requirements
8. Administrative activity monitoring
9. Log forwarding requirements
10. Retention requirements
11. Time synchronization
12. Centralized monitoring expectations
13. Logging health checks
14. Alerting requirements
15. Periodic coverage review

---

## Recommended Log-Source Inventory

Northstar HealthTech should maintain a centralized log-source register.

Suggested fields include:

- asset or platform;
- owner;
- criticality;
- log source;
- event type;
- collection method;
- destination;
- retention period;
- monitoring use case;
- status;
- last validation date;
- known gap or exception.

---

## Risk-Based Logging Model

### Tier 1 — Critical Monitoring

Examples:

- privileged authentication;
- identity administration;
- critical cloud resources;
- sensitive data access;
- security-tool changes;
- production administrative activity.

Expected controls:

```text
Continuous collection
+
central monitoring
+
alerting
+
health validation
+
defined retention
```

### Tier 2 — High-Value Monitoring

Examples:

- business applications;
- important infrastructure;
- non-critical cloud services.

Expected controls:

```text
Central collection
+
defined detection use cases
+
periodic validation
```

### Tier 3 — Standard Monitoring

Baseline logging should still exist, but depth and retention may be lower based on risk.

---

## Logging Coverage Questions

For each critical asset, reviewers should confirm:

- What security events can the asset generate?
- Which events are currently enabled?
- Are logs forwarded centrally?
- Are high-risk event classes excluded?
- Is the collection pipeline healthy?
- Is retention sufficient for investigation?
- Is time synchronized?
- Are detections mapped to the telemetry?
- Can analysts access the data quickly?
- Has collection been tested recently?

---

## Detection-to-Telemetry Mapping

| Detection Use Case | Required Telemetry |
|---|---|
| Brute-force authentication | Windows 4625 |
| Successful login after failures | Windows 4625 + 4624 |
| Local admin membership change | Windows 4732 |
| LSASS process access | Sysmon Event ID 10 |
| Suspicious PowerShell | Process creation / PowerShell telemetry |
| S3 object access | CloudTrail S3 data events |
| Privilege modification | IAM / identity audit events |

This avoids building detection logic for data that is not actually available.

---

## Logging Health Monitoring

A mature program should detect when telemetry disappears.

Examples:

- endpoint stops forwarding;
- CloudTrail trail is disabled;
- log subscription fails;
- expected authentication volume suddenly drops;
- critical log source becomes stale;
- time synchronization drifts;
- storage or ingestion failure occurs.

A missing log source should itself become a security-monitoring event.

---

## Recommended Metrics

| Metric | Purpose |
|---|---|
| Critical assets with required logging enabled | Measures coverage |
| Critical log sources successfully forwarding | Measures collection health |
| Assets with validated telemetry in last 90 days | Measures assurance |
| Open logging exceptions | Measures governance debt |
| Detection use cases with required telemetry available | Measures detection readiness |
| Mean time to identify logging failure | Measures monitoring resilience |
| Critical cloud services with required data events enabled | Measures cloud visibility |
| Log sources without assigned owner | Measures accountability |

---

## Recommended Implementation Actions

### 0–30 Days

- Create a log-source inventory.
- Identify Tier 1 critical assets and event classes.
- Confirm CloudTrail coverage for critical AWS activity.
- Validate endpoint and authentication telemetry.
- Identify high-value systems without central logging.
- Assign owners to critical log sources.

### 31–90 Days

- Publish a formal logging and monitoring standard.
- Map major detections to required telemetry.
- Define retention requirements.
- Implement monitoring for log-forwarding failures.
- Establish logging exceptions and approval process.
- Validate critical telemetry through controlled testing.

### 3–12 Months

- Automate log-source coverage reporting.
- Introduce continuous monitoring-health metrics.
- Periodically test telemetry completeness.
- Expand threat-based monitoring coverage.
- Integrate asset criticality with logging requirements.
- Use incident lessons learned to improve telemetry coverage.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- an authoritative log-source inventory exists;
- required telemetry is defined for critical assets;
- all Tier 1 assets meet required logging standards;
- cloud management and required data events are collected;
- log forwarding is centrally monitored;
- telemetry failures generate alerts or investigations;
- retention requirements are documented;
- detections are mapped to available telemetry;
- monitoring coverage is measured;
- exceptions are documented and governed;
- recurring validation is performed.

---

## Suggested Evidence After Remediation

Examples include:

- security logging standard;
- log-source inventory;
- SIEM or central monitoring architecture;
- CloudTrail configuration evidence;
- endpoint telemetry coverage report;
- detection-to-telemetry matrix;
- log-health dashboard;
- forwarding failure alerts;
- retention configuration;
- logging exception register;
- periodic telemetry validation results.

---

## Priority

**High**

### Priority Rationale

The organization already has technical detection capability, but incomplete telemetry can neutralize that capability.

The AWS-06 evidence demonstrates a concrete example in which meaningful security activity was not visible until a specific log type was enabled.

Because monitoring gaps can delay or prevent detection across multiple attack scenarios, this finding is high priority.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-007 |
| Finding | GRC-007 |
| Risk Domain | Security Monitoring |
| NIST CSF 2.0 | DE.CM |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Security Operations / IT Operations |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Technical-to-Governance Crosswalk

```text
AWS-06
Missing S3 object-level visibility
        ↓
Technical observation
Required telemetry was not enabled
        ↓
Control weakness
Monitoring coverage incomplete
        ↓
Governance gap
No complete risk-based logging standard
        ↓
Business risk
Important activity may go undetected
        ↓
GRC recommendation
Formal logging inventory + coverage governance
```

---

## Relationship to Detection-as-Code

This finding creates an important portfolio narrative:

```text
Detection-as-Code
"I can build and test detections."
        +
GRC-007
"I understand that detections depend on governed telemetry coverage."
        ↓
Security monitoring maturity
```

That connection shows both technical and governance understanding.

---

## Consultant Perspective

A common assessment mistake is to ask:

> "Do you have logging?"

The better question is:

> "Do you have the right telemetry, from the right systems, with sufficient retention, health monitoring, ownership, and detection coverage?"

The maturity progression is:

```text
Some logs exist
        ↓
Critical log sources identified
        ↓
Collection standardized
        ↓
Detections mapped to telemetry
        ↓
Collection health monitored
        ↓
Coverage measured
        ↓
Telemetry continuously improved
```

---

## Final Assessment Statement

Northstar HealthTech has meaningful security telemetry and detection capability, but logging and monitoring coverage remains incomplete and insufficiently governed across all critical systems and activities.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Establishing a formal logging standard, authoritative log-source inventory, risk-based telemetry requirements, detection-to-telemetry mapping, collection-health monitoring, and recurring coverage validation should be treated as a high-priority security improvement.

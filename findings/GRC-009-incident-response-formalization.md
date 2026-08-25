# GRC-009 — Incident Response Procedures Are Incompletely Formalized

## Finding Summary

Northstar HealthTech has basic incident-handling capability and can perform technical investigation activities using endpoint, authentication, Windows, and AWS telemetry.

However, the fictional organization does not maintain a sufficiently formalized, consistently governed incident response program covering preparation, classification, escalation, containment, communications, evidence handling, recovery coordination, and post-incident improvement.

This creates a risk that response quality will depend too heavily on individual experience and ad hoc decision-making during high-pressure events.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **RESPOND (RS)** Function, with relevance to incident management, analysis, communications, mitigation, and improvement.

---

## NIST CSF 2.0 Mapping

### Primary Function

**RESPOND (RS)**

Relevant categories include:

- incident management;
- incident analysis;
- incident response reporting and communication;
- incident mitigation.

This finding focuses on the absence of a sufficiently formalized and repeatable incident response operating model.

The precise subcategory crosswalk will be maintained in the project-wide control matrix.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech has informal incident-handling procedures.
- Security telemetry exists across Windows, Microsoft Defender, authentication systems, and AWS.
- Analysts can investigate selected suspicious activity.
- Technical investigation capability is demonstrated through SOC-style workflows.
- No formally approved enterprise incident response plan has been identified.
- Incident severity criteria are not consistently documented.
- Escalation thresholds are not fully defined.
- Decision authority for containment actions is not consistently formalized.
- Communication procedures are incomplete.
- Responsibilities during major incidents are partly implied rather than fully documented.
- Evidence-handling requirements are not standardized.
- Incident documentation is inconsistent.
- No formal post-incident review requirement has been established for all material incidents.
- Incident response exercises are limited.

---

## Observed Control State

Northstar HealthTech can respond to individual cybersecurity events, but the process is not yet sufficiently repeatable or governed.

The organization cannot consistently demonstrate that:

- incidents are classified using a standard severity model;
- response ownership is immediately clear;
- escalation follows defined thresholds;
- containment actions have documented authority;
- required stakeholders are notified consistently;
- business, legal, communications, and technical teams know their roles;
- evidence is retained in a consistent manner;
- response actions are recorded chronologically;
- recovery handoff is coordinated;
- lessons learned are formally captured and tracked.

The current state is therefore **operationally capable but incompletely formalized**.

---

## Scoring Rationale

Evidence demonstrates that incident-handling activity exists and that technical investigation capability is meaningful.

This supports a score above **1 — Initial**.

However, the absence of:

- a formally approved incident response plan;
- standardized classification;
- documented escalation;
- consistent authority;
- communications procedures;
- evidence-handling standards;
- formal post-incident improvement;

prevents the capability from being assessed as fully **Defined (3)**.

The capability is therefore assessed at **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Incident response activities exist and can be executed, but process consistency, documentation, governance, communications, and assurance remain incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which incident response is:

- formally documented;
- approved by management;
- role-based;
- severity-driven;
- supported by defined escalation;
- tested through exercises;
- measured through response metrics;
- integrated with business continuity and recovery;
- continuously improved through lessons learned.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is material because inconsistent response processes can increase both incident duration and business impact.

---

## Business Risk

Incomplete incident response formalization can result in:

- delayed containment;
- inconsistent escalation;
- conflicting response decisions;
- missed stakeholder notifications;
- weak evidence preservation;
- incomplete incident records;
- uncoordinated recovery;
- delayed executive awareness;
- repeated control failures;
- unnecessary operational disruption.

---

## Risk Statement

> If Northstar HealthTech does not formalize and govern its incident response procedures, cybersecurity incidents may be handled inconsistently or too slowly, increasing the likelihood of prolonged compromise, incomplete containment, poor coordination, loss of evidence, and greater operational or data impact.

---

## Existing Controls

Existing strengths include:

- Windows Security logging;
- Microsoft Defender telemetry;
- AWS CloudTrail;
- authentication monitoring;
- detection-engineering capability;
- SOC-style investigation procedures;
- technical analyst capability;
- ability to investigate cloud and endpoint events.

These controls provide a strong technical foundation for a more mature response program.

---

## Recommended Remediation

Northstar HealthTech should establish a formal incident response program.

The program should define at minimum:

1. Incident response policy
2. Incident response plan
3. Severity classification
4. Incident ownership
5. Escalation thresholds
6. Decision authority
7. Communication requirements
8. Containment procedures
9. Evidence handling
10. Documentation requirements
11. Recovery coordination
12. Third-party coordination
13. Post-incident review
14. Metrics and reporting
15. Testing and exercise requirements

---

## Recommended Incident Severity Model

A practical four-level model could be:

| Severity | Description | Example |
|---|---|---|
| SEV-1 | Critical business or security impact | confirmed major compromise, sensitive data exposure, widespread outage |
| SEV-2 | Significant incident requiring urgent coordination | privileged account compromise, material malware event |
| SEV-3 | Moderate incident with contained impact | isolated endpoint compromise |
| SEV-4 | Low-impact security event | minor policy violation or benign security event |

Severity criteria should consider:

- business impact;
- data sensitivity;
- affected assets;
- privilege involved;
- attacker persistence;
- external exposure;
- operational disruption;
- legal or contractual significance.

---

## Recommended Escalation Model

### SEV-1

```text
Security Lead
+
IT Leadership
+
Executive Sponsor
+
Business Owner
+
Legal / Communications as required
```

### SEV-2

```text
Security Lead
+
System Owner
+
IT Management
```

### SEV-3 / SEV-4

Handled through standard security operations with defined escalation triggers.

---

## Incident Lifecycle

A formal response process should follow a consistent lifecycle:

```text
Preparation
        ↓
Detection
        ↓
Triage
        ↓
Classification
        ↓
Escalation
        ↓
Containment
        ↓
Eradication
        ↓
Recovery
        ↓
Post-Incident Review
        ↓
Improvement Tracking
```

---

## Minimum Incident Record

Each incident should document:

- incident ID;
- date and time detected;
- reporter or detection source;
- affected assets;
- severity;
- incident owner;
- timeline of events;
- indicators of compromise;
- containment actions;
- eradication actions;
- recovery actions;
- communications performed;
- evidence retained;
- business impact;
- root cause where known;
- lessons learned;
- follow-up actions;
- closure approval.

---

## Containment Authority

Containment authority should be defined before an incident occurs.

Examples of potentially disruptive actions include:

- isolating an endpoint;
- disabling a user account;
- revoking cloud credentials;
- blocking network traffic;
- disabling a service;
- taking a workload offline.

For each high-impact action, the organization should define:

```text
Who can authorize?
Who can execute?
Who must be informed?
When is emergency authority permitted?
```

---

## Communications Requirements

Incident response should define communication expectations for:

- security operations;
- IT operations;
- system owners;
- business leadership;
- executive leadership;
- legal;
- privacy;
- communications/public relations;
- third parties;
- customers or regulators where required.

In a real organization, legal and regulatory notification decisions should be made by appropriately qualified personnel.

---

## Evidence Handling

Incident evidence should be collected and retained consistently.

Examples include:

- relevant logs;
- endpoint artifacts;
- cloud audit records;
- screenshots;
- exported alerts;
- timestamps;
- investigation notes;
- hash values where appropriate.

Evidence should be protected from unnecessary modification and retained according to defined requirements.

---

## Recommended Metrics

Northstar HealthTech should track metrics such as:

| Metric | Purpose |
|---|---|
| Mean time to acknowledge | Measures response initiation |
| Mean time to contain | Measures containment efficiency |
| Mean time to recover | Measures operational restoration |
| Incidents by severity | Measures incident profile |
| Incidents with complete documentation | Measures process quality |
| Incidents with post-incident review | Measures improvement discipline |
| Repeated incident root causes | Measures unresolved systemic issues |
| Overdue corrective actions | Measures governance debt |
| Exercises completed | Measures preparedness |

---

## Recommended Implementation Actions

### 0–30 Days

- Assign incident response ownership.
- Document interim severity definitions.
- Define emergency escalation contacts.
- Establish minimum incident-record requirements.
- Define emergency containment authority.

### 31–90 Days

- Approve a formal incident response plan.
- Create incident classification and escalation procedures.
- Define communication responsibilities.
- Establish evidence-handling requirements.
- Create core incident playbooks.
- Define post-incident review requirements.

### 3–12 Months

- Conduct tabletop exercises.
- Measure response performance.
- Integrate incident response with recovery and continuity.
- Track corrective actions to closure.
- Review playbooks after incidents and exercises.
- Automate portions of evidence collection and escalation where appropriate.

---

## Recommended Core Playbooks

Northstar HealthTech should maintain playbooks for common scenarios such as:

- phishing;
- compromised account;
- malware;
- ransomware;
- privileged account misuse;
- cloud credential compromise;
- suspicious PowerShell activity;
- unauthorized cloud data access;
- lost or stolen endpoint;
- third-party security incident.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- an approved incident response plan exists;
- incident severity criteria are documented;
- escalation paths are defined;
- response roles are assigned;
- containment authority is documented;
- communication procedures exist;
- evidence-handling requirements are defined;
- incidents are consistently recorded;
- post-incident review occurs for material incidents;
- corrective actions are tracked;
- exercises are performed;
- response metrics are reported.

---

## Suggested Evidence After Remediation

Examples include:

- incident response policy;
- incident response plan;
- severity matrix;
- escalation matrix;
- contact list;
- incident playbooks;
- incident records;
- evidence-handling procedure;
- tabletop exercise report;
- post-incident review report;
- corrective-action tracker;
- response metrics dashboard.

---

## Priority

**High**

### Priority Rationale

The organization already has meaningful detection and investigation capability, but weak process formalization can reduce the effectiveness of those technical capabilities during real incidents.

Because inconsistent containment, escalation, or communication can materially increase incident impact, this finding is high priority.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-009 |
| Finding | GRC-009 |
| Risk Domain | Incident Response |
| NIST CSF 2.0 | RS |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Security Leadership / IT Leadership |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Technical-to-Governance Crosswalk

This finding links directly to the SOC portfolio.

```text
SOC investigation capability
        ↓
Technical event analysis
        ↓
Incident classification
        ↓
Escalation decision
        ↓
Containment
        ↓
Business communication
        ↓
Recovery
        ↓
Lessons learned
```

Technical investigation answers:

> What happened?

Incident response governance must additionally answer:

> Who owns it, how serious is it, what authority exists, who must be informed, and what happens next?

---

## Relationship to GRC-007

GRC-007 addresses whether the organization has sufficient telemetry to detect security-relevant activity.

GRC-009 addresses what happens after that activity is detected.

```text
GRC-007
Can we see it?
        ↓
GRC-009
Can we respond consistently and effectively?
```

---

## Consultant Perspective

A capable analyst does not automatically create a mature incident response program.

A mature program combines:

```text
People
+
Process
+
Technology
+
Authority
+
Communication
+
Evidence
+
Testing
+
Continuous improvement
```

The consulting objective is to make response quality repeatable even when the individuals involved change.

---

## Final Assessment Statement

Northstar HealthTech has meaningful technical investigation and incident-handling capability, but its incident response procedures are not sufficiently formalized, consistently governed, or routinely tested.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Formalizing incident classification, escalation, authority, communications, evidence handling, playbooks, metrics, and post-incident improvement should be treated as a high-priority resilience improvement.

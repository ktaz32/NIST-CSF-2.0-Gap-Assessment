# GRC-010 — Incident Response Exercises and Testing Are Immature

## Finding Summary

Northstar HealthTech has basic incident-handling capability and is developing formal incident response procedures, but the fictional organization does not yet test those procedures through a mature, recurring exercise program.

Tabletop exercises, technical simulations, and coordinated response tests are limited. As a result, the organization cannot consistently demonstrate that incident roles, escalation paths, communications, containment decisions, and recovery coordination will function as intended during a real high-impact event.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **RESPOND (RS)** and **RECOVER (RC)** Functions.

---

## NIST CSF 2.0 Mapping

### Primary Functions

**RESPOND (RS)**  
**RECOVER (RC)**

This finding focuses on validating incident-response and recovery readiness through recurring exercises and testing.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech has informal incident-handling procedures.
- Technical analysts can investigate endpoint, authentication, and cloud events.
- Core security telemetry exists.
- Incident-response playbooks are not yet fully mature.
- Tabletop exercise history is limited.
- No recurring annual exercise schedule has been identified.
- No formal requirement exists to test high-impact incident scenarios.
- Cross-functional participation is inconsistent.
- Executive involvement in cyber exercises is limited.
- Recovery dependencies are not routinely tested as part of cyber scenarios.
- Exercise objectives and success criteria are not consistently documented.
- Lessons from exercises are not systematically tracked to remediation.
- No formal metric exists for exercise completion or corrective-action closure.

---

## Observed Control State

Northstar HealthTech has the capability to discuss and respond to incidents operationally, but it has not yet established a repeatable assurance process to test whether documented response procedures actually work.

The organization cannot consistently demonstrate that:

- response teams understand their roles under pressure;
- escalation contacts are current;
- containment authority is understood;
- business and technical teams coordinate effectively;
- executives receive appropriate decision information;
- communications procedures function as intended;
- third-party dependencies are incorporated;
- recovery handoffs are tested;
- playbooks remain usable during realistic scenarios;
- corrective actions from exercises are tracked to closure.

The current state is therefore **initial, with limited formal testing discipline**.

---

## Scoring Rationale

Evidence shows that incident-response capability exists and that personnel have some practical investigation experience.

This supports a score above **0 — Not Implemented**.

However, exercise activity remains infrequent, inconsistently documented, weakly governed, insufficiently cross-functional, and not tied to recurring metrics or corrective-action tracking.

The capability is therefore assessed at **1 — Initial**.

---

## Current Maturity

**1 — Initial**

> Incident response exercises occur rarely or informally and are not yet governed through a consistent, repeatable testing program.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which incident-response exercises are:

- formally scheduled;
- risk-based;
- scenario-driven;
- cross-functional;
- measurable;
- documented;
- reviewed by management;
- linked to corrective actions;
- repeated to validate improvement.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 1
Gap:              3
```

The maturity gap is significant because untested procedures may fail during a real incident even when documentation exists.

---

## Business Risk

Immature incident-response testing can result in hidden weaknesses remaining undiscovered until a real event occurs.

Potential consequences include:

- delayed containment;
- confusion over authority;
- incorrect escalation;
- poor executive coordination;
- communications failures;
- incomplete evidence collection;
- untested third-party dependencies;
- ineffective recovery coordination;
- repeated process weaknesses;
- greater operational impact during a real incident.

---

## Risk Statement

> If Northstar HealthTech does not routinely exercise and test its incident response and recovery procedures, weaknesses in roles, escalation, communications, containment, and recovery coordination may remain undiscovered until a real cybersecurity incident occurs, increasing the likelihood of delayed or ineffective response.

---

## Existing Controls

Existing strengths include:

- technical incident investigation capability;
- endpoint and cloud telemetry;
- developing incident-response procedures;
- detection-engineering capability;
- SOC-style investigation experience;
- technical remediation capability.

These controls provide useful readiness but do not replace structured exercises.

---

## Recommended Remediation

Northstar HealthTech should establish a formal incident-response exercise program covering:

1. Annual exercise schedule
2. Scenario selection criteria
3. Exercise objectives
4. Participant roles
5. Executive participation requirements
6. Technical and business coordination
7. Success criteria
8. Exercise facilitation
9. Observation and evidence collection
10. After-action review
11. Corrective-action tracking
12. Retesting requirements
13. Program metrics
14. Management reporting

---

## Recommended Exercise Types

### Tabletop Exercise
Discussion-based exercise focused on decision-making, escalation, communications, and authority.

### Technical Simulation
Hands-on exercise using realistic logs, alerts, or test systems for investigation and containment.

### Recovery Exercise
Tests restoration of systems, data, services, dependencies, and communications.

### Combined Exercise
Integrates technical investigation, business decisions, communications, and recovery.

---

## Recommended Annual Exercise Program

```text
Q1 — Phishing / Account Compromise Tabletop
Q2 — Cloud Credential Compromise Technical Exercise
Q3 — Ransomware / Business Disruption Tabletop
Q4 — Recovery and Executive Coordination Exercise
```

The schedule should evolve based on actual risk and lessons learned.

---

## Recommended Exercise Scenarios

High-value scenarios include:

- compromised privileged account;
- phishing leading to account takeover;
- ransomware;
- malicious PowerShell activity;
- unauthorized AWS data access;
- cloud credential compromise;
- third-party security incident;
- endpoint malware;
- loss of logging visibility;
- critical SaaS outage.

---

## Example Scenario — Cloud Credential Compromise

```text
Suspicious AWS login detected
        ↓
Unusual IAM activity
        ↓
S3 access observed
        ↓
Privilege change attempted
        ↓
Business owner notified
        ↓
Credentials revoked
        ↓
CloudTrail reviewed
        ↓
Scope determined
        ↓
Recovery and reporting decisions
```

Exercise questions should include:

- Who declares an incident?
- What severity is assigned?
- Who can revoke credentials?
- Which logs are required?
- Who contacts the business owner?
- When is executive escalation required?
- How is potential data exposure assessed?
- What evidence must be preserved?
- What conditions allow closure?

---

## Exercise Success Criteria

Examples:

- incident classified correctly;
- incident owner identified within 15 minutes;
- escalation contacts reached;
- containment authority correctly applied;
- required telemetry identified;
- evidence preserved;
- executive update produced;
- recovery owner identified;
- corrective actions documented.

The objective is not to “win” the exercise. The objective is to discover weaknesses safely before a real incident does.

---

## After-Action Review

Every material exercise should produce an after-action report containing:

- scenario;
- objectives;
- participants;
- timeline;
- what worked;
- what failed;
- decision gaps;
- communication gaps;
- technical gaps;
- process gaps;
- corrective actions;
- assigned owners;
- due dates;
- retest requirements.

---

## Corrective-Action Tracking

| Action | Owner | Priority | Due Date | Status | Retest Required |
|---|---|---|---|---|---|
| Update escalation contacts | Security Lead | High | 30 days | Open | Yes |
| Clarify endpoint isolation authority | IT Director | High | 30 days | Open | Yes |
| Add S3 data-event logging requirement | Cloud Owner | High | 60 days | Open | Yes |
| Update ransomware communications template | Business Lead | Medium | 60 days | Open | Yes |

---

## Recommended Metrics

| Metric | Purpose |
|---|---|
| Exercises completed vs planned | Measures program execution |
| Critical scenarios tested | Measures risk coverage |
| Cross-functional participation rate | Measures organizational readiness |
| Corrective actions closed on time | Measures improvement discipline |
| Repeat findings | Identifies persistent weaknesses |
| Average time to complete exercise actions | Measures remediation efficiency |
| Playbooks updated after exercises | Measures learning |
| Executive participation rate | Measures governance engagement |

---

## Recommended Implementation Actions

### 0–30 Days
- Assign an exercise-program owner.
- Define the first tabletop scenario.
- Identify required participants.
- Establish exercise objectives.
- Create an initial after-action template.

### 31–90 Days
- Conduct the first formal tabletop exercise.
- Document results.
- Assign corrective actions.
- Update affected playbooks.
- Schedule follow-up testing.
- Define an annual exercise calendar.

### 3–12 Months
- Conduct multiple scenario types.
- Include executives and business owners.
- Add technical simulations.
- Incorporate third-party and recovery scenarios.
- Track exercise metrics.
- Retest previously identified weaknesses.
- Report exercise maturity to security governance.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- a formal exercise program exists;
- an annual schedule is approved;
- risk-based scenarios are selected;
- cross-functional participants are included;
- exercises have documented objectives;
- after-action reviews are completed;
- corrective actions are assigned and tracked;
- overdue actions are escalated;
- retesting occurs;
- management receives exercise metrics.

---

## Suggested Evidence After Remediation

Examples include:

- annual exercise calendar;
- tabletop exercise plan;
- participant list;
- scenario injects;
- after-action report;
- corrective-action tracker;
- updated playbooks;
- retest results;
- executive briefing;
- exercise metrics dashboard.

---

## Priority

**High**

### Priority Rationale

The organization is developing incident-response capability, but without realistic testing there is limited assurance that people, processes, and communications will function effectively during a real high-impact event.

The maturity gap is also relatively large at **3 points**, making this a material resilience weakness.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-010 |
| Finding | GRC-010 |
| Risk Domain | Incident Response / Resilience |
| NIST CSF 2.0 | RS / RC |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Security Leadership / Business Continuity |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Relationship to GRC-009

GRC-009 addresses whether incident-response procedures are sufficiently formalized.

GRC-010 addresses whether those procedures are actually tested.

```text
GRC-009
Document the process
        ↓
GRC-010
Exercise the process
        ↓
Find weaknesses
        ↓
Correct weaknesses
        ↓
Retest
```

Documentation without testing provides limited assurance.

---

## Consultant Perspective

An incident-response plan is a hypothesis until it is tested.

The real assessment question is not:

> “Do you have a plan?”

It is:

> “Have the people who must execute the plan tested it together under realistic conditions, and were the weaknesses corrected afterward?”

That distinction is central to mature cyber resilience.

---

## Final Assessment Statement

Northstar HealthTech has developing incident-response capability but does not yet operate a mature, recurring exercise and testing program.

The capability is assessed at **Maturity Level 1 — Initial**, with a target of **Level 4 — Managed**.

Establishing a risk-based annual exercise program, documenting after-action findings, assigning corrective actions, and retesting improvements should be treated as a high-priority resilience improvement.

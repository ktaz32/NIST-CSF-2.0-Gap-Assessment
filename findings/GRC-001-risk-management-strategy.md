# GRC-001 — Cybersecurity Risk Management Strategy Not Formally Established

## Finding Summary

Northstar HealthTech performs cybersecurity activities across cloud security, endpoint protection, authentication monitoring, and incident handling, but the fictional organization does not have a formally established and stakeholder-approved cybersecurity risk management strategy.

The current state is therefore operationally active but governance-light: technical security work occurs, yet there is no documented enterprise cybersecurity risk strategy that defines risk objectives, risk ownership, prioritization principles, review cadence, and alignment to business priorities.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **GOVERN (GV)** Function and the **Risk Management Strategy (GV.RM)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**GV.RM — Risk Management Strategy**

Relevant outcome:

**GV.RM-01 — Risk management objectives are established and agreed to by organizational stakeholders.**

Additional GV.RM outcomes may become relevant as the assessment expands, but this finding is intentionally anchored first to the absence of formally agreed cybersecurity risk-management objectives.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech has a small internal IT and cybersecurity team.
- Security controls exist across Microsoft Defender, Windows logging, AWS IAM, CloudTrail, and authentication monitoring.
- Cybersecurity weaknesses are identified and remediated in some technical areas.
- Business priorities include protection of healthcare-related information, service availability, identity protection, secure cloud operations, compliance, and cyber resilience.
- No documented cybersecurity risk-management strategy has been identified.
- No evidence has been provided of formally approved cybersecurity risk objectives.
- No formal risk appetite or risk tolerance statement has been identified.
- No organization-wide cybersecurity risk prioritization methodology has been documented.
- No recurring governance cadence has been defined for reviewing cybersecurity risk objectives with organizational stakeholders.
- Current cybersecurity decisions therefore rely heavily on operational judgment rather than a formally governed enterprise risk strategy.

---

## Observed Control State

Northstar HealthTech demonstrates awareness of cybersecurity risk and performs meaningful technical security activities.

However, these activities are not governed by a sufficiently formalized cybersecurity risk-management strategy.

The organization can identify individual technical weaknesses, but it lacks a documented structure for answering questions such as:

- Which cybersecurity risks matter most to the business?
- What level of cyber risk is acceptable?
- Who is accountable for major cyber-risk decisions?
- How are competing remediation priorities ranked?
- When must risk be escalated to leadership?
- How frequently are cybersecurity objectives reviewed?
- How are cybersecurity objectives connected to business strategy?

The current state is therefore **partially established but primarily informal and reactive**.

---

## Scoring Rationale

Evidence demonstrates that cybersecurity risk is recognized and that technical risk-reduction activities occur.

This prevents a score of **0 — Not Implemented**.

However, the absence of:

- formally approved risk-management objectives;
- documented risk strategy;
- defined risk appetite/tolerance;
- stakeholder agreement;
- recurring governance review;

means the capability is not sufficiently mature to qualify as **Developing (2)** under the project's evidence-first scoring model.

The activity remains largely dependent on informal operational practice rather than a repeatable, documented governance process.

---

## Current Maturity

**1 — Initial**

Definition:

> Cybersecurity risk management exists primarily through ad hoc, informal, reactive, or inconsistently performed activities.

---

## Target Maturity

**4 — Managed**

A suitable target state for Northstar HealthTech is a formally governed cybersecurity risk-management capability in which:

- cybersecurity risk objectives are documented;
- objectives are approved by relevant stakeholders;
- risk appetite and tolerance are defined;
- risk ownership is assigned;
- material risks are tracked through a risk register;
- risk treatment decisions are documented;
- cybersecurity risk metrics are reviewed periodically;
- leadership receives recurring risk reporting;
- the strategy is reviewed when business or technology conditions materially change.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 1
Gap:              3
```

The maturity gap is significant because cybersecurity activity currently lacks an enterprise governance mechanism for consistent prioritization and executive oversight.

---

## Business Risk

Without a formally established cybersecurity risk-management strategy, Northstar HealthTech may make inconsistent security-investment and remediation decisions.

Potential consequences include:

- critical risks receiving insufficient priority;
- resources being allocated to lower-value security activities;
- inconsistent acceptance of cybersecurity risk;
- weak accountability for unresolved risks;
- fragmented decision-making between technical and business stakeholders;
- difficulty demonstrating governance to customers or other stakeholders;
- delayed escalation of risks affecting sensitive information or service availability.

The primary concern is not the absence of technical security activity. The concern is the absence of a consistent mechanism for translating technical findings into business risk decisions.

---

## Risk Statement

> If Northstar HealthTech does not establish and govern organization-wide cybersecurity risk-management objectives, material cybersecurity risks may be inconsistently identified, prioritized, accepted, or remediated, increasing the likelihood that high-impact threats to sensitive information, identities, cloud services, or business operations remain inadequately managed.

---

## Existing Controls

Existing control strengths include:

- basic cybersecurity personnel and responsibilities;
- Microsoft Defender endpoint protection;
- Windows security logging;
- AWS CloudTrail;
- AWS IAM controls;
- technical security assessments;
- detection-engineering capability;
- incident-handling activity.

These controls reduce portions of technical risk but do not replace the need for enterprise cybersecurity risk governance.

---

## Recommended Remediation

Northstar HealthTech should establish a documented cybersecurity risk-management strategy approved by appropriate organizational stakeholders.

The strategy should define at minimum:

1. Cybersecurity risk-management objectives
2. Business and cybersecurity alignment
3. Risk appetite and tolerance
4. Risk ownership and accountability
5. Risk identification process
6. Risk assessment methodology
7. Risk prioritization criteria
8. Risk treatment options
9. Risk acceptance authority
10. Escalation thresholds
11. Risk-reporting requirements
12. Governance review cadence
13. Triggers for out-of-cycle review
14. Linkage to the enterprise risk register

---

## Recommended Implementation Actions

### 0–30 Days

- Assign an executive sponsor for cybersecurity risk management.
- Identify key organizational stakeholders.
- Document initial cybersecurity risk-management objectives.
- Establish an interim cybersecurity risk register.
- Define ownership for each material cybersecurity risk.

### 31–90 Days

- Approve a formal cybersecurity risk-management strategy.
- Define risk appetite and tolerance statements.
- Establish a consistent likelihood and impact methodology.
- Define formal risk-acceptance authority.
- Establish recurring cybersecurity risk-review meetings.
- Define executive reporting metrics.

### 3–12 Months

- Integrate cybersecurity risk with broader enterprise risk management.
- Establish cybersecurity KRIs and trend reporting.
- Review the strategy at least annually and after material organizational changes.
- Use lessons learned, incidents, assessments, and control testing to update risk priorities.
- Introduce automation where useful for risk evidence and reporting.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- a cybersecurity risk-management strategy exists;
- risk-management objectives are documented;
- relevant stakeholders have approved the objectives;
- risk appetite or tolerance is defined;
- cybersecurity risk owners are assigned;
- a formal risk register is maintained;
- a recurring review cadence exists;
- material risk decisions and acceptance are documented;
- executive or governance reporting is performed.

---

## Suggested Evidence After Remediation

Examples of acceptable evidence include:

- approved cybersecurity risk-management strategy;
- governance meeting minutes;
- risk appetite statement;
- current cybersecurity risk register;
- documented risk owners;
- risk review calendar;
- executive cybersecurity dashboard;
- recorded risk-treatment decisions;
- annual strategy review record.

---

## Priority

**High**

### Priority Rationale

The gap affects governance across the entire cybersecurity program rather than one isolated technical control.

Although there is no evidence of an immediate catastrophic exposure caused solely by this governance deficiency, the lack of a formal risk-management strategy can allow significant technical risks to remain inconsistently prioritized or accepted.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-001 |
| Finding | GRC-001 |
| Risk Domain | Cybersecurity Governance |
| NIST CSF 2.0 | GV.RM / GV.RM-01 |
| Likelihood | Likely |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Executive Sponsor / Security Leadership |
| Status | Open |

The numerical risk matrix will be finalized when the project-wide risk-scoring methodology is created.

---

## Consultant Perspective

This finding illustrates the distinction between **having security controls** and **governing cybersecurity risk**.

Northstar HealthTech can operate endpoint protection, monitor logs, remediate IAM weaknesses, and investigate incidents while still lacking a mature risk-management strategy.

The consulting objective is to connect those technical activities to:

```text
Business priorities
        ↓
Cybersecurity risk objectives
        ↓
Risk ownership
        ↓
Prioritization
        ↓
Treatment decisions
        ↓
Executive oversight
```

---

## Final Assessment Statement

Northstar HealthTech has meaningful technical cybersecurity activity but lacks a formally established, stakeholder-approved cybersecurity risk-management strategy. The current capability is assessed at **Maturity Level 1 — Initial**, with a target of **Level 4 — Managed**.

Formalizing cybersecurity risk objectives, ownership, appetite, prioritization, and governance review should be treated as a high-priority foundational improvement because these mechanisms guide the effectiveness of the broader cybersecurity program.

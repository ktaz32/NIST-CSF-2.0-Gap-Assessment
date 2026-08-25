# GRC-002 — Cybersecurity Roles, Responsibilities, and Authorities Are Incompletely Defined

## Finding Summary

Northstar HealthTech has a small internal IT and cybersecurity team and performs a range of security activities across cloud, endpoint, identity, monitoring, and incident response.

However, the fictional organization does not have a sufficiently formalized model that defines cybersecurity roles, responsibilities, decision rights, escalation authority, and accountability across business and technical stakeholders.

Security work is being performed, but responsibility is not consistently documented or governed.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **GOVERN (GV)** Function and the **Roles, Responsibilities, and Authorities (GV.RR)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**GV.RR — Roles, Responsibilities, and Authorities**

Relevant outcomes include the establishment, communication, and coordination of cybersecurity roles, responsibilities, and authorities across the organization.

This finding focuses specifically on the absence of a clearly documented responsibility model for cybersecurity governance and operations.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech has a small internal IT and cybersecurity team.
- Security responsibilities are distributed across IT, cloud administration, endpoint management, and incident handling.
- Technical security activities are occurring across AWS, Microsoft Defender, Windows logging, and authentication monitoring.
- Incident-handling procedures exist but remain partly informal.
- No formal cybersecurity responsibility matrix has been identified.
- No documented RACI model has been identified for major cybersecurity activities.
- Ownership of several security processes is implied rather than explicitly assigned.
- Escalation authority for material cybersecurity risks is not formally documented.
- Responsibility for accepting cybersecurity risk is not consistently defined.
- Third-party security responsibilities are inconsistently governed.
- Security responsibilities between technical teams and business leadership are not fully documented.

---

## Observed Control State

Northstar HealthTech has personnel performing cybersecurity work, so cybersecurity responsibility is not absent.

However, the organization relies heavily on informal role understanding and operational practice.

This creates uncertainty around questions such as:

- Who owns cybersecurity risk management?
- Who approves risk acceptance?
- Who is accountable for privileged-access reviews?
- Who owns vulnerability remediation?
- Who has authority to isolate a compromised endpoint?
- Who communicates with leadership during a major incident?
- Who owns third-party cybersecurity risk?
- Who validates recovery readiness?
- Who is responsible for maintaining security metrics?
- Who approves policy exceptions?

The current state is therefore **partially functioning but insufficiently formalized**.

---

## Scoring Rationale

Evidence demonstrates that IT and cybersecurity activities are actively assigned and performed in practice.

This supports a score above **0 — Not Implemented**.

However:

- responsibilities are not consistently documented;
- formal accountability is incomplete;
- decision rights are not fully established;
- escalation authority is unclear;
- no organization-wide RACI model exists;
- recurring governance review of responsibilities is not evidenced.

Because roles exist operationally but are not yet consistently formalized or governed, the capability is assessed as **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Cybersecurity responsibilities are partially implemented and understood, but documentation, coverage, governance, and consistency remain incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one where cybersecurity responsibilities are:

- formally documented;
- approved by management;
- communicated to relevant personnel;
- mapped to cybersecurity processes;
- tied to decision authority;
- reviewed periodically;
- updated after material organizational changes;
- supported by measurable accountability.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is material because unclear ownership can undermine otherwise effective technical controls.

---

## Business Risk

Incomplete cybersecurity accountability can create:

- delayed response to security incidents;
- inconsistent remediation ownership;
- unresolved vulnerabilities;
- duplicated or missed security work;
- weak risk acceptance governance;
- unclear escalation paths;
- ineffective third-party oversight;
- gaps between technical teams and business leadership.

Security controls may exist technically but fail operationally if no individual or function is clearly accountable for maintaining them.

---

## Risk Statement

> If Northstar HealthTech does not formally define and communicate cybersecurity roles, responsibilities, authorities, and escalation paths, important security activities may be delayed, inconsistently executed, or left unowned, increasing the likelihood that material cybersecurity risks remain unresolved or incidents are handled ineffectively.

---

## Existing Controls

Existing strengths include:

- an internal IT and cybersecurity capability;
- personnel performing cloud security administration;
- endpoint security management;
- authentication monitoring;
- technical incident-handling activity;
- security assessment capability;
- detection-engineering capability.

These controls demonstrate operational responsibility but do not provide a complete accountability framework.

---

## Recommended Remediation

Northstar HealthTech should establish a formal cybersecurity roles and responsibilities model.

The model should define at minimum:

1. Cybersecurity executive sponsor
2. Cybersecurity risk owner
3. IT operations responsibilities
4. Cloud security responsibilities
5. Identity and access management ownership
6. Vulnerability-management ownership
7. Security-monitoring ownership
8. Incident-response roles
9. Business continuity and recovery responsibilities
10. Third-party security ownership
11. Risk acceptance authority
12. Policy exception authority
13. Escalation paths
14. Executive reporting responsibilities

---

## Recommended RACI Domains

A RACI matrix should be created for major cybersecurity processes.

Suggested domains include:

| Process | Example Accountability Area |
|---|---|
| Cybersecurity risk management | Strategy, risk prioritization, risk acceptance |
| IAM | Provisioning, privilege review, access removal |
| Vulnerability management | Identification, remediation, exception handling |
| Security monitoring | Detection coverage, alert triage, escalation |
| Incident response | Coordination, containment, communications |
| Cloud security | IAM, logging, configuration, remediation |
| Third-party risk | Due diligence, review, exception tracking |
| Recovery | Backup ownership, recovery testing, restoration |
| Security policy | Approval, maintenance, exception governance |

The final RACI should identify:

- Responsible
- Accountable
- Consulted
- Informed

for each critical process.

---

## Recommended Implementation Actions

### 0–30 Days

- Assign an executive cybersecurity sponsor.
- Identify accountable owners for major security domains.
- Document interim incident escalation contacts.
- Assign ownership for the cybersecurity risk register.
- Assign responsibility for privileged-access reviews.

### 31–90 Days

- Develop a formal cybersecurity RACI matrix.
- Define risk acceptance and exception authority.
- Document incident-response decision rights.
- Assign owners for vulnerability remediation and third-party risk.
- Communicate responsibilities to affected teams.

### 3–12 Months

- Review cybersecurity responsibilities at least annually.
- Update the RACI after organizational or technology changes.
- Tie control ownership to security metrics.
- Include cybersecurity accountability in relevant job descriptions and performance objectives.
- Test escalation and decision authority through tabletop exercises.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- cybersecurity roles are formally documented;
- accountable owners exist for major security processes;
- a RACI or equivalent responsibility model is approved;
- risk acceptance authority is defined;
- incident escalation authority is documented;
- staff understand relevant responsibilities;
- responsibilities are reviewed periodically;
- ownership changes are tracked and updated.

---

## Suggested Evidence After Remediation

Examples include:

- approved cybersecurity organization chart;
- cybersecurity RACI matrix;
- job descriptions;
- incident-response responsibility matrix;
- documented escalation procedure;
- risk acceptance authority matrix;
- security governance meeting records;
- policy ownership register;
- annual responsibility review record.

---

## Priority

**High**

### Priority Rationale

This gap affects multiple cybersecurity processes and can reduce the effectiveness of otherwise sound technical controls.

The issue is not an immediate exploit condition, but unclear ownership and authority can materially delay risk treatment and incident response.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-002 |
| Finding | GRC-002 |
| Risk Domain | Governance / Accountability |
| NIST CSF 2.0 | GV.RR |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Executive Sponsor / Security Leadership |
| Status | Open |

Final numerical risk scoring will be assigned using the project-wide risk methodology.

---

## Consultant Perspective

A common cybersecurity maturity problem is that organizations have security technology and capable personnel but insufficiently defined accountability.

The maturity progression should be:

```text
People perform security tasks
        ↓
Responsibilities documented
        ↓
Accountability assigned
        ↓
Decision authority defined
        ↓
Responsibilities communicated
        ↓
Performance measured
        ↓
Responsibilities periodically reviewed
```

The objective is not to create bureaucracy. It is to remove ambiguity from critical cybersecurity decisions.

---

## Relationship to GRC-001

GRC-001 addresses the absence of a formally established cybersecurity risk-management strategy.

GRC-002 addresses **who is responsible and authorized to execute that strategy**.

Together:

```text
GRC-001
What cybersecurity risk objectives govern the program?
        ↓
GRC-002
Who owns, executes, approves, and escalates those responsibilities?
```

These two findings establish the governance foundation for the remainder of the assessment.

---

## Final Assessment Statement

Northstar HealthTech has personnel actively performing cybersecurity responsibilities, but those responsibilities, accountabilities, and authorities are not consistently formalized across the organization.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Establishing an approved cybersecurity responsibility model and RACI matrix should be treated as a high-priority governance improvement because clear accountability is necessary for effective risk management, incident response, access governance, vulnerability remediation, and executive oversight.

# GRC-005 — Privileged Access Reviews Are Not Performed on a Formal Recurring Basis

## Finding Summary

Northstar HealthTech has privileged and elevated access across cloud, endpoint, administrative, and security-management functions. Although access is granted and modified operationally, the fictional organization does not perform privileged-access recertification through a formally defined, recurring review process.

This creates a governance gap in which privileged entitlements may remain active after job changes, project completion, temporary assignments, or changes in business need.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **PROTECT (PR)** Function and the **Identity Management, Authentication, and Access Control (PR.AA)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**PR.AA — Identity Management, Authentication, and Access Control**

This finding focuses on periodic review and continued authorization of privileged access.

The exact subcategory crosswalk will be maintained in the project-wide control matrix.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Privileged AWS and administrative roles exist.
- Elevated permissions are actively used for operational purposes.
- Excessive and stale permissions have previously been identified through technical review.
- Some access remediation occurs when individual issues are discovered.
- No documented quarterly privileged-access recertification process has been identified.
- No recurring review calendar has been established.
- No authoritative evidence shows that privileged owners periodically reapprove access.
- No formal process exists for documenting review decisions.
- Temporary privileged access does not consistently have enforced expiry.
- Role changes do not always trigger immediate entitlement revalidation.
- No privileged-access review completion metric is currently reported to management.
- No formal escalation process exists for overdue access reviews.

---

## Observed Control State

Northstar HealthTech can grant, modify, and remove privileged access technically.

However, it lacks a repeatable governance mechanism to confirm that elevated access remains justified over time.

The organization therefore cannot consistently demonstrate that:

- privileged entitlements are reviewed at defined intervals;
- access owners revalidate ongoing business need;
- stale privileges are removed proactively;
- temporary privilege expires automatically or is formally reapproved;
- terminated or transferred users are consistently included in review;
- review outcomes are documented;
- unresolved access-review exceptions are escalated.

The current state is therefore **operationally functional but governance-incomplete**.

---

## Scoring Rationale

Evidence shows that privileged access is technically controlled and that access can be remediated when issues are discovered.

This supports a score above **1 — Initial**.

However, the lack of:

- recurring recertification;
- defined review frequency;
- documented approval evidence;
- review completion tracking;
- exception escalation;
- consistent lifecycle integration;

means the process is not yet sufficiently repeatable and governed to qualify as **3 — Defined**.

The capability is therefore assessed as **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Privileged access controls exist and review activity may occur, but the process is incomplete, inconsistent, or insufficiently documented.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which privileged-access reviews are:

- formally scheduled;
- risk-based;
- performed by accountable owners;
- documented;
- tracked to completion;
- linked to joiner/mover/leaver processes;
- supported by exception management;
- monitored through governance metrics.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is material because privileged permissions can persist beyond legitimate business need.

---

## Business Risk

Failure to periodically recertify privileged access can result in unnecessary elevated permissions remaining active.

Potential consequences include:

- unauthorized administrative access;
- increased blast radius after credential compromise;
- misuse of forgotten or inherited permissions;
- excessive access after internal transfers;
- persistence of temporary administrative privileges;
- weak segregation of duties;
- delayed removal of unnecessary entitlements;
- inability to demonstrate appropriate access governance.

---

## Risk Statement

> If Northstar HealthTech does not perform formal recurring reviews of privileged access, elevated permissions may remain active after they are no longer required, increasing the likelihood and potential impact of unauthorized access, privilege misuse, or credential compromise.

---

## Relationship to GRC-004

GRC-004 identifies the control condition:

> excessive and stale privileged access exists.

GRC-005 identifies the governance mechanism that should prevent that condition from recurring:

> privileged access must be periodically recertified.

The relationship can be represented as:

```text
GRC-004
Excessive / stale privileges identified
        ↓
Root governance weakness
No reliable recurring access review
        ↓
GRC-005
Formal privileged-access recertification required
```

This separation is intentional.

GRC-004 addresses **permission scope and entitlement hygiene**.

GRC-005 addresses **ongoing review and governance cadence**.

---

## Existing Controls

Existing strengths include:

- AWS IAM role-based access;
- ability to modify or revoke access;
- technical least-privilege remediation;
- CloudTrail logging;
- administrative ownership of some privileged roles;
- security assessment capability.

These controls reduce risk but do not replace periodic access recertification.

---

## Recommended Remediation

Northstar HealthTech should implement a formal privileged-access review program.

The process should define:

1. In-scope privileged identities
2. In-scope elevated roles and groups
3. Access owners
4. Review frequency
5. Reviewer responsibilities
6. Required business justification
7. Review decision options
8. Removal deadlines
9. Exception handling
10. Escalation requirements
11. Evidence retention
12. Management reporting

---

## Recommended Review Cadence

### Tier 1 — Critical Privilege

Examples:

- cloud administrators;
- identity administrators;
- security administrators;
- production infrastructure administrators.

Recommended cadence:

```text
Quarterly
```

### Tier 2 — Elevated Operational Access

Examples:

- application administrators;
- database operators;
- infrastructure support roles.

Recommended cadence:

```text
Every 6 months
```

### Tier 3 — Standard User Access

Routine access should follow a risk-based cadence appropriate to business need.

---

## Required Review Decisions

Each reviewed entitlement should receive one of the following dispositions:

```text
Approve
Modify
Remove
Exception
Investigate
```

### Approve

Access remains required and appropriately scoped.

### Modify

Access remains required but scope should be reduced.

### Remove

Business justification no longer exists.

### Exception

Access exceeds standard requirements but has documented approval, rationale, compensating controls, and expiry.

### Investigate

Information is insufficient to make a defensible access decision.

---

## Minimum Review Evidence

For each privileged entitlement, the review record should capture:

- identity;
- role or entitlement;
- system;
- entitlement owner;
- reviewer;
- business justification;
- review date;
- decision;
- remediation action if required;
- completion date;
- exception expiry if applicable.

---

## Suggested Access Review Workflow

```text
Generate privileged entitlement population
        ↓
Validate identity status
        ↓
Route entitlement to accountable owner
        ↓
Confirm current business need
        ↓
Approve / Modify / Remove / Exception
        ↓
Execute required remediation
        ↓
Validate completion
        ↓
Retain evidence
        ↓
Report completion and exceptions
```

---

## Joiner / Mover / Leaver Integration

Recurring review should complement—not replace—event-driven access governance.

### Joiner

Access should be granted according to approved role requirements.

### Mover

Role or department changes should trigger entitlement revalidation.

### Leaver

Access should be revoked according to defined termination procedures.

### Recertification

Periodic review acts as a control to identify permissions missed by normal lifecycle processes.

---

## Exception Management

Any privileged access that exceeds standard entitlement requirements should require:

- documented justification;
- named risk owner;
- compensating controls;
- approval authority;
- review date;
- expiration date.

Permanent exceptions should be avoided where possible.

---

## Recommended Metrics

Northstar HealthTech should track metrics such as:

| Metric | Purpose |
|---|---|
| Privileged reviews completed on time | Measures governance execution |
| Privileged accounts reviewed | Measures coverage |
| Access removed during review | Indicates stale entitlement detection |
| Access modified during review | Indicates excessive-scope correction |
| Open access exceptions | Measures governance debt |
| Expired exceptions | Identifies overdue remediation |
| Average days to remove rejected access | Measures remediation timeliness |
| Accounts without identified owner | Identifies accountability gaps |

---

## Recommended Implementation Actions

### 0–30 Days

- Define what constitutes privileged access.
- Inventory privileged identities and entitlements.
- Assign owners for high-risk roles.
- Establish a quarterly review schedule for critical privilege.
- Identify clearly stale access for immediate removal.

### 31–90 Days

- Document privileged-access review procedures.
- Perform the first formal recertification cycle.
- Record approval and removal decisions.
- Establish an exception register.
- Define escalation for overdue reviews.
- Integrate mover and leaver events with entitlement review.

### 3–12 Months

- Automate entitlement population generation where feasible.
- Introduce access-governance tooling where justified.
- Track review completion metrics.
- Establish dashboards for unresolved access exceptions.
- Use historical review data to identify recurring access-design problems.
- Incorporate review performance into security governance reporting.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- privileged access is formally defined;
- all material privileged identities are inventoried;
- accountable owners are assigned;
- recurring review frequency is documented;
- completed access-review records exist;
- stale access is removed within defined timelines;
- exceptions have approval and expiry;
- overdue reviews are escalated;
- completion metrics are reported;
- access reviews are integrated with identity lifecycle processes.

---

## Suggested Evidence After Remediation

Examples include:

- privileged-access review policy;
- quarterly review schedule;
- privileged entitlement inventory;
- completed review workbook or system export;
- access-owner approvals;
- removal tickets;
- exception register;
- overdue-review escalation records;
- access-review dashboard;
- joiner/mover/leaver process documentation.

---

## Priority

**High**

### Priority Rationale

Privileged identities can make high-impact changes to systems and cloud resources.

The absence of recurring review increases the probability that unnecessary elevated access will remain available over time.

This risk is amplified by the evidence documented in GRC-004 showing that excessive and stale permissions can exist in the environment.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-005 |
| Finding | GRC-005 |
| Risk Domain | Identity Governance |
| NIST CSF 2.0 | PR.AA |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | IAM / IT / Security Leadership |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Technical-to-Governance Crosswalk

```text
Technical evidence
Stale / excessive IAM permissions
        ↓
Control weakness
Entitlements remain broader than required
        ↓
Governance cause
No dependable recurring recertification
        ↓
Business risk
Compromised identity retains unnecessary power
        ↓
Control improvement
Formal privileged-access review program
```

---

## Consultant Perspective

Access reviews should not become a checkbox exercise.

A strong review process asks:

```text
Does this identity still exist?
        ↓
Does this person still perform this role?
        ↓
Is this privilege still required?
        ↓
Is the permission scope appropriate?
        ↓
Can the privilege be reduced?
        ↓
Is an exception justified?
        ↓
Was the final decision actually implemented?
```

The most important part is not generating a review spreadsheet. It is ensuring that review decisions lead to verified access changes.

---

## Final Assessment Statement

Northstar HealthTech has technical mechanisms for granting and removing privileged access but does not perform privileged-access recertification through a consistently defined and governed recurring process.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Implementing risk-based review cadences, entitlement ownership, documented approval decisions, exception governance, remediation tracking, and management reporting should be treated as a high-priority identity-governance improvement.

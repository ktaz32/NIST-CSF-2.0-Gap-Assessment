# GRC-004 — Excessive and Stale Privileged Access

## Finding Summary

Northstar HealthTech has implemented identity and access controls across AWS and other enterprise systems; however, the fictional organization does not consistently enforce least privilege or remove stale permissions in a timely and governed manner.

Technical evidence from the modeled cloud environment demonstrates examples of:

- overly broad AWS-managed permissions;
- wildcard resource scope;
- stale permissions no longer required by a role;
- inconsistent privileged-access review.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **PROTECT (PR)** Function and the **Identity Management, Authentication, and Access Control (PR.AA)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**PR.AA — Identity Management, Authentication, and Access Control**

This finding focuses on the need to ensure that identities and their associated permissions are appropriately authorized, scoped, reviewed, and maintained according to business requirements and least-privilege principles.

The exact subcategory crosswalk will be maintained in the project-wide control matrix.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- AWS identity and access controls are implemented.
- Administrative and application roles exist in the AWS environment.
- Technical assessment activity identified excessive permissions.
- One modeled role held broad AWS-managed S3 access beyond its required scope.
- Another modeled role used wildcard resource permissions.
- A legacy application role retained DynamoDB permissions that were no longer required.
- Least-privilege remediation was possible and validated in technical testing.
- Access-review activity is inconsistent.
- No mature privileged access management program has been identified.
- No formal recurring entitlement recertification process has been documented.
- Stale permissions may remain until discovered through technical review.
- Privileged access decisions are not consistently tied to documented business justification and periodic revalidation.

---

## Technical Portfolio Evidence

This GRC finding can be linked directly to the AWS Cloud Security Assessment portfolio.

### AWS-01 — Excessive AWS-Managed S3 Permissions

Observed condition:

```text
DeveloperRole
        ↓
AmazonS3FullAccess
        ↓
Access exceeded documented requirement
```

Remediation:

```text
Remove broad AWS-managed policy
        ↓
Attach custom least-privilege policy
        ↓
Retest required and denied access
```

---

### AWS-02 — Wildcard Resource Scope

Observed condition:

```text
ReportReaderRole
        ↓
Resource: "*"
        ↓
Access to unnecessary S3 resources
```

Remediation:

```text
Restrict resources to required reports bucket
        ↓
Retest intended access
        ↓
Confirm unrelated access denied
```

---

### AWS-03 — Stale Legacy Permissions

Observed condition:

```text
LegacyAppRole
        ↓
S3 permissions
+
unused DynamoDB permissions
```

Assessment evidence indicated that the DynamoDB permissions were no longer required.

Remediation removed the stale permissions while retaining required application functionality.

---

## Observed Control State

Northstar HealthTech has functioning identity and access controls and can technically implement granular permissions.

However, governance and lifecycle management are incomplete.

The organization does not consistently demonstrate that:

- every privileged permission has a current business justification;
- access is scoped to the minimum resources required;
- wildcard permissions are formally reviewed;
- stale permissions are removed proactively;
- high-risk access receives recurring recertification;
- access exceptions have defined expiration dates;
- dormant roles and permissions are periodically identified;
- changes are tracked through a consistent approval process.

The current state is therefore **technically implemented but only partially governed**.

---

## Scoring Rationale

The organization has real technical access controls and demonstrates the ability to remediate excessive permissions.

This supports a score above **1 — Initial**.

However, evidence of:

- excessive permissions;
- wildcard access;
- stale entitlements;
- inconsistent access review;
- incomplete privileged-access governance;

shows that the control is not yet consistently defined, reviewed, and measured.

The capability is therefore assessed at **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Identity and access controls are partially implemented and technically functional, but least-privilege governance, review, documentation, and lifecycle management remain incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which privileged access is:

- formally approved;
- business-justified;
- least-privilege by design;
- time-bound where appropriate;
- periodically reviewed;
- automatically or systematically monitored;
- promptly removed when no longer required;
- measured using access-governance metrics.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is significant because excessive privileges can materially increase the impact of compromised identities or misused accounts.

---

## Business Risk

Excessive or stale privileged access increases the potential blast radius of account compromise.

Potential consequences include:

- unauthorized access to sensitive cloud data;
- deletion or modification of critical resources;
- privilege misuse;
- lateral movement within cloud environments;
- persistence using overprivileged roles;
- difficulty demonstrating appropriate access governance;
- increased impact from compromised credentials;
- unnecessary exposure through forgotten permissions.

---

## Risk Statement

> If Northstar HealthTech does not consistently enforce least privilege and remove stale privileged access, compromised or misused identities may retain unnecessary permissions that enable unauthorized access to sensitive information, cloud resources, or business-critical systems.

---

## Existing Controls

Existing strengths include:

- AWS IAM;
- custom IAM policies;
- role-based access;
- technical access testing;
- CloudTrail logging;
- ability to remove excessive permissions;
- validation of denied access after remediation.

These are meaningful control strengths but do not replace recurring access governance.

---

## Recommended Remediation

Northstar HealthTech should implement a formal privileged-access governance process.

The process should include at minimum:

1. Least-privilege policy requirements
2. Documented business justification
3. Named access owner
4. Approval workflow
5. Privileged-role inventory
6. Periodic entitlement review
7. Wildcard-permission review
8. Stale-access identification
9. Time-bound temporary access
10. Separation of duties where appropriate
11. Exception tracking
12. Access removal requirements
13. Offboarding integration
14. Metrics and governance reporting

---

## Recommended Access Review Model

### High-Risk Privileged Access

Examples:

- cloud administrators;
- highly privileged IAM roles;
- production administrators;
- security administrators.

Suggested review cadence:

```text
Quarterly
```

### Standard Elevated Access

Examples:

- application-specific elevated roles;
- infrastructure support roles.

Suggested review cadence:

```text
Every 6 months
```

### Standard User Access

Suggested review cadence should be risk-based and aligned with business requirements.

---

## Privileged Access Review Questions

For each entitlement, reviewers should confirm:

- Is the identity still active?
- Is the access still required?
- Is the role appropriate?
- Is the permission scope excessive?
- Are wildcard permissions justified?
- Does the identity have unused permissions?
- Is the owner still correct?
- Is temporary access past its expiry?
- Does the access create segregation-of-duties concerns?
- Has the user changed role or department?

---

## Recommended Implementation Actions

### 0–30 Days

- Create an inventory of privileged identities and roles.
- Identify wildcard and broad permissions.
- Review high-risk cloud administrators.
- Remove clearly unused or stale permissions.
- Assign owners to privileged roles.

### 31–90 Days

- Establish formal access-review procedures.
- Implement quarterly privileged-access recertification.
- Require business justification for high-risk access.
- Define expiration requirements for temporary privilege.
- Establish an exception register.
- Integrate access review with employee role changes.

### 3–12 Months

- Introduce privileged access management where justified.
- Automate stale-permission identification.
- Implement entitlement analytics.
- Track access-review completion rates.
- Establish least-privilege metrics.
- Integrate joiner/mover/leaver processes with access governance.
- Use continuous monitoring for high-risk privilege changes.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- privileged identities are inventoried;
- high-risk access has documented business justification;
- recurring access reviews occur;
- stale permissions are removed;
- wildcard permissions are reviewed and justified;
- temporary access is time-bound;
- review completion is tracked;
- access exceptions are documented;
- access removal is integrated with offboarding and role changes;
- management reporting exists.

---

## Suggested Evidence After Remediation

Examples include:

- privileged-access inventory;
- access review procedure;
- completed quarterly recertification records;
- IAM policy review reports;
- entitlement owner records;
- access exception register;
- temporary-access expiry records;
- joiner/mover/leaver workflow;
- access-governance dashboard;
- IAM remediation evidence.

---

## Priority

**High**

### Priority Rationale

This finding affects identities with elevated access to business-critical systems.

While compensating controls such as logging and technical IAM enforcement exist, excessive and stale privilege materially increases the impact of credential compromise.

The finding is therefore high priority.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-004 |
| Finding | GRC-004 |
| Risk Domain | Identity and Access Management |
| NIST CSF 2.0 | PR.AA |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | IT / Security / Cloud Platform Owner |
| Status | Open |

Final numerical scoring will be assigned under the project-wide risk methodology.

---

## Technical-to-Governance Crosswalk

This finding demonstrates how technical evidence can support a governance assessment.

```text
Technical finding
Excessive IAM permission
        ↓
Control observation
Least privilege not consistently enforced
        ↓
Governance gap
Privileged-access lifecycle not mature
        ↓
Business risk
Compromised account has excessive capability
        ↓
GRC recommendation
Formal access review + entitlement governance
```

This is one of the most important cross-project links in the portfolio.

---

## Relationship to Previous Findings

```text
GRC-001
Cyber risk strategy
        ↓
GRC-002
Roles and accountability
        ↓
GRC-003
Third-party governance
        ↓
GRC-004
Technical access governance
```

GRC-004 begins the transition from high-level governance findings into technical control governance.

---

## Final Assessment Statement

Northstar HealthTech has functional identity and access controls, but technical evidence demonstrates excessive, wildcard, and stale permissions alongside inconsistent privileged-access review.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Formalizing least-privilege governance, recurring access recertification, stale-permission removal, entitlement ownership, and access lifecycle controls should be treated as a high-priority security improvement.

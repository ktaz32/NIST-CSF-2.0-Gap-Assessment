# GRC-006 — Asset Inventory Is Incomplete

## Finding Summary

Northstar HealthTech operates a hybrid technology environment that includes Windows endpoints, AWS cloud resources, Microsoft 365, SaaS applications, GitHub, networking services, and third-party platforms.

Although the fictional organization tracks portions of its technology estate, it does not maintain a sufficiently complete, authoritative, and consistently reconciled inventory of hardware, software, cloud resources, identities, and critical data-related assets.

This creates a foundational visibility gap: security teams cannot reliably protect, monitor, patch, recover, or assess assets that are not known and owned.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **IDENTIFY (ID)** Function and the **Asset Management (ID.AM)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**ID.AM — Asset Management**

This finding focuses on the identification and management of technology assets that support organizational objectives and cybersecurity risk management.

The exact subcategory crosswalk will be maintained in the project-wide control matrix.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech uses Windows 11 endpoints, AWS, Microsoft 365, GitHub, SaaS platforms, VPN infrastructure, and third-party services.
- Some assets are tracked within platform-specific administrative consoles.
- AWS resources can be enumerated within individual services.
- Endpoint-management and security tools provide partial device visibility.
- No single authoritative asset inventory has been identified.
- Cloud, SaaS, endpoint, identity, and application inventories are not consistently reconciled.
- Asset ownership is not defined for every critical system.
- Business criticality is not consistently assigned.
- Unsupported or stale assets may remain present until discovered through operational activity.
- No formal reconciliation cadence has been established.
- No documented process consistently detects unknown or newly created cloud resources.
- Software inventory is incomplete across the environment.
- Third-party-hosted systems are not fully integrated into the internal asset inventory.

---

## Observed Control State

Northstar HealthTech has multiple sources of asset information, but asset visibility is fragmented.

The organization can identify many systems within individual platforms, but cannot consistently answer:

- What assets exist across the enterprise?
- Which assets are business-critical?
- Who owns each asset?
- Which assets process sensitive information?
- Which systems are internet-facing?
- Which systems are unsupported?
- Which cloud resources were created outside standard processes?
- Which assets are missing endpoint-security coverage?
- Which applications or SaaS services are unsanctioned?
- Which assets should be retired?

The current state is therefore **partially implemented but incomplete and decentralized**.

---

## Scoring Rationale

Evidence demonstrates that asset information exists within individual administrative and security platforms.

This supports a score above **1 — Initial**.

However, the organization lacks:

- an authoritative enterprise inventory;
- consistent asset ownership;
- business-criticality classification;
- complete software visibility;
- reconciliation across platforms;
- recurring validation;
- reliable detection of unknown assets.

The capability is therefore assessed as **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Asset information exists and is partially maintained, but coverage, ownership, consistency, and governance are incomplete.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which the asset inventory is:

- authoritative;
- continuously or regularly updated;
- reconciled across major platforms;
- assigned to accountable owners;
- classified by criticality;
- linked to data sensitivity where appropriate;
- monitored for unauthorized or unknown assets;
- measured through inventory-quality metrics.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is significant because asset visibility is a prerequisite for vulnerability management, monitoring, incident response, recovery, and access governance.

---

## Business Risk

Incomplete asset inventory can lead to unmanaged systems remaining outside normal security processes.

Potential consequences include:

- unpatched or unsupported systems;
- missing endpoint protection;
- unmonitored cloud resources;
- forgotten internet-facing services;
- orphaned SaaS applications;
- unclear recovery priorities;
- incomplete vulnerability scanning;
- delayed incident scoping;
- unknown data-processing locations;
- increased attack surface.

---

## Risk Statement

> If Northstar HealthTech does not maintain a complete and authoritative inventory of technology assets, unknown, unmanaged, or incorrectly classified systems may remain outside security monitoring, vulnerability management, access governance, and recovery processes, increasing the likelihood of compromise or operational disruption.

---

## Existing Controls

Existing strengths include:

- endpoint-management tooling;
- Microsoft Defender visibility;
- AWS service inventories;
- Microsoft 365 administration;
- GitHub organization visibility;
- security logging from selected systems;
- technical assessment capability.

These provide useful asset data but are fragmented and not yet governed as one enterprise inventory.

---

## Recommended Remediation

Northstar HealthTech should establish a formal enterprise asset-management process.

The process should cover at minimum:

1. Hardware assets
2. Software assets
3. Cloud resources
4. SaaS applications
5. Identities and service accounts
6. Network infrastructure
7. Security tooling
8. Business applications
9. Internet-facing services
10. Third-party-hosted systems
11. Asset ownership
12. Business criticality
13. Data sensitivity
14. Lifecycle status
15. Support status

---

## Minimum Asset Record

Each asset should capture, where applicable:

- unique asset identifier;
- asset name;
- asset type;
- platform;
- owner;
- business function;
- criticality;
- environment;
- location or hosting model;
- internet exposure;
- data sensitivity;
- support status;
- security-control coverage;
- lifecycle status;
- last verification date.

---

## Recommended Asset Categories

### Endpoints

Examples:

- laptops;
- workstations;
- administrative endpoints.

### Cloud Resources

Examples:

- AWS EC2;
- S3 buckets;
- IAM roles;
- security groups;
- CloudTrail trails.

### Applications

Examples:

- business applications;
- SaaS services;
- internal tools;
- GitHub repositories.

### Infrastructure

Examples:

- VPN gateways;
- networking devices;
- identity systems;
- logging infrastructure.

---

## Asset Ownership Model

Every critical asset should have an accountable owner.

An owner should be able to answer:

- Why does this asset exist?
- What business process depends on it?
- What data does it process?
- What access should exist?
- What is its recovery priority?
- When should it be retired?

Assets without identified owners should be treated as governance exceptions.

---

## Asset Criticality

A simple classification model may include:

### Critical

Failure would cause severe business, security, legal, or customer impact.

### High

Important to business operations or security, but short-term alternatives may exist.

### Moderate

Supports normal operations with manageable disruption if unavailable.

### Low

Limited business impact.

Criticality should drive:

- vulnerability-remediation priority;
- logging requirements;
- backup requirements;
- recovery objectives;
- access-review frequency;
- security-monitoring coverage.

---

## Reconciliation Process

Northstar HealthTech should reconcile asset information across major systems.

Example:

```text
Endpoint management
        +
Microsoft Defender
        +
AWS inventory
        +
Microsoft 365
        +
SaaS register
        +
Identity systems
        ↓
Authoritative asset inventory
        ↓
Exception review
        ↓
Remediation
```

Differences between inventories should create investigation items.

---

## Unknown Asset Detection

The organization should establish processes to identify assets that appear outside standard provisioning workflows.

Examples include:

- unmanaged endpoints;
- newly created cloud resources;
- unauthorized SaaS applications;
- unknown external services;
- orphaned IAM roles;
- unsupported systems.

Unknown assets should be investigated and either:

```text
Authorize
Register
Secure
Retire
```

---

## Recommended Metrics

Northstar HealthTech should track metrics such as:

| Metric | Purpose |
|---|---|
| Assets with assigned owner | Measures accountability |
| Assets with criticality assigned | Measures business context |
| Assets missing security tooling | Measures control gaps |
| Unknown assets discovered | Measures visibility effectiveness |
| Stale assets | Measures lifecycle hygiene |
| Unsupported assets | Measures technology risk |
| Inventory reconciliation exceptions | Measures inventory quality |
| Internet-facing assets | Measures external attack surface |
| Assets verified within required period | Measures governance execution |

---

## Recommended Implementation Actions

### 0–30 Days

- Identify authoritative sources of asset data.
- Create a baseline enterprise asset register.
- Prioritize critical systems and internet-facing assets.
- Assign owners to high-value systems.
- Identify clearly stale or orphaned resources.

### 31–90 Days

- Define required asset fields.
- Establish business-criticality classification.
- Reconcile endpoint, cloud, SaaS, and identity inventories.
- Define inventory review cadence.
- Establish an unknown-asset exception process.
- Integrate asset ownership with vulnerability management.

### 3–12 Months

- Automate asset discovery and reconciliation where feasible.
- Track inventory-quality metrics.
- Integrate asset inventory with incident response and recovery.
- Use asset criticality to drive control requirements.
- Establish retirement and lifecycle governance.
- Introduce continuous cloud-resource inventory monitoring.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- an authoritative asset inventory exists;
- critical systems are identified;
- accountable owners are assigned;
- asset criticality is documented;
- cloud and endpoint inventories are reconciled;
- software and SaaS inventories are maintained;
- unknown assets trigger investigation;
- stale assets are tracked to remediation;
- inventory quality is measured;
- recurring review is performed.

---

## Suggested Evidence After Remediation

Examples include:

- enterprise asset register;
- cloud inventory export;
- endpoint inventory report;
- software inventory;
- SaaS register;
- ownership assignments;
- criticality classification;
- reconciliation report;
- unknown-asset investigation tickets;
- stale-asset remediation records;
- asset-management dashboard.

---

## Priority

**High**

### Priority Rationale

Asset inventory is a foundational cybersecurity control.

While the absence of a complete inventory does not itself represent an active exploit, it creates blind spots across multiple downstream security processes.

The finding is therefore high priority because incomplete asset visibility can undermine vulnerability management, security monitoring, incident response, and recovery.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-006 |
| Finding | GRC-006 |
| Risk Domain | Asset Management |
| NIST CSF 2.0 | ID.AM |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | IT Operations / Security |
| Status | Open |

Final numerical risk scoring will be assigned under the project-wide risk-scoring methodology.

---

## Technical-to-Governance Crosswalk

```text
Fragmented technical inventories
        ↓
Incomplete enterprise visibility
        ↓
Unknown / unmanaged assets
        ↓
Security control gaps
        ↓
Increased attack surface and response uncertainty
        ↓
Formal asset-management governance
```

---

## Consultant Perspective

Asset inventory is not simply a spreadsheet of devices.

A mature asset-management process answers:

```text
What exists?
        ↓
Who owns it?
        ↓
Why does it matter?
        ↓
What data does it handle?
        ↓
What controls protect it?
        ↓
Is it still required?
        ↓
Can we detect when something new appears?
```

The business value comes from connecting asset visibility to risk decisions.

---

## Relationship to Previous Findings

GRC-006 supports several other controls:

```text
Asset inventory
        ↓
Vulnerability management
        ↓
Security monitoring
        ↓
Incident scoping
        ↓
Recovery prioritization
```

Without dependable asset visibility, later security capabilities cannot be evaluated or executed consistently.

---

## Final Assessment Statement

Northstar HealthTech has partial asset visibility through endpoint, cloud, identity, and SaaS platforms, but it lacks a complete and authoritative enterprise asset inventory with consistent ownership, criticality, lifecycle status, and reconciliation.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Establishing an authoritative asset register, assigning owners, defining criticality, reconciling multiple inventory sources, and measuring inventory quality should be treated as a high-priority foundational improvement.

# GRC-003 — Third-Party Cybersecurity Risk Reviews Are Inconsistent

## Finding Summary

Northstar HealthTech relies on multiple SaaS providers, cloud services, software vendors, and other technology partners to support business operations.

Although some vendor-security checks occur, the fictional organization does not have a consistently applied, risk-based third-party cybersecurity review process covering vendor onboarding, reassessment, contractual security requirements, exception handling, and offboarding.

As a result, supplier and service-provider cyber risk may be evaluated unevenly across the organization.

This finding maps primarily to the NIST Cybersecurity Framework 2.0 **GOVERN (GV)** Function and the **Cybersecurity Supply Chain Risk Management (GV.SC)** Category.

---

## NIST CSF 2.0 Mapping

### Primary Category

**GV.SC — Cybersecurity Supply Chain Risk Management**

This finding focuses on the organization's need to identify, assess, manage, and monitor cybersecurity risks arising from suppliers and other third parties.

The precise subcategory mapping will be maintained in the project-wide control matrix so that individual assessment records remain aligned with the selected NIST CSF 2.0 outcomes.

---

## Current-State Evidence

The following fictional assessment evidence supports this finding:

- Northstar HealthTech depends on multiple SaaS and technology vendors.
- Third-party security reviews occur, but not consistently.
- No formal risk-tiering methodology has been identified for suppliers.
- No evidence has been provided of a mandatory cybersecurity review before all relevant vendor onboarding.
- Security questionnaires are not consistently required.
- Contractual cybersecurity clauses are not standardized across material suppliers.
- Recurring reassessment intervals are not formally defined.
- No centralized process exists for tracking vendor-security exceptions.
- No formal process has been identified for escalating high-risk vendor findings.
- Offboarding requirements for data return, data deletion, and access revocation are not consistently documented.
- Monitoring of changes in supplier cybersecurity posture is limited.

---

## Observed Control State

Northstar HealthTech recognizes that third parties can introduce cybersecurity risk and performs selected vendor-security activities.

However, these activities are not governed by a mature, repeatable lifecycle.

The organization cannot consistently demonstrate that:

- every material supplier is identified;
- suppliers are tiered according to business and cyber risk;
- appropriate due diligence occurs before onboarding;
- security requirements are reflected in contracts;
- high-risk suppliers receive deeper scrutiny;
- existing suppliers are periodically reassessed;
- cybersecurity issues are tracked to closure;
- supplier access is removed when the relationship ends;
- significant changes in supplier risk are monitored.

The current state is therefore **partially implemented but inconsistent across the supplier lifecycle**.

---

## Scoring Rationale

Evidence demonstrates that third-party cybersecurity risk is recognized and that some review activity occurs.

This supports a score above **1 — Initial**.

However, the process lacks consistent:

- risk tiering;
- mandatory review criteria;
- standard evidence requirements;
- reassessment cadence;
- exception governance;
- centralized tracking;
- lifecycle monitoring.

The capability is therefore assessed as **2 — Developing**.

---

## Current Maturity

**2 — Developing**

Definition:

> Third-party cybersecurity risk activities exist, but implementation, documentation, coverage, and governance are incomplete or inconsistent.

---

## Target Maturity

**4 — Managed**

A suitable target state is one in which Northstar HealthTech has a formal, risk-based third-party cybersecurity risk management process that is:

- documented;
- consistently applied;
- integrated into procurement and onboarding;
- risk-tiered;
- contractually supported;
- periodically reassessed;
- tracked through defined metrics;
- governed through escalation and exception processes.

---

## Maturity Gap

```text
Target Maturity: 4
Current Maturity: 2
Gap:              2
```

The gap is material because third parties may process sensitive information, provide critical services, or maintain privileged connectivity into the organization.

---

## Business Risk

Inconsistent third-party cybersecurity review can result in Northstar HealthTech relying on vendors whose security posture is not adequately understood.

Potential consequences include:

- exposure of sensitive healthcare-related information;
- compromise through a supplier account or integration;
- service disruption caused by a critical vendor incident;
- weak contractual protection following a breach;
- prolonged exposure because reassessment does not occur;
- orphaned third-party access after offboarding;
- inconsistent treatment of high-risk suppliers;
- inability to demonstrate appropriate supplier due diligence to customers or stakeholders.

---

## Risk Statement

> If Northstar HealthTech does not consistently assess and govern cybersecurity risks across the third-party lifecycle, vulnerabilities or control weaknesses at suppliers may expose sensitive information, identities, cloud services, or critical business operations to compromise or disruption.

---

## Existing Controls

Existing strengths include:

- awareness that suppliers introduce cybersecurity risk;
- some vendor-security review activity;
- centralized use of major enterprise cloud and SaaS platforms;
- technical security controls protecting internal systems;
- identity and access controls for some third-party interactions.

These controls provide partial risk reduction but do not constitute a complete third-party cyber-risk management lifecycle.

---

## Recommended Remediation

Northstar HealthTech should establish a formal third-party cybersecurity risk management process.

The process should define at minimum:

1. Supplier inventory
2. Risk-tiering methodology
3. Cybersecurity review triggers
4. Pre-contract due diligence
5. Standard evidence requirements
6. Security questionnaire requirements
7. Contractual cybersecurity clauses
8. Data-protection requirements
9. Access-control requirements
10. Breach notification requirements
11. Reassessment frequency
12. Exception and risk-acceptance process
13. Issue-remediation tracking
14. Continuous monitoring for critical suppliers
15. Secure offboarding requirements

---

## Proposed Vendor Risk Tiers

A practical model could use:

### Tier 1 — Critical

Examples:

- vendors processing highly sensitive information;
- providers with privileged access;
- critical cloud or identity services;
- providers whose outage would materially disrupt operations.

Expected review:

- full cybersecurity assessment;
- evidence review;
- contractual security requirements;
- annual reassessment;
- ongoing monitoring where feasible.

### Tier 2 — High

Examples:

- vendors processing internal business data;
- important SaaS providers;
- externally hosted business systems.

Expected review:

- structured questionnaire;
- evidence review where appropriate;
- contractual requirements;
- periodic reassessment.

### Tier 3 — Standard

Examples:

- low-data-access vendors;
- low-criticality services;
- suppliers without sensitive connectivity.

Expected review:

- baseline screening;
- minimum contractual controls;
- reassessment based on material change.

---

## Suggested Due-Diligence Evidence

Depending on vendor criticality, Northstar HealthTech may request:

- SOC 2 report;
- ISO/IEC 27001 certification;
- penetration-test summary;
- vulnerability-management information;
- incident-response capability;
- business continuity documentation;
- encryption practices;
- access-control and MFA information;
- secure-development practices;
- subprocessor information;
- breach history where relevant.

Evidence requirements should be proportionate to risk.

---

## Contractual Security Requirements

Material supplier contracts should address appropriate topics such as:

- security responsibilities;
- confidentiality;
- access control;
- encryption;
- vulnerability management;
- security incident notification;
- cooperation during investigations;
- subcontractor/subprocessor controls;
- audit or assurance rights where appropriate;
- data return and deletion;
- service continuity;
- termination responsibilities.

Legal review should be performed by appropriate qualified personnel in a real organization.

---

## Reassessment Requirements

Third-party risk should not be evaluated only during onboarding.

Reassessment should occur based on:

- supplier risk tier;
- contract renewal;
- material architecture change;
- new data access;
- security incident;
- ownership change;
- significant control deterioration;
- expansion of services.

Critical suppliers should receive the most frequent review.

---

## Offboarding Requirements

The third-party lifecycle should include secure termination.

Validation should include:

- removal of user accounts;
- removal of API keys and tokens;
- revocation of cloud access;
- removal of VPN access;
- termination of integrations;
- data return where required;
- data deletion confirmation where applicable;
- ownership transfer for retained assets;
- confirmation that residual access does not remain.

---

## Recommended Implementation Actions

### 0–30 Days

- Establish a centralized supplier inventory.
- Identify critical and high-risk suppliers.
- Define interim vendor-security ownership.
- Require security review for new high-risk suppliers.
- Document unresolved high-risk third-party issues.

### 31–90 Days

- Implement a formal vendor risk-tiering model.
- Create a standard cybersecurity questionnaire.
- Define minimum evidence requirements by tier.
- Create standard security-contract requirements.
- Establish an exception and escalation process.
- Define reassessment intervals.

### 3–12 Months

- Integrate cybersecurity review into procurement workflows.
- Implement centralized issue tracking.
- Establish recurring reassessment for critical suppliers.
- Introduce supplier-security metrics and reporting.
- Monitor material posture changes for high-risk vendors.
- Test third-party incident and continuity dependencies.

---

## Validation Criteria

This finding may be considered remediated when evidence demonstrates that:

- an authoritative supplier inventory exists;
- suppliers are risk-tiered;
- cybersecurity review is required before onboarding material suppliers;
- evidence requirements are defined by tier;
- security requirements are included in relevant contracts;
- reassessment intervals are documented;
- vendor findings and exceptions are centrally tracked;
- offboarding requirements exist;
- critical suppliers receive recurring oversight;
- management reporting is performed.

---

## Suggested Evidence After Remediation

Examples include:

- third-party risk management policy;
- supplier inventory;
- vendor risk-tiering methodology;
- completed assessment records;
- supplier questionnaires;
- assurance reports;
- contractual security clause template;
- exception register;
- remediation tracker;
- reassessment schedule;
- offboarding checklist;
- third-party risk dashboard.

---

## Priority

**High**

### Priority Rationale

Third parties can create material cyber risk without requiring direct compromise of Northstar HealthTech's own technical controls.

The organization uses external technology and SaaS providers, making consistent supplier risk governance a significant business requirement.

The finding is therefore high priority even though no specific supplier compromise is assumed.

---

## Risk Register Candidate

| Field | Value |
|---|---|
| Risk ID | RISK-003 |
| Finding | GRC-003 |
| Risk Domain | Third-Party / Supply Chain Risk |
| NIST CSF 2.0 | GV.SC |
| Likelihood | Possible |
| Impact | Major |
| Inherent Risk | High |
| Treatment | Mitigate |
| Proposed Owner | Security Leadership / Procurement |
| Status | Open |

Final numerical scoring will be assigned under the project-wide risk-scoring methodology.

---

## Consultant Perspective

Third-party cyber risk management is not simply a questionnaire exercise.

A mature lifecycle should connect:

```text
Supplier identification
        ↓
Risk tiering
        ↓
Due diligence
        ↓
Contract controls
        ↓
Onboarding
        ↓
Monitoring
        ↓
Reassessment
        ↓
Issue management
        ↓
Offboarding
```

The consulting objective is to make scrutiny proportional to risk while ensuring that critical suppliers receive consistent governance.

---

## Relationship to GRC-001 and GRC-002

GRC-001 establishes the need for an organization-wide cybersecurity risk-management strategy.

GRC-002 establishes accountability for cybersecurity responsibilities.

GRC-003 applies those governance concepts to external dependencies.

```text
GRC-001
Define how cybersecurity risk is governed
        ↓
GRC-002
Define who owns and manages that risk
        ↓
GRC-003
Extend governance to suppliers and third parties
```

---

## Final Assessment Statement

Northstar HealthTech performs selected third-party security reviews but lacks a consistently applied, risk-based cybersecurity supplier management lifecycle.

The capability is assessed at **Maturity Level 2 — Developing**, with a target of **Level 4 — Managed**.

Establishing supplier inventory, risk tiering, consistent due diligence, contractual security requirements, reassessment, issue tracking, and secure offboarding should be treated as a high-priority governance improvement.

# Article 11Z: SDOH Platform Capabilities for Work Requirement Support
## What Any Effective Platform Must Deliver

### The Platform Opportunity

Work requirements transform social determinants of health from healthcare improvement initiatives into coverage survival necessities. The member who needs transportation assistance to reach medical appointments now needs transportation to reach verification appointments. The member who needs job training to improve economic stability now needs job training to maintain healthcare coverage. The member who needs housing support to stabilize their health now needs housing documentation to prove exemption eligibility.

SDOH platforms built over the past five years to address health-related social needs suddenly become infrastructure for work requirement navigation. Platforms already connecting members to community resources, tracking referral completion, and coordinating care across organizations possess the architectural foundations for work requirement support. Extending these capabilities to verification management and exemption documentation leverages existing infrastructure rather than building parallel systems.

The opportunity is substantial. An estimated 4-6 million of the 12-14 million employed expansion adults could be served through SDOH platform partnerships with MCOs, employers, employer coalitions, and Medicaid ACOs. The market for comprehensive platform services supporting work requirement compliance reaches hundreds of millions annually.

But capturing this opportunity requires platforms to build capabilities specifically designed for the special populations examined throughout this series. Generic SDOH functionality is insufficient. Platforms must accommodate the distinct needs of people with serious mental illness, people experiencing homelessness, domestic violence survivors requiring confidentiality, limited English proficiency populations, and individuals facing multiple simultaneous barriers.

This article maps the platform capabilities required to serve these populations effectively.

---

## Part I: Core Platform Architecture

### Integrated Member Record

Effective SDOH platforms maintain unified member records integrating health status, social needs, and work requirement status. This integration enables holistic support rather than fragmented interventions.

Health status integration draws from claims data, clinical assessments, and care coordination notes. Diagnoses, medications, utilization patterns, and care gaps inform both health interventions and exemption identification. Someone with diabetes, depression, and recent hospitalization needs coordinated support addressing health management, mental health treatment, and medical exemption documentation simultaneously.

Social needs documentation captures housing stability, food security, transportation access, employment status, caregiving responsibilities, and other factors affecting both health and work capacity. SDOH screening results, navigator assessments, and service utilization history create comprehensive social profiles.

Work requirement status tracks verification compliance, exemption status, deadline proximity, documentation gaps, and historical patterns. Real-time status visibility enables proactive intervention before coverage loss occurs.

Cross-domain analytics identifies connections between health events, social circumstances, and verification risk. Hospitalization predicts verification difficulty. Housing loss predicts exemption need. Job loss predicts hour shortfall. Integrated records enable integrated responses.

### Population Identification and Stratification

Platforms must identify special population members and stratify them for appropriate intervention intensity.

Claims-based identification flags members with diagnoses, medications, or utilization patterns suggesting special population membership. Psychiatric claims identify serious mental illness. SUD treatment claims identify substance use disorder. Prenatal claims identify pregnancy. Chronic condition claims identify potential medical frailty.

Screening-based identification captures circumstances not visible in claims. Housing instability screening identifies homelessness risk. Safety screening identifies domestic violence. Language preference identifies LEP needs. Caregiver assessment identifies caregiving burden.

Risk stratification combines identification signals with verification history and engagement patterns to classify members by intervention intensity need. Tier 1 members (10-15%) require intensive navigator support with proactive outreach. Tier 2 members (25-35%) require periodic check-ins and accessible assistance. Tier 3 members (50-65%) can self-navigate with platform tools and occasional support.

Dynamic reclassification adjusts tier assignment based on changing circumstances. Hospitalization elevates risk tier. Successful verification reduces risk tier. Life events trigger reassessment.

### Closed-Loop Referral Management

SDOH platforms must track referrals from identification through service completion with accountability at each step.

Referral initiation captures member need, service type, geographic constraints, and urgency. Automated matching identifies appropriate community resources based on member characteristics and service availability. Referral tracking monitors acceptance, scheduling, attendance, and completion. Platforms should distinguish between referrals accepted but not scheduled, scheduled but not attended, attended but not completed, and fully completed.

Outcome documentation captures service results and member status changes. Did the job training program lead to employment? Did the housing assistance lead to stable housing? Did the exemption navigation lead to approved exemption?

Accountability loops escalate stalled referrals. If a referral is not accepted within 48 hours, the navigator receives an alert. If an appointment is not scheduled within one week, the care coordinator receives notification. If service is not completed within expected timeframe, a supervisor receives escalation. Closed-loop confirmation verifies with members that referred services were received and helpful.

---

## Part II: Work Requirement-Specific Capabilities

### Verification Deadline Management

Platforms must track verification deadlines and drive proactive intervention before deadlines pass.

Deadline visibility displays current month status, days remaining, hours verified, and hours needed. Visual progress indicators help members and navigators understand compliance trajectory. Predictive alerts identify members unlikely to meet deadlines based on current pace. Someone with 30 hours verified on day 20 of the month needs intervention. Alert triggers navigator outreach offering assistance.

Multi-source aggregation consolidates verification from employer submissions, gig platform data, educational enrollment, volunteer hour logs, and self-reported activities. A single dashboard shows total hours regardless of source. Grace period tracking monitors cure periods allowing late documentation submission. Historical pattern analysis identifies members with recurring verification difficulties, distinguishing between those who need permanent support intervention and those experiencing one-time disruption.

### Exemption Documentation Workflow

Platforms must support exemption identification, documentation, submission, and renewal.

Exemption screening helps members and navigators identify potentially applicable exemptions. Guided questionnaires surface exemption categories matching member circumstances. Plain-language explanations clarify eligibility criteria. Documentation checklists specify required materials for each exemption type. Medical exemptions require provider attestation. Caregiving exemptions require care recipient documentation. Circumstantial exemptions require situation verification.

Document collection enables upload from multiple sources: member smartphone camera capture, navigator-assisted scanning, provider portal submission, employer verification letters, and third-party intermediary attestations. Submission tracking monitors exemption application status from submission through determination. Renewal management tracks exemption expiration dates and initiates renewal processes before expiration.

### Resource Matching for Qualifying Activities

Platforms must connect members to activities counting toward work requirements: employment services including job boards, staffing agencies, and employer partnerships filtered by location, schedule flexibility, transportation accessibility, and physical requirements matching member capacity; job training programs including vocational training, certification programs, and apprenticeships where enrollment verification automatically reports to state systems; educational opportunities including GED programs, ESL classes, community college enrollment, and online learning with automated attendance reporting; volunteer opportunities matching member skills, interests, and schedule constraints with verified hour documentation; and job search activity tracking for members meeting requirements through active job search.

---

## Part III: Population-Specific Platform Capabilities

### For Serious Mental Illness Populations

Platforms serving SMI populations require simplified interfaces with large text, minimal steps, and clear visual guidance, plus progress saving allowing completion across multiple sessions. Crisis detection must identify distress signals in member communications with automated escalation to human navigators. Peer specialist integration enables peer navigators to manage caseloads within the platform with workflows emphasizing engagement over task completion. Symptom-aware scheduling avoids outreach during typical high-symptom periods. Hospitalization triggers automatically initiate exemption processes when psychiatric hospitalization claims appear.

### For Substance Use Disorder Populations

Platforms serving SUD populations require enhanced privacy protections exceeding standard HIPAA requirements, with separate consent for SUD information sharing and audit trails specific to 42 CFR Part 2 data. Treatment program integration enables treatment facilities to verify enrollment without disclosing treatment details. Recovery stage awareness recognizes that early recovery requires different support than sustained recovery. Relapse accommodation maintains engagement when members relapse rather than terminating support, with rapid exemption reinstatement when members re-enter treatment. Peer recovery specialist workflows support PRSS caseload management.

### For Homeless Populations

Platforms serving homeless populations must accommodate address instability, device limitations, and intermittent connectivity. Alternative contact methods accept shelter addresses, "care of" designations, and community organization contact points. HMIS integration enables automatic exemption identification when members appear in homeless management information systems. Offline functionality allows navigators to collect information during street outreach without connectivity. Kiosk compatibility enables platform access from shelter and library kiosks. Day labor verification accepts self-attestation for cash economy work with appropriate audit sampling.

### For Domestic Violence and Confidentiality Populations

Platforms serving DV populations require sealed record capability hiding employer information, addresses, and other location-revealing data from standard access. Confidential address integration with state Safe at Home programs substitutes addresses throughout platform records. Alternative verification pathways support redacted documentation, third-party intermediary verification, and self-attestation under penalty of perjury. DV advocate integration enables credentialed advocates to submit exemption attestations. Safety-aware communication avoids messages that could be discovered by abusers.

### For Limited English Proficiency Populations

Platforms serving LEP populations require multilingual interfaces with full functionality in threshold languages, not just translated text but culturally adapted workflows. In-language navigation connects LEP members with navigators sharing their language. Interpreter integration enables three-way communication when bilingual navigators are unavailable. Simplified communication uses plain language at fifth-grade reading level. Community organization intermediary workflows enable trusted organizations to submit verification and exemptions on a member's behalf with appropriate consent.

### For Geographic and Digital Isolation Populations

Platforms serving rural and digitally isolated populations must accommodate connectivity and access limitations through low-bandwidth functionality, offline capability for field navigators, telephonic access providing full functionality through phone calls, community hub integration with libraries and community centers, and seasonal work accommodation supporting annual hour averaging and seasonal verification patterns.

### For Caregiving Populations

Platforms serving caregivers require documentation of both caregiver and care recipient circumstances. Caregiver assessment captures caregiving intensity, care recipient needs, and caregiver capacity for additional activities. Care recipient documentation coordinates with care recipient providers to obtain needs verification. Respite resource matching connects caregivers to services enabling work requirement compliance during respite periods. Kinship care accommodation supports grandparents, aunts, uncles, and other kinship caregivers with documentation pathways not requiring formal custody.

### For Intersectional Populations

Platforms serving members with multiple simultaneous barriers require total burden assessment evaluating cumulative barrier load rather than individual barriers separately. Single navigator assignment provides continuity across all barrier domains. Barrier interaction mapping understands how barriers compound: mental health symptoms worsen during housing instability, housing instability increases during coverage gaps, coverage gaps result from verification failures caused by mental health symptoms. Breaking the cycle requires addressing interactions, not individual barriers. Permanent supported status identifies members whose barrier combinations make standard compliance permanently unrealistic.

---

## Part IV: Integration Requirements

### MCO Care Management Integration

SDOH platforms must integrate with MCO care management systems through bi-directional data exchange sharing member status, referral activity, and outcomes. MCO care coordinators see SDOH platform activity; SDOH navigators see MCO care coordination status. Referral coordination enables MCOs to refer members to platform support and receive outcome confirmation. Risk score sharing informs both clinical risk stratification and platform intervention prioritization. Alert integration notifies care coordinators when members face elevated coverage loss risk.

### State Eligibility System Integration

Platforms must connect to state Medicaid eligibility systems for verification submission enabling platform-facilitated submission directly to state systems, real-time status queries showing current compliance without requiring state system access for every navigator, exemption application submission with required documentation attached, and determination notification receiving approval, denial, and appeal outcomes.

### Provider System Integration

Platforms should connect to provider systems through exemption attestation requests routed to appropriate providers, clinical data access informing exemption eligibility assessment, and care gap coordination connecting work requirement navigation with clinical care management.

### Employer and Payroll Integration

Platforms should facilitate employer verification through payroll processor connections enabling automated verification, employer portals providing simple submission interfaces, and gig platform integration pulling earnings and activity data.

### Community Organization Integration

Platforms must connect to community organizations through CBO case management integration, credentialed intermediary management tracking authorized verification submitters, and service capacity visibility showing real-time availability of community resources.

---

## Part V: Navigator Workforce Tools

Navigators require dashboard views showing all assigned members with status indicators, upcoming deadlines, pending tasks, and priority rankings. Task queues organize work by urgency, member tier, and task type. Communication tools enable multi-channel outreach from a single interface with documentation of all contacts.

Mobile field tools provide smartphone access to full caseload management, document capture through camera scanning, offline functionality for areas without connectivity, and GPS integration for route planning during community outreach.

Supervision and quality tools give managers visibility into navigator performance through dashboards, case review capability, and escalation management for complex situations requiring supervisor involvement.

---

## Part VI: Analytics and Reporting

Operational analytics must track volume metrics (members served, referrals made, verifications facilitated, exemptions processed), timeliness metrics (time from need identification to intervention), success metrics (coverage retention rates, exemption approval rates), and efficiency metrics (cost per member served, navigator productivity).

Population analytics enable understanding of demographic stratification showing outcomes by race, ethnicity, language, and geography for disparity identification. Barrier pattern analysis identifies common barrier combinations and their coverage retention implications. Service utilization patterns reveal which resources members use, decline, and find effective.

Outcome tracking demonstrates value through coverage retention comparing platform-served members versus comparison populations, health outcomes tracking utilization and care gap closure, economic outcomes measuring employment and earnings changes, and ROI calculation connecting platform investment to prevented coverage loss and improved health outcomes.

---

## Part VII: Privacy, Security, and Compliance

Platforms handling sensitive member information require encryption protecting data in transit and at rest (TLS 1.3, AES-256), access controls limiting data visibility based on role and need, audit trails logging all data access, and breach protocols defining response procedures.

Regulatory compliance spans HIPAA including Business Associate Agreements and security rule implementation, 42 CFR Part 2 compliance for substance use disorder information with enhanced consent requirements, and state-specific requirements addressing varying privacy laws and Medicaid regulations.

Consent management must ensure informed consent so members understand data collection and use, granular permissions allowing selective authorization, and consent revocation enabling members to withdraw consent with appropriate data handling.

---

## Conclusion: Platform as Infrastructure

SDOH platforms represent essential infrastructure for work requirement implementation that serves rather than excludes special populations. The capabilities mapped in this article enable platforms to identify members needing support, provide appropriate interventions matched to population-specific needs, track outcomes demonstrating value, and integrate with the broader ecosystem of MCOs, providers, employers, and community organizations.

Building these capabilities requires investment beyond generic SDOH functionality. Population-specific accommodations for serious mental illness, substance use disorder, homelessness, domestic violence, limited English proficiency, and intersectional circumstances demand intentional design. Integration requirements connecting platforms to state systems, MCO platforms, provider EHRs, and community organizations demand technical development and partnership negotiation.

The platforms that build these capabilities will capture significant market opportunity while delivering genuine value to vulnerable populations. Those that treat work requirement support as an afterthought will fail both commercially and ethically. The December 2026 implementation deadline creates urgency. The populations at stake create imperative.

---

## References

1. KLAS Research. "SDOH Platform Market Analysis." KLAS Report, 2024.

2. Gravity Project. "Social Determinants Data Exchange Standards." Gravity Implementation Guide, 2024.

3. Centers for Medicare and Medicaid Services. "SDOH and Medicaid Managed Care." CMS Guidance, 2024.

4. Kaiser Family Foundation. "SDOH Initiatives in Medicaid Managed Care." KFF Report, 2024.

5. National Association of Community Health Centers. "SDOH Platform Integration." NACHC Implementation Guide, 2024.

6. Healthcare Information and Management Systems Society. "Interoperability for SDOH." HIMSS Standards Guide, 2024.

7. Robert Wood Johnson Foundation. "Technology-Enabled Social Care." RWJF Report, 2024.

8. Center for Health Care Strategies. "Closed-Loop Referral Systems." CHCS Brief, 2024.

9. California Health Care Foundation. "SDOH Platforms in Medi-Cal." CHCF Analysis, 2024.

10. Commonwealth Fund. "Community Health Worker Integration." Commonwealth Report, 2024.

11. National Council for Mental Wellbeing. "Behavioral Health SDOH Integration." National Council Guide, 2024.

12. SAMHSA. "42 CFR Part 2 and Care Coordination." SAMHSA Technical Assistance, 2024.

13. National Domestic Violence Hotline. "Technology Safety in SDOH Platforms." NDVH Guide, 2024.

14. Migration Policy Institute. "Language Access in Digital Platforms." MPI Report, 2024.

15. National Alliance to End Homelessness. "HMIS Integration Standards." NAEH Guide, 2024.

16. Office of the National Coordinator. "Social Care Referral Standards." ONC Guidance, 2024.

17. Medicaid and CHIP Payment and Access Commission. "SDOH in Medicaid." MACPAC Report, 2024.

18. Herd, Pamela and Donald Moynihan. *Administrative Burden: Policymaking by Other Means.* Russell Sage Foundation, 2018.

19. Urban Institute. "Projected Coverage Losses Under Medicaid Work Requirements." Multiple state analyses, 2024-2025.

20. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts." *Health Affairs* 39, no. 9 (2020): 1524-1532.

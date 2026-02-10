# Article 11Y: The Technology Architecture for Work Requirement Implementation
## Capabilities Required Across All Stakeholders and Populations

### The System Design Challenge

Technology cannot solve work requirements. But technology designed poorly guarantees failure. Arkansas demonstrated this reality when 18,000 people lost coverage in seven months, with research showing most losses occurred among people who were working or qualified for exemptions but couldn't navigate the documentation process. The technology existed. The design failed the populations it served.

The 18.5 million expansion adults facing work requirements include populations whose circumstances demand technology accommodations that standard systems don't provide. People experiencing homelessness lack stable addresses for correspondence and devices for portal access. People with serious mental illness face cognitive barriers to multi-step processes during symptom exacerbation. People with limited English proficiency cannot navigate English-only interfaces. People in rural areas lack broadband for document upload. People working cash economy jobs have no employer systems generating automatic verification.

This article maps technology capabilities required across all stakeholders: state eligibility systems, MCO platforms, provider EHR integration, employer verification systems, community organization tools, and member self-service interfaces. The organization follows capability domains rather than populations, recognizing that effective technology serves multiple populations through common infrastructure designed for accessibility and flexibility.

---

## Part I: State Eligibility System Capabilities

State Medicaid eligibility systems form the foundation. Every other stakeholder's technology connects to state systems for verification submission, exemption processing, and eligibility determination.

### Core Processing Infrastructure

**Verification intake and processing:** Systems must accept verification from multiple sources through multiple channels. Employer API feeds providing automated hour reporting. Provider portal submissions for exemption attestations. Member portal uploads for self-reported activities. Community organization submissions on member behalf. Paper document processing for populations unable to use digital channels. Each channel requires intake validation, document classification, data extraction, and routing to appropriate processing queues.

**Exemption management:** Exemption processing requires category assignment, duration tracking, renewal scheduling, and transition logic. Systems must handle exemption stacking when members qualify under multiple categories simultaneously. Automatic exemption triggers based on claims data, enrollment data, or external system feeds reduce documentation burden for predictable exemptions.

**Compliance calculation:** Monthly hour aggregation across multiple activity types and verification sources. Quarterly and annual averaging options for seasonal workers. Grace period tracking for members approaching non-compliance. Cure period management allowing documentation submission after initial deadline.

**Appeals and fair hearing integration:** When members contest determinations, systems must support appeal filing, evidence submission, hearing scheduling, and decision implementation. Appeal status must remain visible to all stakeholders supporting the member.

### Automation and Triggers

**Claims-based automatic exemptions:** Delivery claims trigger postpartum exemption. Psychiatric hospitalization claims trigger mental health exemption. SUD treatment claims trigger treatment exemption. Dialysis claims trigger medical frailty exemption. Cancer treatment claims trigger treatment exemption. Automation based on claims data eliminates documentation burden for exemptions the system can identify without member action.

**External data integration:** SSI/SSDI receipt from Social Security Administration triggers automatic disability exemption. Unemployment insurance claims trigger job search activity credit. Incarceration data from corrections systems triggers suspension during incarceration and exemption post-release. HMIS data from homeless service systems triggers homelessness exemption. Child welfare data identifies kinship caregivers. Each integration requires data sharing agreements, technical specifications, and privacy protections.

**Predictive flagging:** Algorithms identifying members at risk of coverage loss based on verification patterns, claims history, and demographic factors. Flagged members receive proactive outreach rather than waiting for non-compliance.

### Multi-Channel Access

**Web portal:** Responsive design functioning on desktop, tablet, and smartphone browsers. Accessibility compliance with WCAG 2.1 AA standards. Session timeout accommodations for users with cognitive processing delays. Progress saving allowing multi-session completion.

**Mobile application:** Native iOS and Android applications with offline functionality for users with intermittent connectivity. Camera integration for document capture. Push notifications for deadline reminders and status updates.

**Telephonic access:** Interactive voice response for status checking and simple submissions. Live agent support for complex situations. Interpretation services for 200+ languages.

**Paper processing:** Document scanning and OCR for paper submissions. Mail processing infrastructure. Return address options including shelter addresses and "care of" designations.

**In-person access:** Kiosk deployment at libraries, community centers, and shelter locations. Field worker mobile access for home visits and street outreach.

### Multilingual and Accessibility Features

**Language support:** Full translation of interfaces and communications into threshold languages (those spoken by 5%+ of population). Real-time translation for additional languages. Simplified English option at fifth-grade reading level.

**Accessibility:** Screen reader compatibility. Keyboard navigation. High contrast and large text options. Video content with captions and audio description. Cognitive accessibility features including simplified workflows and visual progress indicators.

**Alternative formats:** Audio notices for literacy-limited populations. Video explanations with sign language interpretation. Pictographic instructions for complex processes.

---

## Part II: MCO Care Management Platform Capabilities

MCO platforms serve as coordination hubs, connecting member health status with verification status and enabling proactive intervention.

### Risk Stratification and Analytics

**Multi-factor risk scoring:** Algorithms combining claims data (diagnoses, medications, utilization patterns), enrollment data (address stability, coverage history), SDOH screening results, and work requirement compliance history to identify members at elevated coverage loss risk.

**Population segmentation:** Tiered classification enabling appropriate resource allocation. Tier 1 (intensive support): 10-15% of members requiring dedicated care coordinator attention. Tier 2 (moderate support): 25-35% requiring periodic check-ins. Tier 3 (self-service adequate): 50-65% capable of independent navigation with system support.

**Disparity detection:** Analytics identifying coverage retention disparities by race, ethnicity, language, geography, and disability status. Early warning when specific populations show elevated loss rates requiring intervention.

**Predictive modeling:** Machine learning models forecasting coverage loss 30-60-90 days in advance based on verification patterns, claims utilization, and engagement indicators. Predictions drive proactive outreach before deadlines pass.

### Care Coordinator Workflow Integration

**Unified dashboard:** Single interface displaying clinical status (diagnoses, medications, care gaps), social status (SDOH screening results, active referrals), and administrative status (verification compliance, exemption status, upcoming deadlines). Care coordinators address health and coverage needs in integrated interactions.

**Task management:** Automated task creation based on deadline proximity, risk score changes, and claims events. Task routing to appropriate team members based on expertise and caseload. Escalation pathways for complex situations.

**Communication tools:** Multi-channel outreach (phone, text, email, portal message) from single interface. Communication templates for common scenarios. Translation integration for LEP members. Documentation of all member contacts.

**Exemption facilitation:** Workflows enabling care coordinators to initiate exemption applications, coordinate provider documentation, upload supporting materials, and submit to state systems on member behalf with appropriate authorization.

### Provider and Community Integration

**Provider collaboration:** Secure messaging with network providers. Exemption attestation requests routed to appropriate providers. Status visibility for pending attestations. Escalation for delayed documentation.

**Community referral management:** Closed-loop referral tracking from identification through service completion. Integration with SDOH platforms (Unite Us, findhelp, Aunt Bertha) for community resource matching. Outcome documentation for referred services.

**HMIS integration:** Data feeds from homeless management information systems identifying members experiencing homelessness. Automatic exemption triggering and specialized care coordination assignment.

---

## Part III: Provider EHR Integration Capabilities

Providers complete exemption attestations that determine whether members maintain coverage. EHR integration reduces provider burden while ensuring timely documentation.

### Attestation Workflow Integration

**In-workflow attestation:** SMART on FHIR applications launching within clinical workflows. Providers see patients needing exemption documentation during routine care. Pre-populated forms with relevant clinical data. Digital signature within EHR. Submission without leaving clinical workflow.

**Attestation queue management:** Dashboard showing pending attestation requests prioritized by deadline urgency. Batch processing capability for providers with high Medicaid volumes. Delegation to clinical support staff where scope of practice permits.

**Template standardization:** Checkbox-based attestation forms replacing narrative letters. Functional capacity assessment templates. Condition-specific templates for common exemption scenarios. Target completion time under five minutes per attestation.

### Clinical Decision Support

**Exemption eligibility alerts:** EHR alerts when patients with exemption-qualifying conditions have upcoming verification deadlines. Prompts during clinical encounters to complete attestation.

**Documentation prompts:** Reminders to document functional capacity during visits for patients with chronic conditions. Structured data capture enabling automated exemption form population.

**Care gap integration:** Exemption documentation as care gap alongside clinical care gaps. Quality reporting including exemption completion rates.

### Provider Portal Alternative

**Standalone portal:** Web-based attestation interface for providers without EHR integration capability. Single sign-on with state provider credentialing systems. Mobile-responsive design for completion on tablets during patient encounters.

**Batch processing:** Upload capability for practices completing multiple attestations. CSV template for structured data submission.

---

## Part IV: Employer Verification System Capabilities

Employers provide work hour verification for members meeting requirements through employment. System design determines whether verification creates administrative burden or operates seamlessly.

### Automated Integration Tiers

**Tier 1: Payroll processor integration:** Direct API connections with major payroll processors (ADP, Paychex, Gusto, Paycor). Automated verification for all employees of all employers using integrated processors. Zero employer action required. Estimated coverage: 40-50% of employed expansion adults.

**Tier 2: Large employer direct integration:** API connections with large employers (5,000+ employees) having sophisticated HR systems. Employer IT configures connection; verification flows automatically. Bulk verification for entire workforce.

**Tier 3: Employer portal:** Web and mobile interface for employers without integration capability. Simple submission requiring employer name, employee name, pay period, hours worked. Bulk upload for multiple employees. Target completion time under two minutes per employee.

**Tier 4: Navigator-assisted:** For employers unwilling or unable to submit directly. Navigators collect verification information (pay stubs, employer letters) and submit on member behalf with authorization.

### Small Employer Accommodations

**Simplified attestation:** One-page employer letter template. Checkbox confirmation of employment and approximate hours. No detailed payroll documentation required.

**Industry association portals:** Sector-specific portals (restaurant association, retail federation, construction trades) enabling small employers to submit through familiar industry channels.

**Telephonic verification:** Employer call-in option for businesses without internet access. Recorded verification with employer callback confirmation.

### Gig Platform Integration

**Platform API connections:** Direct integration with major gig platforms (Uber, Lyft, DoorDash, Instacart, Amazon Flex). Automated reporting of earnings and estimated hours.

**Earnings-to-hours conversion:** Standardized formulas converting platform earnings to hour equivalents when platforms report earnings but not hours.

**Multi-platform aggregation:** Consolidated verification for workers using multiple platforms. Single compliance calculation across all gig income sources.

---

## Part V: Community Organization and Navigator Tools

Community organizations extend reach into populations distrustful of institutional healthcare. Navigator tools must accommodate organizations with limited technical capacity.

### Case Management Integration

**Referral receipt and tracking:** Integration with MCO and provider referral systems. Automatic caseload assignment based on navigator expertise and capacity. Service documentation within existing case management workflows.

**Member status visibility:** Read access to verification status, exemption status, and upcoming deadlines for members served. Alerts when assigned members approach compliance risk.

**Outcome documentation:** Structured capture of navigation activities and outcomes. Closed-loop confirmation when referred services complete.

### Navigator Mobile Application

**Field-ready design:** Mobile-first application functioning on basic smartphones. Offline capability for areas without reliable connectivity. Data synchronization when connectivity restores.

**Document capture:** Camera integration for photographing member documents. Automatic upload to appropriate systems with member consent.

**Member lookup:** Search by name, date of birth, or Medicaid ID. Display of member status and navigation needs.

**Activity logging:** Quick documentation of member contacts, services provided, and outcomes achieved.

### Minimal Technical Requirements

**Low-bandwidth functionality:** Core functions operating on 3G connections. Image compression for document uploads. Text-based alternatives to video content.

**Basic device compatibility:** Functionality on devices three or more years old. No requirement for latest operating system versions.

**Simple authentication:** Single sign-on reducing password management burden. Biometric authentication option where available.

---

## Part VI: Member Self-Service Capabilities

Members who can self-navigate should have tools enabling independent compliance without navigator assistance. Design must accommodate diverse literacy levels, language preferences, and device access.

### Verification Submission

**Document upload:** Camera-based capture of pay stubs, employer letters, and other verification documents. Automatic document classification. Quality checking with re-capture prompts for illegible images.

**Self-attestation:** Structured forms for reporting work hours, volunteer activities, job search efforts, and educational enrollment. Clear guidance on what activities qualify. Submission confirmation with reference numbers.

**Status dashboard:** Real-time display of current month hours, verification submissions, and compliance status. Visual progress indicators. Days remaining until deadline.

### Exemption Self-Service

**Eligibility screening:** Guided questionnaire helping members identify potentially applicable exemptions. Plain-language explanations of each exemption category.

**Application initiation:** Online exemption applications with required documentation checklist. Upload capability for supporting documents. Submission to navigator or care coordinator for complex applications.

**Renewal reminders:** Push notifications and text messages before exemption expiration. One-click renewal initiation for unchanged circumstances.

### Accessibility and Inclusion

**Multilingual interface:** Full functionality in threshold languages. Language selection persistent across sessions. In-language customer support access.

**Literacy accommodations:** Video tutorials explaining processes. Audio-enabled form completion. Visual icons supplementing text instructions. Fifth-grade reading level for all text content.

**Device flexibility:** Full functionality on smartphones, tablets, and computers. Feature phone access via SMS for basic functions. Kiosk access at public locations for members without personal devices.

**Cognitive accessibility:** Simplified workflows with minimal steps. Progress saving and session restoration. Clear error messages with remediation guidance. Chat support for real-time assistance.

---

## Part VII: Caregiver and Family Member Tools

Family members and informal caregivers often support members with navigation, particularly for populations with cognitive impairments, serious mental illness, or limited English proficiency.

### Authorized Representative Access

**Delegation management:** Member-controlled authorization of family members or caregivers for account access. Granular permissions (view-only, submission authority, full access). Easy revocation when circumstances change.

**Caregiver dashboard:** Separate login for authorized representatives. Clear indication of acting on member's behalf. Audit trail of all caregiver actions.

**Multi-member management:** Single caregiver interface for family members supporting multiple Medicaid members. Consolidated deadline tracking and status display.

### Supported Decision-Making Tools

**Guided completion:** Step-by-step workflows with explanations appropriate for members needing support. Pause-and-resume capability for completing forms across multiple sessions.

**Explanation resources:** Plain-language explanations of verification requirements, exemption categories, and consequences of non-compliance. Video content with captions.

**Care coordinator connection:** Easy escalation to human support when self-service proves insufficient. Warm handoff preserving context from self-service session.

### Guardian and Representative Payee Integration

**Legal authority documentation:** Upload capability for guardianship orders, power of attorney, and representative payee designations. Verification workflow for legal authority claims.

**Guardian-specific features:** Batch management for guardians serving multiple individuals. Reporting capabilities for organizational guardians. Integration with guardianship management systems.

---

## Part VIII: Interoperability and Data Standards

Effective technology requires seamless data exchange across stakeholders. Standards enable integration; proprietary systems create barriers.

### Data Exchange Standards

**FHIR (Fast Healthcare Interoperability Resources):** Standard for health data exchange between providers, MCOs, and other healthcare entities. FHIR-based APIs for clinical data access and exemption documentation.

**Work verification schema:** Standardized format for employment verification across different state systems. Common data elements enabling multi-state employer reporting.

**SDOH data standards:** Common vocabulary for documenting social determinants, barriers, interventions, and outcomes. Gravity Project standards for SDOH screening and referral.

### API Standards

**RESTful APIs:** Standard protocol for system-to-system communication. Published API documentation enabling third-party integration.

**OAuth 2.0 authorization:** Standard for delegating access rights across systems. Consent management enabling member-controlled data sharing.

**Webhook notifications:** Real-time alerts when status changes. Deadline approaching notifications. Exemption approval confirmations.

### Identity and Security

**Identity verification:** Secure, privacy-preserving identity management across systems. Multi-factor authentication options. Biometric authentication where appropriate.

**HIPAA compliance:** All health data exchange following HIPAA security and privacy requirements. Business associate agreements with all data partners.

**Audit trails:** Comprehensive logging of all data access and system actions. Tamper-proof records for compliance and fraud investigation.

**Role-based access:** Granular permissions ensuring users access only information necessary for their role. Elevated access restrictions for confidential records.

---

## Part IX: Privacy and Confidentiality Protections

Special populations require privacy protections beyond standard HIPAA compliance. Technology must enable confidentiality while supporting verification.

### Confidential Record Management

**Sealed records:** Ability to seal employer information, addresses, and other sensitive data from routine access. Elevated permission requirements for sealed record access. Audit logging of all sealed record access.

**Confidential address programs:** Integration with state Safe at Home programs substituting confidential addresses in all records. System-wide address substitution preventing inadvertent disclosure.

**Redacted verification:** Support for verification documents with employer identification redacted. Alternative verification pathways for confidentiality-protected members.

### Population-Specific Protections

**42 CFR Part 2 compliance:** Enhanced protections for substance use disorder treatment records. Consent management for SUD information sharing. Audit trails specific to Part 2 data.

**Domestic violence protections:** Location information firewalls. Abuser cannot access member information through system compromise. Alert protocols if unauthorized access attempted.

**Immigration firewalls:** Work requirement data not shared with immigration enforcement. Clear separation between Medicaid eligibility and immigration status verification.

---

## Part X: Implementation Priorities and Timeline

Technology capabilities must be phased based on implementation timeline and resource constraints.

### Pre-Implementation (2025-2026)

**State systems:** Basic verification portals, exemption submission, eligibility database enhancement. Minimum viable functionality for December 2026 launch.

**MCO platforms:** Risk stratification models, care coordinator dashboards, basic member portals. Integration with state systems for status visibility.

**Provider systems:** Standalone attestation portals. EHR integration for early adopters only.

**Employer systems:** Large employer API connections. Basic employer portal. Payroll processor partnerships initiated.

### Year One (2027)

**State systems:** Enhanced automation based on implementation learning. Expanded external data integration. Analytics for disparity identification.

**MCO platforms:** Refined risk models based on outcomes data. Enhanced community integration. Predictive analytics deployment.

**Provider systems:** Broader EHR integration. Template refinement based on provider feedback.

**Employer systems:** Expanded payroll processor coverage. Gig platform integration. Small employer accommodations.

### Ongoing Enhancement (2028+)

**Advanced analytics:** Machine learning for intervention optimization. Natural language processing for document classification. Predictive modeling refinement.

**Agentic AI capabilities:** Verification coordination agents gathering data across sources. Exemption documentation agents pre-populating forms. Resource matching agents connecting members to services.

**Continuous improvement:** User experience refinement based on member feedback. Accessibility enhancement. Performance optimization.

---

## Conclusion: Technology as Enabler, Not Solution

Technology enables work requirement implementation at scale. Without automated verification, 18.5 million monthly compliance determinations would overwhelm any administrative system. Without integrated care coordination, MCOs couldn't identify members needing support before coverage loss occurs. Without accessible member tools, populations lacking digital fluency would face systematic exclusion.

But technology cannot substitute for human infrastructure. The member with serious mental illness needs a peer specialist who understands their experience, not an algorithm optimizing outreach timing. The domestic violence survivor needs an advocate who can safety plan, not a chatbot offering resources. The person experiencing homelessness needs a street outreach worker who builds trust over months, not a kiosk at a shelter they may not visit.

The technology architecture mapped here provides the foundation for work requirement implementation that serves special populations rather than excluding them. State systems that accept verification through multiple channels. MCO platforms that identify risk before failure occurs. Provider tools that reduce attestation burden. Employer systems that automate verification for those with formal employment while accommodating those without. Community organization tools that extend reach into populations distrustful of institutions. Member interfaces accessible to people with diverse abilities, languages, and circumstances.

Building this architecture requires investment, coordination, and sustained attention to populations whose needs differ from system design assumptions. States that build minimum viable systems will experience coverage loss concentrated among special populations. States that build inclusive systems will demonstrate that work requirements can function without systematic exclusion of vulnerable people.

The technology choices made in the next 14 months will determine outcomes for millions. Those choices deserve the same attention given to policy design and stakeholder coordination.

---

## References

1. Centers for Medicare and Medicaid Services. "Medicaid Information Technology Architecture." CMS Technical Guidance, 2024.

2. Office of the National Coordinator for Health IT. "Interoperability Standards for Health Information Exchange." ONC Guidance, 2024.

3. HL7 International. "FHIR Implementation Guide for Social Determinants of Health." HL7 Standards, 2024.

4. Gravity Project. "Social Determinants of Health Data Standards." Gravity Implementation Guide, 2024.

5. Healthcare Information and Management Systems Society. "Digital Health Equity Framework." HIMSS Report, 2024.

6. Web Content Accessibility Guidelines. "WCAG 2.1 AA Standards." W3C Recommendation, 2018.

7. Sommers BD, et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts." Health Affairs. 2020;39(9):1524-1532.

8. Government Accountability Office. "Medicaid IT Systems: Modernization Challenges." GAO Report, 2024.

9. National Association of Medicaid Directors. "State Medicaid Technology Priorities." NAMD Survey, 2024.

10. Center for Health Care Strategies. "Technology-Enabled Care Coordination." CHCS Brief, 2024.

11. California Health Care Foundation. "Digital Equity in Medicaid." CHCF Report, 2024.

12. Robert Wood Johnson Foundation. "Technology and Health Equity." RWJF Issue Brief, 2024.

13. National Council for Mental Wellbeing. "Behavioral Health Technology Standards." National Council Report, 2024.

14. National Domestic Violence Hotline. "Technology Safety for Survivors." NDVH Guide, 2024.

15. Migration Policy Institute. "Language Access in Digital Government Services." MPI Report, 2024.

16. Federal Communications Commission. "Broadband Deployment Report." FCC, 2024.

17. Pew Research Center. "Digital Divide and Internet Adoption." Pew Report, 2024.

18. SAMHSA. "42 CFR Part 2 Implementation Guidance." SAMHSA Technical Assistance, 2024.

19. Office for Civil Rights. "HIPAA Security Rule Guidance." HHS OCR, 2024.

20. Congressional Budget Office. "Technology Costs for Medicaid Work Requirements." CBO Report, 2024.

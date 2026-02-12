---
title: "Technology Governance"
date: 2026-08-18
author: "Syam Adusumilli"
summary: "Accountability Frameworks for AI and Robotics in Healthcare"
description: "RHTP Series 15: Technology Governance"
tags: ["rural-health", "rhtp", "state-policy", "series-15"]
categories: ["Rural Health Transformation"]
series: ["Series 15: Regulatory and Workforce"]
showtoc: true
tocopen: false
ShowReadingTime: true
ShowWordCount: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
  image: "cover.webp"
  alt: "Technology Governance"
  relative: true
  hidden: false
params:
  article_id: "RHTP-15C"
  article_type: "article"
  series_number: 15
  series_title: "Regulatory and Workforce"
  summary_url: "../technology-governance-summary/"
  collection: "rural-health"
---

Alternative architecture depends on technologies that have **no governance framework**. AI companions that monitor elderly patients and detect emergencies. Clinical decision support that triages patients and recommends treatments. Robotic systems that assist with care delivery. Legal and financial AI that provides services to rural residents who cannot access human professionals. Each technology central to Series 14's vision operates in regulatory uncertainty that deters beneficial deployment while failing to prevent harmful applications.

The governance gap is not an oversight. It reflects the difficulty of regulating technologies that do not fit existing categories. AI clinical decision support is not clearly the practice of medicine, but it influences medical decisions. AI companions are not medical devices, but they monitor health. Robots that assist elderly patients are not subject to healthcare facility standards, but they operate in healthcare settings. The regulatory frameworks designed for pharmaceuticals, medical devices, and professional practice do not map cleanly onto AI and robotic systems.

Rural communities cannot wait for perfect governance. They face **immediate access crises** that technology could address. But they also cannot deploy technology without accountability frameworks that protect patients, allocate liability, and maintain community trust. Building these frameworks is an enabling condition for the alternative architecture that Series 14 describes.

## The Barrier Inventory

Technology governance gaps span five domains: clinical AI, companion systems, robotic care, AI professional services, and algorithmic resource allocation. Each domain presents distinct challenges requiring tailored governance approaches.

### Clinical AI Governance Gaps

**Clinical artificial intelligence** includes systems that analyze medical data, suggest diagnoses, recommend treatments, and prioritize patient care. The FDA has approved over 1,250 AI-enabled medical devices as of July 2025, yet fundamental governance questions remain unresolved.

| AI Function | Governance Gap | Rural Impact |
|-------------|---------------|--------------|
| Diagnostic imaging | Liability allocation unclear | Radiologists hesitate to rely on AI reads |
| Clinical decision support | Practice of medicine determination pending | Hospitals uncertain about deployment authority |
| Triage algorithms | No validation standards for rural populations | Systems trained on urban data may fail rural contexts |
| Predictive analytics | Performance monitoring undefined | Drift detection responsibility unclear |
| Generative AI in clinical settings | LLM hallucination risk unaddressed | No standards for clinical text generation |

The FDA's January 2025 draft guidance on AI-enabled device software functions represents the first comprehensive framework for AI medical devices across the total product lifecycle. The guidance introduces **Predetermined Change Control Plans** allowing manufacturers to update AI systems without new submissions for anticipated modifications. But the guidance does not resolve state-level questions about whether AI providing diagnostic suggestions constitutes the practice of medicine, or who bears liability when AI recommendations prove incorrect.

**Liability uncertainty** deters deployment more than safety concerns. A rural hospital considering AI radiology assistance faces questions no insurer can clearly answer: If the AI misses a finding that a radiologist would have caught, who is liable? If the radiologist overrules the AI and misses something the AI identified, does that change the analysis? If the AI recommends against the standard of care and the physician follows the recommendation, what protection exists? These questions have no settled answers, and **liability insurance pricing reflects that uncertainty**.

The FDA's January 2026 guidance easing regulation of digital health products and AI-enabled devices signals federal movement toward lighter-touch oversight. Commissioner Marty Makary announced changes intended to "promote more innovation with AI in medical devices." But deregulation at the federal level does not resolve state-level liability and practice questions that govern physician behavior.

### AI Companion Governance Gaps

**AI companion systems** provide continuous presence, social interaction, and health monitoring for isolated individuals. Products like ElliQ and emerging systems like Lovot and Lemmy offer what rural elderly populations desperately need: connection, reminders, emergency detection, and cognitive engagement. But these systems operate in a **regulatory vacuum**.

| Companion Function | Current Status | Required Governance |
|-------------------|----------------|---------------------|
| Health monitoring | Not classified as medical device if "wellness" purpose | Clear boundary between wellness and medical |
| Emergency detection | No standards for response protocols | Required alert pathways, response times |
| Conversation and engagement | No privacy framework for continuous recording | Data ownership, retention, access rules |
| Medication reminders | Unclear liability for missed reminders | Responsibility allocation, backup systems |
| Emotional support | No standards for psychological impact | Assessment requirements, dependency monitoring |

The EU AI Act classifies AI systems by risk level, designating healthcare AI as high-risk when classified as medical devices under the Medical Device Regulation. But **companion robots often avoid medical device classification** by characterizing their purpose as social rather than therapeutic. A robot that provides "companionship" faces different regulation than one that "monitors dementia patients," even if the functionality is identical.

California became the first state to enact legislation regulating AI companion chatbots in 2025, requiring developers to implement safety protocols. This state-level action addresses concerns about emotional manipulation and dependency, particularly for vulnerable users. But **a patchwork of state regulations** complicates deployment for systems designed to serve populations across state lines.

The fundamental tension in companion governance involves **balancing protection against access**. Strict governance could prevent beneficial deployment to populations that desperately need continuous presence technology. Minimal governance could enable exploitation of vulnerable users who cannot evaluate AI system quality or protect their interests. Rural elderly populations, often living alone and cognitively declining, face maximum vulnerability to both technology absence and technology harm.

### Robotic Care Governance Gaps

**Healthcare robotics** includes systems that provide physical assistance, perform care tasks, and operate in clinical environments. Unlike industrial robots governed by workplace safety regulations, healthcare robots interact directly with patients, creating unique governance requirements.

| Robot Type | Current Regulation | Gap |
|------------|-------------------|-----|
| Surgical robots | FDA medical device clearance | Cleared for procedure, not operating room integration |
| Rehabilitation robots | Mixed FDA and fitness equipment treatment | No rural deployment standards |
| Care assistance robots | No healthcare-specific standards | Patient handling, malfunction response undefined |
| Pharmacy automation | State board oversight | Limited remote supervision authorization |
| Delivery and logistics robots | No healthcare facility standards | Infection control, patient privacy unaddressed |

The companion robot market is projected to grow from $1.26 billion in 2024 to $2.86 billion by 2030. But **scaling deployment requires governance infrastructure** that does not exist. Who certifies that a care robot is safe for patient interaction? What maintenance requirements apply? What happens when a robot malfunctions during patient care? What human oversight is required, and how can it be provided in understaffed rural facilities?

Scandinavia and Japan lead in healthcare robotics deployment, but their governance frameworks reflect **population density and professional availability** that American rural areas lack. A framework requiring constant human supervision works when staff are available; it fails when the robot is needed precisely because staff are not.

### AI Professional Services Governance Gaps

**AI legal and financial services** could address rural professional deserts where attorneys and financial advisors are unavailable. But these services face **unauthorized practice barriers** that technology governance has not addressed.

| Service | Barrier | Current Status |
|---------|---------|----------------|
| Legal information | Unauthorized practice of law concerns | No clear line between information and advice |
| Tax preparation | Professional licensing requirements | Limited AI authorization |
| Financial planning | Fiduciary duty questions | Unclear application to AI systems |
| Benefits navigation | No framework for government program guidance | Liability for incorrect eligibility determination |
| Estate planning | State-specific requirements | Multi-state AI services face compliance complexity |

Rural communities lack not only healthcare professionals but also attorneys, accountants, and financial advisors. Series 14 envisions AI systems providing these services through service centers and digital platforms. But no jurisdiction has created **safe harbors** for AI professional services that would enable deployment at scale.

The practice of law is defined by state supreme courts and bar associations. Practice without a license constitutes a criminal offense in most states. AI that tells someone "you should file for bankruptcy" may be practicing law without authorization; AI that tells someone "here is general information about bankruptcy" may not be. The **line between prohibited practice and permitted information** has never been clearly drawn, and AI systems cannot be designed around unclear boundaries.

### Algorithmic Resource Allocation Governance

**Algorithmic systems increasingly determine resource allocation** in healthcare: which patients get appointments, which receive referrals, which qualify for programs. When AI makes these decisions, governance must ensure fairness, transparency, and appeal rights.

| Allocation Decision | Algorithm Role | Governance Gap |
|--------------------|---------------|----------------|
| Appointment scheduling | Prioritization algorithms | No transparency requirements |
| Specialist referral | Triage systems | Bias testing not required |
| Program eligibility | Automated determination | Appeal rights unclear |
| Risk stratification | Population health management | Rural calibration not required |
| Resource distribution | Optimization algorithms | Equity criteria undefined |

Algorithms trained on urban populations may systematically disadvantage rural patients. A risk stratification system that predicts hospital readmission based on distance to emergency care will score rural patients higher, potentially triggering interventions that urban patients with identical health status would not receive. **No regulatory framework requires rural-specific validation** of algorithmic systems used in healthcare.

## Current Reform Landscape

Technology governance is evolving rapidly but **unevenly across jurisdictions and domains**. Some areas show substantial progress; others remain entirely unaddressed.

### Federal AI Healthcare Guidance

The FDA's 2025 draft guidance represents the most comprehensive federal framework for AI medical devices. Key elements include:

**Total Product Lifecycle Approach**: The guidance covers design, development, testing, deployment, and post-market monitoring as integrated phases requiring coordinated documentation and risk management.

**Predetermined Change Control Plans**: Manufacturers can specify anticipated modifications and implementation methods in advance, allowing updates without new submissions if changes follow the approved protocol.

**Performance Monitoring Requirements**: The FDA explicitly addresses AI performance drift, requiring manufacturers to establish monitoring systems that detect degradation over time or across populations.

**Transparency Expectations**: The guidance recommends disclosure to users about AI system capabilities, limitations, and the role of human oversight in intended use scenarios.

But the guidance is **non-binding** and focused on medical devices, leaving unaddressed the AI systems most relevant to alternative architecture: companions not classified as devices, professional services AI, and robotic systems outside medical device categories.

### State-Level AI Legislation

California's 2025 AI companion legislation establishes the first state framework addressing emotional AI risks. Key provisions require:

- Safety protocols protecting users from manipulation
- Transparency about AI nature and limitations
- Mechanisms addressing dependency and emotional harm
- Particular protections for minor users

Other states have not followed, creating concerns about **regulatory fragmentation** that could complicate deployment of systems designed for national or regional markets. The companion market cannot support 50 different compliance frameworks.

### International Frameworks

The **EU AI Act** provides the most comprehensive international framework, classifying AI systems by risk level and imposing requirements proportionate to risk. Healthcare AI classified as high-risk faces:

- Conformity assessment before deployment
- Quality management system requirements
- Transparency and documentation obligations
- Human oversight specifications
- Post-market monitoring duties

But the AI Act's interaction with the Medical Device Regulation creates **compliance complexity** for systems that span categories. A robot providing both care assistance (high-risk AI) and companionship (potentially lower-risk) faces uncertain classification.

### Professional Organization Standards

Medical specialty societies have developed guidelines for AI use in specific domains:

- American College of Radiology guidelines for AI in imaging
- American Medical Association principles for AI in clinical practice
- American Nurses Association position on AI in nursing

These guidelines influence practice but **lack regulatory force**. Compliance is voluntary, and guidelines vary across specialties and organizations.

## The Enabling Change

Technology governance for alternative architecture requires **coordinated action across multiple authorities** with distinct jurisdictions and interests.

### Federal Technology Authorization

| Required Change | Authority | Mechanism |
|-----------------|-----------|-----------|
| AI clinical decision support safe harbor | FDA, CMS | Guidance with enforcement discretion |
| Companion system standards | FTC, HHS | Rulemaking under consumer protection authority |
| Healthcare robot certification | FDA, OSHA | Joint framework for patient and worker safety |
| Performance monitoring requirements | FDA | Finalization of 2025 draft guidance |
| Rural validation mandates | CMS | Conditions of participation for AI systems |

The FDA possesses authority to create pathways for AI system deployment through guidance, enforcement discretion, and rulemaking. **What lacks is not authority but priority**. Rural healthcare access does not drive FDA agenda-setting the way major market products do.

CMS could condition Medicare and Medicaid payment on AI system validation for rural populations, creating market incentives for appropriate testing. Current conditions of participation address facility standards but not algorithmic systems making care decisions.

### State Regulatory Coordination

| Required Change | Mechanism | Timeline |
|-----------------|-----------|----------|
| Liability allocation framework | Model state legislation | 2-3 years for widespread adoption |
| Scope of AI practice determination | State medical board coordination | Ongoing, state-by-state |
| Professional AI service safe harbors | Bar association and licensing board action | 3-5 years for significant progress |
| Uniform companion standards | Interstate compact or model act | 4-6 years for coordination |

State coordination is essential because **key governance questions remain state jurisdiction**: medical practice definition, professional licensing, liability law, and consumer protection. Federal action cannot preempt state authority in these domains without constitutional questions.

The National Conference of State Legislatures and Council of State Governments could develop model legislation for AI healthcare governance. Compact mechanisms used for professional licensure could potentially extend to technology standards, though no such compact currently exists.

### Community-Level Technology Governance

Alternative architecture places governance authority at community level through mechanisms Series 14 describes. Technology governance should integrate with community governance structures:

| Community Function | Implementation |
|-------------------|----------------|
| Technology review board | Community oversight of AI/robot deployment decisions |
| Impact assessment | Required before new system implementation |
| Complaint and appeal process | Community mechanism for technology concerns |
| Performance monitoring | Local data on system outcomes |
| Opt-out rights | Individual right to human-only service where feasible |

Community governance does not replace federal and state frameworks but **adds local accountability** that ensures systems serve community interests. A community technology board could review proposed AI deployments, assess privacy implications, require training for users, and maintain complaint processes.

### Liability Framework Development

Clear liability allocation would enable deployment more than any other governance change. A framework should address:

| Scenario | Liability Allocation |
|----------|---------------------|
| AI recommendation followed, harm results | Developer liability for system defect; provider liability for failure to exercise judgment |
| AI recommendation overruled, harm results | Provider liability for professional judgment; no AI developer liability |
| AI fails to detect condition | Developer liability if within claimed capability; no liability if outside capability |
| Patient relies on companion advice | Developer liability for advice beyond system scope; user assumption of risk for appropriate use |
| Robot malfunction causes injury | Developer/manufacturer strict liability; facility liability for inadequate maintenance |

This framework allocates liability based on **fault and capability** rather than leaving all parties uncertain. Developers know their exposure; providers know when professional judgment protects them; patients know who is accountable when harm occurs.

## Stakeholder Analysis

Technology governance involves stakeholders with divergent interests that shape political feasibility.

| Stakeholder | Current Position | Interest | Movability |
|-------------|-----------------|----------|------------|
| Technology developers | Prefer minimal regulation | Market access, liability limitation | Movable toward clear frameworks over uncertainty |
| Healthcare providers | Cautious about AI adoption | Liability protection, clinical authority | Movable toward safe harbors with clear boundaries |
| Professional associations | Protective of scope | Maintain professional authority over AI | Limited movability; see AI as threat |
| Patient advocates | Concerned about safety and equity | Protection without access denial | Movable toward balanced frameworks |
| Rural communities | Desperate for access | Any technology that improves care | Strong support for enabling governance |
| Liability insurers | Unable to price AI risk | Clear liability allocation | Strong support for framework clarity |
| State regulators | Protective of jurisdiction | Maintain state authority | Resistant to federal preemption |

**Technology developers prefer regulatory certainty** over minimal regulation. The current uncertainty deters investment in healthcare AI because liability exposure is unquantifiable. Developers would accept clear requirements over unclear permissiveness.

**Healthcare providers need safe harbors** that specify when AI use creates liability and when it does not. Absent clarity, the rational provider choice is avoiding AI entirely, regardless of patient benefit.

**Professional associations present the strongest opposition** to AI governance that enables independent AI function. Medical associations view clinical AI as practicing medicine; bar associations view legal AI as practicing law. Their interests lie in maintaining human professional gatekeeping even when human professionals are unavailable.

The **political coalition for technology governance** includes developers seeking certainty, providers seeking protection, insurers seeking clarity, and rural communities seeking access. Opposition comes primarily from professional associations protecting scope and state regulators protecting jurisdiction.

## Implementation Pathway

Technology governance enabling alternative architecture requires phased development across multiple authorities.

**Phase 1 (2026-2027): Federal Framework Foundation**
- FDA finalizes AI device guidance with rural validation requirements
- CMS conditions of participation for AI systems in Medicare-certified facilities
- FTC consumer protection framework for companion systems
- HHS coordination guidance for healthcare AI

**Phase 2 (2027-2028): State Coordination**
- Model state legislation for AI liability allocation
- Interstate AI governance compact development
- State medical board coordination on AI practice determination
- Professional licensing adaptation for AI-augmented practice

**Phase 3 (2028-2030): Community Integration**
- Community technology governance toolkit development
- Local oversight mechanism implementation
- Regional coordination for cross-border technology deployment
- Continuous improvement based on deployment experience

This timeline assumes **sustained policy attention** that may not materialize. Technology governance competes with other priorities, and rural healthcare specifically commands limited political attention.

## Vignette: The First Rural AI Triage Center

Beatrice Memorial Health Center in Cherry County, Nebraska, became the state's first authorized AI triage facility in November 2028. The authorization followed 18 months of negotiation among state regulators, the facility, and the AI developer, establishing precedents that later guided national framework development.

The center serves a county with 6,000 residents spread across 6,000 square miles. The nearest hospital is 90 miles away. Before the AI triage system, patients calling with symptoms received advice from a receptionist who had no clinical training. The choice was often "drive to Valentine" or "wait and see."

**The AI triage system changed that calculus**. Patients calling or using the mobile app describe symptoms through structured questions. The AI analyzes responses against a clinical decision tree, identifying conditions requiring immediate emergency transport, same-day evaluation at the center, virtual physician consultation, or home monitoring with return precautions.

The governance framework that enabled deployment specified critical elements:

**Liability allocation**: The AI developer warranted triage accuracy against peer-reviewed clinical guidelines. The facility remained responsible for implementation, including ensuring patients could access recommended care. Neither bore liability for patient choices to ignore recommendations, provided documentation demonstrated appropriate communication.

**Human oversight**: Every triage recommendation above "home monitoring" triggered parallel notification to the on-call physician, who could override AI recommendations within 15 minutes. Overrides were tracked and reviewed quarterly to assess AI calibration.

**Performance monitoring**: The developer committed to quarterly performance reports measuring recommendation accuracy against eventual diagnoses, with automatic system updates if accuracy fell below 95% for emergency classifications.

**Community input**: A community advisory board reviewed the implementation before launch, receiving plain-language explanation of system capabilities and limitations. The board established complaint procedures and required that any resident could request human-only triage by calling during staffed hours.

The **first year's data** showed 847 AI triage encounters. Twelve resulted in emergency recommendations; all twelve were confirmed as appropriate based on subsequent care. Two hundred thirty-one resulted in same-day evaluation recommendations; 94% received appropriate care within 24 hours. The remainder received virtual consultation or home monitoring recommendations. Three patients who received home monitoring recommendations later required emergency care; all three had declined to answer follow-up questions that would have changed the recommendation.

The facility's nurse practitioner, Sarah Whitehorse, initially opposed the system. "I thought it would replace clinical judgment," she explained. "What it actually does is extend my reach. I can't answer every call, but I can review every high-acuity recommendation before the patient acts on it. The AI handles the routine so I can focus on the complex."

The framework developed in Cherry County became the template for Nebraska's statewide AI triage authorization, issued in 2029. Other Great Plains states requested the documentation, beginning the regional coordination that eventually produced the Western States AI Healthcare Compact.

## Conclusion

Technology governance is the enabling condition most within reach and most frequently overlooked. Unlike regulatory transformation requiring legislative battles or interstate infrastructure requiring political coordination, technology governance primarily requires **administrative action by agencies with existing authority**. The FDA can issue guidance. CMS can establish conditions. FTC can enforce consumer protection. State medical boards can clarify scope. None requires legislation.

The barrier is **priority, not authority**. Rural healthcare commands insufficient political attention to drive agency action. Technology companies focus on lucrative urban markets that do not require governance innovation. Professional associations prefer technology governance that maintains human professional gatekeeping.

The opportunity lies in demonstrating that governance enables deployment. Developers want certainty. Providers want protection. Insurers want clarity. Rural communities want access. All these interests align around governance frameworks that specify accountability while enabling beneficial technology. The coalition exists; what lacks is the political entrepreneur who assembles it.

Alternative architecture cannot function without technology governance. AI companions require privacy and safety frameworks. Clinical AI requires liability allocation. Robotic care requires certification standards. Professional AI services require safe harbors. Each component of Series 14 depends on governance infrastructure that does not yet exist.

Building that infrastructure is achievable within the policy process. The question is whether rural health transformation commands sufficient priority to make it happen.

## Cross-References

**Series 14: Alternative Architecture**
- [14A The Inverse Hub](/rural-health/series-14/rhtp-14a/): virtual delivery requiring AI governance
- [14B AI as Infrastructure](/rural-health/series-14/rhtp-14b/): comprehensive AI deployment framework
- [14D The Service Center](/rural-health/series-14/rhtp-14d/): robotic system integration
- [14F Governance Models](/rural-health/series-14/rhtp-14f/): community technology oversight integration

**Series 5: State Agencies**
- [5A Lead Agency Structures](/rural-health/series-5/lead-agency-structures/): state implementation capacity for technology governance
- [5C Procurement](/rural-health/series-5/5c/): technology acquisition and contracting

**Series 7: Healthcare Providers**
- [7A Critical Access Hospitals](/rural-health/series-7/rhtp-7a/): facility-level AI deployment
- [7B Rural Health Clinics](/rural-health/series-7/rhtp-7b/): clinic technology integration

**Series 15: Enabling Conditions**
- [15A Regulatory Transformation](/rural-health/series-15/rhtp-15a/): technology authorization barriers
- [15D Interstate Infrastructure](/rural-health/series-15/rhtp-15d/): regional technology coordination
- [15E Political Economy](/rural-health/series-15/rhtp-15e/): technology industry interests

**Series 16: Futures**
- [16B Transformation Scenario](/rural-health/series-16/rhtp-16b/): technology deployment at scale
- [16E Sustainability](/rural-health/series-16/rhtp-16e/): technology governance maintenance

## Sources

American Action Forum. "AI Companions: Opportunities, Risks, and Policy Implications." AAF Insight, November 2025.

Bipartisan Policy Center. "FDA Oversight: Understanding the Regulation of Health AI Tools." Issue Brief, November 2025.

Blindheim, K., et al. "Social Robots in Scandinavian Elder Care: Implementation and Outcomes." Scandinavian Journal of Caring Sciences, 2023.

California State Legislature. "AI Companion Safety Act." 2025 Legislative Session.

Complizen. "AI Medical Devices: FDA Draft Guidance, TPLC & PCCP Guide 2025." October 2025.

European Commission. "EU Artificial Intelligence Act." Official Journal of the European Union, 2024.

Food and Drug Administration. "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations." Draft Guidance, January 2025.

Food and Drug Administration. "Request for Public Comment: Measuring and Evaluating Artificial Intelligence-enabled Medical Device Performance in the Real-World." FDA-2025-N-4203, October 2025.

Hung, Lillian, et al. "Ethical considerations in the use of social robots for supporting mental health and wellbeing in older adults in long-term care." Frontiers in Robotics and AI, March 2025.

IntuitionLabs. "AI Medical Devices: 2025 Status, Regulation & Challenges." October 2025.

MedTech Dive. "FDA exempts more wearable, AI features from oversight." January 2026.

PMC. "Ethical implications in using robots among older adults living with dementia." Frontiers in Psychiatry, August 2024.

PMC. "Artificial Intelligence (AI) and Robotics in Elderly Healthcare: Enabling Independence and Quality of Life." 2023.

PMC. "Investigating Elderly Individuals' Acceptance of Artificial Intelligence (AI)-Powered Companion Robots." May 2025.

STAT News. "FDA announces sweeping changes to oversight of wearables, AI-enabled devices." January 2026.

360iResearch. "Companion Robots Market Size & Share 2025-2030." Market Analysis, 2025.

*Rural Health Transformation Project*
*Series 15: Enabling Conditions*
*Article 15C V1*
*February 2026*

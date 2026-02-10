# Article 7F: Consolidated Rulemaking Decision Matrix

## Complete Policy Choice Framework for State Regulators

State regulators implementing work requirements face hundreds of granular policy decisions across exemption design, verification architecture, coordination timing, delegation authority, and tribal sovereignty. Each decision interacts with others; choices made in exemption categories ripple through verification processes, coordination timelines, and delegation structures. This consolidated matrix synthesizes all rulemaking choices from the Series 7 handbooks while cross-referencing accommodation requirements for the sixteen special populations analyzed in Series 11 and Article 4D.

The matrix is organized by decision domain, with each choice presented alongside the special populations most affected, recommended approaches, and critical interdependencies. States should read this document alongside the detailed analysis in Articles 7A through 7E, using this matrix as a decision checklist and cross-reference tool rather than a replacement for the underlying analysis.

## Part I: Exemption Rulemaking Decisions

### 1.1 Age-Based Exemptions

**Decision Point:** Upper age threshold for automatic exemption

| Option | Description | Populations Affected |
|--------|-------------|---------------------|
| Age 50 | Acknowledges age discrimination, physical limitations | Transitions (11G), Non-SSI/SSDI Disabilities (11K) |
| Age 55 | Moderate approach | Same |
| Age 60 | Mirrors Social Security early retirement | Same |
| Age 65 | Aligns with Medicare eligibility | Same |

**Recommended:** Age 60 automatic exemption

**Special Population Cross-Reference:**
- **Transitions (11G):** Andre Williams lost coverage two weeks before turning 60 when his exemption expired. Grace periods should bridge to automatic age exemption.
- **Non-SSI/SSDI Disabilities (11K):** Older workers with partial disabilities often cannot sustain 80 hours. Lower age threshold provides earlier protection.

**Interdependencies:** Transition grace periods (7C) must account for approaching age thresholds. System must flag members within 90 days of age exemption to prevent termination immediately before automatic protection begins.

---

### 1.2 Social Security Disability Integration

**Decision Point:** Automatic exemption for SSI/SSDI recipients

| Option | Description | Implementation |
|--------|-------------|----------------|
| Automatic SSI | Data match with SSA | Quarterly refresh |
| Automatic SSDI | Medicare Entitlement Data | CMS data sharing |
| Manual application | Individual must apply | Documentation burden |

**Recommended:** Automatic exemption for both SSI and SSDI recipients through data matching

**Special Population Cross-Reference:**
- **Autism/IDD (4D):** Adults receiving SSI face no work requirements; those in expansion without SSI face full requirements despite similar functional limitations
- **Non-SSI/SSDI Disabilities (11K):** Jordan Mitchell's TBI prevents full-time work but doesn't qualify for SSI. The gap between SSI threshold and work requirement threshold creates coverage cliff.
- **Serious Mental Illness (11B):** Many with SMI denied SSI despite substantial functional impairment

**Interdependencies:** Data sharing agreements with SSA must be executed by March 2026. Trial work period monitoring must maintain exemption during SSDI work attempts.

---

### 1.3 Caregiver Exemptions

**Decision Point:** Child age threshold for parent/guardian exemption

| Option | Child Age | Rationale |
|--------|-----------|-----------|
| Under 1 | Restrictive | Assumes childcare availability after infancy |
| Under 6 | Moderate | Georgia 2025 model |
| Under 13 | Expanded | Arkansas proposal; school-age children still need supervision |

**Recommended:** Under 6 automatic; under 13 with documentation of childcare unavailability

**Decision Point:** Special needs extension regardless of child age

| Trigger | Documentation |
|---------|---------------|
| Child receives SSI | Automatic via data match |
| Child on disability waiver | State system flag |
| Child has IEP with substantial limitations | School system verification |

**Special Population Cross-Reference:**
- **Pregnant/Postpartum (11A):** Jessica Martinez couldn't document childcare unavailability because waitlist screenshots weren't accepted. Requirement should specify acceptable documentation formats.
- **Caregiving (11F):** Rosa Martinez cared for sister's children after overdose plus mother with dementia. Multi-generational caregiving requires accommodation.
- **Autism/IDD (4D):** Parents of adults with autism/IDD need indefinite exemption for ongoing care responsibilities

**Documentation Accommodation by Population:**

| Population | Standard Documentation | Alternative Pathway |
|------------|----------------------|---------------------|
| Pregnant/Postpartum | Childcare denial letters | Waitlist screenshots, provider attestation of unavailability |
| Caregiving | Care recipient needs assessment | Provider attestation, HCBS waiver enrollment |
| Autism/IDD caregivers | IEP or SSI documentation | Provider attestation of ongoing care needs |

---

### 1.4 Medical Exemption Framework

**Decision Point:** Approach to medical exemption determination

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| Diagnosis list | Specified conditions qualify | Clear criteria | Over/under-inclusive |
| Functional assessment | Provider attests to work incapacity | Clinical judgment | Subjective variation |
| Hybrid | Automatic for severe; functional for others | Combines benefits | Two-tier complexity |

**Recommended:** Hybrid approach

**Automatic Medical Exemptions (No Application Required):**
- Active cancer treatment (chemotherapy, radiation)
- Organ failure requiring transplant listing
- Psychiatric hospitalization within 90 days
- Home health services recipient
- Hospice enrollment
- Recent hospitalization (30-day automatic)

**Provider Attestation Pathway:**
- Single-page checkbox form
- "Patient cannot consistently meet 80-hour monthly work requirements due to medical conditions"
- No detailed diagnosis required
- 5% random audit rate

**Special Population Cross-Reference:**

| Population | Automatic Triggers | Attestation Considerations |
|------------|-------------------|---------------------------|
| Serious Mental Illness (11B) | Psychiatric hospitalization within 90 days | Anosognosia may prevent self-identification; provider must initiate |
| Substance Use Disorders (11C) | Residential treatment enrollment | 42 CFR Part 2 confidentiality; self-attestation option |
| Complex Medical (11O) | Multiple chronic conditions with recent utilization | Algorithmic flagging from claims data |
| Pregnancy (11A) | Pregnancy confirmation through claims | Postpartum extension through 12 months automatically |

**Interdependencies:** Provider payment structure (7C) must incentivize attestation completion. EHR integration must enable direct submission.

---

### 1.5 Episodic Condition Accommodations

**Decision Point:** Framework for conditions with unpredictable fluctuation

**Qualifying Conditions:** Bipolar disorder, multiple sclerosis, rheumatoid arthritis, Crohn's disease, lupus, severe migraines, PTSD with acute episodes

**Recommended Framework:**

| Component | Specification |
|-----------|---------------|
| Initial documentation | Provider completes functional assessment documenting episodic nature |
| Review frequency | Annual (not semi-annual) |
| Automated triggers | Healthcare utilization activates temporary exemption |

**Automated Exemption Triggers:**

| Utilization Event | Exemption Duration |
|-------------------|-------------------|
| Hospitalization | 60 days automatic |
| ED visit | 14 days automatic |
| Rescue medication increase | 30 days automatic |
| Provider portal submission | Immediate, duration per attestation |

**Hour Averaging:** 60-hour average over six months acceptable (40 hours bad months, 80+ good months)

**Special Population Cross-Reference:**
- **Serious Mental Illness (11B):** Marcus Thompson was hospitalized when verification deadline passed. Hospitalization must automatically trigger exemption and deadline extension.
- **Substance Use Disorders (11C):** Relapse is expected disease course, not rule violation. Treatment re-entry should trigger automatic exemption.
- **Complex Medical (11O):** Multiple chronic conditions create unpredictable capacity patterns

---

### 1.6 Temporary Disability Rules

**Decision Point:** Automatic exemption periods by condition type

| Condition | Automatic Period | Extension Pathway |
|-----------|------------------|-------------------|
| Surgery requiring hospitalization | 90 days | Provider attestation for complications |
| Organ transplant | 12 months | Provider review at 12 months |
| Cardiac procedures (CABG, valve, stent) | 6 months | Provider attestation |
| Orthopedic surgery (joint replacement, spinal fusion) | 6 months | Provider attestation |
| Cancer surgery | Treatment duration + 6 months | Automatic extension if treatment continues |
| Stroke | 6 months minimum | Recovery trajectory assessment |
| Pregnancy | Entire pregnancy | Automatic via claims data |
| Postpartum | 12 months (not 6 weeks) | Complication extension available |
| Miscarriage/pregnancy loss | 90 days | Provider attestation for extended recovery |
| NICU stay | Hospital discharge + 90 days | Automatic via claims |

**Special Population Cross-Reference:**
- **Pregnant/Postpartum (11A):** 12-month postpartum period accommodates recovery, breastfeeding, infant care establishment, childcare arrangement, postpartum depression treatment
- **Complex Medical (11O):** Surgery recovery periods must account for comorbidity complications

---

### 1.7 Confidentiality-Protected Exemptions

**Decision Point:** Documentation requirements for domestic violence, trafficking, stalking survivors

**Recommended Framework:**

| Documentation Type | Acceptance | Risk Level |
|-------------------|------------|------------|
| Protective order | Accept but don't require | Creates public record trail |
| Police report | Accept but don't require | May not exist; creates trail |
| DV advocate attestation | Primary pathway | Lower disclosure risk |
| Self-attestation | Accept with verification call | Lowest documentation burden |
| Shelter enrollment | Automatic via data match if available | Requires HMIS integration |

**Location Protection Requirements:**
- Employer name NOT required for verification; industry category sufficient
- Residential address NOT required; P.O. box or confidential address program accepted
- Phone number alternatives including shelter voicemail systems accepted
- Portal access without SMS two-factor authentication available

**Special Population Cross-Reference:**
- **Confidentiality (11H):** Lisa Martinez was found by her abuser after providing employer information. Verification must permit location-protecting alternatives.
- **Human trafficking survivors:** Trafficker monitoring makes any location data dangerous
- **LGBTQ in hostile environments (11N):** Disclosure of workplace may reveal identity to hostile family/community

**Interdependencies:** Verification systems (7B) must include location-protected pathways. Appeals processes must maintain confidentiality throughout.

---

## Part II: Verification Rulemaking Decisions

### 2.1 Core Architecture

**Decision Point:** Distributed submission authority vs. centralized individual reporting

| Architecture | Coverage Loss Risk | Administrative Cost |
|--------------|-------------------|---------------------|
| Centralized individual | High (25% Arkansas) | Lower initial; higher remediation |
| Distributed submission | Low | Higher initial; lower remediation |

**Recommended:** Distributed submission authority as primary pathway

**Special Population Cross-Reference:**
- **All populations:** Centralized reporting places documentation burden on individuals whose conditions may impair documentation capacity
- **Serious Mental Illness (11B):** Executive function impairment prevents multi-step documentation
- **Autism/IDD (4D):** Cognitive processing differences make form completion impossible without support
- **Homelessness (11E):** No stable address, phone, or document storage for individual reporting

---

### 2.2 Large Employer Integration

**Decision Point:** Mandatory payroll integration threshold

| Threshold | Coverage | Implementation Burden |
|-----------|----------|----------------------|
| 500+ employees | 15-20% of expansion adults | Low |
| 250+ employees | 25-30% | Moderate |
| 100+ employees | 40-50% | Higher |

**Recommended:** 100+ employees mandatory; smaller encouraged

**Technical Requirements:**
- API integration or credentialed payroll processor (ADP, Gusto, Paychex, Workday)
- Monthly submission: SSN/Medicaid ID, hours worked, pay period dates
- Integration deadline: October 2026

---

### 2.3 Small Employer Solutions

**Decision Point:** Verification pathways for employers under 100 employees

| Pathway | Description | Best For |
|---------|-------------|----------|
| Web portal | Employer monthly login and entry | Office-based small employers |
| Industry association | Bulk submission through trade groups | Restaurants, construction, retail |
| MCO intermediary | Health plan coordinates verification | Complex cases, multiple jobs |
| Simplified attestation | One-page monthly form | Micro-employers, informal arrangements |

**Recommended:** All pathways available; employer chooses

**Special Population Cross-Reference:**
- **Geographic Isolation (11I):** Rural employers may lack internet access. Paper attestation pathway essential.
- **Seasonal Workers (11Q):** Agricultural employers need seasonal batch reporting
- **Gig Economy:** Platform partnerships eliminate employer-by-employer verification

---

### 2.4 Self-Employment Verification

**Decision Point:** Documentation requirements for self-employed individuals

| Documentation | Purpose | Audit Rate |
|---------------|---------|------------|
| Quarterly estimated tax | Proves ongoing self-employment | N/A |
| Calendar logs | Hour tracking | 15% random |
| Business license/registration | Confirms legitimate business | Initial only |

**Accommodation:** First 6 months of new business counts automatically (business plan development, licensing, setup)

**Special Population Cross-Reference:**
- **Geographic Isolation (11I):** Self-employment may be only option in employment deserts
- **Justice Reentry (11D):** Self-employment may be necessary when employers won't hire
- **LEP (11J):** Self-employment common in immigrant communities; may lack formal documentation

---

### 2.5 Gig Economy and Platform Work

**Decision Point:** Verification pathway for platform workers

| Approach | Implementation | Coverage |
|----------|----------------|----------|
| Platform partnerships | Direct API from Uber, DoorDash, etc. | Majority of gig workers |
| Bank statement verification | Deposits prove work | When partnerships unavailable |
| Self-attestation with high audit | 25% random audit | Last resort |

**Recommended:** Pursue platform partnerships aggressively Q1 2026; bank statement fallback; self-attestation only when neither available

**Special Population Cross-Reference:**
- **Substance Use Disorders (11C):** Gig work offers flexibility for treatment schedules but generates fragmented documentation
- **Justice Reentry (11D):** Gig work may be only available employment with criminal record
- **Homelessness (11E):** Day labor through apps creates no paper trail

---

### 2.6 Seasonal and Irregular Work

**Decision Point:** Accommodation for employment patterns that don't match monthly requirements

| Mechanism | Description | Federal Flexibility Needed |
|-----------|-------------|---------------------------|
| Hour banking | Excess hours carry forward (max 240) | No |
| Annual averaging | 960 annual hours, any distribution | Yes (waiver) |
| Known off-season exemption | Automatic exemption during industry off-seasons | Possibly |

**Recommended:** Hour banking as primary; request federal waiver for annual averaging; known off-season exemptions for clearly seasonal industries

**Special Population Cross-Reference:**
- **Agricultural/Seasonal Workers (11Q):** May work 160+ hours monthly peak season, zero off-season
- **Geographic Isolation (11I):** Tourism-dependent areas have inverse seasonal patterns
- **Caregiving (11F):** Care needs may be seasonal (school year vs. summer)

---

### 2.7 Alternative Documentation Standards

**Decision Point:** Acceptable verification when standard documentation unavailable

| Population | Standard Documentation | Alternative Pathway |
|------------|----------------------|---------------------|
| Day labor | Employer attestation | Self-attestation + 25% audit |
| Cash employment | Pay stubs | Bank deposits + self-report |
| Informal caregiving | N/A (exemption pathway) | Care recipient attestation |
| Volunteer work | Organization attestation | Supervisor attestation + activity logs |
| Homelessness | Any of above | Trusted intermediary submission |

**Special Population Cross-Reference:**
- **Homelessness (11E):** Christina Robinson worked day labor with cash payment. No paystubs exist. Self-attestation with audit must be accepted.
- **LEP (11J):** Cash employment common; may have documentation in non-English
- **Undocumented family concerns (within 11H):** Fear of documentation creating immigration trail

---

### 2.8 Communication Infrastructure Requirements

**Decision Point:** Accessibility of verification systems

| Channel | Requirement | Populations Served |
|---------|-------------|-------------------|
| Online portal | Mobile-responsive, language support | Primary pathway |
| Phone verification | Available for those without internet | Geographic isolation, digital exclusion |
| Paper submission | Accepted when other channels impossible | Rural, elderly, disabled |
| In-person assistance | Available at county offices, community orgs | Complex cases, multiple barriers |

**Special Population Cross-Reference:**
- **Geographic/Digital Isolation (11I):** Tom Henderson had no internet and no transportation to internet. Phone and paper pathways essential.
- **LEP (11J):** Portal must support threshold languages; phone interpreters for 200+ languages
- **Autism/IDD (4D):** Plain language, visual aids, navigation support required

**Two-Factor Authentication Alternative:** SMS-based 2FA excludes people without phones. Email-based or security question alternatives required.

---

## Part III: Coordination and Timing Decisions

### 3.1 Redetermination Scheduling

**Decision Point:** Synchronized vs. staggered renewal cycles

| Approach | Best For | Considerations |
|----------|----------|----------------|
| Synchronized (June/December) | States under 100K expansion adults | Volume spikes manageable |
| Staggered by birth month | States over 500K expansion adults | Smooths workload |
| Regional staggering | States with geographic variation | Targets support resources |

**Recommended:** Staggered by birth month for large states; synchronized acceptable for small states

---

### 3.2 Grace Periods

**Decision Point:** Duration of grace periods across transition types

| Transition Type | Recommended Grace Period | Rationale |
|-----------------|-------------------------|-----------|
| First-time requirements | 90 days | Learning curve, exemption applications |
| Job loss | 60 days | Job search, UI application |
| Exemption expiration | Equal to exemption duration (90-180 days) | Proportional to barrier significance |
| Geographic move | 90 days | Employment search in new location |
| Between semesters | Automatic coverage | Intent to continue enrollment sufficient |
| Treatment completion (SUD) | 180 days | Recovery stabilization |
| Postpartum | 12 months from delivery | Physical recovery, infant care, mental health |

**Special Population Cross-Reference:**
- **Transitions (11G):** Andre Williams lost coverage two weeks before age exemption. Grace periods must bridge to approaching automatic exemptions.
- **Serious Mental Illness (11B):** Medication stabilization takes 2-6 months post-hospitalization
- **Substance Use Disorders (11C):** 180-day post-treatment grace accommodates recovery fragility
- **Pregnant/Postpartum (11A):** 12-month postpartum period prevents coverage gaps during maximum vulnerability

---

### 3.3 Warning and Escalation Cascade

**Decision Point:** Timeline from non-compliance detection to coverage action

| Day | Action | Channel |
|-----|--------|---------|
| 1-10 after deadline | Warning notification | Text, email, portal |
| 11-20 | Phone outreach | Navigator contact |
| 21-30 | Final notice | Certified mail |
| 31 | Coverage suspension (not termination) | Reinstatement without full reapplication |
| 61 | Coverage termination | Full reapplication required |

**Recommended:** Suspension rather than immediate termination; easy reinstatement when documentation arrives

**Special Population Cross-Reference:**
- **Serious Mental Illness (11B):** Marcus Thompson was hospitalized when deadline passed. 30-day warning period wouldn't help someone who can't receive warnings.
- **Homelessness (11E):** Mail doesn't reach people without addresses. Phone calls don't reach people whose phones were stolen.

**Accommodation:** Hospitalization, incarceration, or other institutional status automatically extends all deadlines by duration of institutional stay plus 30 days.

---

### 3.4 Appeals Timeline and Process

| Stage | Timeline | Coverage Status |
|-------|----------|-----------------|
| Filing deadline | 90 days from denial | Continues |
| Standard review | 45 days | Continues |
| Expedited review | 3 business days | Continues |
| Independent medical review | 30 days | Continues |

**Expedited Appeals Available For:**
- Active treatment at risk
- Chronic condition requiring continuous medication
- Pregnancy
- Mental health crisis

**Special Population Cross-Reference:**
- **All populations:** Coverage ALWAYS continues during appeals. Burden of delay falls on state.
- **Autism/IDD (4D):** Appeals process assumes capacity to navigate bureaucracy. Support required.
- **LEP (11J):** Appeals materials in threshold languages; interpreter services throughout

---

### 3.5 Provider Payment for Exemption Documentation

**Decision Point:** Compensation structure for provider attestations

| Structure | Amount | Pros | Cons |
|-----------|--------|------|------|
| Flat fee per attestation | $35 | Simple, incentivizes participation | May under-compensate complex cases |
| Tiered by complexity | $25-100 | Matches effort | Administrative complexity |
| PMPM to safety-net clinics | $2 PMPM | Predictable revenue | May not match actual workload |

**Recommended:** $35 flat fee primary; capitated payments to FQHCs serving high proportions of expansion adults

---

## Part IV: Delegation Authority Decisions

### 4.1 Credentialed Entity Tiers

**Tier 1: Primary Submitters (Direct State Delegation)**

| Entity Type | Submission Authority | Credentialing |
|-------------|---------------------|---------------|
| Employers | Work hours for employees | EIN verification, designated submitter training |
| Healthcare providers | Medical exemption attestation | License verification, NPI, training |
| Educational institutions | Enrollment and attendance | Accreditation verification, data agreement |
| State workforce agencies | Job training, UI data | Interagency agreement |

**Tier 2: Intermediary Submitters (Aggregation Authority)**

| Entity Type | Submission Authority | Credentialing |
|-------------|---------------------|---------------|
| MCOs | Aggregate verification from multiple sources | Managed care contract |
| Payroll processors | Submit for multiple employers | Business registration, security certification |
| Staffing agencies | Hours for placed workers | Business license, workforce agency relationship |

**Tier 3: Community-Based Submitters (Limited Authority)**

| Entity Type | Submission Authority | Credentialing |
|-------------|---------------------|---------------|
| Volunteer organizations | Volunteer hours | 501(c)(3) verification, training |
| Faith-based organizations | Community service hours | Registration, training |
| CBOs | Facilitate applications as trusted intermediary | Registration, navigator training |
| Tribal entities | Verification for tribal members | Government-to-government agreement |

**Special Population Cross-Reference:**
- **Homelessness (11E):** Shelter case managers and street outreach workers must be credentialed as trusted intermediaries
- **Substance Use Disorders (11C):** Treatment program staff can verify treatment participation hours
- **Faith communities serving immigrants:** May be only trusted institution for LEP populations

---

### 4.2 Safe Harbor Provisions

**Employer Safe Harbor:**
- Protected for submitting hours as recorded in standard payroll systems
- No liability for employee coverage loss due to accurate reporting
- No liability for good-faith errors corrected when discovered
- Exceptions: intentional false reporting, retaliation, systematic timekeeping failure

**Provider Safe Harbor:**
- Protected for attestations based on clinical relationship and professional judgment
- No malpractice liability for good-faith exemption attestations
- No liability if state denies exemption despite provider recommendation
- Documentation in medical record required

**Special Population Cross-Reference:**
- **Confidentiality (11H):** Employer safe harbor should NOT extend to responding to third-party inquiries about employee schedules (enables stalking)
- **Substance Use Disorders (11C):** Provider safe harbor must accommodate 42 CFR Part 2 confidentiality requirements

---

### 4.3 Individual Rights to Challenge Delegated Actions

| Action Type | Challenge Window | Process | Coverage During |
|-------------|------------------|---------|-----------------|
| Employer-reported hours | 60 days from statement | State reviews payroll records | Continues |
| Provider exemption denial | Ongoing | Seek different provider or state review | Continues |
| Educational institution error | 60 days from notification | Contrary evidence submission | Continues |
| MCO navigation denial | Ongoing | Request state navigator | Continues |

---

## Part V: Tribal Sovereignty Decisions

### 5.1 IHS Exemption Implementation

**Decision Point:** Verification of IHS eligibility for automatic exemption

| Approach | Description | Burden |
|----------|-------------|--------|
| IHS data match | State requests eligibility data from IHS | Requires federal agreement |
| Tribal attestation | Tribal enrollment office confirms eligibility | Government-to-government negotiation |
| Self-attestation with verification | Individual attests; random verification | Lowest burden, higher audit |

**Recommended:** IHS data match where federal agreement allows; tribal attestation as primary alternative; self-attestation with verification as fallback

---

### 5.2 Data Sovereignty Accommodations

| Principle | Implementation |
|-----------|----------------|
| No unilateral state access to tribal records | Government-to-government negotiation required |
| Tribal council approval for data sharing | Formal agreement process |
| Tribal audit rights | Agreements include tribal review of state data use |
| Cultural competency | State staff training on tribal sovereignty |

---

### 5.3 Tribal Administration Option

**Decision Point:** Whether tribes can administer work requirements for their own members

| Component | State Flexibility | Federal Flexibility Needed |
|-----------|------------------|---------------------------|
| Qualifying activities definition | Tribal determines | Possibly (waiver) |
| Verification processes | Tribal determines | No |
| Exemption categories | Tribal determines | Possibly (waiver) |
| Funding for administration | State provides | No |

**Culturally Appropriate Qualifying Activities:**
- Subsistence hunting, fishing, gathering
- Traditional ceremony participation
- Elder care according to traditional responsibilities
- Tribal program volunteer service

---

## Part VI: Special Population Accommodation Matrix

This matrix summarizes accommodations required for each Series 11 population across all rulemaking domains.

### 6.1 Pregnant and Postpartum (11A)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Automatic pregnancy exemption via claims; 12-month postpartum; complications extend further |
| Verification | Employment verification only; childcare documentation alternatives accepted |
| Timing | No deadlines during 90 days postpartum; graduated return at 6 months |
| Appeals | Expedited for pregnancy complications |

### 6.2 Serious Mental Illness (11B)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Hospitalization triggers 60-day automatic; episodic framework with annual review |
| Verification | Provider can submit on behalf; crisis exemption by phone |
| Timing | Deadline extension for hospitalization; 180-day post-hospitalization grace |
| Appeals | Expedited for treatment continuity; independent psychiatric review |
| Delegation | Behavioral health providers as attestation sources |

### 6.3 Substance Use Disorders (11C)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Treatment hours count as qualifying activity; residential treatment automatic exemption |
| Verification | 42 CFR Part 2 compliance; self-attestation option; treatment program verification |
| Timing | 180-day post-treatment grace; relapse triggers automatic exemption, not termination |
| Appeals | Expedited for MAT continuity |
| Confidentiality | No diagnosis disclosure required; functional attestation only |

### 6.4 Justice Reentry (11D)

| Domain | Accommodation |
|--------|---------------|
| Exemption | 90-day post-release automatic exemption; reentry program hours count |
| Verification | Probation/parole officer can verify activities; employer reluctance accommodation |
| Timing | Incarceration automatically extends all deadlines |
| Delegation | Reentry organizations as trusted intermediaries |

### 6.5 Homelessness (11E)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Automatic via HMIS integration; homeless status = presumptive medical exemption |
| Verification | Trusted intermediary submission; self-attestation with audit; no address required |
| Timing | Extended deadlines (30 days not 10); suspension not termination |
| Communication | Shelter voicemail; library terminal alerts; no SMS 2FA requirement |
| Delegation | Shelter staff, outreach workers as credentialed submitters |

### 6.6 Caregiving (11F)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Care recipient needs-based; multi-generational care recognized; HCBS enrollment automatic |
| Verification | Care recipient attestation; provider attestation of care needs |
| Timing | Grace period when caregiving ends; no cliff when care recipient status changes |

### 6.7 Transitions (11G)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Grace periods bridging to approaching automatic exemptions |
| Timing | 90-day bridge when within 90 days of age exemption; semester bridges for students |
| System flags | Alert when member approaching automatic exemption to prevent termination |

### 6.8 Confidentiality Protections (11H)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Self-attestation option; DV advocate verification; no public record documentation required |
| Verification | Industry category not employer name; P.O. box accepted; confidential address programs |
| Communication | No location-revealing information in databases; sealed records option |
| Delegation | DV advocates, trafficking service providers as attestation sources |

### 6.9 Geographic and Digital Isolation (11I)

| Domain | Accommodation |
|--------|---------------|
| Exemption | High-unemployment area automatic exemption; transportation barrier accommodation |
| Verification | Phone verification available; paper accepted; extended deadlines |
| Communication | No internet-only requirements; mail alternatives |
| Timing | 60-day deadlines (not 30) for isolated areas |

### 6.10 Limited English Proficiency (11J)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Verbal applications via interpreter; community organization facilitation |
| Verification | Threshold language materials; telephonic interpretation; translated portal |
| Communication | All notices in preferred language; bilingual navigators |
| Delegation | Ethnic community organizations as trusted intermediaries |

### 6.11 Non-SSI/SSDI Disabilities (11K)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Partial capacity framework (40-60 hours); functional assessment focus |
| Verification | Variable hour documentation; averaging over longer periods |
| Timing | Extended grace when capacity fluctuates |

### 6.12 Intersectionality (11L)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Graduated requirements based on barrier count; single application for multiple exemptions |
| Verification | Coordinated documentation across barriers |
| Navigation | Complexity-matched navigator assignment |

### 6.13 Autism/IDD (4D)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Functional capacity focus; supported decision-making |
| Verification | Navigator-assisted submission; verbal applications; extended processing time |
| Communication | Plain language; visual aids; caregiver notification |
| Delegation | Disability service providers as trusted intermediaries |

### 6.14 Veterans (11M)

| Domain | Accommodation |
|--------|---------------|
| Exemption | VA disability 30%+ automatic via VA data; service-connected conditions |
| Verification | VA data integration; military records |
| Delegation | VSOs as trusted intermediaries |

### 6.15 LGBTQ+ (11N)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Confidentiality for those in hostile environments |
| Verification | No disclosure of identity to employers; alternative contact methods |
| Communication | Chosen name use; confidential correspondence |

### 6.16 Foster Care Alumni (11P)

| Domain | Accommodation |
|--------|---------------|
| Exemption | Extended transition periods; trauma-informed documentation |
| Verification | Former foster status verification via child welfare data |
| Navigation | Dedicated support given lack of family assistance |

---

## Part VII: Implementation Interdependencies

### Critical Path Dependencies

1. **Data sharing agreements** (SSA, DOL, IHS, HMIS) must be executed by **March 2026** before system development can incorporate automatic exemptions

2. **Provider portal development** requires **provider payment structure** finalization by **April 2026** to enable training

3. **Employer credentialing** cannot begin until **verification architecture** decisions are final (**May 2026**)

4. **MCO contract amendments** require **delegation authority** framework by **June 2026**

5. **Tribal consultation** must produce **government-to-government agreements** before any tribal population provisions can be implemented

6. **Special population accommodations** must be coded into eligibility systems during **July-September 2026** development

### System Integration Requirements

| System | Integration Purpose | Deadline |
|--------|---------------------|----------|
| SSA (SSI/SSDI) | Automatic disability exemption | March 2026 |
| DOL (UI) | Automatic job loss exemption | March 2026 |
| DOC (Corrections) | Incarceration status | March 2026 |
| National Student Clearinghouse | Education verification | April 2026 |
| HMIS | Homeless status | April 2026 |
| VA Benefits | Veteran disability | April 2026 |
| IHS | Tribal eligibility | Ongoing negotiation |

---

## References

1. Articles 7A-7E, Work Requirements Series (2025)
2. Series 11: Special Populations Analysis (2025)
3. Article 4D: Autism, IDD, and the Redetermination Penalty (2025)
4. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas." Health Affairs, 2020.
5. Government Accountability Office. "Medicaid Demonstrations: Evaluations Yielded Limited Results." GAO-24-106490, 2024.
6. Kaiser Family Foundation. "Medicaid Waiver Tracker." KFF.org, 2025.
7. National Health Law Program. "State Exemption Policy Issues." HealthLaw.org, 2025.
8. National Indian Health Board. "Tribal Perspectives on Medicaid Work Requirements." NIHB.org, 2025.
9. Herd, Pamela and Donald Moynihan. Administrative Burden: Policymaking by Other Means. Russell Sage Foundation, 2018.
10. Center on Budget and Policy Priorities. "Work Requirement Verification Systems: Lessons from SNAP and TANF." CBPP.org, 2025.

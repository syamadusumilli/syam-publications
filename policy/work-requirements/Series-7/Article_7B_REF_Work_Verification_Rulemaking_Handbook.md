# Work Requirements Article 7B

# Work Verification Rulemaking Handbook
*Complete guide to work verification policy choices for state regulators*

Work requirements mean nothing without verification systems. States must decide how employers report hours, how individuals document work, what activities qualify, and how to handle edge cases. These decisions determine whether verification creates 40-50% administrative efficiency gains through automation or becomes a paperwork nightmare driving coverage losses.

## Core Verification Architecture Decision

**The fundamental choice:** Distributed submission authority versus centralized individual reporting.

**Distributed model:** Employers, educational institutions, volunteer organizations, and others submit verification directly to state system on behalf of individuals.
- Advantages: Reduces burden on individuals, enables automation, more reliable data
- Challenges: Requires credentialing thousands of organizations, building

 submission infrastructure

**Centralized model:** Individuals responsible for gathering documentation and submitting monthly.
- Advantages: Simpler state system, individual control over data
- Challenges: High individual burden, low compliance, documentation challenges

**Arkansas 2018 used centralized model: 25% coverage loss despite only 3-4% being ineligible.**

**Recommended rule:** Distributed submission authority as primary pathway with individual self-reporting as backup for situations without credentialed submitters.

## Employer Verification Standards

### Large Employer Automation (100+ employees)

**Payroll integration via API:**

**Requirements for employers:**
- Employers with 100+ employees must integrate with state verification system OR use credentialed payroll processors (ADP, Gusto, Paychex, Workday)
- Submit monthly hours worked for each employee receiving Medicaid
- Standard data format: SSN/Medicaid ID, hours worked, pay period dates
- Transmission security: encrypted data transfer, HIPAA compliant

**State requirements:**
- Build API infrastructure accepting data from multiple sources
- Standardize data formats across payroll systems
- Real-time confirmation of successful submission
- Error notifications to employers for rejected submissions

**Timeline:** Employers must complete integration by October 2026 for December launch.

**Cost:** One-time integration cost $500-5,000 per employer depending on payroll system complexity. Ongoing cost minimal (automated process).

**Coverage estimate:** This automation should cover 40-50% of expansion adult population working for large employers.

### Small Employer Solutions (Under 100 employees)

Small employers lack HR infrastructure for system integration but employ significant portions of expansion adults.

**Option A - Web portal:**
- Simple web portal where employers log in monthly
- Enter employee SSN/Medicaid ID and hours worked
- Confirmation email upon submission
- Cost: Minimal for employers, moderate for state (portal development)

**Option B - Employer liaisons:**
- Industry associations (restaurant associations, construction groups, chambers of commerce) serve as intermediaries
- Small employers report to association, association submits to state in bulk
- Cost: State contracts with associations, employers pay minimal association fees

**Option C - Health plan intermediary:**
- MCOs serve as verification intermediaries for their members
- Employers submit to health plan, plan submits to state
- Cost: Included in capitation rates

**Option D - Simplified attestation:**
- Employer completes one-page form monthly: "I attest [employee name] worked [X hours] in [month]"
- Email, fax, or mail submission
- Cost: Minimal technology, higher manual processing for state

**Recommended rule:** Combination approach. Web portal as primary (Option A), with industry association partnerships (Option B) for sectors with many small employers (restaurants, construction, retail, home health). MCO intermediary (Option C) as fallback.

### Employer Credentialing Process

**To submit verification, employers must:**

**Registration:**
- Register with state Medicaid agency online
- Provide EIN, business name, contact information
- Designate authorized submitter(s)
- Accept terms including data security and accuracy requirements

**Verification:**
- State verifies EIN against IRS business database
- Confirms business is active and legitimate

**Training:**
- Complete brief online training (15 minutes) on submission process
- Review accuracy requirements and audit procedures

**Ongoing:**
- Reconfirm annually that information remains current
- Update immediately if authorized submitters change

**Timeline:** Registration takes 3-5 business days. Bulk registration available for payroll processors handling multiple employers.

## Self-Employment Verification

Self-employed individuals have no employer to verify hours. Three approaches:

**Option A - Tax-based:**
- Quarterly estimated tax payments prove ongoing self-employment
- Business receipts or invoices for prior month
- Challenge: Doesn't capture hours, only income

**Option B - Calendar logs:**
- Self-employed person maintains calendar showing hours worked daily
- Submit monthly via portal
- Random audit requests supporting documentation (invoices, receipts, client emails)
- Challenge: Honor system with audit, fraud risk

**Option C - Client attestation:**
- Self-employed person provides client/customer letters attesting to work performed
- Similar to employer attestation but from customers
- Challenge: Burden on clients, may not be feasible for many self-employed

**Recommended rule:** Combination. Quarterly estimated tax payment plus business license/registration proves active self-employment. Monthly hour self-reporting with 15% random audit rate requiring supporting documentation.

**Starting business counts:** First 6 months of launching business counts as qualifying activity automatically (business plan development, licensing, setup).

## Gig Economy and Platform Work

Platform companies (Uber, DoorDash, Instacart, TaskRabbit) resist being treated as employers. Workers cannot easily document hours because platform payments don't break down time worked.

### Platform Partnership Approach

**Negotiate data sharing agreements** with major platforms:

**Platform provides:**
- Monthly hours logged by workers on their platform
- Automated transmission to state system
- Worker consent managed through platform app

**State provides:**
- Safe harbor liability protection (platforms not responsible for verifying work quality, just hours logged)
- Clear data specifications
- No platform obligation to verify employment status or contractor classification

**Recommended platforms for partnership:** Uber, Lyft, DoorDash, Instacart, Shipt, TaskRabbit, Upwork, Fiverr. Together these cover majority of gig workers.

### Bank Statement Verification (Fallback)

For platforms without data agreements:

**Individuals submit:**
- Bank statements showing deposits from platform companies
- Explanation of hours (self-reported) corresponding to income
- Random audit requests platform screenshots showing hour history

**Verification standard:** Bank deposits prove work occurred. Hour calculations approximate but not exact. Accept reasonable estimates.

### Self-Attestation with High Audit

**Last resort for gig work:**
- Worker self-reports hours via portal
- Uploads screenshot of platform hour history when possible
- 25% random audit rate (higher than other categories due to fraud risk)
- Audits request detailed platform data, tax documents, or bank records

**Recommended rule:** Pursue platform partnerships aggressively (priority for Q1 2026). Use bank statement verification where partnerships don't exist. Self-attestation only when worker cannot provide platform data or bank records.

## Seasonal and Irregular Work

Agricultural workers, tourism workers, holiday retail workers have months with zero hours and months with 200+ hours.

### Hour Banking Rules

**Option A - Monthly with carryforward:**
- Requirement remains 80 hours monthly
- Excess hours above 80 carry forward to next month
- Can bank up to 240 hours (3 months cushion)
- Challenge: Provides flexibility but complicated to track

**Option B - Annual averaging:**
- Total annual requirement: 960 hours
- Can work 0 hours some months, 200+ hours others, as long as annual total meets requirement
- Challenge: OB3 specifies monthly requirements - need federal flexibility waiver

**Option C - Known off-season exemptions:**
- State identifies industries with predictable seasonal patterns
- Automatic exemption during documented industry off-seasons
- Requires meeting requirements during peak seasons
- Challenge: Defining which industries qualify, industry boundaries

**Recommended rule:** Hour banking (Option A) as primary mechanism. Request federal flexibility for annual averaging. Known off-season exemptions for clearly seasonal industries (agriculture, ski resorts, summer tourism).

**Implementation:** System tracks cumulative hours. Individuals see "hours banked" balance in portal. Employers submit hours normally, system automatically applies banking rules.

## Multiple Part-Time Jobs

Someone working 30 hours at Job A, 25 at Job B, 25 at Job C must coordinate documentation from three employers.

### MCO Verification Concierge

**Recommended approach:** Managed care plans serve as verification intermediaries.

**Process:**
- Member authorizes MCO to gather verification on their behalf
- Care coordinator contacts all employers
- MCO consolidates data and submits to state as single transaction
- Member sees combined total in portal

**Payment:** Include verification support costs in capitation rates.

**Alternative for FFS:** State creates navigator positions specifically to assist people with multiple employment sources.

## Informal and Cash Economy Work

Babysitting, yard work, house cleaning, handyman work often paid cash with no documentation.

### Community Verification Model

**Option A - Client attestation:**
- Worker provides letters from customers/clients confirming work
- Similar to self-employment client letters
- Challenge: Requires customers willing to document

**Option B - Community organization intermediary:**
- Trusted community organizations (churches, neighborhood groups) verify work performed
- Organization representatives act as credentialed submitters
- Challenge: Requires building relationships with many community organizations

**Option C - Self-attestation with neighbor confirmation:**
- Worker self-reports hours
- Provides contact info for 2-3 neighbors/community members who can confirm
- State spot-checks via phone calls to confirmers
- Challenge: Creates burden on community members

**Option D - Lower standards, higher audits:**
- Accept self-reporting with minimal documentation
- 30% random audit rate requiring detailed follow-up
- Focus on pattern detection (someone claiming 80 hours of yard work in January in Minnesota gets audited)
- Challenge: Higher fraud risk

**Recommended rule:** Combination of Options A, B, and D. Community organization intermediaries where possible, client attestation for ongoing relationships, self-attestation with high audit for sporadic work.

**Recognition:** Some legitimate work cannot be documented through traditional means. Choice is between excluding this work (forcing people to only traditional employment) or accepting some fraud risk to avoid excluding legitimate informal workers.

## Educational Activities

### College and University

**Full-time student (12+ credit hours):**
- Educational institution submits enrollment data automatically
- Counts as full compliance (meets 80-hour monthly requirement)
- Verification: National Student Clearinghouse data OR direct institutional reporting

**Part-time student:**
- Credit hours convert to actual hours (3 credit hours = 9 hours weekly including study time)
- Counts toward requirement proportionally
- Example: 6 credit hours = 18 hours weekly = 72 hours monthly, person needs 8 additional hours from work/volunteering

**Implementation:** Data sharing agreements with institutions. Most already report to National Student Clearinghouse for financial aid.

### Vocational and Trade Programs

**Programs meeting 20+ hours weekly:**
- Count as full compliance
- Verification: Program enrollment and attendance data

**Programs under 20 hours weekly:**
- Count at actual attendance hours toward requirement
- Verification: Program attestation of hours

### GED and ESL Programs

**Count hour-for-hour as qualifying activity.**
- Verification: Program attendance records
- Many expansion adults need GED or English language skills for employment - should count

### Job Training and Workforce Development

**Formal programs through workforce system:**
- Automatic verification through workforce agency data sharing
- Count hour-for-hour

**Apprenticeships:**
- Count as full compliance (combination of work and training)
- Verification: Apprenticeship program attestation

## Volunteer and Community Service

### Credentialed Organization Model

**Nonprofit organizations register with state to submit volunteer hours:**

**Qualifying organizations:**
- 501(c)(3) nonprofits
- Government agencies
- Schools
- Faith-based organizations (churches, synagogues, mosques, temples)
- Community organizations

**Registration process:**
- Online registration providing EIN and organization details
- Verification of nonprofit status
- Designate authorized submitter
- Training on submission process

**Ongoing verification:**
- Organization submits volunteer hours monthly via portal
- Includes volunteer name, SSN/Medicaid ID, hours volunteered, dates, type of activity
- Organization confirms volunteer work was performed and meaningful

**Hours counted:**
- Direct service hours (serving food, tutoring, building homes, etc.)
- Administrative volunteer work (event planning, outreach, fundraising)
- Exclude purely social activities (attending religious services doesn't count, but setting up for services does)

## Job Search Documentation

### Traditional Job Search

**Qualifying activities:**
- Submitting applications (1 hour per application)
- Attending interviews (2 hours per interview including travel)
- Attending job fairs (actual hours attending)
- Networking events for job seekers (actual hours)

**Documentation options:**

**Option A - Detailed:**
- Copy of each application submitted
- Interview confirmation emails
- Job fair attendance proof
- Maximum 40 hours monthly from job search

**Option B - Attestation:**
- Self-report job search activities
- Provide contact info for employers contacted
- 20% random audit verifies contacts
- Maximum 40 hours monthly

**Option C - Workforce agency:**
- Registration with state workforce agency
- Job search activities documented through workforce system
- Count hour-for-hour up to 40 monthly

**Recommended rule:** Option C as primary (workforce agency documentation), Option B (attestation with audit) as backup, maximum 40 hours monthly from job search alone.

**Rationale:** Job search is legitimate activity but full-time job searching (80 hours) is less productive than combining moderate search (40 hours) with volunteer work or training.

## Monthly vs. Real-Time Reporting

**Traditional monthly:** Individual responsible for submitting all verification once monthly by deadline.
- Arkansas model
- High burden, procrastination risk, late submissions

**Real-time continuous:** Employers and organizations submit as work occurs throughout month.
- Member can check portal anytime to see current status
- Early warning if falling behind pace
- Proactive intervention possible

**Recommended rule:** Real-time submission by credentialed submitters. Individual portal shows cumulative monthly total updating as verification submitted. Mid-month notifications if below pace.

**Example notification:** Text message on 20th of month: "You're at 45 hours with 10 days remaining. Check your portal to see options for additional qualifying activities."

## Mixed Activities Reporting

### Combining Multiple Sources

Someone works 40 hours at part-time job, volunteers 20 hours, attends GED class 15 hours. Three different verification sources.

**System requirements:**
- Aggregate hours from all sources automatically
- Display breakdown by activity type
- Handle simultaneous submissions from multiple sources
- De-duplicate if same hours reported from multiple sources

**Member portal view:**
```
Current Month Status:
Employment: 40 hours (Verified by ABC Company)
Education: 15 hours (Verified by Adult Ed Center)  
Volunteer: 20 hours (Verified by Community Kitchen)
Total: 75 hours / 80 required
Days remaining: 8
```

## Verification Timing and Deadlines

### Submission Deadlines

**Option A - End of month:**
- All verification for month due by last day of month
- Challenge: Late-month work can't be verified in time

**Option B - 10 days after month end:**
- Verification for January due February 10th
- Allows time for end-of-month hours to be verified
- Challenge: Delayed determination of compliance

**Option C - Rolling deadline:**
- Verification due within 10 days of work being performed
- Continuous compliance rather than monthly snapshots
- Challenge: More complex tracking

**Recommended rule:** Verification due by 10th of following month. Example: January hours verified by February 10th. This allows end-of-month work to be documented while maintaining reasonable timelines.

**Grace period:** If verification submitted 11th-15th (up to 5 days late), person receives warning but maintains coverage. After 15th, coverage consequences begin.

## Non-Compliance and Cure Periods

### Falling Below 80 Hours

**What happens when someone doesn't meet requirement:**

**Option A - Immediate suspension:**
- Coverage suspends first day of following month
- Must submit verification showing compliance before coverage reinstates
- Challenge: Harsh, no second chances

**Option B - Warning month:**
- First month of non-compliance triggers warning
- Coverage continues
- Second consecutive month triggers suspension
- Challenge: May delay addressing actual barriers

**Option C - Cure period:**
- Non-compliance triggers 30-day cure period
- Must submit plan for how will meet requirements going forward
- Can make up deficit hours or apply for exemption
- Coverage continues during cure period
- Challenge: Administrative complexity

**Recommended rule:** Warning month (Option B) for first instance. Cure period (Option C) for second consecutive month. Immediate suspension only after three consecutive months of non-compliance without engaging cure process.

**Rationale:** One missed month likely represents temporary situation. Multiple consecutive months suggests genuine barrier requiring different approach (exemption or additional support).

## Reasonable Modifications and Accommodations Framework

### Georgia's Innovation: Variable Hour Requirements

Georgia's 2025 Pathways refinement introduced "reasonable modifications" allowing individualized hour requirements for people who can work but cannot consistently meet 80 hours monthly due to disability or medical conditions. This framework bridges the gap between full exemption and standard requirements.

**The gap being filled:**
- Someone with disability preventing 80 hours but could work 40-60 hours
- Someone recovering from major medical intervention needing graduated return
- Someone with episodic condition having good months and bad months
- Someone with chronic pain managing 15 hours weekly but not 20+

Without reasonable modifications, these individuals face binary choice: claim inability to work (exemption) or attempt full requirements and fail repeatedly. Modifications provide middle ground recognizing partial capacity.

### Graduated Return to Work After Major Medical Interventions

**Major surgical procedures requiring hospitalization:**

**Month 1 post-surgery:** 0 hours required (recovery)
**Month 2:** 20 hours required (limited return)
**Month 3:** 40 hours required (half-time)
**Month 4:** 60 hours required (three-quarter time)
**Month 5 onward:** 80 hours required (full requirement)

**Examples qualifying:**
- Organ transplant surgery
- Cardiac procedures (CABG, valve replacement)
- Orthopedic surgery (joint replacement, spinal fusion)
- Cancer surgery with ongoing treatment
- Major abdominal surgery
- Neurological surgery

**Documentation:** Surgeon provides letter specifying procedure and expected recovery timeline. Modifications applied automatically based on clinical recommendation.

**Extensions:** If complications arise, surgeon can extend graduated timeline an additional 1-3 months via simple attestation.

**Cancer Treatment Protocol:**

**Active chemotherapy/radiation:**
**Treatment weeks:** 0 hours required
**Recovery weeks between cycles:** 20-40 hours required based on tolerance
**Post-treatment:** 60 hours for 2 months, then 80 hours

**Documentation:** Oncologist provides treatment schedule and functional capacity assessment. System automatically adjusts requirements based on treatment calendar.

**Mental Health Stabilization:**

**Post-psychiatric hospitalization:**
**Month 1:** 0 hours required (immediate stabilization)
**Month 2:** 20 hours required (gradual engagement)
**Month 3:** 40 hours required
**Month 4:** 60 hours required
**Month 5 onward:** 80 hours OR continued modification if partial capacity documented

**Maintenance phase for serious mental illness:**
- Someone stable on medication but unable to work full-time
- Psychiatrist attests to partial capacity (e.g., 50 hours monthly sustainable)
- Modified requirement applied ongoing with annual review

**Documentation:** Psychiatrist or psychiatric nurse practitioner attestation of stabilization timeline and sustainable work capacity.

**Substance Use Disorder Recovery Phases:**

**Intensive treatment phase (residential/IOP):** Treatment hours count toward requirement, no additional work needed

**Early recovery (first 6 months post-treatment):**
**Months 1-2:** 40 hours required (half-time allows recovery focus)
**Months 3-4:** 60 hours required (increasing capacity)
**Months 5-6:** 80 hours required (return to standard)

**Rationale:** Early recovery requires treatment engagement, support group attendance, therapy appointments. Full-time work stress creates relapse risk. Graduated approach supports sustained recovery.

**Documentation:** Treatment provider attestation of program completion and recovery status.

**Pregnancy and Postpartum Graduated Return:**

**High-risk pregnancy requiring reduced activity:**
- Provider documents activity restrictions
- Modified requirements based on restrictions (e.g., 40 hours for desk work, no physical labor)
- Applies for duration of pregnancy

**Postpartum return:**
**Months 1-3 postpartum:** 0 hours required (immediate postpartum recovery and infant care)
**Months 4-6:** 40 hours required (gradual return while establishing childcare)
**Months 7-9:** 60 hours required
**Months 10-12:** 80 hours required

**Extension for complications:** C-section, postpartum depression, NICU stay extend graduated timeline automatically.

### Permanent or Long-Term Partial Capacity Modifications

**Disability accommodations (ADA parallel):**

Someone with disability can work but requires modifications to meet requirement:

**Reduced hours based on documented capacity:**
- 40 hours monthly for someone with severe chronic pain managing part-time work
- 50 hours monthly for someone with cognitive disability in supported employment
- 60 hours monthly for someone with progressive MS having functional limitations

**Documentation required:**
- Healthcare provider functional capacity assessment
- Specific hour threshold person can sustain
- Expected duration (ongoing vs. time-limited)
- Review frequency (annually for permanent, semi-annually for evolving conditions)

**Employer verification at modified level:**
- Employer verifies actual hours worked
- Requirement adjusted to person's documented capacity
- No penalty if meets modified requirement even if below 80 hours

**Episodic Condition Averaging:**

For conditions with unpredictable good and bad periods (bipolar disorder, rheumatoid arthritis, migraines, MS, lupus, Crohn's disease):

**Variable monthly requirements averaging over 6 months:**
- Bad month: 20-40 hours required
- Moderate month: 60 hours required
- Good month: 80-100 hours required
- Six-month average: 60 hours required

**Automatic triggers for reduced requirements:**
- Hospitalization: Following month automatically 20 hours
- ED visit: Following 2 weeks reduced to 40 hours monthly equivalent
- Increased rescue medication use (detected via pharmacy claims): Following month 40 hours

**Provider authority:** Treating physician can submit simple modification request: "Patient experiencing exacerbation of [condition]. Recommend 40 hours monthly for next 3 months." Applied automatically.

**Documentation:** Initial assessment documents episodic condition. Ongoing modifications based on healthcare utilization or provider attestation, not repeated applications.

### Structural Accommodations for External Barriers

**Transportation-limited modifications:**

Rural areas without public transportation or areas with limited service:

**Reduced requirements reflecting realistic employment access:**
- Standard: 80 hours monthly
- Modified for transportation barriers: 60 hours monthly (15 hours weekly, one day lost to transportation limitations)

**Documentation:** Geographic determination (rural area designation) plus self-attestation of transportation barrier. No individual vehicle ownership should not be prerequisite for employment.

**Alternative:** Transportation barrier time counts toward requirement. Hours spent traveling to/from work via public transit count at 50% toward requirement (2 hours travel = 1 hour toward requirement).

**Childcare availability accommodations:**

Areas with childcare deserts (counties where childcare availability is less than 30% of need):

**Modified requirements during childcare gaps:**
- Parent can work during school hours but not after-school hours
- Modified to 25 hours monthly during summer when school-year childcare unavailable
- Returns to 60-80 hours during school year

**Documentation:** Geographic childcare availability data plus self-attestation. No requirement to document unsuccessful childcare search.

**Seasonal employment accommodations with carryforward:**

Agricultural workers, tourism workers, ski resort workers with predictable seasonal patterns:

**Annual requirement with seasonal flexibility:**
- Work 160 hours during 2-3 peak months
- Banked hours carry forward through off-season
- Must average 60 hours over 12-month period (720 annually)
- No requirement to find employment during known industry off-season

**Example:** Farm worker works 180 hours in June (harvest), 160 in July, 140 in August = 480 hours banked = covers 6 months at 80/month. Actual requirement: 4 months at 160, 8 months at 0, averages 53/month = meets 60-hour modified annual requirement.

**Documentation:** Employment in recognized seasonal industry plus work pattern history.

### Process for Requesting Reasonable Modifications

**Who can request:**
- Individual directly
- Healthcare provider on behalf of patient
- MCO care coordinator on behalf of member
- Employer on behalf of employee (with employee authorization)

**Documentation required:**

**For medical modifications:**
- Provider letter or attestation form specifying:
  - Condition affecting work capacity
  - Functional limitations
  - Recommended hour modification
  - Expected duration
  - Review frequency

**For structural modifications (transportation, childcare):**
- Self-attestation plus
- Geographic data (rural designation, childcare desert data) OR
- Documentation of specific barrier (no vehicle, childcare wait lists)

**For graduated return protocols:**
- Provider documentation of qualifying event (surgery, hospitalization, treatment completion)
- Expected recovery timeline
- Automatically applied based on clinical recommendation

**Processing timeline:**
- Modifications requested and reviewed within 10 business days
- Presumptive approval during processing (modified requirement applies pending determination)
- If denied, individual can appeal with coverage continuing at modified level during appeal

### Modification Duration and Review

**Time-limited modifications:**
- Graduated return protocols: Pre-defined timeline, automatic progression
- Acute episode accommodations: 3-6 months with option to extend
- Recovery phases: Specified duration with extension available

**Ongoing modifications:**
- Permanent partial capacity: Annual review
- Episodic conditions: Semi-annual review of continued appropriateness
- Structural barriers: Annual review, automatic renewal if geographic barriers persist

**Review process:**
- Provider submits brief update on functional status
- Individual confirms modification still needed
- State reviews and continues, adjusts, or ends modification
- Coverage continues during review

**Modification termination:**
- Provider documents capacity improved
- Individual requests return to standard requirement
- Review determines modification no longer needed
- 30-day notice before returning to standard requirement

### Reasonable Modification vs. Full Exemption

**Clear distinction needed:**

**Modification appropriate when:**
- Person has partial capacity to work
- Barrier is to meeting 80 hours, not working at all
- Some work hours feasible with accommodation
- Time-limited recovery or graduated return anticipated

**Full exemption appropriate when:**
- Person cannot work at all
- Medical condition prevents any employment
- Barrier is to working, not just to meeting hours
- Permanent or long-term inability

**Provider guidance:**
"Can this person work some hours, or cannot work at all? Modifications for partial capacity. Exemptions for no capacity."

**Individual choice:**
Person with partial capacity can choose:
- Request modification and work at reduced level
- Request full exemption claiming inability to work
- Attempt standard 80-hour requirement

Modification is accommodation, not requirement. People not required to use modifications if they prefer to attempt full hours or claim exemption.

### Technology Requirements for Modifications

**System must support:**
- Variable hour requirements by individual
- Graduated timelines automatically adjusting monthly
- Averaging over multiple months (6-12 month windows)
- Carryforward banking for seasonal workers
- Automatic triggers based on healthcare utilization
- Provider portal for modification requests
- Modification status visible to individual in real-time

**Member portal displays:**
- Current modified requirement (if applicable)
- Timeline for graduated increases (if applicable)
- Banked hours from previous months (if applicable)
- Modification expiration date and review schedule
- How to request modification or renewal

**Employer portal shows:**
- Modified requirement for each employee (if applicable)
- Verification against modified standard, not 80 hours
- Clear indication that meeting modified requirement = compliance

### Monitoring and Evaluation

**Track modification utilization:**
- How many people request modifications?
- What types of modifications most common?
- Approval rates by modification type
- Demographics of people using modifications
- Employment outcomes for people with modifications vs. exemptions vs. standard requirements

**Success metrics:**
- Coverage retention rates for people with modifications
- Progression from modifications to standard requirements (graduated return success)
- Employment stability for people with partial capacity modifications
- Provider satisfaction with modification process

**Adjustment triggers:**
If certain modifications are widely needed, consider whether standard requirement should be adjusted for entire population rather than individualized accommodations.

### Legal Foundation: ADA and Rehabilitation Act Parallels

**Americans with Disabilities Act principles applied:**
- Reasonable accommodation for people with disabilities
- Interactive process determining appropriate accommodation
- Individualized assessment, not categorical exclusions
- Accommodation enables participation rather than excluding people

**Medicaid context:**
- Work requirements without modifications may violate ADA by excluding people with disabilities from program
- Modifications as reasonable accommodation allowing people with partial capacity to participate
- States must provide modifications as accommodation, not discretionary benefit

**Federal approval considerations:**
- CMS likely to favor modification frameworks as ADA compliance
- Demonstrates good faith effort to accommodate disability
- Reduces risk of litigation challenging work requirements as discriminatory

### State Variation in Modification Approaches

**Georgia model (pioneering):**
- Individualized modifications based on caseworker discretion
- Provider-recommended hour adjustments
- Graduated return protocols
- Annual review

**Recommended enhancements:**
- Standardize graduated return protocols (remove discretion)
- Automatic triggers for episodic conditions
- Clear documentation standards reducing subjective assessment
- Technology-enabled modification tracking

**Alternative state approaches:**

**California (if implementing):** Likely to emphasize broad modifications, liberal approval, maximum accommodation. Structural modifications for transportation, childcare, language barriers as well as medical.

**Texas (if implementing):** Likely more restrictive modifications, requiring extensive documentation, shorter duration, frequent reviews. Emphasis on time-limited modifications over ongoing adjustments.

**Recommendation for all states:** Start with Georgia's framework. Add standardized protocols for common situations (surgery recovery, mental health stabilization). Build in automatic triggers. Expand to structural accommodations. Make modifications accessible through simple processes.

## Audit and Verification Integrity

### Random Audit Protocols

**Self-reported activities:** 15-20% random audit rate
**Employer verification:** 5% random audit rate
**Educational verification:** 2% random audit (institutions less likely to misreport)
**Volunteer verification:** 10% random audit rate

**Audit process:**
- Computer randomly selects cases monthly
- Auditor requests supporting documentation
- Reviews for consistency and accuracy
- Identifies patterns suggesting fraud
- Refers suspected fraud to special investigations unit

**Audit findings used to:**
- Improve system (identify common errors)
- Provide additional training to submitters
- Detect systematic fraud (fake employers, document mills)
- Not primarily for individual recoupment unless fraud clear

### Employer Accuracy Requirements

**Employers must certify data accuracy:**
- Hours submitted reflect actual hours worked
- Employee SSN/Medicaid ID verified
- Payroll records support hours claimed

**Penalties for false reporting:**
- Warning for first instance if unintentional
- Temporary suspension of submission privileges for repeated errors
- Referral to fraud prosecution for intentional false reporting
- Employers not liable for good-faith errors

**Safe harbor:** Employers relying on standard payroll systems and submitting data as recorded are protected from liability even if data contains errors they couldn't reasonably detect.

## Technology Infrastructure Requirements

### State System Specifications

**API capabilities:**
- RESTful API accepting JSON data
- Authentication via OAuth 2.0
- Rate limiting (prevent system overload)
- Error messages in plain language
- Sandbox environment for testing before production

**Employer portal:**
- Web-based, mobile-responsive
- Compatible with all modern browsers
- No special software required
- Average page load time under 2 seconds
- 99.5% uptime guarantee

**Member portal:**
- Mobile app (iOS and Android) and website
- Real-time status updates
- Push notifications for warnings
- Document upload via smartphone camera
- Multiple language support

**Data security:**
- Encryption in transit (TLS 1.3)
- Encryption at rest (AES-256)
- HIPAA compliant
- SOC 2 Type II certified
- Regular security audits

### Integration Requirements

**Data sources requiring integration:**
- Social Security Administration (SSI/SSDI data)
- Department of Labor (unemployment insurance)
- Department of Corrections (incarceration)
- Educational institutions (National Student Clearinghouse)
- Workforce development system
- SNAP employment & training program
- Child welfare (foster care placements)

**Integration timeline:**
- Data sharing agreements executed by March 2026
- Technical integration complete by August 2026
- Testing complete by October 2026

## Communication and Support Infrastructure

### Member Communications

**Advance notification (90 days before implementation):**
- Letter explaining requirements and exemptions
- Available in threshold languages
- 6th grade reading level
- QR code to video explainer

**Monthly status notifications:**
- Text message showing hours verified so far
- Email with detailed breakdown
- Portal alerts for status changes

**Warning notifications:**
- Text and email when falling behind pace
- List of nearby resources to close gap
- Phone number for navigator assistance

**Multilingual support:**
- Translation of all materials into threshold languages (5%+ of population)
- Bilingual navigator support available
- Telephonic interpretation for 200+ languages

### Employer Support

**Help desk for employers:**
- Phone support 8am-6pm Monday-Friday
- Email support with 24-hour response time
- Chat support during business hours
- FAQ database and tutorials

**Outreach to industries:**
- Restaurant association partnerships
- Construction industry outreach
- Retail sector briefings
- Home health agency coordination
- Agricultural employer seasonal preparation

## State Variation Across Federal Parameters

Federal law requires monthly work requirements but allows state flexibility in implementation. States should decide:

**Hour thresholds:**
- 80 hours monthly (typical)
- Or adjust based on state minimum wage and cost of living
- Lower threshold (60 hours) in high-wage states
- Higher threshold (100 hours) in low-wage states

**Qualifying activities:**
- Employment (universal)
- Education (most states include)
- Job training (most states include)
- Volunteer work (some states, with limits)
- Community service (some states, with limits)
- Caregiving (not typically counted as "work" but exemption pathway instead)
- Job search (some states, with limits)

**Verification frequency:**
- Monthly verification (most common)
- Quarterly verification (reduces burden but delays detection)
- Real-time continuous (most supportive but most complex)

## Implementation Timeline

**Q1 2026 (January-March):**
- Finalize verification policies
- Execute data sharing agreements
- Begin employer outreach

**Q2 2026 (April-June):**
- Build technical infrastructure
- Develop portals and APIs
- Create training materials

**Q3 2026 (July-September):**
- Employer registration and credentialing
- Staff training
- System testing

**Q4 2026 (October-November):**
- Pilot with 1,000-5,000 individuals
- Soft launch with high tolerance for errors
- Rapid iteration based on feedback

**December 2026:**
- Full implementation
- First month grace period (warnings, no terminations)

**Q1 2027 (January-March):**
- Monitor closely for problems
- Adjust policies based on real-world experience
- Monthly stakeholder feedback sessions

---

*Next in series: Article 7C, "Coordination and Timing Rules"*

*Previous in series: Article 7A, "Exemption Rulemaking Handbook"*

## References

1. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts on Coverage, Employment, and Affordability of Care." Health Affairs, vol. 39, no. 9, 2020, pp. 1522-1530.

2. Government Accountability Office. "Medicaid Demonstrations: Evaluation of Arkansas Work Requirement." GAO-20-149, November 2019.

3. National Conference of State Legislatures. "Medicaid Work Requirements: State Approaches." NCSL.org, 2025.

4. Urban Institute. "Understanding Gig Economy Work and Medicaid Work Requirements." Urban.org, March 2025.

5. Kaiser Family Foundation. "Medicaid Work Requirements: Key Questions." KFF.org, September 2025.

6. Center on Budget and Policy Priorities. "Work Requirement Verification Systems: Lessons from SNAP and TANF." CBPP.org, April 2025.

7. U.S. Department of Labor. "API Documentation for Unemployment Insurance Data Sharing." DOL.gov, 2025.

8. National Student Clearinghouse. "Enrollment Verification for Government Programs." StudentClearinghouse.org, 2025.

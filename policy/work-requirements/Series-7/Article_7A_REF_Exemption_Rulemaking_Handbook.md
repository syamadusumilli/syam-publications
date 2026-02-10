# Work Requirements Article 7A

# Exemption Rulemaking Handbook
*Complete guide to exemption policy choices for state regulators*

State regulators writing exemption rules for December 2026 implementation face hundreds of specific decisions. This handbook provides decision frameworks, implementation requirements, and recommended approaches for each exemption category and edge case.

## Design Principles Framework

Four principles should guide all exemption rulemaking:

**Presumptive access:** When in doubt, presume people qualify and verify later through audits rather than creating documentation barriers upfront.

**Functional over categorical:** Focus on whether someone can consistently work 80 hours monthly, not whether they fit rigid diagnostic categories.

**Proactive over reactive:** Identify likely-exempt populations through data and reach out, rather than waiting for applications.

**Grace over enforcement:** Build transition periods, grace periods, and second chances into every process.

## Safe Harbor Exemptions (Automatic)

### Age-Based Exemptions

**Federal parameters:** States may exempt adults under 19 and over specified age (typically 50-65).

**State choice - Lower threshold:**
- Under 19 (universal)
- Under 24 if full-time student (optional state choice)

**State choice - Upper threshold:**
- Age 50: Acknowledges age discrimination in hiring, addresses reality that many cannot work into 60s
- Age 55: Moderate approach
- Age 60: Mirrors Social Security early retirement
- Age 65: Aligns with Medicare eligibility

**Recommended rule:** Under 19 mandatory, over 60 automatic exemption.

**Transition handling:**
- Someone turning 19 gets 90-day grace period before requirements begin
- Someone turning 60 gets automatic exemption without application

**Implementation specs:**
- Eligibility system checks birth date against thresholds
- Automatic exemption flag, no individual action required
- Advance notice 60 days before 19th birthday explaining upcoming requirements
- Monthly age calculation to catch birthdays

### Social Security Disability (Automatic)

**SSI recipients:** States already receive SSI data for Medicaid eligibility. Expand exemption rules to automatically exempt SSI recipients.

**SSDI recipients:** Requires Medicare Entitlement Data from CMS showing disability as basis for Medicare qualification.

**Recommended rule:** Automatic exemption for anyone receiving Social Security disability benefits (SSI or SSDI) without individual application.

**Implementation requirements:**
- Data sharing agreement with SSA (finalize by March 2026)
- Medicare Entitlement Data import and matching to Medicaid files
- Quarterly data refresh updating exemption status
- Manual review process for discrepancies

**Edge case - Disability work attempts:** Someone receiving SSDI may attempt work during trial work period. Maintain exemption during trial work period automatically.

### Children in Household (Automatic)

**Age-based caregiver exemptions:**

**Option A - Restrictive:** Children under 1 only
**Option B - Moderate:** Children under 6 (Georgia 2025 model)
**Option C - Expanded:** Children under 13 (Arkansas proposal)

**Recommended rule:** Automatic exemption for parents/guardians of children under 6.

**Implementation:**
- Birth records integration for automatic identification
- Custody/guardianship data from child welfare systems
- Grace period: child turns 6, parent gets 90-day grace period before requirements begin

**Special needs extension:** Parents of children with disabilities exempt regardless of child's age. Triggers:
- Child receives SSI
- Child on Medicaid disability waiver
- Child has IEP documenting substantial limitations

## Medical Exemptions

### Medical Frailty Definitions

**State choice between three approaches:**

**Approach A - Diagnosis list:** State specifies qualifying conditions (schizophrenia, intellectual disability, advanced cancer, severe COPD requiring oxygen, advanced heart failure, etc.). Anyone with listed condition qualifies automatically if diagnosed.

- Pros: Clear criteria, simple documentation
- Cons: Over-inclusive (mild cases exempt), under-inclusive (unlisted conditions denied)

**Approach B - Functional assessment:** Exemption based on provider attestation that person cannot consistently meet 80 hours monthly regardless of specific diagnosis.

- Pros: Focuses on actual capacity, allows clinical judgment
- Cons: More subjective, variable across providers

**Approach C - Hybrid:** Automatic for severe conditions (SSI disability, active cancer treatment, hospitalized mental illness, organ failure). Function-based for others via provider attestation.

- Pros: Combines certainty with flexibility
- Cons: Two-tier system complexity

**Recommended rule:** Hybrid approach.

**Automatic medical exemptions (no application):**
- Active cancer treatment (chemotherapy, radiation)
- Organ failure requiring transplant listing
- Recent psychiatric hospitalization (within 90 days)
- Anyone receiving home health services
- Hospice recipients

**Provider attestation for other conditions:**
- Single-page checkbox form
- "I attest that due to medical conditions, this patient cannot consistently meet 80-hour monthly work requirements"
- No detailed diagnosis required, just functional limitation confirmation
- 5% random audit requiring additional documentation

### Temporary and Partial Disability

**Temporary disability rules:**

**Surgical recovery:**
- Automatic 90-day exemption for anyone with surgery requiring hospitalization
- Extended automatically if complications documented
- No separate application, triggered by claims data

**Major medical interventions:**
- Organ transplant: 12 months automatic
- Cardiac procedures (CABG, valve replacement, stent): 6 months
- Orthopedic surgery (joint replacement, spinal fusion): 6 months
- Cancer surgery: Duration of treatment plus 6 months
- Stroke: 6 months minimum, extended based on recovery trajectory

**Pregnancy and postpartum:**
- Pregnancy: automatic exemption entire pregnancy
- Postpartum: 12 months after delivery (not 6 weeks)
- Pregnancy complications requiring bed rest: exemption from diagnosis through 6 months postpartum
- Miscarriage or pregnancy loss: 90-day exemption
- NICU stay for infant: exemption extended through hospital discharge plus 90 days

**Acute illness requiring hospitalization:**
- Any hospitalization triggers 30-day exemption automatically
- Extended via provider attestation if needed
- No application required, claims data triggers exemption

**Partial disability framework:**

Someone with disability can work some hours but not 80 monthly. Three approaches:

**Option A - Variable hours:** Reduced requirement (40 hours) with employer verification during periods of partial capacity

**Option B - Averaging:** Person must average 60 hours over 6-month period, allowing flexibility for good/bad months

**Option C - Episodic accommodation:** Healthcare utilization triggers (hospitalization, ED visits, medication fills) automatically activate temporary full exemption during acute episodes

**Recommended rule:** Combination. Variable hour accommodation (40-60 hours based on documented capacity) with automatic episodic triggers for acute exacerbations.

### Episodic Conditions

Conditions with unpredictable good and bad periods: bipolar disorder, multiple sclerosis, rheumatoid arthritis, migraines, Crohn's disease, lupus.

**Recommended approach:**

**Initial documentation:** Provider completes functional assessment documenting episodic condition and variable capacity.

**Ongoing exemption:** Presumed continuing, annual review (not semi-annual) sufficient.

**Automated triggers:** Healthcare utilization activates temporary exemption without application:
- Hospitalization: 60-day automatic exemption
- ED visit: 14-day automatic exemption
- Pharmacy fills for rescue medications increased: 30-day automatic exemption

**Provider authority:** Treating physician can extend exemption during exacerbations via simple portal submission, effective immediately.

**Variable averaging:** Person can meet 40 hours during bad months, 80+ during good months, averaging 60 over six-month periods.

## Caregiver Exemptions

### Adult and Elder Care

**Care recipient qualification:**

**Option A - ADL-based:** Care recipient cannot perform 2+ activities of daily living (bathing, dressing, eating, toileting, transferring, continence) without assistance

**Option B - LTSS-based:** Care recipient receives Medicaid LTSS or qualifies for nursing home level of care

**Option C - Attestation:** Caregiver self-attests to providing 20+ hours weekly unpaid care for person with substantial functional limitations

**Recommended rule:** Care recipient qualifies if receiving LTSS through Medicaid OR has medical documentation of inability to perform 2+ ADLs. Caregiver provides self-attestation of care provision.

**Documentation:** Medical provider confirms care recipient has functional limitations requiring caregiving (not detailed medical records). Caregiver completes self-attestation.

**Spot verification:** 10% random sample contacts care recipients to confirm caregiving arrangement exists.

### Kinship and Foster Care

**Kinship caregivers:** Grandparents, aunts/uncles, siblings, or other relatives serving as primary caregivers.

**Challenges:**
- May lack legal guardianship
- Limited access to medical records
- Didn't plan for caregiving role

**Recommended accommodation:** Accept kinship care affidavit from child welfare agency OR school enrollment showing kinship caregiver as primary contact OR medical provider confirmation of caregiving relationship. Don't require formal guardianship.

**Foster parents:**
- Automatic exemption for foster parents of children under 6
- Automatic exemption for foster parents of children with disabilities regardless of age
- Documentation: foster care placement letter from agency

### Aging Out and Transition Ages

**18-21 transition:** Many young adults with disabilities don't achieve independence at 18.

**Recommended rule:** Parents of children with disabilities exempt through child's 21st birthday if:
- Young adult receives SSI
- Young adult on disability waiver
- Provider documents continued caregiving needs

**Grace period:** When child ages out (turns 21, moves to independent living, etc.), parent gets 6-month grace period before requirements resume.

## Substance Use Disorder Treatment

### Treatment Program Definitions

**Residential treatment:** Person enrolled in licensed residential SUD facility. Verification: facility enrollment data.

**Intensive outpatient (IOP):** Programs meeting 9+ hours weekly. Verification: program enrollment and attendance.

**Outpatient treatment:** Individual or group counseling at least 2 hours weekly. Verification: provider attestation.

**Medication-assisted treatment (MAT):** Receiving methadone, buprenorphine, or naltrexone for opioid use disorder with counseling component. Verification: prescriber confirmation.

**Peer support:** Mutual aid groups (AA/NA). Cannot be sole basis for exemption (no verifiable documentation) but can supplement other treatment.

**Recommended rule:** Exemption for anyone in residential, IOP, or receiving MAT with counseling. Outpatient qualifies if attending 2+ hours weekly.

### Duration and Recovery Support

**Active treatment:** Exemption continues for duration of active treatment participation.

**Post-treatment transition:** Exemption continues 6 months after treatment completion. This recognizes early recovery fragility and employment stress during this period creates relapse risk.

**Relapse accommodation:** If someone relapses and re-enters treatment, exemption reinstates immediately without counting as "new" exemption or penalizing previous exemption use.

### Documentation and Privacy

**42 CFR Part 2 compliance:** SUD treatment records have additional federal privacy protections.

**Recommended approach:**
- Treatment provider confirms enrollment without disclosing diagnosis
- Person signs standard consent allowing provider to verify participation to state Medicaid agency
- Consent form limited to enrollment/attendance verification only, not detailed treatment records

## Domestic Violence and Safety

### Documentation Standards

Five options from most to least restrictive:

**Option A - Police report required:** Excludes survivors who don't involve law enforcement
**Option B - Protective order required:** Excludes those who haven't accessed courts
**Option C - Shelter verification required:** Excludes those staying with family/friends
**Option D - Provider attestation:** Healthcare provider, counselor, DV advocate confirms person fleeing DV
**Option E - Self-attestation:** Survivor attests to fleeing DV, no external verification

**Recommended rule:** Provider attestation from any licensed healthcare provider, counselor, DV advocate, or social worker. Self-attestation accepted if person cannot safely access provider due to isolation or immediate danger, with follow-up review within 60 days.

**No requirements for:** Police reports, protective orders, shelter stay, or details about abuse circumstances.

### Duration and Renewal

DV situations don't resolve on predictable timelines. Safety concerns may persist for years.

**Recommended rule:**
- Initial exemption: 6 months
- Renewal: Indefinite 6-month renewals based on provider attestation or self-attestation that safety concerns continue
- No limit on renewal count
- Transition grace period: If safety improves and exemption ends, 90-day grace period before requirements begin

## Geographic and Economic Exemptions

### High Unemployment Areas

**Geographic definition options:**
- County level (BLS data available)
- ZIP code level (more granular, data less reliable)
- Labor market area (crosses county lines)

**Recommended rule:** County-level determination, updated quarterly. County qualifies if unemployment rate exceeds 10% for two consecutive quarters.

**Verification:** Automatic exemption for all residents of qualifying counties based on address. No individual attestation or job search documentation required.

**Rationale:** Purpose is acknowledging structural labor market failure, not assessing individual effort.

### Seasonal Workers

**Challenge:** Work concentrated in certain months (agricultural harvest, tourism peak season, holiday retail).

**Recommended accommodation:**
- Annual hour requirement (960 annually) instead of monthly (80 monthly)
- Hour banking: excess hours in high months cover shortfalls in low months
- Known off-season exemptions: automatic exemption during documented industry off-seasons

**Implementation:** Employment history data identifies seasonal workers. System automatically applies annual averaging without requiring application.

## Education and Training

### Student Status

**Full-time student definition:** 12+ credit hours per semester in degree-granting program OR vocational/trade program meeting 20+ hours weekly.

**Part-time student:** Counts toward requirements at hour-for-hour rate (3 credit hours = ~9 classroom hours per week including study time).

**Verification:** Educational institution enrollment data automatically reported to state system.

**Transition periods:**
- Between semesters: Grace period through end of semester plus 30 days
- Graduation: Grace period of 90 days after graduation before work requirements begin
- Program completion: Same 90-day grace period for vocational/trade programs

**GED and ESL programs:** Count as qualifying activities at actual attendance hours.

## Incarceration and Justice Involvement

### Incarcerated Individuals

**Federal law:** Automatically exempt while incarcerated.

**Release transition:** Critical gap between release and employment.

**Recommended rule:**
- Exemption continues 90 days post-release automatically
- Can be extended to 180 days if enrolled in reentry program
- No application required, triggered by corrections data

**Implementation:** Data sharing with Department of Corrections, automatic exemption flag based on incarceration status.

### Probation and Parole

People on probation/parole face complex reporting requirements, restrictions on employment type, and unpredictable court dates.

**Recommended rule:** Automatic exemption during first 6 months of probation/parole. After 6 months, variable hour accommodation (40 hours minimum instead of 80) recognizing ongoing constraints.

**Drug court and diversion programs:** Participation counts as qualifying activity hour-for-hour.

## Homelessness

### Documentation Challenges

Without stable address, portal access, document storage, or consistent provider relationships.

**Recommended accommodations:**

**Medical exemption presumed:** Anyone documented as homeless in HMIS (Homeless Management Information System) presumed to qualify for medical exemption (mental illness, substance use, chronic health conditions highly correlated with homelessness).

**Verification through outreach:** Street outreach teams and shelter staff authorized to submit verification/exemptions on person's behalf with consent.

**Portal alternatives:** Phone-based reporting, verbal attestation recorded by shelter staff, health plan care coordinator submission.

**Address requirements waived:** Accept shelter address, general delivery, or "care of" community organization address for correspondence.

**Grace period on housing:** Upon obtaining housing, 90-day exemption to stabilize before requirements begin.

## Military and Veterans

### Active Duty Spouses

**Frequent relocations:** Military families relocate every 2-3 years, disrupting employment.

**Deployment caregiving:** Spouse becomes sole caregiver during deployment.

**Recommended rule:**
- Spouses of deployed service members: automatic exemption during deployment plus 90 days post-deployment
- Spouses who relocated due to military orders within past 12 months: automatic exemption
- Verification: Military ID and deployment/relocation orders

### Veterans with Service-Connected Disabilities

**VA disability ratings:** Veterans with service-connected disabilities receive disability ratings from VA (0-100%).

**Recommended rule:**
- VA disability rating 30%+: automatic exemption
- Verification: VA benefits data, no separate application required
- State Medicaid agency obtains VA data through interagency agreement

### Reserve and Guard

**Drilling requirements:** Monthly drill weekends and annual training periods.

**Recommended accommodation:** Drill and training time counts toward work requirements hour-for-hour, verified through military unit.

## Immigration Status

### Mixed-Status Families

Families where some members are documented and others undocumented may fear any government interaction.

**Recommended accommodation:**
- Exemption applications don't require immigration status disclosure for any household member
- Clear communication that work verification won't be shared with immigration enforcement
- Accept verification through community organization intermediaries trusted in immigrant communities
- Multilingual materials in threshold languages

### DACA Recipients

May face work restrictions or uncertainties about employment authorization.

**Recommended rule:** Employment authorization documents showing DACA status trigger streamlined verification process. Renewals during EAD gaps trigger automatic temporary exemption.

### Asylum Seekers and Refugees

May have work authorization but face language barriers, credential recognition issues, and trauma.

**Recommended accommodation:**
- First 12 months in US: automatic exemption (resettlement period)
- Refugee service organization assistance with verification
- Multilingual navigation support

## Language and Literacy

### Beyond Translation

**Non-literate populations:** Cannot complete written applications in any language.

**Recommended accommodations:**
- Verbal applications recorded by navigators or caseworkers
- Video submission explaining circumstances instead of written forms
- Pictographic decision trees showing "work OR exemption = keep coverage"
- Community organization intermediaries for facilitated applications

### Cultural Competency

Different cultures have different help-seeking behaviors, understanding of disability, and comfort with government systems.

**Recommended approach:**
- Community health workers from specific cultural communities
- Culturally adapted materials, not just translated
- Recognition that "disability" concepts vary across cultures
- Faith-based organization partnerships in communities where churches/mosques/temples are trusted

## Terminal Illness and Hospice

### End-of-Life Care

**Recipients in hospice:** Automatically exempt, no renewal required.

**Terminal diagnosis:** Provider attests person has terminal condition, exemption is permanent without periodic review.

**Caregivers for terminally ill:** Automatic exemption, continues through death plus 6 months for bereavement and adjustment.

**Implementation:** Hospice enrollment data triggers automatic exemption. Provider attestation for terminal diagnosis outside hospice enrollment.

## Process Rules Across All Exemptions

### Presumptive Eligibility

**Recommended rule:** Universal presumptive eligibility. All exemption applications maintain coverage during processing.

**Processing timeline:** Determinations within 30 days. If state cannot complete within 30 days, presumptive eligibility continues automatically for additional 30 days. After 60 days, exemption automatically approved if no determination made.

**Appeals:** Coverage continues during appeals automatically.

### Grace Periods

**Medical recovery:** 90 days after medical exemption expires
**Caregiver status ends:** 90 days after caregiving responsibility ends
**Student graduation:** 90 days after program completion
**Treatment completion:** 180 days after SUD treatment ends
**DV safety:** 90 days if safety circumstances improve

### Provider Payment

**Recommended structure:** Flat fee of $35 per exemption attestation, regardless of complexity or whether completed during billable visit.

**Rationale:** Incentivizes participation, compensates provider time, administratively simple.

**Portal requirements:**
- Web-based, no special software
- Single sign-on with common EHR systems
- Mobile-responsive
- Confirmation number upon submission
- Status tracking

### Appeals Process

**Timeline:** 90 days to file appeal after denial. State completes review within 45 days. Expedited appeals (3 days) available for urgent medical need.

**Coverage:** Continues during entire appeal process.

**Independent review:** Medical exemption denials reviewed by medical professional not employed by state. Decision is binding.

**Denial notices:** Must explain specific reason for denial, what documentation could support approval, how to appeal, that coverage continues during appeal. Written at 6th grade reading level.

### Data Matching and Automation

**Automatic exemptions (no application):**
- SSI/SSDI recipient status
- Age qualification
- Incarceration status
- Unemployment insurance receipt
- Child age (for parent exemptions)
- Hospice enrollment
- Recent hospitalization

**Algorithmic flagging for outreach:**
System identifies people likely eligible based on:
- Multiple psychiatric hospitalizations
- Cancer diagnoses
- Multiple chronic condition medications
- Caregiving-related service patterns

**Flags trigger proactive outreach,** not automatic approval.

**Audit protocols:** 5% random audit of automated exemptions annually. Findings improve systems, not primarily for recoupment.

## State Implementation Timeline

**January-March 2026:** Policy development
- Finalize exemption categories
- Draft State Plan Amendment
- Execute interagency data agreements

**April-June 2026:** System development
- Build exemption workflows
- Create provider portal
- Establish data interfaces

**July-September 2026:** Training
- Train eligibility workers
- Train providers
- Test systems

**October-November 2026:** Soft launch with pilot

**December 2026:** Implementation begins with liberal approval standards for first 90 days

---

*Next in series: Article 7B, "Work Verification Rulemaking Handbook"*

*Previous in series: Article 6B, "Managing Dual Eligibles Under Work Requirements"*

## References

1. Centers for Medicare & Medicaid Services. "State Medicaid Director Letter #18-002: Opportunities to Promote Work and Community Engagement." CMS.gov, January 2018.

2. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts on Coverage, Employment, and Affordability of Care." Health Affairs, vol. 39, no. 9, 2020, pp. 1522-1530.

3. Georgia Department of Community Health. "Pathways to Coverage Section 1115 Demonstration." DCH.Georgia.gov, 2023-2025 Updates.

4. Arkansas Department of Human Services. "Arkansas Works Program Section 1115 Waiver - 2025 Revision." DHS.Arkansas.gov, May 2025.

5. Kaiser Family Foundation. "Medicaid Waiver Tracker: Approved and Pending Section 1115 Waivers by State." KFF.org, October 2025.

6. Substance Abuse and Mental Health Services Administration. "42 CFR Part 2: Confidentiality of Substance Use Disorder Patient Records." SAMHSA.gov, 2024.

7. National Health Law Program. "Protecting the Right to Health Care: State Exemption Policy Issues." HealthLaw.org, September 2025.

8. Government Accountability Office. "Medicaid Demonstrations: Evaluations Yielded Limited Results." GAO-24-106490, March 2024.

9. Center on Budget and Policy Priorities. "Taking Away Medicaid for Not Meeting Work Requirements Harms People with Disabilities." CBPP.org, June 2018.

10. Georgetown University Health Policy Institute. "Medicaid Work Requirements: Implementation Lessons from Multiple States." Georgetown.edu, October 2025.

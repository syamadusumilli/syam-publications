# Work Requirements Article 7C

# Coordination and Timing Rules
*Operational coordination requirements for successful implementation*

Exemption and verification rules mean nothing without coordination systems determining when people face requirements, how long they have to respond, what happens during transitions, and who provides support. These coordination choices determine whether implementation is orderly or chaotic.

## Redetermination Scheduling: The Fundamental Choice

Expansion adults face semi-annual redetermination starting January 2027 (six months after December 2026 work requirement implementation). States must decide whether everyone faces redetermination simultaneously or staggered across the year.

### Synchronized Cycles (All renewals in June and December)

**Advantages:**
- Predictable volume spikes enable staffing plans
- Employers know when verification requests arrive
- Community organizations can plan support capacity
- Training and communications occur twice annually
- Clear start/end periods for exemption validity

**Disadvantages:**
- Overwhelming volume in renewal months
- System capacity must handle peak load (costly infrastructure for 2 months/year)
- Provider bottlenecks in June and December
- Impossible to give individualized attention during peaks
- Any system failures affect everyone simultaneously

**Recommended for:** Small states (under 100K expansion adults) where volume is manageable.

### Staggered Cycles (Renewals distributed across 12 months)

**Advantages:**
- Smooths workload across year
- More realistic provider capacity
- System capacity requirements lower (handles average, not peak)
- Staff can provide individualized attention
- System problems affect subset, not entire population
- Continuous learning and improvement

**Disadvantages:**
- Employers face continuous verification requests
- More complex tracking (every member has different renewal month)
- Communications must be individualized, not mass campaigns
- Grace periods and transitions harder to communicate
- Exemption validity periods vary by individual

**Recommended for:** Large states (over 100K expansion adults) where volume requires smoothing.

### Hybrid Approach

**Birth month staggering:**
- Renewal month tied to birth month (born January-June renew June, born July-December renew December)
- Creates two large groups but still enables some messaging efficiency
- Splits volume 50/50 across two months

**Regional staggering:**
- Different counties or regions renew different months
- Enables targeting support resources geographically
- Volume distributed but maintains some economies of scale

**Recommended rule:** Staggered by birth month for states over 500K expansion adults. Synchronized for smaller states.

## Grace Periods Across All Transitions

### First-Time Work Requirements

Someone who never faced work requirements before (newly enrolled, just turned 19, exemption expired) needs transition time.

**Recommended rule:** 90-day grace period before requirements begin. During grace period:
- Receive education about requirements
- Complete exemption applications if qualifying
- Register with workforce system if needed
- Establish employment or qualifying activities
- No coverage consequences during grace period

**Example:** Someone turns 19 on March 15, 2027. Grace period runs through June 15. Work requirements begin June 16, with first compliance determination end of July.

### Job Loss Transition

Someone working full-time loses job unexpectedly.

**Recommended rule:** 60-day grace period from job loss before exemption application required. Allows time for:
- New job search
- Registration for unemployment benefits (which may exempt)
- Assessment of whether barrier is temporary or requires exemption
- Application for exemption if needed

**Implementation:** Job loss detected through employer reporting of zero hours or termination notification. Grace period begins automatically.

### Exemption Expiration

Temporary exemption expires (surgery recovery, treatment completion, caregiver responsibility ends).

**Recommended rule:** Grace period equals original exemption duration, minimum 90 days, maximum 180 days.

**Examples:**
- 30-day surgery recovery exemption: 30-day grace period (total 60 days)
- 6-month SUD treatment exemption: 180-day grace period (total 12 months)
- 12-month pregnancy/postpartum exemption: 180-day grace period (total 18 months)

**Rationale:** Longer exemptions indicate more significant barriers. Recovery/transition after barrier resolves should be proportional.

### Geographic Moves

Someone moves from county with automatic high-unemployment exemption to county without exemption, or vice versa.

**Recommended rule:** 90-day grace period after move before exemption status changes based on geography. Allows time to:
- Find employment in new location
- Understand local resources
- Apply for exemption if still needed despite area employment availability

**Implementation:** Address changes in Medicaid system trigger grace period.

### Between Semesters

Student completes fall semester, spring semester begins in January.

**Recommended rule:** Break periods between semesters covered automatically if:
- Person enrolled for both semesters, OR
- Person enrolled for fall, plans to enroll for spring (intent sufficient)

**Summer break:** 90-day grace period after spring semester. Must enroll for fall OR find employment/qualifying activity by end of grace period.

## Appeals and Dispute Resolution

### Standard Appeals Timeline

**Exemption denials:**
- 90 days to file appeal after denial notice
- Coverage continues during appeal (presumptive eligibility)
- State completes review within 45 days
- Decision letter explains reasoning

**Work verification disputes:**
- 60 days to dispute non-compliance determination
- Coverage continues during dispute resolution
- State reviews disputed hours within 30 days
- Decision letter with findings

**Recommended rule:** Coverage always continues during appeals. Burden of delay falls on state, not individual.

### Expedited Appeals

**Available for urgent medical circumstances:**
- Active treatment at risk if coverage lost
- Chronic condition requiring continuous medication
- Pregnancy
- Mental health crisis

**Timeline:** 3 business days from appeal filing to decision.

**Standards:** Medical director review, presumption in favor of appellant unless clear evidence of ineligibility.

### Independent Medical Review

When exemption denied based on medical determination, person entitled to review by medical professional not employed by state Medicaid agency.

**Reviewer qualifications:**
- Licensed physician in relevant specialty
- Active clinical practice
- No financial relationship with state Medicaid program
- Training on disability determination standards

**Review scope:**
- Access to person's medical records
- Can order additional functional assessments
- Can consult with treating providers
- Decision is binding unless state can show reviewer applied incorrect legal standard

**Timeline:** Completed within 30 days of request.

**Cost:** State pays reviewer fee ($500-1,000 per review).

## Provider Infrastructure and Payment

### Provider Capacity Planning

**Provider workload from work requirements:**
- Exemption initial applications
- Exemption renewals every 6 months
- Exemption extensions for episodic conditions
- Appeals supporting documentation
- Functional assessments

**Estimated workload:** Each exemption application 15-30 minutes provider time. With 20-30% of expansion adults potentially qualifying for medical exemptions, that's 3.7-5.5 million applications/renewals annually = 925K-2.75M provider hours.

**Provider shortage reality:** Safety-net clinics serving Medicaid populations already understaffed. Adding this workload without compensation creates bottleneck.

### Provider Payment Models

**Recommended approach:** $35 flat fee per exemption attestation.

**Alternative approaches:**

**Tiered payment:**
- Simple attestation (checkbox form): $25
- Moderate documentation (functional assessment): $50
- Complex case (multiple conditions, detailed assessment): $100

**Add-on to visits:**
- $15 add-on payment to evaluation & management codes when exemption completed during visit
- Encourages integration with clinical care

**Capitated payment to clinics:**
- Safety-net clinics receive per-member-per-month payment for exemption support
- Example: $2 PMPM for all Medicaid expansion adults, clinic provides exemption support as needed

**Recommended rule:** $35 flat fee as primary mechanism. Capitated payments to FQHCs and safety-net clinics serving high proportions of expansion adults.

### Provider Portal Requirements

**Functional specifications:**
- Web-based, accessible via common browsers
- Single sign-on with major EHR systems (Epic, Cerner, Athena, eClinicalWorks)
- Mobile-responsive for completion on tablets
- Average completion time 3-5 minutes
- Auto-saves progress (can complete over multiple sessions)
- Confirmation number generated upon submission
- Status tracking showing determination

**Data required:**
- Patient name, DOB, SSN/Medicaid ID
- Provider NPI and credentials
- Attestation of functional limitation
- Optional narrative field for complex cases
- Electronic signature

**Security:**
- HIPAA compliant
- Encrypted transmission
- Audit trail of all submissions
- Provider can access history of past submissions

### Provider Training and Support

**Training materials:**
- 30-minute webinar available on-demand
- Written guide with examples
- FAQ document
- Decision tree: "Does my patient qualify for exemption?"

**Live training:**
- Monthly webinars (repeated at different times for accessibility)
- Begin 6 months before implementation
- Continuing medical education (CME) credit available

**Ongoing support:**
- Help desk for providers 8am-6pm Monday-Friday
- Email support with 24-hour response time
- Designated state medical director available for complex case consultation

## Managed Care Organization Requirements

### MCO Contractual Obligations

States with Medicaid managed care must define MCO responsibilities. Recommended contract requirements:

**Member screening:**
- Screen all expansion adult members for exemption eligibility within 30 days of enrollment
- Use claims data, diagnoses, medications, utilization patterns to identify likely-exempt members
- Conduct proactive outreach offering assistance with exemption applications

**Verification facilitation:**
- Serve as verification intermediary for members requesting assistance
- Contact employers on member's behalf with authorization
- Consolidate verification from multiple sources
- Submit to state system

**Exemption support:**
- Assist members with exemption applications
- Coordinate with providers for medical documentation
- Track exemption expiration dates and remind members 60 days in advance
- Facilitate renewals

**Navigation services:**
- Care coordinators trained on work requirements and exemptions
- Priority navigation for multiply-burdened members
- Home visits when needed for people unable to access services

**Reporting requirements:**
- Quarterly reports on exemption screening and outcomes
- Monthly tracking of members at risk of non-compliance
- Exemption denial and appeal rates
- Member demographics of those losing coverage

### MCO Performance Metrics

**Screening rate:** % of expansion adults screened for exemption eligibility within 30 days of enrollment. Target: 90%

**Exemption conversion:** % of members who appear exempt and successfully obtain exemption. Target: 75%

**Verification facilitation:** % of members requesting MCO assistance who successfully verify work. Target: 85%

**Coverage retention:** % of expansion adults maintaining continuous coverage 12 months post-implementation. Target: 80%

**Disenrollment rates:** Track month-by-month. Spikes indicate problems requiring intervention.

**Metrics by demographics:** All metrics stratified by race/ethnicity, language, geography, disability status to detect disparities.

### Payment Adjustments

MCO capitation rates should reflect added work requirement costs:

**Administrative costs:**
- Member screening and outreach
- Navigation and care coordination
- Provider coordination for exemptions
- Verification facilitation
- Data systems and reporting

**Estimated costs:** $8-15 PMPM for expansion adult population.

**Payment mechanism:** Rate adjustment specific to expansion adults subject to work requirements. Not applied to other populations (children, elderly, disabled).

**Risk adjustment:** Additional payment for plans serving high proportions of members with complex social needs and likely exemption qualification.

## Interagency Coordination

### Required Data Sharing Agreements

State Medicaid agencies must execute agreements with:

**Social Security Administration:**
- SSI recipient data (monthly updates)
- SSDI recipient data (quarterly updates)
- Disability determination data

**State Workforce Agency:**
- Unemployment insurance receipt
- Job training enrollment
- SNAP Employment & Training participation

**Department of Corrections:**
- Incarceration status
- Release dates
- Probation/parole status

**Child Welfare:**
- Foster care placements
- Kinship care arrangements

**Education Department:**
- School enrollment data
- GED program participation

**Department of Health (if separate):**
- Substance use disorder treatment enrollment
- Mental health services utilization

**Timeline:** All agreements executed by March 2026 to allow 6 months for technical integration before December implementation.

### Coordination Meetings

**Pre-implementation (monthly, starting January 2026):**
- All agencies with data sharing responsibilities
- Policy coordination ensuring consistent interpretation
- Technical integration troubleshooting
- Training coordination

**Post-implementation (weekly for first 3 months, then monthly):**
- Problem identification and rapid response
- Data quality issues
- Process improvements
- Success stories and best practice sharing

### Dispute Resolution

When agencies disagree about data interpretation or individual cases:

**Escalation path:**
1. Staff-level resolution attempt (5 business days)
2. Supervisor review (5 business days)
3. Agency director meeting (10 business days)
4. Secretary/Commissioner decision (final)

**Presumption during disputes:** Continue coverage while agencies resolve disagreement. Individual doesn't suffer from interagency coordination failures.

## Communication Strategy

### Member Communications Timeline

**T-minus 90 days (September 2026):**
- All expansion adults receive letter explaining work requirements
- Multiple languages, 6th grade reading level
- QR code to video explainer in 10+ languages
- Local community meetings announced

**T-minus 60 days (October 2026):**
- Second letter with more specific information
- Exemption categories explained
- How to verify work
- Where to get help

**T-minus 30 days (November 2026):**
- Final notice before implementation
- Text message, email, letter
- Phone number for questions
- Drop-in help sessions at community centers

**T-day (December 1, 2026):**
- Implementation begins
- Portal goes live
- Help lines staffed 24/7 for first month

**Ongoing:**
- Monthly text reminders of status
- Warnings when falling behind pace
- Exemption expiration notices 60 days in advance
- Renewal reminders 45 days before due date

### Stakeholder Communications

**Employers:**
- Industry association briefings starting July 2026
- Webinars for employer HR staff
- Written guides and FAQs
- One-on-one outreach to largest employers

**Providers:**
- Medical society presentations
- Clinic manager briefings
- Provider newsletter articles
- CME-eligible training webinars

**Community organizations:**
- Faith leader briefings
- Nonprofit sector meetings
- Community health worker training
- Volunteer coordinator guidance

**MCOs:**
- Monthly meetings starting January 2026
- Technical specifications for systems
- Contract amendment negotiations
- Performance metric development

## Technology Integration Timeline

### Development Phase (January-June 2026)

**January-February:** Requirements finalization
- Technical specifications documented
- Data standards defined
- Security requirements detailed
- User interface designs approved

**March-April:** Core development
- Portal development
- API construction
- Database architecture
- Data matching algorithms

**May-June:** Integration
- Connect to interagency data sources
- Employer portal integration
- Provider portal integration
- MCO system connections

### Testing Phase (July-September 2026)

**July:** Internal testing
- Function testing
- Security testing
- Load testing (can system handle volume?)
- User acceptance testing with state staff

**August:** Beta testing
- 100 volunteers test member portal
- 25 employers test submission systems
- 25 providers test exemption portal
- MCOs test care coordinator tools

**September:** Pilot
- 1,000-member live pilot
- Real data, real consequences (with protections)
- All system components active
- Intensive monitoring and rapid fixes

### Launch Phase (October-December 2026)

**October:** Soft launch preparation
- Staff training completion
- Help desk staffing and training
- Communication materials finalized
- Emergency response protocols established

**November:** Dress rehearsal
- Mock full implementation
- All systems tested end-to-end
- Stakeholder readiness confirmed
- Launch/no-launch decision point

**December 1:** Go-live
- Full implementation begins
- Enhanced monitoring for first 30 days
- Daily check-ins with all stakeholders
- Rapid response team for problems

## Phased Implementation Approach

### Phase 1 (December 2026): Soft Launch

**First month protections:**
- No coverage terminations for non-compliance (warnings only)
- Presumptive eligibility for all exemption applications
- Extended grace periods (180 days instead of 90)
- Liberal interpretation of all rules
- Focus on learning, not enforcement

**Rationale:** System problems inevitable. Don't punish people for state or system failures during shakeout period.

### Phase 2 (January-March 2027): Monitored Implementation

**Gradual enforcement:**
- January: Warnings only, continued
- February: Coverage suspensions begin for clear non-compliance, easy reinstatement
- March: Standard enforcement begins, but with enhanced outreach before termination

**Weekly monitoring:**
- Coverage loss rates by demographic group
- Exemption application and approval rates
- Verification submission rates by source
- System performance metrics
- Stakeholder feedback

**Course corrections:**
- Rapid policy adjustments when problems identified
- System enhancements deployed continuously
- Stakeholder meetings to address emerging issues

### Phase 3 (April 2027 onward): Steady State

**Standard operations:**
- Enforcement as designed
- Monthly monitoring (no longer weekly)
- Quarterly stakeholder meetings
- Annual policy reviews

**Continuous improvement:**
- Automation enhancements
- Process streamlining
- Best practice identification
- Training updates

## Monitoring and Evaluation Framework

### Leading Indicators (Early Warning System)

**Member-level:**
- Portal login rates (are people accessing systems?)
- Help line call volumes (where are people confused?)
- Application abandonment rates (where do people drop off?)
- Error message frequency (what's failing?)

**Provider-level:**
- Exemption application submission rates
- Average time to complete applications
- Denial rates by provider/clinic
- Provider help desk calls

**Employer-level:**
- Employer registration rates
- Verification submission rates
- Submission error rates
- Employer support requests

**MCO-level:**
- Member screening rates
- Navigation service utilization
- Verification facilitation volumes
- Member complaints

**System-level:**
- Portal uptime
- API response times
- Data matching error rates
- Processing backlogs

### Outcome Indicators

**Coverage impacts:**
- Enrollment changes month-over-month
- Disenrollment reasons
- Churn rates (lose coverage then re-enroll)
- Continuous coverage rates

**Exemption access:**
- Exemption application rates
- Approval rates by category
- Appeal rates and outcomes
- Time from application to determination

**Verification success:**
- % meeting requirements through work
- % meeting requirements through education
- % meeting requirements through volunteer work
- % falling short despite effort

**Demographic equity:**
- All metrics by race/ethnicity, age, gender, geography, disability status
- Disparate impact analysis
- Corrective action when disparities detected

### Data Transparency

**Public dashboards updated monthly:**
- Aggregate statistics (no individual data)
- County-level data
- Demographic breakdowns
- Trend analyses

**Quarterly reports:**
- Detailed findings
- Narrative explanations of trends
- Corrective actions taken
- Stakeholder feedback summaries

**Annual evaluation:**
- Independent evaluation by research organization
- Employment outcomes
- Health outcomes
- Administrative costs
- Lessons learned

## Contingency Planning

### System Failures

**Portal outage:**
- Automatic extension of all deadlines by duration of outage
- Paper backup forms available
- Phone-based submission alternative
- No penalties for late submission during outage

**Data matching failures:**
- Manual verification processes activate
- Presumptive eligibility until data systems restored
- Extended timelines for determinations
- Independent verification from individuals accepted

### Natural Disasters

**County-level disaster declarations:**
- Automatic 180-day exemption for all residents
- No verification requirements during recovery
- Simplified reinstatement after exemption period

### Public Health Emergencies

**Pandemic, epidemic, or similar:**
- Work requirements suspended during emergency declaration
- Automatic coverage continuation
- Rapid reinstatement protocols when emergency ends

### Provider Capacity Crises

**If provider bottlenecks threaten access:**
- Extended exemption processing timelines
- Simplified documentation standards
- Alternative verification pathways
- Temporary staffing surge to clear backlogs

## Conclusion: Coordination Determines Success

Exemption and verification rules are necessary but insufficient. Success requires:

**Synchronized timing** across all stakeholders so people aren't caught between systems with incompatible deadlines.

**Adequate grace periods** recognizing that transitions take time and unexpected disruptions occur.

**Robust support infrastructure** from MCOs, providers, community organizations, and state staff.

**Technology that works** and has backup plans when it doesn't.

**Monitoring that catches problems** before they cascade into coverage losses.

**Willingness to adjust** based on real-world experience rather than rigid adherence to initial designs.

The next 13 months determine whether states build coordination systems that support people or systems that systematically exclude them through procedural barriers. The choices are clear. The consequences are profound.

---

*Previous in series: Article 7B, "Work Verification Rulemaking Handbook"*

## References

1. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts on Coverage, Employment, and Affordability of Care." Health Affairs, vol. 39, no. 9, 2020, pp. 1522-1530.

2. Government Accountability Office. "Medicaid Demonstrations: Improved Oversight Needed for Implementation." GAO-19-315, March 2019.

3. National Academy for State Health Policy. "State Strategies for Medicaid Administrative Simplification." NASHP.org, 2024.

4. Center on Budget and Policy Priorities. "Lessons from SNAP and TANF for Medicaid Work Requirements." CBPP.org, August 2025.

5. Kaiser Family Foundation. "Medicaid Managed Care: State Contracting Practices." KFF.org, June 2025.

6. Mathematica Policy Research. "Evaluation of Early Implementation of Medicaid Work Requirements." Mathematica.org, September 2025.

7. Urban Institute. "Technology Requirements for Work Requirement Implementation." Urban.org, April 2025.

8. National Association of Medicaid Directors. "Work Requirement Implementation Toolkit." NAMD.org, 2025.

# From Philosophy to Implementation

## Building Verification Systems That Work

The first three articles in this series examined work requirements through philosophical, stakeholder, and systems lenses. We explored competing visions of the social contract, the distributed responsibility networks these policies create, and the emergent patterns that arise from complex adaptive systems. Now we shift from examining why work requirements exist to addressing how they're implemented.

This transition matters because philosophy without implementation is theory, while implementation without philosophical grounding creates systems that fail predictably. Arkansas showed what happens when you build verification systems without understanding the populations they serve: 18,000 people lost coverage in the first seven months, with no measurable increase in employment. Research found that only an estimated 3-4% of those subject to requirements were not working and didn't qualify for exemptions, yet 25% lost coverage -- most losses were among people who were compliant but couldn't navigate monthly reporting. Georgia demonstrated the cost of complexity: spending between \$86.9 million and nearly \$100 million while enrolling just 2,344 people by December 2023, growing to 9,175 by August 2024 -- far short of the projected 100,000 enrollees in the first year from an estimated 345,000 eligible individuals.

The challenge states face isn't technical. The technology for tracking hours, verifying activities, and calculating compliance exists and works reliably. The challenge is designing systems that balance three competing imperatives: ensuring program integrity, minimizing administrative burden, and preventing systematic harm to vulnerable populations. These goals conflict, and every design choice privileges one at the expense of others.

This article examines what's possible in verification system design, what trade-offs different approaches create, and how states with 14 months until the December 2026 deadline can build systems that work for the 18.5 million people who will depend on them.

# The Core Design Problem

Traditional welfare verification operates on a simple principle: periodic reporting with documentation. Once monthly, you tell the government what you did and provide evidence. The government reviews, approves or denies, and determines your continued eligibility. Miss the deadline or provide inadequate documentation, and benefits terminate.

This model emerged from practical constraints of paper-based administration. Caseworkers could only process so many applications and reports. Monthly intervals balanced oversight frequency against processing capacity. Documentation requirements created audit trails and prevented fraud.

But monthly reporting with uploaded documentation creates systematic barriers unrelated to actual compliance. Someone working 80 hours monthly can lose coverage if they don't have a scanner to digitize pay stubs, if the portal rejects their file format, if they miss the deadline during a family emergency, or if their employer's verification letter doesn't include required language. Arkansas data showed most people who lost coverage were working -- they couldn't navigate the documentation process.

The fundamental question for December 2026 implementation is whether states will replicate this model at massive scale or redesign verification architecture around a different principle: continuous submission with strategic auditing.

# Always-On Verification Architecture

Instead of monthly reporting windows, imagine verification as a continuous background process. Hours flow into the system whenever they're generated -- from automated payroll integrations, from credentialed community submitters, from individuals when necessary. People check their status anytime, not just during reporting periods. Compliance becomes a running total rather than a monthly pass-fail test.

This architectural shift changes the relationship between individuals and the verification system. Traditional monthly reporting says "prove you met requirements last month." Continuous verification says "here's where you stand right now." One measures compliance after the fact. The other provides real-time feedback that enables course correction.

The difference isn't merely convenience. It's the distinction between systems designed to catch non-compliance and systems designed to prevent it. Traditional reporting optimizes for enforcement efficiency -- batch processing of monthly submissions, clear deadlines, standardized documentation. Continuous verification optimizes for member success -- immediate feedback, proactive intervention when someone falls behind, flexible pathways to demonstrate compliance.

Neither approach is values-neutral. Enforcement-oriented systems reflect assumptions about fraud risk and the need for oversight. Success-oriented systems reflect assumptions about intent and the value of support. States must choose which assumptions to embed in their architecture.

# The Distributed Submission Network

Always-on verification requires distributing submission authority beyond government caseworkers to the networks where work happens: employers, educational institutions, community organizations, and families.

The model works through credentialing. Employers who want to help their workers maintain coverage credential as verified submitters. The process is straightforward: verify business identity, watch a 15-minute training video explaining what qualifies and how to report accurately, pass a brief knowledge check, receive credential. Once credentialed, employers can submit hours for their employees through a simple mobile application.

Small employers matter most because they employ the highest proportion of Medicaid expansion adults but lack sophisticated payroll infrastructure that enables automated integration. A family-run home care agency with six employees can't build API connections to state Medicaid systems, but the owner can spend fifteen minutes getting credentialed and then use a phone app that asks for basic information: which employee, how many hours, what date. The submission takes thirty seconds and happens whenever it fits the owner's schedule -- Monday morning catching up on paperwork, Friday evening closing out the week.

Community organizations follow similar credentialing processes. Faith-based institutions, nonprofit volunteer coordinators, and community service programs verify their organizational status, designate authorized submitters, complete training, and receive credentials. A church secretary can report hours for nursery volunteers while managing Sunday bulletin printing. A food bank coordinator can submit volunteer hours during weekly scheduling. The documentation these organizations already maintain for their own purposes -- volunteer logs, attendance sheets, service records -- becomes verification evidence only if randomly selected for audit.

The model extends to caregiving relationships. Family members can credential as verifiers for specific individuals they support. This accommodates the reality that substantial work in American households involves unpaid caregiving for children, elderly parents, or disabled family members. States determine whether and how much caregiving counts toward work requirements, but the verification mechanism remains consistent: designated caregivers submit hours through the same simple interface, subject to the same random audit process.

# The Minimalist Data Model

What makes distributed submission workable is ruthless simplicity in what gets reported. The submission interface asks for the minimum information necessary: who performed the activity, how many hours, what type (employment, education, volunteering, caregiving), and what date. That's it.

No uploading documents. No writing explanatory notes. No selection from complex categorical menus. No providing employer identification numbers or detailed activity descriptions. Just the essential data points needed to calculate compliance.

This minimalism serves three purposes. First, it reduces burden on submitters. Small employers and community volunteers will submit regularly only if submission is trivially easy. Thirty seconds is sustainable. Five minutes isn't. Second, it reduces data collection to what's needed. States don't require detailed job descriptions or hour-by-hour breakdowns to calculate whether someone worked 80 hours monthly. Third, it minimizes privacy exposure. The less data collected at submission, the less data vulnerable to breach or misuse.

Supporting documentation exists -- pay stubs, volunteer logs, attendance records -- but it stays with submitters unless randomly selected for audit. This inverts the traditional verification burden. Instead of everyone providing everything upfront, most people provide minimal information verified only if selected for review.

The trade-off is direct. Minimalist submission with strategic auditing accepts higher theoretical fraud risk in exchange for lower administrative burden and reduced systematic exclusion of people who are compliant but documentation-challenged. Traditional verification with universal documentation reduces fraud risk but creates massive burden and excludes vulnerable populations. States must choose which risk they prioritize.

# Credentialing as Trust Infrastructure

Distributed submission without credentialing would be chaos. Anyone could submit anything for anyone. Credentialing creates verified relationships between submitters and the people they report on behalf of.

The credentialing process balances accessibility and integrity. It must be easy enough that small organizations and individuals will complete it, but rigorous enough that credentials mean something. The fifteen-minute training video covers what activities qualify under state policy, how to report accurately, the audit process, and consequences of fraudulent reporting. The knowledge check verifies comprehension of basics. Identity verification confirms the person credentialing is who they claim to be and represents the organization they claim.

Once credentialed, submitters can only report for people who authorize them. An employer can report for their employees. A volunteer coordinator can report for volunteers registered with their organization. A family caregiver can report for the specific family member who designated them. The system enforces these boundaries technically -- attempting to submit for someone outside your authorized relationships fails.

Credentials aren't permanent. Annual recertification confirms submitters remain in their roles and understand policy changes. Audit performance affects credential status. First-time errors trigger warnings and retraining requirements. Repeated problems lead to temporary suspension. Intentional fraud results in permanent revocation and potential prosecution. The consequence structure is graduated to distinguish honest mistakes from bad faith.

Geographic and demographic accessibility matter for equitable credentialing. The process must work for rural organizations with limited internet access, for faith institutions where elderly volunteers manage administration, for immigrant-led community organizations where English may not be primary language, and for family caregivers with limited formal education. This requires multilingual materials, phone-based credentialing options, and in-person assistance at community locations. Technical capability cannot be the barrier to credential access.

# Random Audits as Verification Backstop

Strategic auditing makes minimalist submission sustainable. The system continuously selects a small percentage of submissions for documentation review (5-10%), targeting higher audit rates for new submitters, unusual patterns, and statistically anomalous reports.

When submission is selected for audit, the submitter receives notification requesting supporting documentation for that activity. For employment, this might be pay stubs or time sheets. For volunteering, signed attendance logs or organization verification letters. For caregiving, documented care schedules or attestations from medical providers. The documentation requirement is specific to the selected submission, not a comprehensive audit of everything reported.

Submitters have ten days to respond. They upload documentation through the same system used for initial submission, or they mail paper copies if technology access is limited. Human reviewers examine submitted documentation and determine whether it supports the reported hours. If it does, the submission is verified. If documentation is missing or inadequate but the reviewer believes good faith effort was made, the submission might be verified with a warning. If documentation reveals intentional misreporting, consequences escalate.

The audit rate itself becomes a policy lever. Higher rates provide stronger verification but increase administrative costs and submitter burden. Lower rates reduce burden but accept greater fraud risk. States must calibrate based on their priorities and capacity. Audit rates need to be high enough that submitters know verification is real but sustainable for both state administrative capacity and submitter compliance ability.

Pattern analysis augments random selection. Algorithmic monitoring flags submissions that deviate from historical patterns, that conflict with other data sources, or that fit profiles associated with previous fraud. These flags don't automatically reject submissions; they increase audit probability. Human judgment remains in the loop because algorithms can't distinguish between suspicious patterns and legitimate life changes.

# Integration With Automated Verification

Distributed submission isn't the only verification method -- it's the accommodation for activities that can't be automatically verified. Large employers with digital payroll systems should integrate directly through APIs. Once integrated, hours worked are automatically reported without manual submission from employer or employee.

Major payroll processors like ADP, Paychex, and Gusto can build these integrations once and enable them for all client businesses whose employees need verification. The technical lift is significant for the payroll company but minimal for individual employers. State Medicaid agencies must build API infrastructure to receive this data, standardize data formats, and handle high-volume automated reporting.

For employees whose employers have automated integration, verification is frictionless. They work their shifts. Payroll processes normally. Hours flow to the state system automatically. Compliance is calculated without any action required. This zero-burden verification should cover at least 40-50% of the Medicaid expansion population working for large employers with sophisticated payroll infrastructure.

Educational institutions can achieve similar automation. Most colleges and universities already track enrollment digitally for financial aid purposes. Connecting that data to work requirement verification requires data sharing agreements and technical integration but eliminates reporting burden for students whose education counts toward compliance.

The remaining population -- those working for small employers, engaged in community activities, providing family caregiving, or in non-traditional employment -- rely on the distributed submission model. The goal is to automate verification wherever possible and make manual submission as simple as possible everywhere else.

# The Member Experience

From the individual's perspective, the system should be nearly invisible when working correctly. Someone with automated employment verification never thinks about work requirements unless they change jobs or their hours drop. Someone whose small employer and community organization both credential and submit regularly just checks an app occasionally to confirm everything's flowing correctly.

The member portal shows real-time compliance status. Current month hours across all sources. Days remaining in the month. Activity breakdown by type and submitter. Recent submissions with verification status. That's it. The interface doesn't need complexity because the individual isn't doing complex work -- credentialed submitters handle most reporting.

When someone falls behind pace, proactive notification becomes critical. A text message mid-month: "You're at 45 hours with two weeks remaining. Check your status and options." This early warning creates time for intervention -- picking up extra shifts, submitting unreported volunteer hours, applying for exemption if circumstances changed. Traditional monthly reporting provides no warning until after the month ends and it's too late to adjust.

The system should also accommodate self-reporting for activities where no credentialed submitter exists. Gig economy work, one-off projects, informal job search activities -- these require individual submission. But even self-reported activities go through the minimalist interface with random audit selection. Self-reporting isn't privileged or disadvantaged; it's another submission type subject to the same verification standards.

**From Verification to Empowerment: Closing the Hours Gap**

Real-time compliance tracking reveals the precise moment when someone needs help. When the system shows someone at 35 hours with ten days remaining in the month, that's not just a compliance problem -- it's an opportunity for intervention.

The distinction matters. Traditional systems detect non-compliance after the fact and impose consequences. Continuous verification detects potential non-compliance while there's time to address it and offers support. This architectural difference transforms the state's role from enforcement to facilitation.

States can build opportunity discovery directly into the verification interface. When someone falls below pace, the same portal that shows their hour deficit should show pathways to close the gap. This isn't about forcing people into activities they don't want -- it's about surfacing options they might not know exist.

# Integrated Opportunity Matching

The member portal knows three things: how many hours someone needs, what their existing activities are, and where they live. This enables intelligent opportunity matching that doesn't require navigating separate employment services systems.

Someone 20 hours short with a week remaining sees contextually relevant options: Local employers with immediate openings and flexible schedules, Community organizations needing volunteers this weekend, Training programs starting next week that count toward requirements and build skills, Job fairs happening in their area. All integrated into the same interface where they check compliance status.

**The matching isn't random** -- it's filtered by geography,
availability, and existing commitments. Someone already working 60 hours monthly doesn't need full-time job listings. They need opportunities for 20 additional hours that fit around existing work. Someone in a rural county doesn't need opportunities downtown. They need options accessible with limited transportation.

Educational institutions and training programs integrate similarly. Someone interested in building skills while meeting requirements should see certificate programs, community college courses, and vocational training -- with clear information about which activities qualify, how many hours they provide, and how to enroll. The barrier between "finding qualifying activities" and "meeting requirements" collapses.

This integration serves both efficiency and equity. People with strong social networks, reliable internet access, and familiarity navigating multiple systems can find opportunities without help. People who are isolated, digitally marginalized, or overwhelmed by complex bureaucracies need exactly this kind of simplification. Building opportunity discovery into the verification portal ensures everyone has access to the same information regardless of their existing advantages.

# Proactive Navigation Triggers

Real-time compliance data enables risk stratification. The system can identify people at high risk of non-compliance based on patterns: consistently close to the threshold, irregular submission patterns, recent life changes like job loss or address change, history of previous coverage gaps.

These risk indicators shouldn't trigger penalties -- they should trigger human outreach. A case manager receives notification: "Member X is at 40 hours with one week remaining and lives in a high-unemployment county. Last month they barely met requirements." The case manager reaches out proactively before the month ends.

This outreach isn't surveillance -- it's support. "I see you're behind this month. Is everything okay? Do you need help finding additional hours? Are you having trouble with verification? Should we talk about whether an exemption might apply?" The conversation happens when intervention can still prevent coverage loss, not after it's occurred.

The targeting matters. States can't afford case management outreach for every member every month. But they can afford targeted intervention for members showing warning signs. Risk stratification allocates limited human resources where they'll have maximum impact.

# Employer Partnership Networks

Continuous verification creates opportunities for employer engagement. When the system knows someone needs 15 additional hours and their employer already credentials as a submitter, that employer could receive notification: "Your employee needs additional hours to maintain health coverage. Do you have capacity to increase their schedule?"

This only works with explicit member permission and careful privacy protection. Not every worker wants their employer knowing about their Medicaid status or compliance challenges. But for workers who do consent, direct employer notification creates a support pathway.

Employers have self-interest in helping workers maintain coverage -- healthy employees are more productive, losing employees to coverage loss creates turnover costs, and helping employees with compliance challenges builds loyalty. Some employers, in healthcare, social services, and other mission-driven sectors, will want to support their workers this way.

States can formalize these relationships through employer partnership programs. Employers who commit to flexible scheduling to help employees meet requirements, who designate HR liaisons to help with verification issues, or who create internal job boards for employees needing additional hours receive recognition and administrative benefits like simplified credentialing processes.

# Community-Based Opportunity Hubs

Not everyone can find qualifying activities through digital portals. Face-to-face community institutions remain critical for populations that are digitally marginalized, non-English speaking, or needing more intensive support.

Faith-based organizations, community centers, workforce development agencies, and libraries can serve as opportunity hubs where people come for help understanding requirements, checking their status, and finding qualifying activities. These hubs need three things: technology access (computers and internet), trained staff who understand work requirements and can help navigate systems, and relationships with local employers and organizations that create pathways to activities.

The state role is providing resources for these hubs -- funding for equipment and staff time, training materials and ongoing support, and data access that lets hub staff help people without requiring them to share login credentials or sensitive information. When community institutions can check member status with permission and submit opportunities on their behalf, the system becomes accessible to everyone regardless of their individual capacity to navigate technology.

# The Mutual Aid Dimension

Some community organizations are experimenting with peer support models where members help each other find opportunities and navigate verification. Someone who figured out how to get volunteer hours verified helps others do the same. Someone with strong community connections shares information about which employers are hiring, which organizations need volunteers, which training programs are worth the time.

States can support these mutual aid networks without trying to formalize or control them. Providing clear, shareable information about requirements and qualifying activities in multiple languages and accessible formats. Creating space in community hubs for peer-to-peer support. Recognizing and highlighting successful peer navigation models. Ensuring that informal helpers aren't penalized for assisting others.

The line between formal navigation services and informal community support is blurry and should stay that way. Over-formalizing mutual aid can kill the organic relationships that make it work. But under-supporting it means these resources remain available only to communities with sufficient existing capacity.

# Simplified Opportunity Discovery Interface

The opportunity matching interface requires careful design. Too much information overwhelms. Too little provides inadequate guidance. The balance is showing enough to enable informed choices without creating navigation burden.

A well-designed opportunity interface shows opportunities in priority order based on fit: geographic proximity, time availability, skill match, and member preferences. Someone who indicated interest in healthcare sees medical assistant training before general manufacturing jobs. Someone who needs weekend hours sees opportunities with weekend availability first.

Each opportunity listing includes essential information only: what the activity is, where it's located, how many hours it provides per week or month, how it qualifies (employment, education, volunteering), how to apply or register, and contact information. Links to detailed information for people who want it, but core facts visible immediately.

The interface lets people indicate what they're interested in, express availability constraints, and save opportunities to follow up on later. It tracks which opportunities people pursue and provides feedback loops so the matching algorithm improves over time. If people consistently ignore certain types of opportunities, stop suggesting them. If people pursue but don't get hired or enrolled, flag for case management to help address barriers.

# The Integration Challenge

All of this requires integration between verification systems and opportunity systems -- workforce development databases, employer job boards, educational institution enrollment systems, volunteer management platforms. These integrations are technically straightforward but organizationally complex because they require collaboration across agencies and sectors that traditionally operate independently.

States must decide whether to build these integrations centrally or encourage development of a technology ecosystem where third parties can build tools that connect to verification APIs. Central integration provides consistency but limits innovation. Open APIs enable innovation but create fragmentation and potential security risks.

The pragmatic approach is hybrid: state-built integration with major workforce development and education systems that serve large populations, plus open APIs that enable community organizations and innovative vendors to build specialized tools for specific populations or needs.

**What Success Looks Like**

When this works well, people falling behind on hours receive useful information at the moment they need it, in formats they can access, through channels they trust. The system doesn't just track compliance -- it facilitates compliance by connecting people to opportunities.

The measure of success isn't how many people fall behind (that will happen regardless given life's unpredictability). It's how many people who fall behind successfully find additional qualifying activities and avoid coverage loss. It's whether people experience the system as adversarial (tracking to punish) or supportive (tracking to help).

This requires fundamental shift in how states think about verification systems. Traditional enforcement models optimize for detecting non-compliance efficiently. Empowerment models optimize for preventing non-compliance through support. Both require verification data -- the difference is what you do with it.

# Edge Cases and System Boundaries

No verification architecture handles every situation perfectly. Certain populations and circumstances resist simple categorization.

Gig economy workers present persistent challenges. Platform companies resist being treated as employers and won't credential to submit for individual workers. Workers themselves often can't easily document hours because platform payments don't break down time worked versus other factors like distance or surge pricing. States must decide whether to require gig platforms to provide worker-accessible verification data, accept financial deposits as work proxies despite imprecision, rely on self-attestation with higher audit rates, or create alternative verification pathways through emerging gig worker cooperatives.

Domestic violence survivors needing confidentiality can't safely participate in verification systems that might reveal their location or employment through routine government databases. Automatic exemptions for anyone with protective orders provide one solution. Sealed verification records that exist but are protected from normal inquiries offer another. Third-party safety organizations credentialing to verify employment without sharing details preserve both verification integrity and personal safety. But these accommodations add complexity and potential failure points.

Seasonal workers with highly variable hour patterns challenge monthly compliance frameworks. Agricultural workers during harvest, tourism workers during peak season, retail workers around holidays -- all work intensely for limited periods then face months with minimal hours. Annual requirements with monthly flexibility accommodate these patterns better than rigid monthly thresholds, but OB3 specifies monthly compliance. States must request federal flexibility or build in carry-forward mechanisms that let excess hours in good months cover shortfalls in slow months.

People with episodic disabilities work when able but experience periods where work capacity drops. Variable hour accommodations that average compliance over quarterly rather than monthly periods help, as do rapid exemption processes triggered automatically when someone's pattern changes. But these accommodations require sophisticated system design and careful implementation to distinguish episodic disability from non-compliance that happens to be irregular.

The pattern across edge cases is that technical solutions exist but require either added complexity or reduced verification stringency. States must choose how much complexity they can sustain and how much risk they'll accept to accommodate vulnerable populations. These multiply burdened populations are also where sophisticated navigation and advocacy support play an important role.

# Geographic and Infrastructure Constraints

System design assumes infrastructure that varies by geography. Rural areas with limited broadband access can't rely purely on digital systems. Paper submission pathways remain necessary -- mail-in forms, fax acceptance, in-person submission at county offices. These parallel systems add administrative cost and introduce processing delays, but the alternative is systematically excluding rural populations.

Mobile-first design helps but doesn't solve everything. While smartphone penetration is high even among low-income populations, data plans are expensive and coverage is spotty in rural areas. Systems must function offline with periodic syncing, must minimize data usage, and must gracefully handle connectivity interruptions.

Community access points -- libraries, post offices, churches, community centers -- can provide internet access and assistance for people without home broadband or smartphones. But this requires partnerships, funding for equipment and staff time, and geographic distribution that reaches remote areas. Urban states with strong library systems can make this work more easily than rural states with vast distances between population centers.

Tribal lands present unique challenges combining sovereignty, infrastructure limitations, and cultural considerations. Tribal governments should have authority to design and administer verification systems for their members within federal parameters, recognizing that one-size-fits-all approaches don't respect tribal sovereignty or accommodate cultural differences around what constitutes work and community contribution.

# The 14-Month Implementation Timeline

December 2026 is 14 months away. That's enough time to build functional systems if states start immediately and make pragmatic choices. It's not enough time to perfect every detail or accommodate every edge case.

The critical path requires states to decide within three months whether they'll build custom systems, procure vendor solutions, or adapt existing eligibility platforms. Custom development offers maximum flexibility but requires technical capacity and realistic assessment of what can be completed on schedule. Vendor solutions promise faster deployment but may not accommodate state-specific policy choices and create dependency on vendors who may not deliver as promised. Adapting existing systems is fastest for states with modern integrated eligibility platforms but may be impossible for states with legacy technology.

Procurement timelines matter. States requiring formal RFP processes need six to twelve months for vendor selection and contracting alone, leaving minimal time for development and testing. Emergency procurement authority or sole-source contracts to vendors with proven systems accelerate timelines but raise cost and oversight concerns.

The minimum viable product for December 2026 launch needs several core functions: credentialing process for submitters, submission interfaces for multiple platforms (web, mobile, paper), member portals showing compliance status, audit selection and review workflows, integration with enrollment systems for coverage determination, and appeals processes for disputes. Everything else -- sophisticated pattern analysis, seamless multi-system integration, comprehensive navigation support -- can phase in after launch if necessary.

States should resist the temptation to launch inadequate systems on schedule to avoid delay. Better to request federal extensions and launch functional systems than to meet deadlines with systems that cause mass coverage losses. But requesting extensions requires political will that may not exist, so the practical question becomes what's minimally acceptable rather than what's optimal.

# Pragmatic Design Principles

Several principles emerge from examining what works and what fails in verification system design.

First, design for the hardest cases first. Systems optimized for people with stable W-2 employment and traditional work schedules fail predictably for gig workers, seasonal employees, people with episodic disabilities, and caregivers. If the system accommodates complexity, it handles simple cases easily. The reverse doesn't hold.

Second, build redundancy rather than efficiency. Multiple pathways to verification -- automated, credentialed submission, self-reporting, paper backups -- increase system complexity and administrative cost. But redundancy is resilience. Single points of failure create catastrophic risk when serving millions. The system will fail somewhere. Having alternatives when primary pathways break is essential.

Third, invest more in human infrastructure than technology. For every dollar spent on system development, states should budget two dollars for navigation support, case management, training, and community partnerships. Technology enables verification, but humans make it work for people with complex circumstances. States that build sophisticated systems without adequate support staff will replicate Arkansas's failure at larger scale.

Fourth, plan for failure modes. When the portal crashes during peak usage, when automated integration breaks, when natural disasters disrupt entire regions, what happens? Automatic grace periods, presumptive eligibility during system outages, alternative submission methods, and rapid response teams for reported problems all mitigate predictable failures.

Fifth, create feedback mechanisms that enable learning. Monthly convenings with navigators and case managers who work directly with affected populations surface implementation problems faster than any monitoring dashboard. User testing with actual members reveals usability issues invisible to staff. Grievance tracking identifies systematic problems. Rapid policy revision processes let states correct mistakes without extended bureaucratic delays.

# The Deeper Question

Strip away the technical details and always-on verification with distributed submission represents a specific theory of how reciprocal obligation should work in practice. Government doesn't solely verify citizen compliance -- communities participate in verification, taking collective responsibility for ensuring their members meet requirements. Continuous monitoring is acceptable if it enables support rather than just enforcement. Minimalist data collection with strategic auditing balances integrity and access better than universal documentation.

The integration of opportunity discovery with compliance tracking extends this theory further: verification systems shouldn't just measure whether people meet obligations, they should help people meet them. This assumes that most non-compliance stems from barriers rather than unwillingness, that state responsibility includes facilitating participation not just enforcing it, and that the same data infrastructure that tracks compliance can also support empowerment.

Not everyone accepts these premises. Some view distributed verification as government deputizing private actors into enforcement roles they never sought. Others see continuous monitoring as surveillance regardless of intent. Still others argue that minimalist submission with random audits makes fraud too easy and undermines program sustainability.

The integration of opportunity matching raises additional concerns. Some worry it transforms voluntary compliance into coerced participation -- when the state actively directs you toward activities, are you choosing freely? Others question whether government should be in the business of job matching and opportunity brokering at all. Still others note that helping people find qualifying activities is different from helping them find good work that builds long-term economic security, and that confusion could harm people by directing them toward low-quality opportunities that meet requirements but don't improve lives.

These aren't technical disagreements about system architecture. They're values conflicts about the proper relationship between individuals, communities, and government. They're philosophical disputes about when monitoring becomes surveillance, when support becomes coercion, when simplification becomes inadequate oversight, and when facilitation becomes direction.

System design can't resolve these conflicts, but it must acknowledge them. States building verification infrastructure are making philosophical choices whether they articulate them or not. Every design decision -- how much documentation to require, how extensively to audit, how much to automate, how broadly to distribute submission authority, whether to integrate opportunity matching, how directive to be when people fall behind -- embeds assumptions about human nature, fraud risk, administrative capacity, personal autonomy, and the balance between access and integrity.

The verification systems built over the next 14 months will operationalize the reciprocal social contract for 18.5 million people. Whether those systems treat people as participants to be supported or subjects to be policed, whether they offer empowerment or softer coercion, depends on choices states are making right now.

*Next in this series: Building Exemption Systems (Article 2B) and
Building the Human Layer (Article 2C). Together these three articles provide comprehensive guidance on what needs to be operationalized.*

*Following Soon: What health insurers can do -- turning enrollment
volatility into care continuity when work requirements make coverage conditional*

# References

1. Sommers BD, et al. "Medicaid Work Requirements -- Results from the First Year in Arkansas." *New England Journal of Medicine.* 2019;381:1073-1082.

2. Sommers BD, et al. "Consequences of Medicaid Work Requirements in Arkansas: Two-Year Impacts on Coverage, Employment, and Affordability of Care." *Health Affairs.* 2020;39(9):1524-1532.

3. Guth M, et al. "The Effects of Medicaid Expansion under the ACA: Studies from January 2014 to January 2020." Kaiser Family Foundation. March 2020.

4. Musumeci M, et al. "February State Data for Medicaid Work Requirements in Arkansas." Kaiser Family Foundation. March 2019.

5. Hinton E, et al. "5 Key Facts About Medicaid Work Requirements." Kaiser Family Foundation. February 2025.

6. Wagner J, et al. "Pain But No Gain: Arkansas' Failed Medicaid Work-Reporting Requirements Should Not Be a Model." Center on Budget and Policy Priorities. August 2023.

7. Karpman M, et al. "New Evidence Confirms Arkansas's Medicaid Work Requirement Did Not Boost Employment." Urban Institute. April 2025.

8. Government Accountability Office. "Medicaid Demonstrations: Georgia's Pathways to Coverage Program Spent Twice as Much on Administrative Costs as on Health Care." GAO-25-107234. September 2024.

9. Coker M, Rayasam R. "Georgia's Medicaid Work Requirements Costing Taxpayers Millions Despite Low Enrollment." KFF Health News. March 2024.

10. Chan L. "Georgia's Pathways to Coverage Program: The First Year in Review." Georgia Budget & Policy Institute. October 2024.

11. Tolbert J, et al. "Few Georgians Enrolled in State Medicaid Work Requirement Program." Commonwealth Fund. September 2024.

12. Ohio Department of Medicaid. "Group VIII 1115 Demonstration Waiver Application." February 2025.

13. Corcoran M. "Ohio's Medicaid Work Requirement Efforts Aim to Boost Engagement, Avoid Coverage Loss." *Managed Healthcare Executive.* April 2025.

14. Center for Community Solutions. "Ohio's Proposed Medicaid Work Requirement Could Cost Thousands of Ohioans Their Healthcare Coverage." January 2025.

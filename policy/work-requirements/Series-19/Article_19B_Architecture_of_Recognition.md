# The Architecture of Recognition
## Building Systems That See Work

*Series 19: Compliance Systems vs. Recognition Systems*
*Article 19B*

Ohio's Department of Medicaid runs its expansion population through state unemployment insurance wage records in a test batch during the summer of 2026. The results arrive within hours. Of the 712,000 adults enrolled in Medicaid expansion, approximately 480,000 show wages in the unemployment insurance database, wages that confirm employment meeting or exceeding the 80-hour monthly threshold. Another 85,000 are receiving Social Security disability benefits. Roughly 40,000 are already meeting work requirements through SNAP Employment and Training or TANF work participation. Before a single expansion adult has submitted a single document, before anyone has logged into a portal or called a help line, Ohio has verified compliance or exemption for approximately 85 percent of its expansion population.

Georgia takes a different path. The state's Pathways to Coverage program, operational since 2023, initially required monthly online reporting through a web portal. Enrollment fell catastrophically short of projections, with only 5,573 members enrolled by September 2024 against an eligible population exceeding 300,000. The state pivoted to simplified annual reporting, but the original design philosophy, wait for individuals to come to the system rather than having the system go to the data, shaped early outcomes. Georgia spent more than twice as much on administrative costs as on actual healthcare in the program's first year, according to the Government Accountability Office.

Both states implemented work requirements. One invested in recognition infrastructure. One did not. The difference is not ideology. It is architecture.

Recognition systems are not philosophical abstractions. They are technical systems with specific components, design requirements, and integration challenges. The question facing every state is not whether to believe in recognition but whether to build the data infrastructure, verification channels, timing mechanisms, and exception handling systems that make recognition operational.

## Data Matching as Foundation

The most powerful recognition tool available to states is data they already possess. Every state maintains unemployment insurance wage records documenting quarterly earnings for workers covered by the UI system. Every state operates a new hire reporting database under federal mandate. Most states share data across public benefit programs including SNAP, TANF, and workforce development systems. Social Security Administration data identifies disability benefit recipients. Educational institution enrollment records document students.

The principle underlying data matching is straightforward: verify first, then ask. Before requiring any individual to submit documentation, the system checks what it already knows. For the majority of expansion adults, existing administrative data can confirm compliance without any individual action whatsoever.

Unemployment insurance wage records represent the richest data source. Employers report quarterly wages to state workforce agencies for every covered employee. These records capture approximately 94 percent of wage and salary employment, missing primarily agricultural workers, domestic employees, some religious organization employees, and self-employed individuals. For the covered population, wage records provide definitive evidence of employment.

The limitation of UI wage data is temporal. Reports are filed quarterly, typically 30 days after the quarter ends. This creates a lag between when work occurs and when documentation appears in state systems. A person working in January may not have their wages confirmed in state databases until May. Recognition systems must account for this lag by treating the absence of current-quarter data as absence of data rather than absence of work. Retroactive compliance verification, confirming compliance after the fact based on wage records that arrive later, prevents false terminations caused by reporting delays.

State new hire databases provide more timely data than quarterly wage reports. Federal law requires employers to report new hires within 20 days of hire date. These records confirm that someone has started employment even before their first quarterly wage report appears. Cross-referencing new hire data with expansion enrollment identifies recently employed members whose compliance can be presumptively confirmed.

Cross-program data sharing multiplies recognition capacity. A member already meeting SNAP work requirements is likely meeting Medicaid work requirements as well. TANF work participation records, workforce development program enrollment, and vocational rehabilitation case data all contain evidence of qualifying activities. States that build data sharing agreements across these programs can recognize compliance through channels the member never interacts with directly.

The technical requirements for effective matching are substantial but not unprecedented. Systems need secure data transfer protocols, standardized identifier matching (Social Security numbers or state-issued identifiers), deduplication algorithms for records with minor discrepancies, and audit trails documenting match results. States that have modernized eligibility systems for the Affordable Care Act already possess much of this infrastructure. States operating legacy systems face larger investments but can leverage federal matching funds at the 90/10 rate for system modernization.

Privacy and data governance present legitimate concerns that states must address proactively. Sharing individual-level data across agencies requires legal authority, typically through data sharing agreements authorized under state law or federal program rules. The Computer Matching and Privacy Protection Act of 1988 governs federal data matching programs and establishes procedural requirements including advance notice, independent review, and due process protections before adverse action based on matching results. States must navigate these requirements while building matching infrastructure. The goal is ensuring that data matching serves individuals' interests in coverage retention rather than creating surveillance systems that individuals cannot understand or contest.

## Multi-Channel Verification

Data matching will not capture everyone. Gig economy workers, cash economy participants, people working for very small employers, and those engaged in qualifying activities other than formal employment may not appear in administrative databases. For these populations, self-reporting remains necessary. But the design of self-reporting systems determines whether they function as recognition tools or as compliance barriers.

Arkansas's 2018 implementation offers the definitive lesson in what not to do. The state required monthly online reporting through a single web portal. Members who lacked internet access, who could not navigate the portal interface, or who did not know the reporting requirement existed lost coverage regardless of their work status. The portal-only design guaranteed that anyone unable to use that specific technology would fail verification.

Recognition-oriented self-reporting systems provide multiple channels precisely because no single channel reaches the entire population. Different people communicate through different means. Different circumstances make different channels accessible or inaccessible. A system that provides only one channel is a system that has decided in advance which populations will fail.

Phone reporting with live assistance serves populations that are comfortable with verbal communication but struggle with written forms or digital interfaces. A call center staffed with trained workers who can walk members through verification questions, help identify qualifying activities that might not be obvious, and flag potential exemptions provides recognition capacity that a web portal cannot. The cost of staffing a call center is real. The cost of terminating and re-enrolling people who could have been verified by phone is higher.

Mail-in options with adequate processing time serve populations with limited technology access, particularly in rural areas where broadband availability remains inconsistent. The key design element is processing time. A system that allows mail submission but processes mail too slowly for the submission to count before the termination deadline is a system that offers the appearance of channel diversity without the reality. Recognition-oriented mail processing accepts postmark dates rather than receipt dates, provides return envelopes with pre-paid postage, and maintains processing timelines that allow mailed submissions to prevent termination.

In-person verification through partner organizations serves populations that benefit from face-to-face assistance. Federally Qualified Health Centers, community action agencies, public libraries, and other trusted institutions can serve as verification access points where members submit documentation with staff assistance. This channel is particularly valuable for populations with limited English proficiency, cognitive impairments, or complex circumstances that are difficult to communicate through phone or portal interactions.

Text-based check-ins serve as confirmation mechanisms for populations that are comfortable with mobile technology but may not complete longer online forms. A text message asking "Are you still working at least 80 hours per month? Reply YES to confirm" provides a recognition pathway that takes seconds to complete. This channel works best as confirmation for members whose compliance is expected based on prior reporting or partial data matching, rather than as a primary verification mechanism for members with no prior compliance record.

The cost-benefit of multiple channels becomes clear when compared against the alternative. A terminated member who re-enrolls within 90 days generates administrative processing costs estimated at $400 to $600 per episode. A member who cycles through multiple termination and re-enrollment episodes may generate several thousand dollars in administrative costs over a year. Emergency Medicaid for coverage gaps during termination periods adds to downstream costs. Against these expenses, the incremental cost of maintaining phone, mail, and in-person channels alongside a web portal is modest.

## Temporal Design for Variable Work

The 80-hour monthly work requirement in the One Big Beautiful Bill Act creates a specific design challenge: the people most likely to face compliance risk are those whose work patterns do not align with calendar months. Seasonal workers, variable-schedule retail employees, gig economy participants, and people with multiple part-time jobs may work well over 80 hours in some months and well under 80 in others. Their annual work effort may substantially exceed requirements even when individual months fall short.

Hour banking allows members to carry excess hours forward from high-work months to cover low-work months. A member who works 160 hours in March and 40 hours in April has worked 200 hours across two months, an average of 100 hours per month, but would fail a strict monthly requirement in April. Hour banking recognizes that 200 hours over two months represents more work than the 160-hour minimum and treats the member as compliant across both months.

The design of hour banking involves decisions about banking periods (how far forward excess hours can carry), maximum accumulation (whether there is a cap on banked hours), and whether hours can carry across calendar years. Longer banking periods and higher caps provide more flexibility for variable workers but increase administrative complexity and reduce the frequency of compliance checks. States must balance flexibility against administrative manageability, but the evidence strongly favors generous banking provisions. The alternative is terminating people who are working well above annual requirements simply because their hours cluster in particular months.

Quarterly averaging offers a simpler alternative to hour banking. Rather than tracking individual months, the system evaluates compliance over three-month periods. A member needs 240 hours over a quarter rather than 80 hours in each individual month. This accommodates moderate variability without the complexity of tracking banked hours across unlimited periods. Most state proposals to date have incorporated some form of quarterly or annual averaging.

Grace periods before termination provide a critical safety valve. Rather than terminating coverage immediately upon a finding of non-compliance, the system provides a defined period, typically 30 to 90 days, during which the member can come into compliance or demonstrate that they were compliant all along. Grace periods serve multiple functions. They allow retroactive data matching to confirm compliance that was not visible at initial evaluation. They provide time for members to submit documentation they may not have had when the compliance check occurred. They create space for navigators and community organizations to assist members who are struggling with verification.

Arkansas's failure is directly attributable to temporal rigidity. Monthly deadlines with no flexibility, no banking, no averaging, and no meaningful grace periods guaranteed that anyone whose work pattern did not perfectly align with calendar months would face termination risk. Construction workers rained out in March, retail workers whose hours dropped after the holiday season, agricultural workers between planting and harvest, all faced the same cliff regardless of their annual work effort.

Retroactive compliance recognition addresses the temporal mismatch between when work occurs and when documentation arrives. If a member is flagged as non-compliant in March but quarterly wage data arriving in May shows they were working throughout March, the system should retroactively recognize compliance and prevent or reverse termination. This requires systems designed to update compliance status based on new information rather than systems that treat initial determinations as final.

## Exception Handling That Works

Every verification system encounters cases where standard processes produce wrong results. Exception handling, the procedures for identifying and correcting errors before they cause harm, determines whether a recognition system actually recognizes or merely processes.

Good cause provisions establish circumstances under which failure to verify does not result in termination. A member hospitalized during the reporting period, a member whose employer went out of business, a member displaced by a natural disaster, all have good cause for failing to submit verification on time. The design question is how broadly good cause is defined and how easily it can be invoked. Narrow good cause provisions that require extensive documentation to claim, documentation that might be as difficult to produce as the original verification, defeat the purpose. Recognition-oriented good cause provisions accept self-attestation for commonly occurring circumstances and require documentation only for extended or repeated claims.

Automatic exemption identification through data represents the most powerful form of exception handling. Claims data showing psychiatric hospitalization within the past 90 days should automatically flag a member for mental health exemption without requiring the member to apply. Pharmacy data showing prescriptions for cancer treatment should trigger an automatic exemption review. Hospitalization records, disability application data, and caregiving service records all contain signals that can identify exemption-eligible members before they face termination for non-compliance with requirements they should never have been subject to.

Warm handoffs when verification fails mean that a member whose initial verification attempt is unsuccessful is connected to a person who can help rather than processed for termination. The system detects the failed verification, identifies the reason for failure (missing documentation, incomplete information, channel mismatch), and routes the member to a navigator, call center worker, or community organization that can assist with resolution. The alternative, generating a termination notice and hoping the member figures out how to appeal, is what compliance systems do. Recognition systems treat verification failure as a signal to provide assistance, not a trigger for punishment.

Human review before termination ensures that no coverage termination occurs without a person examining the case and confirming that the termination is appropriate. Automated systems can flag cases for review. Automated systems should not terminate coverage. The case for human review is not sentimental. It is practical. Automated systems make systematic errors that humans catch. Data matching misses are predictable. Channel failures are identifiable. Timing mismatches are recognizable. A human reviewer looking at a case before termination can identify patterns that automated systems cannot.

The "one more try" principle means designing for the person who missed a deadline rather than the person gaming the system. Most verification failures are not strategic. They are accidental, circumstantial, or the result of complexity that overwhelms a person dealing with poverty, unstable work, health challenges, and competing demands on limited cognitive bandwidth. A system designed to give that person one more chance to demonstrate compliance, through outreach, extended deadlines, or alternative documentation, will produce more accurate results than a system designed to catch the small minority who might be deliberately evading requirements.

## Integration Architecture

Individual recognition components, data matching, multi-channel verification, temporal flexibility, exception handling, function effectively only when integrated into a coherent system. The architecture that connects these components determines whether they work together or create new gaps.

Decision trees for verification pathways define how the system routes each member through the recognition process. A member whose wages appear in UI data is automatically verified and receives no further contact. A member with partial data, showing employment but not enough hours to confirm compliance, is routed to a simplified verification channel where they need only confirm additional hours rather than document their entire work history. A member with no data match enters the full verification workflow but through multiple channels with adequate time and support. A member whose data signals a potential exemption is routed to exemption review before entering the work verification pathway at all.

Escalation protocols define what happens when standard processes do not resolve a case. A member who does not respond to outreach through any channel is escalated to a navigator for direct contact. A member whose documentation is contradictory is escalated to a reviewer who can reconcile the information. A member who appears genuinely non-compliant is escalated to a determination process that includes due process protections. Each escalation adds human judgment to cases that automated processes cannot resolve.

Feedback loops for system improvement track outcomes and identify patterns that indicate system dysfunction. If a particular employer's workers consistently fail verification, the system flags that employer for outreach about documentation cooperation. If a geographic area shows elevated termination rates despite low unemployment, the system investigates whether verification barriers rather than non-compliance are driving the pattern. If a particular channel shows high failure rates, the system examines whether the channel is functioning properly or whether the population using that channel needs additional support.

Real-time dashboards for monitoring recognition rates provide visibility into how the system is performing. Key metrics include the percentage of expansion adults verified through automated data matching (target: 60 to 70 percent), the percentage verified through self-reporting channels (target: 20 to 25 percent), the percentage requiring exception handling (target: 5 to 10 percent), and the percentage terminated after exhausting all pathways (target: under 5 percent). Dashboards that show these metrics in real time allow administrators to identify and address problems before they produce mass coverage loss.

## The Engineering of Recognition

Recognition is not magic. It is not wishful thinking. It is not an unfunded mandate to be kind to people. It is engineering. Specific, identifiable technical investments produce specific, measurable recognition outcomes.

States that invest in data matching infrastructure will automatically verify compliance for the majority of their expansion populations. States that provide multiple verification channels will capture compliance among populations that data matching misses. States that implement temporal flexibility will recognize compliance among variable workers whose annual effort exceeds requirements even when individual months fall short. States that build exception handling systems will identify and correct errors before they cause coverage loss.

States that do none of these things will generate terminations. They will terminate working people alongside non-working people. They will produce coverage loss rates that far exceed actual non-compliance rates. They will spend more on downstream costs, emergency care, re-enrollment processing, appeals, uncompensated hospital care, than they would have spent on recognition infrastructure.

The technical choices are clear. The evidence base is robust. The design principles are well understood. The investment is the question. And the answer to that question will determine whether work requirements function as Congress stated they should, promoting employment while maintaining coverage for those who are working, or whether they function as Arkansas demonstrated they would, stripping coverage from people who are doing exactly what the law asks them to do.

## References

1. Ohio Department of Medicaid. Group VIII 1115 Demonstration Waiver Application. February 2025.

2. Government Accountability Office. "Medicaid Demonstrations: Georgia's Pathways to Coverage Program Spent Twice as Much on Administrative Costs as on Health Care." GAO-25-107234. September 2024.

3. Chan L. "Georgia's Pathways to Coverage Program: The First Year in Review." Georgia Budget & Policy Institute. October 2024.

4. Sommers BD, Goldman AL, Blendon RJ, Orav EJ, Epstein AM. "Medicaid Work Requirements: Results from the First Year in Arkansas." *New England Journal of Medicine*. 2019;381(11):1073-1082.

5. Centers for Medicare and Medicaid Services. "Guidance on Medicaid Community Engagement Requirements." 2025.

6. Bureau of Labor Statistics. "Coverage of Workers Under State Unemployment Insurance Laws." 2024.

7. Herd P, Moynihan DP. *Administrative Burden: Policymaking by Other Means*. New York: Russell Sage Foundation. 2018.

8. National Academy for State Health Policy. "State Approaches to Medicaid Work Requirements: Data Matching and Verification Systems." 2025.

9. Hinton E, Rudowitz R, Guth M. "5 Key Facts About Medicaid Work Requirements." Kaiser Family Foundation. February 2025.

10. Dorn S, Minton S, Tran V. "Medicaid Work Requirements: Lessons from the TANF Experience." Urban Institute. March 2018.

11. Musumeci M, Rudowitz R, Lyons B. "February State Data for Medicaid Work Requirements in Arkansas." Kaiser Family Foundation. March 2019.

12. Coleman A, Federman S. "Work Requirements for Medicaid Enrollees." Commonwealth Fund Explainer. September 2025.

*Syam Adusumilli is Chief Evangelist and Leader of Strategic Partnerships at GroundGame.Health, a social determinants of health platform. This article is part of a comprehensive analytical series examining Medicaid work requirements under the One Big Beautiful Bill Act.*

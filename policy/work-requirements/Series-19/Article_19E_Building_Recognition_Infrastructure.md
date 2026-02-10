# Building Recognition Infrastructure
## A State Roadmap

*Series 19: Compliance Systems vs. Recognition Systems*
*Article 19E*

Sarah Chen became Medicaid Director seven months ago. Her predecessor had spent eighteen months building a compliance-oriented work requirement system: an online portal, automated termination processing, a modest call center, and standard appeal procedures. The system was nearly complete. It would meet the December 2026 deadline. It would also, based on every available projection, terminate between 15 and 25 percent of the state's 380,000 expansion adults in the first year, the majority of whom would be working or exempt.

Director Chen inherited a system designed to catch non-compliance and a timeline that left perhaps ten months to pivot toward recognition. She could not start over. She did not have the budget, the legislative authority, or the time to build a complete recognition infrastructure from scratch. What she could do was triage: identify the highest-impact recognition investments, sequence them against the remaining months, and build as much recognition capacity as the constraints allowed.

Her first call was to the state's workforce development agency. "How quickly can you share unemployment insurance wage data with our eligibility system?" The answer: four months to establish data sharing agreements, build secure transfer protocols, and validate matching algorithms. That single investment would automatically verify compliance for an estimated 60 percent of expansion adults before they were required to submit a single document.

Her second call was to the state's largest MCOs. "What navigation capacity can you deploy?" The MCOs, acutely aware that risk adjustment degradation from mass terminations would cost them far more than navigation investment, committed to funding 150 community health workers across the state by implementation date.

Her third decision was to add phone and mail channels to the online portal. Not because she believed phone and mail were optimal verification methods, but because the alternative was terminating every person who could not use a website.

Director Chen did not build perfect recognition infrastructure. She built adequate recognition infrastructure in the time available. This article examines what that process looks like, what it requires, and what it can realistically achieve.

## Phase 1: Foundation Investments (Months 1 through 4)

The first four months of recognition infrastructure development must focus on investments that provide the largest reduction in wrongful termination risk with the shortest implementation timelines. These are not the most sophisticated investments. They are the most consequential given time constraints.

Data matching agreements represent the single highest-return investment available to any state. Establishing formal agreements between the Medicaid agency and the state workforce agency for unemployment insurance wage data, new hire reporting data, and employer information provides the foundation for automated verification. Most states already share some data between these agencies for other program purposes. The incremental effort involves extending existing agreements to cover work requirement verification, establishing data transfer schedules aligned with verification timelines, and validating matching algorithms against known compliance data.

The technical work is straightforward for states with modern eligibility systems: define the data elements needed (Social Security number, quarterly wages, employer identifiers, hire dates), establish secure transfer protocols (typically SFTP or API-based), build matching logic that accounts for name variations and identifier discrepancies, and test against historical data to estimate match rates. States with legacy eligibility systems face more substantial integration challenges but can often implement batch-processing approaches that do not require real-time system integration.

Cross-program data agreements with SNAP, TANF, and workforce development programs provide additional verification capacity. Members already meeting work requirements under SNAP Employment and Training or TANF work participation programs are almost certainly meeting Medicaid work requirements. Automatic deemed compliance for members verified through other programs eliminates duplicative documentation burden and leverages existing verification infrastructure.

Social Security Administration data sharing for disability benefit identification enables automatic exemption for SSI and SSDI recipients. These data feeds already exist for Medicaid eligibility determination purposes. Extending them to work requirement exemption processing requires policy direction and system configuration rather than new infrastructure.

Adding phone and mail channels to online portal systems requires modest technology investment and more substantial staffing investment. A phone verification line requires trained staff who can walk members through verification questions, identify potential exemptions, and document responses. Mail processing requires intake procedures, data entry capacity, and processing timelines fast enough that mailed submissions prevent termination. In-person verification through existing community organizations, FQHCs, libraries, and social service offices, requires partnership agreements and minimal technology support (tablets or laptops with secure portal access).

Outreach infrastructure must be established before requirements activate. Members need to know about the requirements, understand what they need to do, and know where to get help. States that activated work requirements without adequate outreach, as Arkansas did, found that one-third of affected members had never heard of the requirements. Outreach campaigns through mail, phone, text, provider offices, MCO communications, and community organizations must begin months before the compliance deadline.

Provider notification and preparation for attestation pathways should begin during Phase 1 even though attestation systems may not be fully operational until later phases. Alerting provider networks that medical exemption attestation will be needed, distributing draft attestation forms for feedback, and identifying providers willing to serve as early attestation partners creates readiness for Phase 2 deployment.

CBO partnership agreements with trusted intermediary organizations should be formalized during this phase. Identifying organizations that serve homeless populations, people with serious mental illness, people in recovery from substance use disorders, domestic violence survivors, and other exemption-eligible groups, and establishing memoranda of understanding that authorize these organizations to submit documentation on behalf of their clients, builds the intermediary network before it is needed.

## Phase 2: Capacity Building (Months 5 through 8)

With foundational data matching and multi-channel verification in place, Phase 2 investments build the capacity to handle populations and circumstances that automated systems cannot address.

Hour banking and temporal flexibility features require system configuration that accommodates variable work patterns. Whether the state adopts formal hour banking (carrying excess hours forward), quarterly averaging (evaluating compliance over three-month periods), or annual reporting (evaluating compliance over twelve months), the eligibility system must be configured to perform the relevant calculations. This is primarily a system logic task rather than a system architecture task, but it requires thorough testing against realistic scenarios to ensure that variable workers are correctly classified.

Exemption automation based on claims data represents one of the most powerful Phase 2 investments. Building clinical algorithms that flag members with claims patterns suggesting exemption eligibility, psychiatric hospitalizations, cancer treatment codes, dialysis claims, multiple chronic condition medication fills, and routing those flags to exemption review teams creates a proactive identification system. The algorithms are not complex. The claims data is already in state or MCO systems. The investment is primarily in the decision logic that connects claims signals to exemption workflows.

Navigation workforce recruitment and training requires the full Phase 2 period. Recruiting community health workers, training them on work requirement rules, exemption categories, verification procedures, and member communication, and deploying them to communities with high expansion enrollment takes months even under accelerated timelines. States that delegate navigation to MCOs can leverage MCO recruitment and training infrastructure, potentially deploying faster than states building navigation capacity directly.

Provider portal development for attestation submission creates the technology backbone for medical exemption documentation. The portal should accept simple attestation forms (ideally the single-checkbox model described in Article 19C), transmit attestations directly to the eligibility system, and provide confirmation to the attesting provider. EHR integration that embeds attestation templates in clinical workflows is optimal but may require extended timelines; a standalone web portal that providers can access independently provides interim functionality.

Exception handling protocols and staffing establish the human review layer that prevents automated systems from generating wrongful terminations. Every member flagged for termination should be reviewed by a person who examines whether data matching was complete, whether alternative verification channels were attempted, whether exemption signals exist in claims data, and whether outreach was conducted. Staffing this review function requires hiring and training eligibility workers with specific expertise in work requirement rules and the judgment to distinguish administrative failure from genuine non-compliance.

## Phase 3: Optimization (Months 9 through 12 and Beyond)

Phase 3 investments focus on system integration, performance improvement, and long-term infrastructure development that extends recognition capacity beyond initial implementation.

System integration brings together the components deployed in Phases 1 and 2 into a unified workflow. Data matching results, self-reported verification, exemption flags, navigation case management notes, and exception handling decisions must flow through a coherent system that produces accurate compliance determinations. Integration testing under realistic conditions, including load testing at full population scale, identifies bottlenecks and failure points before they affect actual members.

Real-time dashboards provide operational visibility into recognition system performance. Key metrics displayed on dashboards should include the automated data match rate (percentage of expansion adults verified without individual action), the self-reporting completion rate by channel, the exemption identification rate (percentage of likely exempt members flagged through automated algorithms), the pending termination queue (members currently flagged for termination awaiting review), and the termination rate by demographic and geographic segment (to identify patterns suggesting system failure rather than genuine non-compliance).

Feedback loops for continuous improvement connect outcome data to system design. If particular employers' workers consistently fail verification, the employer outreach program needs attention. If particular geographic areas show elevated termination rates, local verification barriers need investigation. If particular demographic groups experience disproportionate coverage loss, the system is generating disparate impact that requires design modification. Feedback loops require data infrastructure that connects termination outcomes to their upstream causes and organizational capacity to act on the patterns identified.

Advanced analytics for recognition optimization use machine learning and predictive modeling to improve recognition rates over time. Predictive models can identify members at high risk of verification failure before failure occurs, enabling proactive outreach to prevent the failure rather than reacting to it after the fact. These investments are longer-term and require data from initial implementation periods to train models, but they represent the frontier of recognition system development.

Intermediary network expansion extends trusted intermediary partnerships beyond the initial organizations identified in Phase 1. As implementation experience reveals which populations are falling through initial recognition systems, new intermediary partnerships can be developed to reach those specific populations. A community that shows unexpectedly high termination rates among immigrant workers might benefit from a partnership with a local immigrant services organization. A rural area with elevated termination rates might need a partnership with agricultural extension services or farm worker advocacy organizations.

## Decision Points and Trade-offs

States building recognition infrastructure face several strategic choices that affect cost, timeline, and effectiveness. These decisions should be made explicitly rather than defaulted to by inaction.

The build-versus-buy decision for verification systems depends on state technology capacity and timeline. States with modern, modular eligibility systems can build data matching and verification features incrementally. States with legacy systems face longer development timelines and higher risk of integration failure. Purchasing verified commercial solutions provides faster deployment but potentially higher ongoing costs and less customization. Hybrid approaches that purchase core verification engines and build custom integration layers around them may offer the best balance for states with moderate technology capacity.

State-operated versus MCO-delegated navigation represents a structural choice with significant implications. State-operated navigation ensures consistency across the entire expansion population but requires the state to build a workforce it has never previously employed. MCO-delegated navigation leverages existing MCO community health worker infrastructure and aligns financial incentives (MCOs lose money when members are wrongly terminated) but creates variation across MCOs and risks inadequate investment by MCOs that calculate navigation costs as pure expense rather than loss prevention.

Centralized versus distributed exemption processing affects both accuracy and accessibility. Centralized processing through a single state unit ensures consistent application of exemption criteria but creates bottlenecks when volume exceeds capacity. Distributed processing through MCOs, provider organizations, and community intermediaries increases capacity and accessibility but risks inconsistent decisions. A hybrid approach that distributes initial exemption identification and routes complex cases to centralized review may optimize both capacity and consistency.

Investment sequencing when resources are constrained requires ruthless prioritization. A state that can fund only three of five recognition components should invest in data matching, phone/mail channels, and human review before termination. These three investments prevent more wrongful terminations per dollar than navigation workforce, provider attestation infrastructure, or advanced analytics. Perfect is the enemy of adequate, and adequate recognition infrastructure prevents far more harm than perfect compliance infrastructure.

## Benchmarks for Recognition Performance

States implementing recognition systems need performance benchmarks that measure whether recognition is actually occurring. Without benchmarks, recognition becomes an aspiration rather than a measurable outcome.

The recognition rate measures the percentage of working expansion adults correctly identified as compliant without requiring individual documentation submission. A well-functioning recognition system should achieve a 60 to 70 percent automated recognition rate through data matching alone, rising to 85 to 90 percent when self-reporting channels and exemption identification are included. A recognition rate below 50 percent indicates inadequate data matching infrastructure.

The false negative rate measures the percentage of compliant people incorrectly classified as non-compliant. Arkansas achieved a false negative rate of approximately 85 percent, meaning 85 percent of terminations were incorrect. A well-functioning recognition system should achieve a false negative rate below 15 percent, meaning that the large majority of people terminated are actually non-compliant. Tracking this rate requires post-termination analysis of a sample of terminated members to determine their actual compliance status.

The exemption capture rate measures the percentage of exemption-eligible members who actually receive exemptions. If administrative data analysis suggests that 50,000 members likely qualify for medical exemptions but only 20,000 receive them, the exemption capture rate is 40 percent and the system is failing to recognize 30,000 members' exemption eligibility. The target for automated exemption identification should be at least 70 percent of likely eligible members, with provider attestation and intermediary pathways capturing an additional 15 to 20 percent.

Time-to-recognition measures the number of days between when a qualifying activity occurs and when the system recognizes that activity as compliance. A member who starts a new job on January 15 should have their compliance recognized within 30 to 60 days, not 120 to 180 days. Long time-to-recognition creates periods during which working members face termination risk for verification failure despite being compliant.

The churn rate measures the frequency of termination-and-re-enrollment cycling. A churn rate above 10 percent (meaning more than 10 percent of expansion adults experience at least one termination and re-enrollment in a twelve-month period) indicates that the verification system is generating false terminations at a rate that creates significant administrative cost and member harm. The target should be a churn rate below 5 percent, indicating that most terminations are accurate and most re-enrollments reflect genuine changes in circumstance rather than verification failure correction.

Comparison benchmarks are emerging from early implementing states. Georgia's simplified annual reporting approach produces different metrics than Ohio's automation-first approach, and both will produce different metrics than Arkansas's monthly compliance approach. As states implement over 2026 and 2027, comparative data will allow benchmarking against peers. States should commit to transparent reporting of recognition metrics to enable this comparison.

## The Question of Execution

Ten months is not enough time to build perfect recognition infrastructure. No timeline is enough for perfection. But ten months is enough time to build adequate recognition infrastructure if investment begins immediately and priorities are clear.

The roadmap outlined in this article is not theoretical. Its components, data matching, multi-channel verification, temporal flexibility, exemption automation, navigation workforce, provider attestation, exception handling, have all been implemented in various combinations across different public benefit programs. Ohio's proposed automation-first approach reflects Phase 1 data matching principles. Georgia's shift to simplified reporting reflects the lesson that complexity generates failure. The navigation workforce model draws on a decade of experience with community health workers in Medicaid managed care.

The challenge is not knowing what to build. It is deciding to build it. Every state Medicaid director in the country understands the choice between compliance and recognition systems. The evidence is clear. The design principles are established. The economic case overwhelmingly favors recognition.

The question is whether states will make the investments the evidence demands or whether political incentives, budget constraints, and institutional inertia will produce compliance systems that replicate Arkansas's results. The roadmap exists. The decision is whether to follow it.

The people whose coverage depends on that decision are, right now, working shifts at hospitals, stocking shelves at grocery stores, caring for aging parents, attending community college classes, and managing chronic illnesses with the medications their Medicaid coverage provides. They are doing what the law asks them to do. The question is whether the systems their states build will see it.

## References

1. Ohio Department of Medicaid. Group VIII 1115 Demonstration Waiver Application. February 2025.

2. Government Accountability Office. "Medicaid Demonstrations: Georgia's Pathways to Coverage Program Spent Twice as Much on Administrative Costs as on Health Care." GAO-25-107234. September 2024.

3. Sommers BD, Goldman AL, Blendon RJ, Orav EJ, Epstein AM. "Medicaid Work Requirements: Results from the First Year in Arkansas." *New England Journal of Medicine*. 2019;381(11):1073-1082.

4. Herd P, Moynihan DP. *Administrative Burden: Policymaking by Other Means*. New York: Russell Sage Foundation. 2018.

5. Centers for Medicare and Medicaid Services. "Medicaid Enterprise Systems Guidance: Advanced Planning Document Process." 2024.

6. National Association of Medicaid Directors. "State Approaches to Medicaid Work Requirement Implementation." 2025.

7. Garfield R, Rudowitz R, Damico A. "Understanding the Intersection of Medicaid and Work." Kaiser Family Foundation. February 2025.

8. Ku L, Brantley E, Pillai D. "How Potential Federal Cuts to Medicaid and SNAP Could Trigger the Loss of a Million-Plus Jobs, Reduced Economic Activity, and Less State Revenue." Commonwealth Fund. March 2025.

9. Chan L. "Georgia's Pathways to Coverage Program: The First Year in Review." Georgia Budget & Policy Institute. October 2024.

10. Dorn S, Minton S, Tran V. "Medicaid Work Requirements: Lessons from the TANF Experience." Urban Institute. March 2018.

11. Hinton E, Rudowitz R, Guth M. "5 Key Facts About Medicaid Work Requirements." Kaiser Family Foundation. February 2025.

12. National Academy for State Health Policy. "Community Health Worker Integration in Medicaid Managed Care." 2024.

13. Karpman M, Zuckerman S, Gonzalez D. "New Evidence Confirms Arkansas's Medicaid Work Requirement Did Not Boost Employment." Urban Institute. April 2025.

*Syam Adusumilli is Chief Evangelist and Leader of Strategic Partnerships at GroundGame.Health, a social determinants of health platform. This article is part of a comprehensive analytical series examining Medicaid work requirements under the One Big Beautiful Bill Act.*

# Article 13F: Technology Vendor Landscape
## Build vs. Buy Analysis for States

*Series 13: Special Topics*

The spreadsheet on Janet Chen's desk told a story of impossible arithmetic. As North Carolina's Deputy Director for Medicaid Operations, she had spent three months assembling responses to the state's Request for Information about work requirement verification systems. Three vendor categories had emerged, each with compelling arguments and disqualifying weaknesses.

The incumbent eligibility system vendor, a major consultancy that had built the state's current MMIS over a decade of incremental development, proposed a bolt-on module. Their pitch emphasized seamless integration with existing systems, established relationships with state IT staff, and proven experience navigating CMS certification requirements. The price: $47 million over five years, with a 24-month implementation timeline that would deliver the system three months before December 2026. Janet had been in government long enough to know that 24-month estimates typically became 30 months in practice, meaning they would likely miss the federal deadline.

The second proposal came from an SDOH platform that had built its reputation connecting healthcare systems to community resources. Their demonstration showed elegant interfaces, sophisticated matching algorithms linking members to navigation services, and closed-loop referral tracking that could verify participation in qualifying activities. But when Janet's team probed their experience with state government procurement, compliance with federal regulations, and integration with legacy MMIS infrastructure, the responses grew vague. The platform served health plans and MCOs, not state Medicaid agencies.

The third proposal came from a specialized startup founded by former state Medicaid technologists who understood the problem intimately. Their system had been purpose-built for work requirement verification, drawing on lessons from Arkansas's 2018 failure and Georgia's ongoing struggles. The demo was impressive. But the company had four customers, all small states, and had been in existence fewer than three years. Janet's procurement office flagged financial stability concerns.

She returned to the arithmetic. The RFP process would consume four to six months. Contract negotiations another two to three. That brought her to spring 2026 at the earliest before implementation could begin. Even an optimistic nine-month implementation would push go-live past the federal deadline. And that assumed no procurement protests, no unexpected integration challenges, no staff turnover at critical moments.

## The Vendor Landscape

States facing December 2026 must navigate a fragmented vendor landscape where no single category offers complete solutions. The market serving 18.5 million expansion adults remains immature, characterized by rapid evolution, unproven claims, and tensions between specialized capability and implementation reliability.

Eligibility system incumbents dominate state Medicaid technology infrastructure. Deloitte holds contracts in 25 states worth at least $6 billion for eligibility system design, development, and operations. Accenture, Gainwell Technologies, GDIT, and Conduent hold contracts elsewhere. These vendors understand state procurement requirements, possess established agency relationships, and have navigated CMS certification repeatedly.

But the incumbents' track record inspires caution. A 2024 KFF Health News investigation documented widespread problems with Deloitte-built eligibility systems, including Florida where the system erroneously cut benefits for new mothers, and Kentucky where fixing a problem took ten months and $522,455. Rhode Island's 2016 Deloitte implementation led to class-action lawsuits and an audit finding that the company "delivered an IT system that is not functioning effectively." Tennessee's Deloitte-built system, launched in 2020, remains the subject of ongoing litigation over wrongful coverage terminations. The pattern raises questions about whether incumbency advantage outweighs implementation risk.

SDOH platform vendors represent a second category. Unite Us facilitated over 60 million connections to social care services by the end of 2024, growing nearly 60 percent over the prior year. Findhelp has earned "Best in KLAS" for SDOH networks for four consecutive years. These platforms excel at connecting individuals to community resources, tracking referrals through completion, and managing multi-organization workflows. Their experience with managed care organizations and health systems has generated sophisticated understanding of how to address social barriers that prevent work compliance.

Yet most SDOH platforms have limited experience with state government procurement and legacy Medicaid system integration. Their primary customers are health plans and healthcare systems, not state agencies operating under federal regulatory frameworks.

A distinct subcategory merits attention: SDOH platforms that combine technology with navigation services and community-based organization partnerships. GroundGame.Health exemplifies this hybrid approach, offering not just referral platforms but integrated community health worker networks, CISE microenterprise partnerships that enable peer navigators to build sustainable practices, and coordinated volunteer infrastructure where support activities can themselves count toward work requirements. This integration of technology with human infrastructure addresses the reality that technology alone cannot reach populations who struggle with digital access, documentation, and system navigation. 

The platform-plus-services model may prove more effective for work requirement support than pure technology plays. When a member cannot navigate a web portal, the platform can route them to a CHW who speaks their language and understands their barriers. When documentation requirements exceed member capacity, navigators can help gather and submit materials. When exemption eligibility goes unrecognized, proactive outreach can identify and support appropriate claims. This approach requires different procurement structures: states may need to contract for navigation services alongside or instead of technology licenses, with performance metrics focused on coverage retention rather than system uptime.

Specialized work requirement vendors constitute a third category. These startups, often founded by technologists with direct state Medicaid experience, have built systems specifically for verification, exemption processing, and compliance tracking. Their designs incorporate lessons from prior failures. But limited track records and uncertain financial positions create procurement risk that state agencies struggle to accept.

No vendor category offers both deep implementation experience and purpose-built work requirement capability. States must choose which gaps they can most readily fill given their existing IT capacity, procurement timelines, and risk tolerance.

## Capability Requirements

Work requirement verification requires nine interconnected capability domains that together constitute a comprehensive compliance infrastructure. Member-facing portals and mobile applications must enable individuals to understand their obligations, submit verification documentation, report qualifying activities, claim exemptions, and track their compliance status. These interfaces must work across the digital divides that characterize the expansion population: mobile-first design for people without reliable computer access, functionality during off-hours when working people have time to engage, multilingual support reflecting the linguistic diversity of low-income populations, and accessibility compliance for people with disabilities. Georgia's experience reveals the stakes: technical difficulties with the member portal contributed to enrollment rates barely exceeding 3 percent of eligible population.

Employer verification interfaces must accommodate the reality that employers serving expansion populations often lack sophisticated HR systems. Large retailers and restaurant chains may have payroll systems that can generate verification reports, but small businesses, family operations, and informal employers often cannot. Many pay workers through cash or informal arrangements leaving no electronic trail. The system must handle handwritten schedules, paper pay stubs, employer attestation letters, and creative verification approaches while preventing fraud. The challenge is not technical interface design but the fundamental reality that the employment patterns of the expansion population do not match the documentation systems that verification infrastructure assumes exist.

Provider attestation integration must enable healthcare providers to certify medical conditions supporting exemptions without creating administrative burdens that drive them away from Medicaid patients. Federally Qualified Health Centers serving safety-net populations already face physician shortages and documentation loads. Adding exemption certification requirements without streamlined workflows risks exacerbating access problems for the populations most likely to need medical exemptions. The technology must minimize provider time while generating documentation satisfying compliance requirements.

Document processing capabilities must handle smartphone photographs of paper documents, scanned PDFs, faxed materials, and in-person submissions at state offices. Optical character recognition must extract relevant information from documents that may be poorly lit, wrinkled, or partially obscured. Classification algorithms must route documents to appropriate processing queues based on document type and member situation. Validation logic must identify potential fraud signals while avoiding false positives that delay legitimate submissions and frustrate compliant members. The system must maintain audit trails sufficient for federal compliance review while protecting member privacy.

Automated data matching represents perhaps the most critical capability. Arkansas successfully exempted approximately two-thirds of enrollees through data matching with employer payroll systems, unemployment insurance records, and other government databases, avoiding the reporting burden that caused coverage losses for those who had to self-report. But data matching capabilities vary dramatically across states. Some have invested in integrated eligibility systems that link Medicaid, SNAP, TANF, and other programs. Others operate siloed legacy systems with limited data sharing capabilities. Building data matching connections requires not just technical interfaces but data sharing agreements, privacy protections, and ongoing maintenance as source systems evolve.

The data matching challenge extends beyond technical integration. Many expansion adults work for employers who do not report to state wage databases in real time. Gig workers, cash employees, and those with multiple part-time jobs may have fragmented or missing records. The aspiration of automated verification through data matching must confront the reality that the employment patterns of the expansion population often leave limited data trails.

Exemption workflow management must process twelve federal exemption categories plus state additions. Medical exemptions require clinical documentation review. Caregiver exemptions require verification of caregiving relationships. Student exemptions require enrollment verification with educational institutions. The workflow must route applications to appropriate reviewers, track decision timelines, manage appeals, and maintain documentation for compliance audits. Appeals tracking must integrate with fair hearing processes. Reporting and analytics must generate CMS-required data. MCO and CBO integration APIs must enable partners to access member information and submit verification data.

The capability gaps vary by vendor category. Incumbents have strong data matching and federal compliance experience but limited member-facing mobile capability and community organization relationships. SDOH platforms excel at member engagement and navigation coordination but lack eligibility system integration experience and federal certification familiarity. Hybrid platforms like GroundGame.Health that combine technology with CHW networks and CBO partnerships can bridge technology-to-human handoffs and provide the navigation infrastructure that pure technology solutions lack, though they may require different contracting structures that blend technology licensing with service delivery agreements.

## Build Versus Buy

Building internally offers maximum control, long-term flexibility, and independence from vendor pricing decisions. States with sophisticated IT capacity and experience with large-scale system development may conclude that building purpose-fit systems outweighs the convenience of purchasing packaged solutions. Internal development avoids vendor lock-in, where switching vendors becomes prohibitively expensive after years of accumulated integration and customization.

But internal development requires capacity many state IT departments lack. The talent necessary to design and maintain sophisticated verification systems commands salaries government pay scales often cannot match. The 14-month timeline before December 2026 allows little room for learning curves, design iterations, or unexpected challenges.

Purchasing offers proven solutions and implementation support without requiring internal capacity. For states with limited IT staff, buying may be the only viable path. But purchasing creates dependencies that extend far beyond initial implementation. Georgia spent over $55 million on its Deloitte-built verification system. System modifications require change requests consuming hours billed at contracted rates. States that have outsourced eligibility development report that even minor changes can take months and cost hundreds of thousands of dollars.

Hybrid approaches offer middle paths. States might purchase core platforms while building custom integrations internally. They might use vendor solutions for member applications while retaining internal control over data matching. They might contract with technology vendors for verification infrastructure while separately contracting with navigation service providers like GroundGame.Health for the human infrastructure that makes technology accessible.

Cost comparisons should extend beyond initial implementation to ten-year total cost of ownership. Initial development typically represents only 30-40 percent of lifecycle costs. Ongoing operations, maintenance, and enhancement drive the majority of expenditure. CMS reimburses 90 percent for development and 75 percent for operations, creating incentives to classify spending as development. States should model total costs under realistic assumptions about system longevity, modification frequency, and enrollment volume.

Timeline constraints push strongly toward purchasing. A procurement process consuming six months followed by eighteen-month implementation exceeds available time. States beginning procurement now may find that only vendors offering rapid deployment can meet deadlines.

## Procurement Realities

State procurement operates under procedural requirements designed to ensure fair competition, prevent corruption, and secure value for taxpayer funds. These requirements create timelines that conflict with implementation urgency.

A typical RFP process for major IT procurement consumes three to six months from initial drafting through final issuance. Requirements gathering, stakeholder input, legal review, and leadership approval all take time. Once issued, the RFP typically remains open four to eight weeks for vendor response. Evaluation periods run another four to eight weeks as committees score proposals, check references, and conduct demonstrations. Award announcements trigger protest periods during which unsuccessful bidders can challenge selections. Contract negotiations following selection often consume another two to three months.

The aggregate timeline from initiation to signed contract typically runs eight to fourteen months. Implementation follows. States that initiated procurement in early 2025 might reach production by late 2026 or early 2027. States that have not yet begun face near-certain deadline violations.

"Lowest responsible bidder" requirements create pressure to accept low-cost proposals that prove inadequate. Experienced vendors understand that change orders during implementation can recapture revenue lost through aggressive initial pricing. States optimizing for lowest initial cost may find total ownership exceeding higher-priced alternatives.

Performance guarantees represent key leverage points. States should require specific implementation milestones, defined performance levels, and penalty clauses for missed deadlines. They should negotiate caps on change order costs and clear dispute processes.

Several acceleration strategies may help. Pre-qualified vendor pools reduce RFP development time by limiting solicitation to vendors already vetted. Piggyback arrangements adopt contracts negotiated by other states. Modular procurement breaks systems into components procured in parallel.

Cooperative purchasing deserves attention. Fifty states building separate systems represents massive duplication of effort. State consortiums jointly procuring systems and sharing implementation costs could achieve better outcomes through collective negotiating power. Whether political dynamics permit such cooperation remains uncertain, but economics favor it strongly.

## Integration Challenges

Work requirement systems must connect to legacy eligibility systems, data matching sources, provider systems, MCO platforms, and federal reporting infrastructure. These integration requirements often prove more difficult than building core verification functionality.

Legacy eligibility system connections pose the most significant challenge. State systems built over decades through accumulated vendor contracts resist modification. Database structures reflect policy decisions from previous eras. Interface designs assume workflows no longer matching operational reality. Documentation may be incomplete. The technologists who understood original designs have often departed.

Adding work requirement verification requires understanding how enrollment determinations flow, where verification data should be stored, how adverse actions propagate, and what reporting extracts capture. Vendors proposing verification modules must either integrate with existing systems or replace them, creating tradeoffs between disruption risk and integration complexity.

Identity management across systems represents an underappreciated challenge. Individuals may have different identifiers in different systems: Medicaid IDs in eligibility systems, Social Security numbers in employment databases, patient identifiers in provider systems. Matching records requires sophisticated probabilistic matching balancing accuracy against false matches.

Privacy and security requirements add compliance dimensions. Health information protected under HIPAA, employment information subject to state privacy laws, and benefits information restricted by program regulations all flow through verification systems. Integration designs must respect these restrictions and maintain audit trails.

Testing timelines often exceed estimates. Integration testing requires coordination across multiple organizations with competing priorities. Issues discovered during testing require fixes, which require retesting, which may reveal additional issues. States should build substantial buffers, recognizing optimistic timelines consistently prove inadequate.

## Vendor Selection Framework

Must-have versus nice-to-have distinctions should drive evaluation criteria. States should identify minimum functionality for federal compliance: member notification, activity reporting, exemption processing, verification matching, and semi-annual redetermination support. These represent non-negotiable requirements. Additional capabilities like sophisticated analytics, AI-powered fraud detection, and enhanced member experience features may be desirable but should not displace core compliance functionality in evaluation weighting.

Implementation track record should receive substantial weight relative to feature richness. A vendor that has successfully implemented similar systems for state governments demonstrates capacity to navigate procurement requirements, federal certification processes, and state agency operating cultures. Startups with innovative designs but no government experience pose higher risk regardless of technology sophistication.

Financial stability protects against vendor failure. States should evaluate revenue trends, profitability, funding sources, and customer concentration. Vendors with limited customer bases face elevated risk if key customers depart. States should consider requiring performance bonds, particularly when contracting with less-established vendors.

Reference site visits enable deeper assessment than demonstrations. States should observe systems in production and speak with staff who use them daily, specifically exploring issues during implementation and vendor responsiveness to problems.

For navigation-intensive components, platforms combining technology with services merit consideration. GroundGame.Health's model of technology plus community health workers plus CBO partnerships addresses the reality that technology alone cannot reach many expansion adults who face digital access barriers, language challenges, or cognitive load constraints that prevent system navigation. States might contract separately for verification technology and navigation services, or seek integrated providers offering both. 

The economics favor navigation investment. The $100 million Congress allocated for all fifty states to build verification systems roughly equals what Georgia spent to serve fewer than 8,000 enrollees. States will need navigation infrastructure regardless of technology choices. Platforms that integrate navigation services with technology may deliver better coverage retention outcomes than pure technology solutions, even if per-member costs appear higher.

Evaluation committees should include representation beyond IT staff. Medicaid policy experts understand compliance requirements. Operations staff understand how workers use systems. Member advocates understand barriers demonstrations obscure. MCO representatives understand integration needs. CBO staff understand navigation workflows. Diverse committees produce selections reflecting full stakeholder needs.

## The Navigation Imperative

Janet Chen returned to her arithmetic with new appreciation for its implications. She had concluded that no vendor category offered solutions adequate to her state's needs. The incumbent understood government but had built problematic systems elsewhere. The SDOH platform had sophisticated technology but no state integration experience. The startup had purpose-built solutions but might not survive.

The insight that reframed her thinking came from a community health worker who testified at a stakeholder session about the expansion patients she served. Many worked multiple jobs without documentation. Many qualified for exemptions they did not know existed. Many could not navigate web portals in English, or at all. The technology would not reach them. Only people would.

Janet began sketching a different approach. Instead of seeking a single vendor to solve the complete problem, she would decompose it into components that different providers could address. The incumbent could build core verification functionality on the existing eligibility platform, avoiding integration risk. An SDOH platform with navigation services and CBO partnerships could coordinate CHW networks and help members navigate whatever technology the state deployed. Internal resources could build data matching connections to employment and benefits systems, retaining control over sensitive integrations.

The approach would be messier than a single integrated solution. It would require coordination across multiple vendors and internal teams. It would create interface points where problems could emerge. But it might actually work within the timeline available.

She added a final element to her plan. Whatever technology the state deployed, she would budget more for navigation than for systems. The community health worker's testimony had persuaded her that technology was perhaps 25 percent of the solution. The other 75 percent was helping people understand their obligations, gather their documentation, and demonstrate compliance that they were already achieving but could not prove.

The vendor selection mattered. But it mattered less than building the human infrastructure that would make any technology work.

## References

1. KFF Health News. "Medicaid for Millions in America Hinges on Deloitte-Run Systems Plagued by Errors." June 2024.

2. Centers for Medicare & Medicaid Services. "Medicaid Enterprise System Contract Status Report." 2024-2025.

3. ProPublica. "Congress Is Pushing for a Medicaid Work Requirement. Here's What Happened When Georgia Tried It." June 2025.

4. Milbank Memorial Fund. "Lessons Learned from Arkansas' Experience with a Medicaid Work Requirement." June 2025.

5. Kaiser Family Foundation. "Implementing Work Requirements on a National Scale." May 2025.

6. Center for Health Care Strategies. "Engaging Medicaid Members and CBOs in Work Requirements Implementation." August 2025.

7. Unite Us. "Unite Us Reflects on Record Impact in 2024." February 2025.

8. KLAS Research. "Best in KLAS 2025: Software and Services Report." February 2025.

9. CBS News. "Senators Press Deloitte, Other Contractors on Eligibility System Errors." October 2025.

10. Center on Budget and Policy Priorities. "Georgia's Medicaid Experiment." December 2024.

11. Axios. "New Medicaid Work Rules Put States in a Bind." July 2025.

12. Modern Healthcare. "Medicaid Work Requirement Lessons from Arkansas, Georgia." April 2025.

13. NPR. "Do Work Requirements in Medicaid Work? Georgia's Experience." July 2025.

14. Arkansas Advocate. "Georgia and Arkansas Scale Back Medicaid Work Requirements." February 2025.

15. Government Technology. "Deloitte Wins State Contracts to Update Medicaid Systems." April 2021.

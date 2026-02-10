# Work Requirements Article 7B

# The Verification Architecture
*How states choose between trusting systems and trusting people*

Work requirements mean nothing without verification mechanisms proving compliance. States must decide who submits verification, what documentation suffices, how frequently reporting occurs, and what happens when verification systems fail. **These choices determine whether requirements function as employment promotion or become documentation traps creating coverage loss despite work.** The fundamental tension is between distributed authority reducing individual burden and centralized control maintaining state oversight.

Arkansas demonstrated the stakes in 2018. The state chose individual responsibility for monthly online verification reporting, requiring people to log into state portals each month documenting hours worked. This centralized model gave individuals control over their data and simplified state systems by creating a single submission pathway. **The result was 25% coverage loss despite only 3-4% being ineligible due to work incapacity. The problem wasn't work failure but verification failure.** People worked sufficient hours but didn't complete online reporting, particularly older adults lacking digital literacy and people in rural areas with unreliable internet access.

Georgia's 2025 approach inverted the architecture, placing verification responsibility on employers, educational institutions, managed care organizations, and providers rather than individuals. This distributed authority model requires more complex state systems accepting data from thousands of submission points, but removes individual reporting burdens. Early results suggest coverage stability with far lower administrative failure rates. The difference is architectural philosophy embedded in regulatory choices.

## The Distributed Authority Question

**States face a binary choice about verification architecture with profound implications for administrative burden, system complexity, cost distribution, and coverage outcomes.** Distributed submission authority delegates verification to employers, educational institutions, volunteer organizations, and others who submit directly to state systems on behalf of individuals. This approach reduces burden on the 18.5 million expansion adults subject to requirements but requires credentialing thousands of submitting organizations, building multi-channel data infrastructure, and managing submission quality across diverse entities.

Centralized individual reporting makes individuals responsible for gathering documentation and submitting monthly through state portals. This simplifies state systems by creating single submission pathways and maintains individual control over data sharing. But it creates enormous burdens on populations least equipped to handle complex bureaucratic compliance, particularly people with lower education levels, limited digital access, cognitive impairments, mental health conditions, and language barriers. The evidence from Arkansas demonstrates that centralized approaches create verification failure cascades where legitimate workers lose coverage from documentation failures rather than work incapacity.

The recommended approach is distributed submission as primary pathway with individual self-reporting as backup for edge cases where credentialed submitters don't exist. This hybrid acknowledges that not every employment situation involves employers willing or able to credential with states, particularly informal work arrangements, very small employers, and family caregiving situations. The backup pathway prevents coverage loss when distributed systems cannot accommodate specific circumstances.

The political economy of this choice matters. Distributed systems shift costs from individuals to organizations. Employers bear submission system costs. Payroll processors integrate with state systems. Managed care organizations provide verification concierge services. Educational institutions report enrollment automatically. These entities have capacity to absorb costs that individuals lack, but they resist mandates creating compliance obligations. State regulators must balance efficiency gains from distributed systems against political resistance from organizations bearing costs.

Employers particularly resist verification mandates. They view work hour reporting to Medicaid as outside their business scope, creating administrative burdens and potential liability exposure. Large employers can absorb integration costs through existing payroll systems, but small employers lack infrastructure. States can make employer participation voluntary, accepting lower automation rates. Or states can mandate participation above size thresholds, potentially facing legal challenges about whether states can require employers to participate in federal-state health programs.

## Large Employer Integration

Employers with 100 or more employees typically use sophisticated payroll systems from providers like ADP, Gusto, Paychex, or Workday. These systems already track hours worked for wage calculation, overtime management, and tax reporting. Integration with state Medicaid verification requires building API connections transmitting monthly hours for employees receiving Medicaid, using standardized data formats including Social Security numbers or Medicaid IDs, hours worked, and pay period dates.

The technical implementation is straightforward for payroll providers who already manage similar data transmissions for unemployment insurance, wage garnishment, and child support. The question is business incentive. States can mandate participation, creating compliance obligations. Or states can create incentives through reduced administrative burden elsewhere, liability protections, or direct payment. The regulatory choice determines participation rates and implementation timelines.

Cost allocation matters. One-time integration costs range from $500 to $5,000 per employer depending on payroll system complexity. Ongoing costs are minimal since automation handles monthly transmission. States can require employers to bear these costs as condition of operation, essentially imposing unfunded mandates on business. Or states can fund integration costs directly, treating verification infrastructure as legitimate government expense. The first approach shifts costs but may face political resistance. The second approach protects businesses but increases state budgets.

Coverage estimates suggest that large employer automation could verify work for 40-50% of expansion adults, since significant portions work for corporations and institutions with established HR infrastructure. This automation concentration creates verification for half the population through perhaps 5,000 to 10,000 large employers, leaving the other half requiring different approaches. The verification architecture must accommodate both automated and manual pathways simultaneously.

## Small Employer Accommodation

Small employers under 100 employees lack HR infrastructure for system integration but employ significant portions of expansion adults, particularly in retail, restaurants, construction, home health, and personal services. These sectors feature irregular scheduling, cash pay, informal arrangements, and high turnover complicating verification. States need verification pathways accommodating small business limitations without creating coverage loss from missing documentation.

Simple web portals offer one approach. Employers log into state systems monthly, enter employee Medicaid IDs and hours worked, and receive confirmation emails. This requires no special software or integration, just internet access and willingness to complete monthly tasks. The burden is modest for employers with few Medicaid-enrolled employees but becomes substantial for restaurants or home health agencies with dozens. The approach works for willing employers but provides no mechanism for reluctant ones.

Industry association intermediaries provide sector-specific solutions. Restaurant associations, construction industry groups, home health associations, and chambers of commerce can serve as bulk submitters, accepting reports from member employers and transmitting to states in aggregated files. This leverages existing relationships and creates submission infrastructure without requiring states to manage thousands of small employer relationships. But it depends on association willingness to add administrative functions to their missions and capacity to manage data security obligations.

Managed care organization intermediaries shift verification responsibility to health plans. Employers submit verification to the MCO covering their employee rather than to the state. MCOs aggregate submissions from multiple employers for their members and transmit to state systems. This decentralizes verification across health plans while maintaining automation potential. It aligns with MCOs' care coordination missions and leverages their existing member relationships. The cost is included in capitation rates, distributing verification expenses across the entire Medicaid managed care system rather than concentrating on small employers.

Simplified attestation creates the lowest-burden pathway. Employers complete one-page forms monthly confirming employees worked specific hours, submitted via email, fax, or mail. This requires minimal employer effort and no technology investment, but creates substantial manual processing burdens for states. The approach works as backup for situations where other methods fail, but cannot scale to verify work for millions.

States will likely need all four approaches simultaneously. Web portals for motivated small employers with computer access. Industry associations for sectors with strong trade groups. MCO intermediaries for members whose employers resist direct state reporting. Simplified attestation as last resort. This creates system complexity but accommodates the employment landscape diversity facing expansion adults.

## Self-Employment Paradox

**Self-employed individuals have no employer to verify hours, creating verification challenges where autonomy and entrepreneurship clash with documentation requirements.** Someone running a small business, working as independent contractor, or freelancing generates income but may not produce conventional employment documentation. States must balance verification integrity against creating barriers that effectively exclude self-employed people from Medicaid regardless of work.

Tax-based approaches use quarterly estimated tax payments as self-employment proof. Business receipts and invoices document ongoing activity. This verifies income generation but not hours worked, since successful businesses may require few hours while struggling ones demand many with little income. The approach works for verification that work occurs but poorly for hour threshold compliance.

Calendar logs shift to self-reporting, requiring people to maintain records showing daily hours worked and submit monthly through portals. Random audits request supporting documentation like invoices, receipts, client emails, or contracts. This creates honor systems with verification, accepting that perfect accuracy is impossible but deterring fraud through audit risk. The fraud concern is real, since self-reporting invites exaggeration, but the question is whether states trust people more than they fear false claims.

Client attestation mimics employer verification by having customers or clients confirm work performed. Someone providing lawn care, house cleaning, childcare, or consulting can request client letters verifying services and approximate hours. This creates verification parallels with employment but imposes burdens on clients who may resist providing documentation for service providers' government program participation. The approach works in some contexts, particularly ongoing service relationships, but fails for transactional or customer-facing businesses where client attestation is impractical.

The recommended approach combines quarterly tax evidence proving active self-employment with monthly hour self-reporting backed by moderate audit rates around 15%, higher than standard employment verification but lower than maximum audit intensity. This accepts some verification uncertainty in exchange for not excluding self-employed people through documentation impossibility. Starting businesses count as qualifying activity for the first six months, recognizing that business launch involves substantial work before revenue generation.

## Gig Economy Architecture

Platform companies like Uber, DoorDash, Instacart, and TaskRabbit resist classification as employers, complicating verification since workers cannot easily document hours. Platform payments don't itemize time worked. Workers often engage with multiple platforms simultaneously, creating aggregation challenges. The population is significant and growing, making gig work verification essential to preventing coverage loss for this emerging workforce segment.

Platform partnership negotiations could resolve this cleanly. States can negotiate data sharing agreements where platforms provide monthly hours logged by workers, automated transmission to state systems, and worker consent management through platform apps. In exchange, states provide safe harbor liability protections clarifying that platforms reporting hours face no obligation to verify work quality, employment status, or contractor classification. The data sharing creates verification without forcing platforms into employment relationships they resist.

The business incentive for platforms is avoiding individual worker documentation burdens that create platform reputation problems. If platform workers lose Medicaid coverage from inability to document gig work, platforms face worker dissatisfaction and potential organizing pressure. Providing verification data costs platforms little since they already track hours for payment purposes. The regulatory challenge is negotiating agreements with perhaps 20 major platforms covering the majority of gig workers without requiring universal platform participation.

Bank statement verification provides fallback for platforms without data agreements. Individuals submit bank statements showing deposits from platform companies, explaining hours corresponding to income through self-reporting, with random audits requesting platform screenshots or payment records. This creates verification pathways when platform partnerships don't exist but imposes more individual burden than automated platform reporting. The verification standard accepts reasonable hour estimates rather than demanding perfect accuracy.

Self-attestation with high audit rates becomes last resort. Workers self-report platform hours through portals, uploading screenshots when possible, with 25% random audit rates reflecting heightened fraud concerns. Audits request detailed platform data, tax documents, or bank records. This maintains access when other approaches fail but creates verification uncertainty that some states will resist accepting.

## Seasonal Work and Hour Banking

Agricultural workers, tourism employees, holiday retail staff, and construction workers in harsh climates face months with zero hours and months with 200-plus hours. Traditional monthly 80-hour requirements fail to accommodate predictable seasonal employment patterns. States must decide whether to build flexibility mechanisms or force seasonal workers into off-season exemption applications despite planning to return to work when seasons resume.

Hour banking allows excess hours above 80 monthly to carry forward to future months, creating cushions for off-seasons. Someone working 180 hours in July can bank 100 excess hours, covering August and September at zero hours while maintaining compliance. Banking caps prevent indefinite accumulation, perhaps limiting banks to 240 hours providing three-month cushions. This creates flexibility through accounting mechanisms without requiring federal waivers or exemption processing.

The system complexity is manageable. Eligibility systems track cumulative hour balances. Portals show members their banked hours. Employers submit hours normally without needing to understand banking rules. Automation applies banking logic calculating net positions after each month's hours. The administrative burden falls on systems rather than people.

Annual averaging would provide more flexibility by requiring 960 annual hours without monthly minimums, allowing workers to concentrate hours in peak seasons and work zero in off-seasons. But OB3 specifies monthly requirements, making annual averaging potentially non-compliant without federal flexibility waivers. States can request waivers arguing that annual averaging better serves seasonal workers, but approval timelines may not align with December 2026 implementation deadlines.

Known off-season exemptions provide sector-specific relief by automatically exempting workers in industries with predictable seasonal patterns during documented off-seasons. Agricultural workers exempt November through March. Ski resort employees exempt May through October. Summer tourism workers exempt October through April. This requires defining which industries qualify and determining geographic seasonal patterns, creating administrative complexity but potentially preventing thousands of exemption applications.

## The Communication Architecture

**Verification architecture means nothing without communication systems ensuring people understand requirements, know how to comply, and receive help when struggling.** State communication choices determine whether verification barriers create systematic exclusion or manageable compliance processes.

Notification timing and clarity matter. Someone learning about requirements one week before first compliance deadline faces scrambling to establish verification pathways. Someone receiving information 90 days before requirements begin with clear explanations of multiple compliance options has realistic opportunity to succeed. States can send notices 30, 60, or 90 days before requirements begin, each creating different preparation timelines. The question is whether states prioritize giving people maximum preparation time or minimize advance notice periods.

Channel diversity acknowledges that different populations access information differently. Mailed letters reach people with stable addresses. Text messages reach people with phones. Email reaches digitally connected populations. MCO member services reach people engaged with health plans. Provider communication reaches people during healthcare visits. Community organization outreach reaches people connected to social services. States can rely primarily on mail, accepting that unstably housed people and address change situations create gaps. Or states can use multi-channel approaches accepting higher communication costs to maximize reach.

Language access determines whether non-English speakers can understand requirements and compliance pathways. Materials in threshold languages serving significant populations are minimally compliant with civil rights requirements, but dozens of languages below threshold percentages still represent thousands of people who cannot access English-language information. States can provide materials in 10 threshold languages, serving perhaps 85% of non-English speakers. Or states can invest in comprehensive translation covering 30-plus languages, serving 95-plus percent. The gap represents thousands of people whose coverage depends on translation investment levels.

Literacy accommodation matters regardless of language. Sixth-grade reading level is standard government communication guidance, but many expansion adults read at lower levels or are functionally non-literate. Visual materials using graphics, pictographs, and symbols can communicate requirements to non-literate populations. Video content explains processes for people who understand spoken language but struggle with written text. States can rely on text-based materials at sixth-grade level, accepting literacy-based exclusion. Or states can invest in multimedia approaches accommodating varied literacy levels.

**The verification infrastructure question is ultimately about trust and burden distribution. States trusting people create verification support infrastructure minimizing individual burden. States skeptical of compliance create individual responsibility systems expecting people to navigate complexity without support.** The regulatory choices determining verification architecture reveal fundamental assumptions about human motivation, bureaucratic capacity, and safety net purposes that shape coverage outcomes far more than technical specifications suggest.

---

*Next in series: Article 7C, "The Coordination Architecture"*

*Previous in series: Article 7A, "The Exemption Architecture"*

## References

1. Sommers, Benjamin D., et al. "Medicaid Work Requirements in Arkansas: Two-Year Impacts on Coverage, Employment, and Affordability of Care." Health Affairs, vol. 39, no. 9, 2020, pp. 1522-1530.

2. Government Accountability Office. "Medicaid Demonstrations: Evaluation of Arkansas Work Requirement." GAO-20-149, November 2019.

3. National Conference of State Legislatures. "Medicaid Work Requirements: State Approaches." NCSL.org, 2025.

4. Urban Institute. "Understanding Gig Economy Work and Medicaid Work Requirements." Urban.org, March 2025.

5. Kaiser Family Foundation. "Medicaid Work Requirements: Key Questions." KFF.org, September 2025.

6. Center on Budget and Policy Priorities. "Work Requirement Verification Systems: Lessons from SNAP and TANF." CBPP.org, April 2025.

7. U.S. Department of Labor. "API Documentation for Unemployment Insurance Data Sharing." DOL.gov, 2025.

8. National Student Clearinghouse. "Enrollment Verification for Government Programs." StudentClearinghouse.org, 2025.

9. Georgia Department of Community Health. "Pathways to Coverage Implementation Reports." DCH.Georgia.gov, 2025.

10. Arkansas Department of Human Services. "Arkansas Works Lessons Learned." DHS.Arkansas.gov, 2019.

---
title: "Regional Health Information Organizations"
date: 2026-05-15
author: "Syam Adusumilli"
summary: "Data Infrastructure or Overhead?"
description: "RHTP Series 6: Regional Health Information Organizations"
tags: ["rural-health", "rhtp", "series-6"]
categories: ["Rural Health Transformation"]
series: ["Series 6: Intermediary Organizations"]
showtoc: true
tocopen: false
ShowReadingTime: true
ShowWordCount: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
  image: "cover.webp"
  alt: "Regional Health Information Organizations"
  relative: true
  hidden: false
params:
  article_id: "RHTP-6C"
  article_type: "article"
  series_number: 6
  series_title: "Intermediary Organizations"
  summary_url: "../regional-health-information-organizations-summary/"
  collection: "rural-health"
---

Regional Health Information Organizations face a fundamental tension between **technical value and overhead cost**. RHIOs and Health Information Exchanges promise the data infrastructure that enables care coordination and population health management. The premise is straightforward: transformation requires information, information requires exchange, exchange requires infrastructure, and RHIOs provide that infrastructure.

The reality is considerably more complicated. Some RHIOs deliver genuine technical value. They aggregate clinical data across providers, enable real-time care coordination, support population health analytics, and integrate public health reporting. These organizations justify their costs through measurable improvements in care quality and efficiency.

Other RHIOs absorb significant resources while delivering minimal actual functionality. They report extensive activities, maintain organizational infrastructure, employ staff, and consume funding. But the promised data exchange remains limited, adoption lags, and providers continue operating in information silos despite the RHIO's existence.

**RHTP implementation depends on states' ability to distinguish between these categories.** Many states lack the technical expertise to assess RHIO claims. The result: transformation funding flows to organizations whose value remains uncertain, while states assume data infrastructure exists that may function only on paper.

## The Technical Promise

The theoretical case for RHIOs as transformation infrastructure is compelling. Rural healthcare transformation requires several capabilities that depend on information exchange.

**Care coordination across fragmented systems** represents the core use case. Rural patients frequently travel to urban specialists, receive care from multiple providers, and present to emergency departments that lack access to their medical histories. When a patient from rural Kentucky presents to a Louisville emergency department, the treating physician needs access to medication lists, allergies, recent test results, and active diagnoses. Without exchange infrastructure, this information exists only in the patient's memory or scattered across paper records and disconnected EHR systems.

**Population health management** requires aggregated data that no single provider possesses. Identifying patients at risk for diabetes complications, tracking vaccination coverage, monitoring chronic disease outcomes, and targeting interventions to high-risk populations all depend on data from multiple sources. Individual providers see only their own patients. Population health requires the broader view that data aggregation enables.

**Quality measurement and improvement** similarly depends on aggregated data. RHTP requires states to demonstrate transformation outcomes. Those outcomes require measurement. Measurement requires data. For many metrics, the relevant data spans multiple providers and settings.

**Public health integration** has become increasingly urgent since the COVID-19 pandemic exposed reporting infrastructure limitations. Electronic case reporting, syndromic surveillance, immunization registries, and disease tracking all benefit from HIE infrastructure that connects clinical care to public health systems.

The Trusted Exchange Framework and Common Agreement now provides federal backing for nationwide interoperability, with **seven Qualified Health Information Networks connecting over 244 million individuals** to facilitate exchange across state and network boundaries (CommonWell Health Alliance). This national infrastructure creates new possibilities while raising questions about state-level RHIO relevance.

## The Overhead Reality

Against this technical promise stands the persistent reality of HIE sustainability challenges. Many RHIOs depend primarily on grant funding rather than sustainable revenue models. This dependency suggests that the value proposition for participating organizations has not materialized sufficiently to support ongoing operations.

**Research consistently shows limited participation and use despite organizational claims.** One study found that only **10.7% of US hospitals engaged in HIE with unaffiliated providers**, indicating that organizational participation rates dramatically overstate actual exchange activity (Adler-Milstein et al.). Hospitals may technically participate in an HIE while rarely or never actually exchanging data.

**Critical Access Hospitals, the rural facilities most dependent on transformation, show particularly low HIE participation.** South Carolina data found that while overall hospital HIE participation increased from 43% in 2014 to 82% by 2020, **Critical Access Hospitals were 90% less likely to participate** than prospective payment system hospitals even after controlling for other factors (Zhang et al.). The facilities that transformation targets may be least connected to the infrastructure designed to support them.

**Actual use rates remain low even where infrastructure exists.** Indiana's mature statewide HIE, the Indiana Network for Patient Care, connecting 117 hospitals and over 17,000 practices, found that only **4.7% of all clinical encounters resulted in providers accessing external patient information** through the exchange (Vest et al.). Infrastructure existence does not equal infrastructure use.

**Competition dynamics undermine exchange.** For-profit hospitals and those with smaller market shares prove significantly less likely to engage in HIE, suggesting that competitive concerns about sharing data with rivals override the potential benefits of exchange (Adler-Milstein et al.). Rural transformation requires collaboration that market dynamics discourage.

## RHIO and HIE Landscape

The following table examines state-designated HIEs and major RHIOs to illustrate the variation in organizational capacity, functionality, and RHTP role:

| Organization | State | Participants | Technical Capability | RHTP Role | Subaward | Value Assessment |
|--------------|-------|--------------|---------------------|-----------|----------|------------------|
| Indiana Network for Patient Care | Indiana | 117 hospitals, 17,000+ practices | Query-based exchange, clinical messaging, analytics | Population health data | $8.2M | High |
| CRISP | Maryland/DC | 4,000+ care sites | ADT alerts, query, analytics, PDMP integration | Care coordination infrastructure | $7.8M | High |
| CORHIO | Colorado | 8,500+ providers | Query, public health reporting, rural outreach | Rural connectivity | $6.4M | Moderate-High |
| Healthcurrent | Arizona | 3,200+ providers | Query, ADT alerts, public health | Data infrastructure | $5.9M | Moderate |
| CurrentCare (RIQI) | Rhode Island | 850+ care sites | Query, public health, consent management | Care coordination | $4.2M | Moderate-High |
| SHIN-NY Network | New York | 10 RHIOs statewide | Federated query, DSRIP support | Transformation data | $14.6M | Moderate |
| Health Info Net | Maine | 400+ care sites | Clinical messaging, query | Rural coordination | $3.8M | Moderate |
| Kansas Health Information Network | Kansas | 180+ care sites | Direct messaging, limited query | Basic exchange | $2.9M | Low-Moderate |

The variation is stark. Indiana's INPC represents a mature, functional infrastructure developed over two decades with demonstrated use patterns and measurable value. Kansas Health Information Network offers basic functionality that may not justify the overhead required to maintain it. Most state HIEs fall somewhere between these poles, with capabilities that exceed minimal functionality but fall short of the sophisticated infrastructure that transformation requires.

## The Activity-Outcome Gap

A fundamental challenge pervades RHIO oversight: **the difference between activity and outcome often remains invisible to state agencies**. RHIOs report activities because activities are measurable and contractually defensible. Onboarding sessions conducted, alerts deployed, dashboards developed, data feeds established. Activity metrics can appear strong while actual functionality remains limited.

States typically lack technical expertise to assess RHIO claims independently. Agencies overseeing RHTP implementation employ policy analysts and program managers, not health IT specialists. When an HIE reports deploying care coordination alerts to 23 facilities, the state cannot easily determine whether 23 facilities actively use those alerts or whether the technology sits dormant.

**The pattern produces predictable failure modes.** Onboarding sessions occur, but providers do not adopt systems. Alerts deploy, but workflows do not incorporate them. Dashboards exist, but data does not populate them. Population health analytics require data from 34 rural providers but contain information from only 12. Public health data feeds transmit information but format inconsistencies prevent integration.

This pattern is not universal. High-functioning HIEs like Indiana's INPC demonstrate that meaningful exchange can occur. But distinguishing genuinely functional infrastructure from activity-reporting organizations **requires technical assessment capacity that most state agencies lack**. RHTP investment in RHIO infrastructure without corresponding investment in state oversight capacity risks funding technology that exists on paper while providers continue operating in information silos.

## Alternative Perspective: The Disintermediation Argument

Some observers argue that **state-level RHIOs represent obsolete infrastructure** whose functions have been superseded by national networks and vendor-enabled interoperability. This disintermediation argument merits serious consideration.

**National networks now enable direct exchange without state-level intermediaries.** CommonWell Health Alliance connects over 37,000 provider organizations with more than 8.5 billion health records retrieved. Carequality links additional networks and EHR vendors. TEFCA creates a framework for nationwide interoperability with federal backing. These national capabilities raise legitimate questions about whether state-level infrastructure remains necessary.

**EHR vendors increasingly offer built-in interoperability.** Epic's Care Everywhere, Cerner's CommonWell integration, and similar vendor capabilities enable exchange among facilities using the same or connected systems. For providers already connected through their EHR vendor, a state RHIO may duplicate existing functionality while adding cost.

**Assessment: This argument is partially valid for clinical exchange between large providers but less valid for the specific functions that rural transformation requires.** National networks connect primarily large health systems with sophisticated EHR implementations. Rural providers, particularly small practices and Critical Access Hospitals with older systems and limited IT capacity, often lack the infrastructure to leverage national network connectivity directly.

State-level RHIOs retain potential value for several functions:
- **Rural provider connectivity** to providers too small to connect directly to national networks
- **Public health data integration** with state surveillance and reporting systems
- **Population health analytics** using data aggregated across a defined geography
- **Local relationship management** supporting adoption and workflow integration

The disintermediation argument reveals a strategic question RHTP implementation must address: **Which functions require state-level infrastructure, and which can leverage national capabilities?** States investing in RHIOs should demonstrate specific value that national alternatives cannot provide.

## RHTP Subaward Analysis

RHIO subawards reveal consistent patterns across states:

**Technical deliverables often lack specificity.** Subawards specify "data exchange infrastructure" or "population health capabilities" without defining measurable functionality standards. This vagueness enables RHIOs to report completion while actual functionality remains uncertain.

**Sustainability models rarely survive beyond grant funding.** RHIOs propose fee-based or value-based sustainability during subaward negotiation. These models typically depend on provider adoption rates that do not materialize or payer participation that fails to emerge. RHTP funding often supports organizations that will struggle to continue operations after 2030.

**Rural provider focus varies significantly.** Some subawards explicitly target rural connectivity and measure progress by rural provider adoption. Others treat rural providers as one segment among many, with limited accountability for rural-specific outcomes.

**Pass-through percentages range from 15% to 55%.** Some RHIOs retain most funding for infrastructure and staff while passing limited resources to providers. Others function primarily as pass-through entities directing resources to connected facilities. Neither model guarantees value; the appropriate structure depends on what infrastructure actually requires.

**Outcome accountability remains rare.** States measure provider connections, system deployments, and data volume. They rarely measure whether providers access exchanged data, whether access improves clinical decisions, or whether patients experience better coordinated care. Activity metrics dominate; outcome metrics barely exist.

## When RHIOs Help Transformation

RHIOs contribute genuine value under specific conditions:

**Mature, functional infrastructure that predates RHTP.** States with established HIEs demonstrate years of operational experience. Indiana, Maryland, and Colorado built infrastructure over decades before RHTP existed. RHTP funding enhances existing capability rather than building from scratch. Transformation benefits from infrastructure that already works.

**Population health data aggregation for rural areas.** Small rural providers cannot aggregate population-level data independently. State HIEs with comprehensive rural provider participation can generate analytics that individual facilities cannot produce. This value depends on actual rural provider data flowing through the exchange.

**Public health integration.** COVID-19 revealed critical gaps in clinical-to-public-health data flows. States with functional HIE infrastructure responded more effectively to pandemic surveillance needs. This public health value exists independent of individual provider benefit, justifying public investment.

**Quality measurement support.** RHTP requires outcome measurement that depends on data from multiple sources. HIEs can aggregate the measurement data that transformation accountability requires. This function depends on HIE capacity to produce reliable, standardized measures.

**Rural provider technical assistance.** Some HIEs pair infrastructure with implementation support, helping rural providers adopt systems and integrate exchange into workflows. This combination of technology and support proves more valuable than either alone.

## When RHIOs Hinder Transformation

RHIOs impede transformation under different conditions:

**Overhead absorption without technical delivery.** RHIOs employ staff, maintain offices, conduct outreach, and report activities. When these activities do not translate to functional infrastructure, the overhead consumes resources that could support direct provider assistance or alternative approaches.

**Promises exceeding demonstrated capability.** RHIOs seeking RHTP funding often propose capabilities they have not demonstrated. States accept proposals based on promised functionality. When functionality fails to materialize, transformation proceeds without the assumed infrastructure.

**Sustainability models dependent on RHTP continuation.** Some RHIOs' only viable business model is continued grant funding. These organizations may provide value during the grant period but create dependency rather than lasting infrastructure. The 2030 cliff becomes a cliff for HIE operations as well as transformation generally.

**Competition with proven alternatives.** RHTP funding directed to state RHIOs may divert resources from national network participation, EHR vendor interoperability, or direct provider investment that would deliver greater value. Incumbent RHIOs may advocate for their continued funding despite evidence that alternatives perform better.

**Technical complexity exceeding state oversight capacity.** States lacking health IT expertise cannot assess RHIO performance independently. RHIOs may deliver inadequate functionality while reporting success, with states unable to identify the gap until transformation outcomes fail to materialize.

## The Sustainability Challenge

RHIO sustainability has proven elusive despite decades of investment. Understanding why illuminates risks that RHTP investment faces.

**Grant dependency persists because value propositions have not materialized.** If providers found HIE access valuable, they would pay for it. Most do not. This market signal suggests that the value delivered to individual providers does not justify the cost. Public goods arguments, based on benefits that accrue to the system rather than individual participants, justify public investment but do not solve organizational sustainability.

**Fee-based models struggle with rural participation economics.** RHIOs charging per-transaction fees or subscription costs may find rural providers unable or unwilling to pay. Rural facilities with thin operating margins cannot afford services that urban facilities absorb. Fee structures that enable urban sustainability may exclude rural participation.

**Value-based payment incentives have not consistently materialized.** Some RHIOs proposed sustainability models dependent on value-based payment creating incentives for HIE participation. But value-based payment adoption varies. States and payers implementing VBP may not direct savings to HIE support. The business model depends on external decisions RHIOs cannot control.

**The 2030 cliff affects RHIOs directly.** Organizations dependent on RHTP funding face uncertain futures after program conclusion. States assuming continued RHIO functionality may find that infrastructure disappears when funding ends. Investment in organizations that cannot survive beyond the grant period does not build lasting transformation capability.

States should require sustainability plans with evidence of viability before committing RHTP resources to RHIO expansion. Plans dependent on external factors, such as payer decisions or market changes, that RHIOs cannot control represent hope rather than strategy.

## Recommendations

**For States:**
Commission independent technical assessment of RHIO capabilities before finalizing subawards. Assessment should evaluate actual functionality, not organizational claims. Examine data volumes, query response times, adoption rates, and usage patterns. Compare claimed capabilities to measured performance.

Specify outcome metrics, not just activity metrics. Measure whether providers access exchanged data, not just whether systems exist. Measure whether exchanged data affects clinical decisions, not just whether data flows through the system.

Evaluate RHIO value against national alternatives. Determine which functions require state-level infrastructure and which can leverage TEFCA, Carequality, CommonWell, or EHR vendor capabilities. Invest in state infrastructure only where state-specific value exists.

Require sustainability planning that does not depend on continued grant funding. Assess whether proposed business models have evidence of viability. Avoid building dependency on infrastructure that cannot survive the 2030 transition.

**For RHIOs:**
Demonstrate specific value that national alternatives cannot provide. Identify the functions where state-level infrastructure adds capability beyond what providers can access through their EHR vendors or national networks.

Accept outcome accountability. Report not just what you have built but evidence that what you have built delivers value. Usage data, adoption rates, and clinical workflow integration provide more meaningful measures than system deployment counts.

Focus on rural provider needs specifically. Generic HIE infrastructure may serve urban providers adequately while leaving rural facilities disconnected. Design implementation approaches that address the specific barriers rural providers face, including limited IT staff, older EHR systems, connectivity challenges, and workflow constraints.

Plan for sustainability from inception. Grant-dependent business models postpone sustainability challenges; they do not solve them. Develop revenue models that can survive RHTP conclusion and test those models during the grant period.

**For CMS:**
Develop technical standards that reveal actual versus claimed functionality. Standardized measures of exchange activity, adoption rates, usage patterns, and outcome impact would enable meaningful comparison across states.

Require independent technical assessment for major RHIO subawards. States often lack expertise to evaluate HIE claims. Federal technical assistance or independent assessment requirements would strengthen oversight.

Monitor RHIO overhead ratios across states. Significant variation in pass-through percentages suggests variation in value delivered. High overhead organizations should demonstrate corresponding high value.

Support alternatives to RHIO-dependent models. Some states may achieve better outcomes through national network participation, direct provider investment, or regional collaboration that does not depend on a single state-designated entity.

## The Rural Connectivity Gap

The technical challenges facing rural providers merit specific examination. RHIOs often describe universal participation rates without distinguishing between urban health systems with sophisticated IT infrastructure and rural providers struggling with basic connectivity.

**Critical Access Hospitals frequently operate older EHR systems** that lack native interoperability features built into newer platforms. These systems may support basic clinical documentation while lacking the APIs and interfaces that enable HIE participation. Upgrading requires capital investment many rural hospitals cannot afford.

**Small rural practices may lack IT staff entirely.** A three-physician family medicine practice serving a rural community typically has no dedicated information technology support. The practice manager handles billing, scheduling, and basic computer troubleshooting. Configuring HIE connections, maintaining interfaces, and troubleshooting exchange failures falls outside available expertise.

**Broadband limitations affect rural connectivity.** Some rural areas still lack reliable high-speed internet access. Real-time clinical data exchange requires bandwidth that dial-up or basic DSL connections cannot provide. RHIOs may report rural provider participation without acknowledging that participation produces minimal actual exchange.

**Workflow integration proves particularly challenging** for small practices. Larger organizations can assign staff to monitor HIE alerts and retrieve relevant information. In small practices, clinicians must interrupt patient care to access exchange systems. If accessing outside records takes more time than calling the referring provider, workflow economics discourage use even where technical connectivity exists.

These rural-specific barriers mean that aggregate participation statistics often overstate rural provider engagement. **A state HIE may report 80% provider participation while rural providers contribute minimally to actual exchange.** States evaluating RHIO subawards should examine rural participation specifically, not overall statistics that may mask rural connectivity gaps.

## Measuring What Matters

The fundamental challenge in evaluating RHIO value is measurement. Activity metrics are easy to count: providers connected, data volumes transmitted, sessions logged. But these metrics may not capture whether exchange improves care.

**Clinical utility differs from technical functionality.** A physician may have technical access to a patient's records from another provider while finding those records practically useless. If the exchange delivers documents formatted for billing rather than clinical decision-making, if relevant information is buried in hundreds of pages of data, or if access requires interrupting patient care to navigate unfamiliar systems, technical exchange may not produce clinical value.

**Population health value requires analytical capability.** RHIOs aggregating data for population health management must do more than store information. They must analyze it, identify patterns, produce actionable insights, and deliver those insights in formats that support intervention. An RHIO that collects data without producing usable analytics provides storage, not intelligence.

**Public health integration requires more than data feeds.** Transmitting data to public health agencies helps only if those agencies can receive, process, and act on the information. Format incompatibilities, data quality issues, and inadequate public health informatics capacity can render exchange technically successful but practically worthless.

States evaluating RHIO performance should examine:
- **Query volumes** indicating how often providers actually access exchanged information
- **Clinical utility assessments** from providers using exchange systems
- **Population health outputs** demonstrating analytical capability, not just data aggregation
- **Public health integration results** showing that transmitted data supports surveillance and response

Activity metrics alone cannot distinguish between infrastructure that delivers value and infrastructure that exists without consequence.

## Conclusion

Regional Health Information Organizations occupy an uncertain position in RHTP implementation. Their theoretical value is clear: transformation requires data infrastructure, and RHIOs promise to provide it. But the gap between promise and delivery varies enormously across states and organizations.

Some RHIOs represent mature, functional infrastructure that genuinely enables care coordination, population health management, and public health integration. Investment in these organizations builds on proven capability. Other RHIOs absorb resources while delivering minimal actual functionality. Investment in these organizations diverts funding from alternatives that might perform better.

The challenge for states is distinguishing between these categories. Activity reports document what RHIOs do. They do not reveal whether what RHIOs do actually works. States lacking technical expertise to assess functionality independently may invest in infrastructure that exists only on paper.

**The rise of national exchange networks creates additional complexity.** TEFCA, Carequality, and CommonWell offer capabilities that reduce dependence on state-level infrastructure for many exchange functions. States should evaluate which functions require state-level investment and which can leverage national alternatives.

**The core tension remains: technical value versus overhead cost.** Some RHIOs deliver value that justifies their cost. Others represent overhead without corresponding technical delivery. RHTP success depends partly on states' ability to invest in the former while avoiding the latter. Without technical assessment capacity and outcome accountability, that distinction remains difficult to make.

## Sources

Adler-Milstein, Julia, et al. "Health Information Exchange Among US Hospitals." *American Journal of Managed Care*, vol. 17, no. 11, 2011, pp. 761-768.

Brown-Podgorski, Brittany L., et al. "The Association Between State-Level Health Information Exchange Laws and Hospital Participation in Community Health Information Organizations." *AMIA Annual Symposium Proceedings*, 2018, pp. 313-320.

Civitas Networks for Health. "Health Information Exchange: Things to Consider." *Civitas for Health*, 2025, civitasforhealth.org/health-information-exchange/.

CommonWell Health Alliance. "TEFCA Connectivity." *CommonWell Health Alliance*, 2025, www.commonwellalliance.org/tefca/.

HealthIT.gov. "Interoperability and Methods of Exchange among Hospitals in 2021." *Office of the National Coordinator for Health Information Technology*, 2022.

HealthIT.gov. "TEFCA Awareness and Planned Participation Among U.S. Hospitals: 2023." *Office of the National Coordinator for Health Information Technology*, 2024.

HealthIT.gov. "Trusted Exchange Framework and Common Agreement (TEFCA)." *Office of the National Coordinator for Health Information Technology*, 2024, www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca.

New York State Department of Health. "Single Source Procurement: SHIN-NY Regional Health Information Organizations (RHIO)." *New York State Department of Health*, 2024.

Vest, Joshua R., et al. "Trends in User-Initiated Health Information Exchange in the Inpatient, Outpatient, and Emergency Settings." *Journal of the American Medical Informatics Association*, vol. 28, no. 5, 2021, pp. 1037-1044.

Wikipedia. "Health Information Exchange." *Wikipedia*, 13 Sept. 2025, en.wikipedia.org/wiki/Health_information_exchange.

Wikipedia. "Regional Health Information Organization." *Wikipedia*, 30 Aug. 2025, en.wikipedia.org/wiki/Regional_Health_Information_Organization.

Zhang, Xueyan, et al. "Successes and Barriers of Health Information Exchange Participation Across Hospitals in South Carolina From 2014 to 2020: Longitudinal Observational Study." *JMIR Medical Informatics*, vol. 11, 2023, e40959.

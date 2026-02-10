# Article 17A: Risk Adjustment Models in Medicaid Managed Care

## A State-by-State Analysis of Methodological Approaches in Expansion States, Georgia, and Wisconsin

Risk adjustment represents the actuarial backbone of Medicaid managed care payment systems. These statistical models translate clinical complexity into capitation rate differentials, ensuring that managed care organizations receive appropriate compensation for enrollees with varying health burdens. As work requirements reshape the Medicaid expansion landscape beginning December 2026, understanding how states calibrate payments to population risk becomes essential for MCOs, providers, and policymakers navigating compliance infrastructure investments.

### The Purpose of Risk Adjustment in Medicaid

**Risk adjustment modifies per-member per-month capitation payments** based on enrollee health status, demographic characteristics, and predicted healthcare utilization. Without such adjustment, MCOs would face powerful incentives toward favorable selection, preferentially enrolling healthier individuals while avoiding those with complex medical needs. The actuarial soundness requirements codified at 42 CFR 438.4 mandate that capitation rates be developed using generally accepted actuarial principles, with risk adjustment serving as the primary mechanism for ensuring payment adequacy across diverse population segments.

The fundamental challenge involves predicting future healthcare expenditures using observable characteristics from prior periods. Models accomplish this through hierarchical diagnostic classification systems that group ICD-10 codes into clinically coherent categories with associated cost weights. A beneficiary diagnosed with both diabetes and congestive heart failure receives a composite risk score reflecting the additive cost burden of managing multiple chronic conditions. This score then adjusts the base capitation rate upward, compensating the MCO for anticipated higher utilization.

### Classification of Risk Adjustment Methodologies

Four primary methodological families dominate Medicaid risk adjustment nationally, each with distinct origins, data requirements, and predictive characteristics.

**Chronic Illness and Disability Payment System (CDPS)** emerged from University of California San Diego research specifically designed for Medicaid populations. Unlike Medicare-derived models, CDPS addresses conditions disproportionately prevalent among low-income populations, including serious mental illness, substance use disorders, and developmental disabilities. The model maps ICD-10 diagnostic codes to 52 categories within 19 major hierarchies, with severity levels ranging from extra low to very high within each category. CDPS Version 7.0, released in 2023, incorporates managed care claims data from 2017 through 2019, reflecting contemporary treatment patterns rather than historical fee-for-service utilization.

**CDPS+Rx** combines diagnostic classification with pharmaceutical markers, integrating 15 restricted Medicaid Rx categories into the CDPS framework. Pharmacy data often provide more reliable condition identification than diagnostic coding alone, particularly for chronic conditions requiring ongoing medication management. California pioneered pharmacy-based risk adjustment through Medicaid Rx before transitioning to the combined model, recognizing that prescription patterns reveal disease burden even when diagnostic coding remains incomplete.

**Johns Hopkins Adjusted Clinical Groups (ACG)** takes a fundamentally different approach, grouping individuals into mutually exclusive morbidity categories based on total disease burden rather than individual conditions. Developed initially for commercial populations, ACG assigns each beneficiary to a single risk category reflecting cumulative comorbidity patterns. The system emphasizes ambulatory care sensitivity, capturing primary care utilization patterns that predict future healthcare needs.

**Solventum Clinical Risk Groups (CRG)**, formerly 3M Clinical Risk Groups, assigns each patient to a single mutually exclusive category based on historical clinical and demographic characteristics. The methodology incorporates over 360 base groups with more than 1,300 total concurrent model risk groups including severity levels. New York Medicaid adopted CRGs in 2008 for MCO capitation rate adjustment, valuing the categorical clarity that comes from assigning beneficiaries to discrete risk tiers rather than accumulating additive condition scores.

**Diagnostic Cost Groups (DxCG)**, developed through Boston University research in partnership with CMS, provides the methodological foundation for Medicare Advantage risk adjustment. While Medicare applications dominate, Massachusetts employs DxCG for Medicaid populations, leveraging the model's extensive validation across large populations and its sophisticated handling of hierarchical condition relationships.

### State-by-State Model Adoption

Among states implementing Medicaid work requirements or operating expansion programs subject to future federal mandates, **CDPS variants dominate the methodological landscape**. Of 38 state Medicaid programs employing risk adjustment, 33 utilize CDPS or CDPS+Rx, reflecting the model's explicit design for Medicaid populations and its availability through the University of California San Diego without proprietary licensing fees.

| State | Model | Year Implemented | Populations Covered |
|-------|-------|------------------|---------------------|
| Arizona | CDPS+Rx | 2020 | SSI + TANF + Expansion |
| California | CDPS+Rx | 2009/2023 | SSI + TANF + Expansion |
| Colorado | CDPS | 1997 | SSI + TANF |
| Delaware | CDPS+Rx | 2000 | SSI + TANF + Expansion |
| District of Columbia | CDPS+Rx | 2014 | SSI + TANF |
| Florida | CDPS+Rx | 2006 | SSI + TANF |
| Georgia | CDPS+Rx | 2017 | TANF only |
| Hawaii | CDPS+Rx | 2014 | SSI + TANF + Expansion |
| Illinois | CDPS+Rx | 2011 | SSI + TANF + Expansion |
| Indiana | CDPS+Rx | 2015 | SSI + TANF + Expansion |
| Iowa | CDPS+Rx | 2016 | SSI + TANF + Expansion |
| Kansas | CDPS+Rx | 2018 | SSI + TANF + CHIP |
| Kentucky | CDPS+Rx | 2019 | SSI + TANF + Expansion |
| Louisiana | ACG | 2012 | SSI + TANF + Expansion |
| Maryland | ACG | 1997 | SSI + TANF |
| Massachusetts | DxCG | 2009 | SSI + TANF |
| Michigan | CDPS+Rx | 2000 | SSI + TANF + Expansion |
| Minnesota | CDPS+Rx | 2000 | TANF + Expansion + BHP + SSI |
| Mississippi | CDPS+Rx | 2017 | SSI + TANF |
| Missouri | CDPS+Rx | 2012 | TANF |
| Nebraska | CDPS+Rx | 2018 | SSI + TANF |
| Nevada | CDPS+Rx | Unknown | TANF + Expansion |
| New Hampshire | CDPS+Rx | 2014 | SSI + TANF + Expansion |
| New Jersey | CDPS+Rx | 2000 | SSI + TANF + Expansion |
| New Mexico | CDPS+Rx | 2021 | SSI + TANF + Expansion |
| New York | CRG | 2008 | SSI + TANF |
| North Carolina | CDPS+Rx | 2021 | SSI + TANF |
| Ohio | CDPS+Rx | 2006 | SSI + TANF |
| Oregon | CDPS+Rx | 1998 | SSI + TANF + Expansion |
| Pennsylvania | CDPS+Rx | 2003 | SSI + TANF + Expansion |
| Puerto Rico | CDPS+Rx | 2018 | SSI + TANF + Expansion |
| South Carolina | CDPS+Rx | 2009 | SSI + TANF |
| Tennessee | ACG | 2000 | SSI + TANF |
| Texas | CDPS+Rx | 2007 | SSI + TANF + CHIP |
| Utah | CDPS | 1998 | SSI |
| Virginia | CDPS | 2003 | SSI + TANF + Expansion |
| Washington | CDPS+Rx | 2003 | SSI + TANF + CHIP + Expansion |
| Wisconsin | CDPS+Rx | 2011 | SSI + TANF |

**California** represents a transitional case, initially implementing Medicaid Rx (pharmacy-only) risk adjustment in 2009 before transitioning to CDPS+Rx Version 6.5 for 2023 capitation rates. The state's extensive sub-capitation arrangements with provider organizations complicated diagnostic data collection, making pharmacy claims the more reliable data source during the earlier period.

### Model Performance and Predictive Accuracy

Risk adjustment models explain only a fraction of individual-level cost variation, with **R-squared values ranging from 0.11 to 0.39** across Medicaid populations. The CDPS concurrent model achieves approximately 0.26 R-squared for disabled beneficiaries, 0.11 for children, and 0.39 for adults. These values indicate that even sophisticated diagnostic classification systems leave substantial individual variation unexplained, reflecting the inherent unpredictability of healthcare utilization and the influence of factors beyond captured diagnoses.

Prospective models, which predict future-year costs based on prior-year diagnoses, necessarily achieve lower explanatory power than concurrent models examining same-year relationships. However, prospective specification better reflects the actual risk adjustment application, where MCOs receive payments based on documented conditions before incurring the costs those conditions generate.

**Model stability** varies considerably across populations. The correlation between CDPS predictions using different model versions reaches 0.98 to 0.99 across aid categories, indicating that methodological updates produce relatively consistent risk stratification despite underlying changes in code mappings and category weights. Pharmacy model correlations prove lower, ranging from 0.78 to 0.87, reflecting the continuous introduction of new medications and therapeutic categories.

### Social Determinants and Risk Adjustment Limitations

Recent policy interest has focused on incorporating social determinants of health into risk adjustment formulas, recognizing that beneficiaries facing housing instability, food insecurity, or transportation barriers may require additional resources beyond what diagnostic coding captures. Research from University of California San Diego explored adding Social Deprivation Index indicators to CDPS models, testing whether beneficiaries in economically deprived communities demonstrated systematically higher expenditures after controlling for documented health conditions.

**The findings proved unexpectedly null.** Across eight states and 17 million person-year observations, area-level deprivation showed no consistent relationship with healthcare spending once CDPS categories controlled for documented morbidity. Among adults, spending was actually negatively associated with deprivation, with beneficiaries in less deprived areas demonstrating 1.8 to 2.5 percent higher expenditures than those in the most deprived quintile.

This counterintuitive result likely reflects **access barriers** rather than lower healthcare needs. Beneficiaries in deprived areas may face greater obstacles obtaining care, resulting in lower measured utilization despite higher underlying need. Alternatively, since all Medicaid beneficiaries are low-income by definition, variation in area characteristics may not meaningfully differentiate social risk within an already disadvantaged population.

The policy implication is that **risk adjustment alone cannot address health disparities**. States seeking to direct additional resources toward socially vulnerable populations should employ direct payment mechanisms for specific services rather than attempting to incorporate social factors into capitation rate formulas.

### Implications for Work Requirements Implementation

Work requirements will reshape the characteristics of Medicaid expansion populations, with predictable consequences for risk adjustment dynamics. **Individuals unable to maintain compliance face disproportionate likelihood of having complex health conditions** that interfere with employment capacity or documentation capability. As these higher-acuity beneficiaries lose coverage, the remaining expansion population will trend toward lower average risk scores, reducing the capitation rates MCOs receive even as per-beneficiary administrative burden increases.

The **risk adjustment degradation effect** compounds the financial consequences of coverage loss. An MCO losing a beneficiary with multiple chronic conditions loses not only that member's capitation payment but also the risk-adjusted premium increment reflecting their documented morbidity. A member with congestive heart failure, diabetes, and depression might generate a risk score 3.5 times the base rate. Disenrollment eliminates that premium differential while leaving the MCO's fixed infrastructure costs unchanged.

States employing prospective risk adjustment face particular challenges during implementation transitions. **Members who lose coverage mid-year may have their prior diagnoses captured** in base period data used to calculate current-year risk scores, creating misalignment between payment levels and actual enrollment. Retrospective reconciliation mechanisms can partially address this timing mismatch, but they introduce cash flow uncertainty that complicates MCO financial planning.

### Population-Specific Model Considerations

Different Medicaid eligibility categories present distinct risk adjustment challenges that states address through model customization. **Expansion adults** represent a population without historical Medicaid analog, initially requiring states to extrapolate risk patterns from TANF adults or newly available exchange marketplace data. As expansion enrollment stabilized, states accumulated sufficient encounter data to calibrate models specifically for this population.

**Individuals with disabilities** (SSI beneficiaries) demonstrate the highest predictable cost variation, with CDPS achieving its strongest explanatory power for this population. The conditions driving disability determination, including serious mental illness, developmental disabilities, and severe physical impairments, map clearly to diagnostic categories with substantial associated costs.

**Children** present the opposite challenge, with lower cost variation making risk adjustment less impactful. Most pediatric utilization concentrates in acute episodic care rather than chronic disease management, reducing the predictive value of prior diagnoses. Several states exclude children from risk adjustment entirely or apply simplified demographic-only adjustments.

### Methodological Stability and Regulatory Oversight

CMS provides detailed guidance through annual Medicaid Managed Care Rate Development Guides, specifying documentation requirements for risk adjustment methodology selection and application. States must demonstrate that chosen models appropriately reflect population characteristics and that rate calculations follow generally accepted actuarial principles. **ASOP No. 45** (Use of Health Status Based Risk Adjustment Methodologies) and **ASOP No. 49** (Medicaid Managed Care Capitation Rate Development and Certification) establish professional standards governing actuarial practice in this domain.

Rate certification requirements ensure that risk adjustment methodologies receive systematic review rather than operating as black boxes insulated from scrutiny. Certifying actuaries must document the rationale for model selection, the data sources underlying score calculation, and the algorithms translating risk scores into capitation rate adjustments. This transparency supports both regulatory oversight and MCO financial planning.

### Risk Adjustment Impacts on Medicaid MCOs Under OB3

The One Big Beautiful Bill Act's work requirements create a **structural tension between risk adjustment mechanics and coverage stability** that will fundamentally reshape MCO financial dynamics beginning December 2026. Understanding this tension requires examining how compliance patterns interact with the risk scoring process across multiple dimensions.

**Adverse Selection Through Compliance Failure**

Work requirements do not operate as random filters on enrollment. Individuals who fail to document compliance disproportionately include those with serious mental illness, substance use disorders, cognitive limitations, unstable housing, and multiple chronic conditions. These are precisely the beneficiaries who generate the highest CDPS risk scores and contribute most substantially to MCO risk-adjusted revenue. When a member with a 3.5 risk score loses coverage for documentation failure, the MCO loses not merely the base capitation rate but the entire risk-adjusted premium, potentially exceeding $15,000 annually in high-acuity cases.

The **composition effect** compounds individual losses. As higher-risk members disproportionately churn out of coverage, the remaining enrolled population trends toward lower average acuity. State actuaries, observing declining average risk scores in encounter data, may reduce base capitation rates for subsequent contract periods. MCOs thus face a double penalty: immediate revenue loss from disenrolled high-acuity members followed by rate reductions reflecting the healthier residual population.

**Documentation Lag and Risk Score Timing**

CDPS risk scores depend on documented diagnoses from claims and encounter data, typically using a 12 to 24 month lookback period. Members who lose coverage mid-year may have their conditions captured in base period data used to calculate current-period risk scores, creating **temporal misalignment** between payment levels and actual enrollment. An MCO might receive January capitation payments reflecting a December risk score calculation that included a member who lost coverage on January 15th for work requirement noncompliance.

Prospective risk adjustment exacerbates this timing challenge. States calculating 2027 capitation rates using 2025 encounter data will capture diagnostic profiles from a period before work requirements took effect. The 2027 enrolled population, having survived twelve months of compliance screening, will demonstrate systematically different risk characteristics than the historical data underlying their payment rates.

**Risk Corridor and MLR Implications**

Many states employ **risk corridors** to share financial uncertainty between the state and MCOs during periods of enrollment volatility. These mechanisms cap both gains and losses, protecting MCOs from catastrophic underperformance while limiting windfall profits. Work requirements introduce a new source of systematic risk that existing corridor designs may inadequately address.

Medical loss ratio requirements create additional pressure. If MCOs lose high-acuity members while retaining administrative infrastructure for compliance support, their MLR numerator (medical expenses) may decline faster than their denominator (premium revenue), pushing ratios below state-mandated minimums and triggering remittance obligations. Alternatively, if MCOs invest heavily in retention navigation services, administrative costs may increase while the member base generating premium revenue shrinks.

**Strategic Responses and Retention Economics**

Sophisticated MCOs recognize that **retention investment generates asymmetric returns** under risk adjustment. The cost of navigator services, transportation assistance, and documentation support typically ranges from $300 to $500 per member annually. For a member with a 2.5 risk score generating perhaps $8,000 in annual capitation, this investment produces a 15:1 to 25:1 return if it prevents disenrollment. The economics become even more compelling for the highest-acuity members, where retention investment of $1,000 might protect $20,000 or more in risk-adjusted revenue.

This calculus creates a **natural segmentation strategy**: MCOs should concentrate retention resources on members with the highest risk scores who face the greatest compliance barriers. Chronic care management programs, traditionally focused on utilization management, become enrollment preservation mechanisms. The same infrastructure that coordinates care for members with diabetes, heart failure, and depression can simultaneously document medical exemptions, track activity hour accumulation, and ensure timely redetermination submissions.

**Network and Provider Implications**

Risk adjustment flows through MCO networks to providers through various payment arrangements. Capitated provider groups receiving delegated risk bear exposure similar to the parent MCO when their assigned members lose coverage. Value-based contracts linking provider compensation to quality metrics may produce paradoxical results if the highest-risk members, who are most likely to have care gaps, disproportionately lose coverage. Quality scores might improve even as population health deteriorates simply because the sickest patients disappear from measurement denominators.

Providers engaged in care coordination for complex Medicaid patients face **revenue cliff effects** when those patients lose coverage. A primary care practice managing 50 expansion adults with multiple chronic conditions might see significant revenue reduction if 30 percent lose coverage for compliance failures. The risk-adjusted payments supporting their care vanish overnight, with no corresponding reduction in fixed practice costs.

### Medicaid Accountable Care Organizations in the Work Requirements Era

Medicaid ACOs represent an alternative delivery model that assumes population-level accountability for cost and quality outcomes. Unlike traditional MCO arrangements where the health plan bears insurance risk, ACO models typically involve provider organizations accepting shared savings or shared risk contracts tied to total cost of care benchmarks. Work requirements introduce novel challenges that current ACO design frameworks did not anticipate.

**Attribution Instability and Benchmark Disruption**

ACO payment models depend on **stable attribution** of members to provider organizations over performance periods. Members must remain continuously enrolled and attributed long enough for care coordination investments to generate measurable returns. Work requirements introduce systematic churn that disrupts this continuity. A member attributed to an ACO in January who loses coverage in April for work requirement noncompliance cannot contribute to the ACO's annual quality metrics or cost benchmarks.

Benchmark calculations face similar instability. If an ACO's historical cost baseline reflects a population that included members who subsequently lost coverage under work requirements, the benchmark may systematically overstate expected costs for the remaining population. The ACO might appear to achieve savings simply because higher-cost members were administratively removed rather than because care delivery actually improved.

**Quality Measurement Denominator Effects**

ACO quality metrics typically calculate performance rates using attributed members as denominators. Work requirements create **selective attrition** that affects these calculations in unpredictable ways. If members with uncontrolled diabetes disproportionately lose coverage because their condition interferes with employment, the ACO's diabetes control rate might improve even though no actual clinical improvement occurred. Conversely, if the remaining population includes members with multiple barriers to care who barely maintained compliance, quality metrics might decline as these complex cases dominate shrinking denominators.

HEDIS and other quality measures explicitly address the denominator problem through continuous enrollment requirements, typically requiring 11 of 12 months coverage for inclusion. Work requirements will increase the number of members excluded from quality measurement due to coverage gaps, potentially undermining the statistical validity of performance comparisons.

**Shared Savings Distribution Under Enrollment Volatility**

Shared savings calculations compare actual expenditures to risk-adjusted benchmarks, distributing savings between the ACO and the payer when costs come in below target. Work requirements complicate every element of this calculation. **Actual expenditures** decline when high-cost members lose coverage, but this reflects administrative disenrollment rather than care efficiency. **Risk-adjusted benchmarks** may not accurately reflect the changing composition of the attributed population. **Savings attribution** becomes ambiguous when cost reductions result from coverage loss rather than care improvement.

States operating Medicaid ACO programs must develop methodologies to distinguish genuine efficiency gains from enrollment-driven cost changes. This might involve excluding disenrolled members from savings calculations, adjusting benchmarks retrospectively for population changes, or implementing minimum continuous enrollment requirements for shared savings eligibility.

**ACO Role in Compliance Support Infrastructure**

Despite these challenges, ACOs possess capabilities that could support work requirement compliance at scale. Provider-based ACOs maintain **longitudinal relationships** with attributed members that MCOs often lack. Primary care practices within ACO networks see patients regularly for chronic disease management, creating natural touchpoints for compliance monitoring and documentation support. The same care coordinators who schedule follow-up appointments and medication refills could simultaneously verify activity hour documentation and flag members at risk of coverage loss.

Oregon's Coordinated Care Organizations provide a potential model, combining MCO-like capitated payment with ACO-like provider integration and community accountability. CCOs receive global budgets covering physical health, behavioral health, and oral health services, with flexibility to invest in social determinants interventions. This integrated structure could support compliance infrastructure development in ways that fragmented MCO-provider arrangements cannot easily replicate.

**Risk Adjustment in ACO Payment Models**

ACO benchmark calculations typically incorporate risk adjustment to account for differences in population health status across organizations and over time. The same CDPS or ACG models used for MCO capitation often inform ACO benchmark development. Work requirements introduce the same risk score instability concerns affecting MCOs, with the added complexity that ACO attribution rules differ from MCO enrollment rules.

A member might lose Medicaid coverage entirely while remaining attributed to an ACO based on historical utilization patterns. The ACO's benchmark calculation might include risk scores for members no longer enrolled in Medicaid, creating systematic mismatch between payment assumptions and actual population served. States must carefully coordinate attribution rules, benchmark methodologies, and coverage policies to maintain coherent ACO payment models under work requirements.

**Integration Opportunities and Structural Advantages**

Vertically integrated delivery systems combining ACO and MCO functions may hold structural advantages in the work requirements environment. Organizations like Denver Health, which operates both a Medicaid managed care plan and an integrated delivery network, can coordinate insurance functions with care delivery in ways that separate entities cannot. Member retention benefits both the insurance and delivery components, aligning incentives around compliance support investment.

Similarly, provider-sponsored health plans where the MCO and dominant provider network share ownership can internalize the retention economics that create misaligned incentives in arm's-length contracting relationships. These integrated models may prove more resilient to work requirement disruption than traditional MCO-provider arrangements characterized by transactional rather than strategic relationships.

### Conclusion

Risk adjustment provides the technical infrastructure enabling capitated payment while accommodating population heterogeneity. The near-universal adoption of CDPS variants across Medicaid programs reflects the model's design for low-income populations and its availability without proprietary licensing barriers. As work requirements introduce new coverage instability into expansion populations, the interaction between compliance patterns and risk score dynamics will reshape both MCO and ACO financial incentives in ways that current models may inadequately capture.

For MCOs, the strategic imperative shifts toward retention investment concentrated on high-acuity members whose risk-adjusted premiums justify substantial navigation support. For ACOs, the challenge involves maintaining benchmark integrity and quality measurement validity despite enrollment volatility driven by administrative processes rather than care quality. For both organizational forms, vertically integrated structures that align insurance and delivery functions may prove most resilient to work requirement disruption.

States implementing work requirements should monitor risk score distribution changes closely, adjusting rate development methodologies and value-based payment designs as the characteristics of their enrolled populations evolve under compliance pressure.

---

### References

Gilmer, Todd, and Richard Kronick. "Updating the Chronic Illness and Disability Payment System." *Medical Care*, vol. 62, no. 3, 2024, pp. 175-181. doi:10.1097/MLR.0000000000001968.

Kronick, Richard, et al. "Improving Health-Based Payment for Medicaid Beneficiaries: CDPS." *Health Care Financing Review*, vol. 21, no. 3, 2000, pp. 29-64.

Pope, Gregory C., et al. "Risk Adjustment of Medicare Capitation Payments Using the CMS-HCC Model." *Health Care Financing Review*, vol. 25, no. 4, 2004, pp. 119-141.

Kautter, John, et al. "The HHS-HCC Risk Adjustment Model for Individual and Small Group Markets Under the Affordable Care Act." *Medicare and Medicaid Research Review*, vol. 4, no. 3, 2014, pp. E1-E46.

Centers for Medicare and Medicaid Services. "2024-2025 Medicaid Managed Care Rate Development Guide." CMS.gov, 22 Jan. 2024.

Institute for Medicaid Innovation. "Medicaid Risk Adjustment: CDPS+Rx Version 7.0 Fact Sheet." Medicaidinnovation.org, Apr. 2023.

Ash, Arlene S., et al. "Social Determinants of Health in Managed Care Payment Formulas." *JAMA Internal Medicine*, vol. 177, no. 10, 2017, pp. 1424-1430.

Actuarial Standards Board. "ASOP No. 49: Medicaid Managed Care Capitation Rate Development and Certification." American Academy of Actuaries, June 2015.

University of California San Diego. "Guidelines for Using CDPS Models for Risk Score Development." Herbert Wertheim School of Public Health and Human Longevity Science, 2023.

Solventum (formerly 3M Health Information Systems). "Clinical Risk Groups (CRGs) Classification System." 3m.com, 2024.

MACPAC. "Medicaid Managed Care Capitation Rate Setting." Issue Brief, June 2024.

Horstman, Celli E., and Corinne Lewis. "The Basics of Risk Adjustment." Commonwealth Fund Explainer, 11 Apr. 2024.

Health Management Associates. "Medicaid Managed Care Enrollment Update: Q4 2024." HMA Weekly Roundup, 10 Apr. 2025.

Society of Actuaries. "Comparison of Risk Adjustment Programs: California Medicaid Managed Care Versus CMS Medicare Advantage, Parts I and II." *Emerging Topics in Actuarial Practice*, 2023.

Johns Hopkins Bloomberg School of Public Health. "The Johns Hopkins ACG System." Center for Population Health Information Technology, 2024.

Kaiser Family Foundation. "Strategies to Manage Unwinding Uncertainty for Medicaid Managed Care Plans: Medical Loss Ratios, Risk Corridors, and Rate Amendments." KFF.org, Aug. 2023.

Oregon Health Authority. "Coordinated Care Organization 2.0: 2025 Rate Setting Methodology." Oregon.gov, Oct. 2024.

McWilliams, J. Michael, et al. "Performance Differences in Year 1 of Pioneer Accountable Care Organizations." *New England Journal of Medicine*, vol. 372, no. 20, 2015, pp. 1927-1936.

Medicaid Innovation Accelerator Program. "Risk Stratification for Beneficiary Care Needs." CMS.gov, 2020.

# Article 13D: Gaming, Fraud, and Program Integrity
## When Anti-Fraud Measures Cause More Harm Than Fraud

*Series 13: Special Topics in Work Requirements Implementation*

---

**Opening Vignette: Three Cases on Jennifer's Desk**

Jennifer has been a program integrity analyst for the state Medicaid agency for eleven years. This morning she has three flagged cases waiting for review. The fraud detection system treats all three the same way: probable cause for investigation, benefits suspended pending resolution.

The first case is obvious. The system detected 47 separate work verification submissions originating from the same IP address within a six-hour window. The names are different, the employers are different, the documents look superficially different. But the metadata reveals they were created using the same software template, uploaded sequentially, and submitted by someone who forgot to mask their location. This is a document mill, someone selling verification services to people who cannot obtain legitimate documentation or who want to avoid work requirements entirely. Jennifer refers it to the fraud investigation unit with confidence.

The second case is complicated. Tanya Williams claims 85 hours of qualifying activity through caregiving for her elderly mother. There is no formal caregiving arrangement, no home health agency, no respite care documentation. Her mother receives Social Security but no Medicaid-funded home and community-based services. Tanya submitted a written attestation describing the care she provides: bathing assistance, medication management, meal preparation, transportation to medical appointments. She included three months of pharmacy receipts showing prescriptions she picks up for her mother and a letter from her mother's physician confirming that the mother requires daily assistance with activities of daily living.

Is this fraud? Tanya is genuinely providing care. Her mother genuinely needs it. But the verification does not fit the expected documentation pattern for paid employment, volunteer hours at a registered organization, or formal caregiving through a state program. The work requirement allows caregiving as a qualifying activity, but the system was designed around employment verification and struggles with informal arrangements. Jennifer cannot determine from the file whether Tanya is gaming the system or whether the system was not designed to accommodate her legitimate circumstances.

The third case is clearly not fraud, but it arrived on Jennifer's desk anyway. Marcus Thompson's employer verification letter was rejected by the automated document processing system because it lacked a company letterhead. The letter is signed by Marcus's supervisor at a small landscaping company. It states that Marcus has worked 90 to 100 hours per month for the past six months. It includes the supervisor's phone number and email address. But the company does not have formal letterhead because it is a three-person operation run out of someone's garage. The owner prints letters on plain paper.

Marcus's coverage has been suspended for 23 days while his case sat in the review queue. He has diabetes and has not been able to afford his insulin during this period. He went to an emergency room last week when his blood sugar spiked dangerously. That emergency room visit will cost the state substantially more than six months of Marcus's insulin would have cost.

Jennifer can resolve Marcus's case quickly. She will call the supervisor, verify the information, note the verification in the file, and restore Marcus's coverage. But she wonders how many Marcus cases are in the queue, how many people with legitimate documentation that does not fit expected templates are losing coverage while algorithms flag them for human review that takes weeks to complete.

Three cases. One obvious fraud. One ambiguous situation that might be gaming, might be legitimate, might be a system design problem. One clear non-fraud that the system treated as suspicious anyway. Jennifer's challenge is that the tools available to her do not distinguish effectively among these categories. The resources devoted to catching the document mill are the same resources that delayed Marcus's insulin. The scrutiny applied to Tanya's caregiving attestation would apply equally to a fabricated claim. The system optimizes for detecting anomalies without adequately distinguishing harmful anomalies from harmless ones.

---

## Section 1: The Gaming Landscape

Work requirements create verification systems, and verification systems create gaming opportunities. Understanding the landscape of potential fraud is necessary before evaluating whether anti-fraud measures are appropriately calibrated.

**Fabricated work hours** represent the most straightforward form of fraud. A person who is not working claims to be working, submitting false documentation to maintain coverage. This might involve forged pay stubs, fabricated employer letters, or false attestations. The motive is clear: obtain healthcare benefits without meeting work requirements. The harm is equally clear: program resources flow to people who have not satisfied the conditions attached to those resources.

**False exemption claims** involve people who do not qualify for exemptions claiming that they do. Someone without a disabling medical condition claims a medical exemption. Someone without caregiving responsibilities claims caregiving hours. Someone not enrolled in education claims student status. Like fabricated work hours, this involves intentional misrepresentation to avoid work requirements.

**Document mills** represent organized fraud rather than individual deception. Entrepreneurs recognize that some people cannot obtain legitimate verification documentation and offer to create it for a fee. These operations might produce fake pay stubs, fabricated employer letters, or fraudulent educational enrollment verification. Document mills represent a different kind of harm than individual fraud because they enable fraud at scale and corrupt the verification infrastructure itself.

**Employer collusion** occurs when employers cooperate with employees to generate false verification. A business owner might report hours that were never worked, either as a favor to employees or in exchange for compensation. This form of fraud is difficult to detect because the documentation appears legitimate and comes from a genuine business entity. It corrupts the employer verification pathway that states rely upon.

**Identity-based fraud** involves using someone else's identity to obtain benefits or using fraudulent identities to enroll multiple times. This overlaps with broader identity theft concerns but takes specific forms in work requirement contexts when verification is tied to Social Security numbers, state identification, or employer records.

**The critical context is that fraud in benefit programs is rare.** The 2024 Medicaid improper payment rate was 5.09%, but 79% of those improper payments resulted from insufficient documentation rather than ineligibility or fraud. The error rate is not a fraud rate. Most improper payments reflect paperwork failures, not intentional deception.

SNAP provides a useful comparison. The USDA estimated that about 1.6% of SNAP benefits were trafficked in the 2015-2017 period, representing the clearest form of intentional program abuse. The broader improper payment rate is higher, but as the Congressional Research Service emphasizes, the overwhelming majority of SNAP errors result from honest mistakes by recipients, eligibility workers, data entry clerks, or computer programmers rather than intentional fraud.

This does not mean fraud does not exist or does not matter. Document mills are real. Fabricated claims occur. But the prevalence of actual fraud is far lower than political rhetoric often suggests. Program integrity efforts calibrated to an imaginary epidemic of fraud will necessarily impose burdens on compliant populations that exceed any benefit from fraud prevention.

---

## Section 2: Fraud Versus Documentation Failure

The fundamental challenge in program integrity is that fraud and documentation failure produce identical administrative outcomes. A person whose work hours cannot be verified might be committing fraud by claiming hours they did not work. Or they might be working exactly as claimed but unable to prove it. The verification system sees the same thing: unverified hours, coverage termination.

**Genuine fraud** involves intentional misrepresentation of material facts to obtain benefits. The person knows they are not working, knows they do not qualify for an exemption, and deliberately provides false information to maintain coverage. The intent is to deceive. The benefit is obtained through deception.

**Documentation failure** involves true circumstances with inadequate proof. The person is actually working, actually qualifies for an exemption, or actually meets the requirements. But they cannot produce documentation that satisfies the verification system. The intent is honest. The administrative outcome is identical to fraud.

**System failure** involves compliant people defeated by broken processes. The person has the documentation, submits it correctly, and the system fails. Portal glitches lose uploads. Algorithmic screening rejects legitimate documents. Processing backlogs delay reviews beyond appeal deadlines. The person did everything right, and the system still recorded them as non-compliant.

Why do systems conflate these categories? Because distinguishing them requires investigation that costs more than automated processing. An algorithm can flag an anomaly instantly. Determining whether that anomaly represents fraud, documentation failure, or system failure requires human judgment, which requires staff time, which requires resources. Programs facing budget constraints and volume pressures naturally favor automation over investigation.

Arkansas demonstrated the consequences of this conflation. In ten months of work requirement implementation, approximately 18,000 people lost Medicaid coverage. Subsequent research found that most of these people were actually working or qualified for exemptions. They were not committing fraud. They were experiencing documentation failure in a system designed without adequate pathways for their circumstances.

The policy question is not whether fraud exists. It does. The question is whether systems designed to catch fraud are appropriately distinguishing fraud from documentation failure. If most coverage losses affect compliant people who cannot prove compliance rather than non-compliant people trying to cheat, the system is failing at its stated purpose while succeeding at a purpose no one would defend: punishing people for administrative incapacity rather than for failing to work.

---

## Section 3: Anti-Fraud Measures and Collateral Damage

Every anti-fraud measure creates burden. The question is whether the burden falls primarily on fraudsters or primarily on legitimate claimants. When prevention measures burden compliant populations more than they burden fraudsters, the cost-benefit calculation shifts dramatically.

**Universal documentation requirements** demand that everyone prove compliance, treating all members as suspected fraudsters until proven otherwise. This approach catches fraud that would otherwise slip through but imposes verification burden on 100% of the population to identify problems in a small fraction. If 98% of members are compliant and the documentation process causes 5% of compliant members to lose coverage, the collateral damage exceeds any plausible fraud prevention benefit.

**Identity verification barriers** have proliferated following concerns about identity-based fraud. These barriers require sophisticated identity documentation that some populations struggle to provide. People experiencing homelessness may lack stable identification. Immigrants may have complex documentation histories. People who have changed their names may face verification challenges. The fraud these barriers prevent is real, but the legitimate claimants they exclude are more numerous.

**Fraud scoring algorithms** assign risk scores to applications and verifications based on patterns associated with historical fraud. These algorithms are efficient but imperfect. They generate false positives, flagging legitimate claims for investigation. They may embed biases, flagging populations with documentation patterns that differ from assumed norms. They create delay even when they ultimately clear legitimate claims, and delay itself causes harm when people lose coverage during investigation periods.

**Investigation delays** compound documentation problems. When a claim is flagged for investigation, coverage may be suspended or terminated pending resolution. Investigation queues grow during implementation periods when staff resources are stretched. A legitimate claimant whose case sits in a queue for weeks experiences the same coverage loss as a fraudster, even if their claim is ultimately approved.

**Burden shifting** places the responsibility for proving legitimacy on claimants rather than the responsibility for disproving legitimacy on the program. The legal presumption in criminal proceedings is innocence until proven guilty. The operational presumption in benefit programs is often the reverse: ineligibility until proven eligible, non-compliance until proven compliant. This presumption multiplies the documentation burden on legitimate claimants while doing little to deter sophisticated fraud.

The program integrity calculation must account for what economists call the deadweight loss of prevention measures. Every hour a legitimate claimant spends gathering documentation is a cost. Every coverage day lost during investigation delays is a cost. Every medical expense incurred because coverage was suspended for administrative reasons is a cost. These costs are real even if they do not appear on program integrity balance sheets.

When prevention costs exceed fraud costs, the program is destroying value rather than protecting it. CMS reported that 79% of Medicaid improper payments in 2024 resulted from insufficient documentation. This means the vast majority of improper payment findings reflected paperwork failures rather than fraud or ineligibility. Systems optimized to reduce improper payment rates may be reducing documentation failures rather than fraud, which is worthwhile, but they may also be creating new documentation failures that harm people who would otherwise be compliant.

---

## Section 4: Strategic Audit Approaches

If universal verification imposes excessive burden on compliant populations, the alternative is strategic targeting. Rather than treating everyone as a suspected fraudster, systems can concentrate scrutiny on claims that exhibit patterns associated with actual fraud while allowing routine claims to proceed with minimal friction.

**Risk-based targeting** uses indicators to identify claims that warrant enhanced scrutiny. A single claim from someone with a stable employment history and consistent documentation pattern receives expedited processing. A claim exhibiting anomalies, such as sudden changes in employment patterns, documentation from unfamiliar sources, or inconsistencies with other data sources, triggers additional review. The key is calibrating risk indicators to actual fraud patterns rather than to proxies that correlate with documentation difficulty.

**Pattern analysis** for anomaly detection can identify fraud operations that individual claim review would miss. The document mill in Jennifer's opening case was detected because 47 claims from the same IP address is not a pattern consistent with legitimate individual submissions. Organized fraud leaves signatures that individual fraud does not. Systems designed to detect these signatures can catch fraud operations while reducing scrutiny of ordinary claims.

**Post-payment audit** offers an alternative to pre-eligibility barriers. Rather than requiring exhaustive documentation before coverage begins, systems can provide coverage based on reasonable verification and audit a sample of approved claims afterward. If audits reveal problems, correction mechanisms can recover improper payments and identify systemic issues. This approach prioritizes access over prevention while maintaining accountability through retrospective review.

**Sampling strategies** can achieve program integrity goals without burdening entire populations. If 5% of claims in a particular category exhibit problems, auditing 100% of claims in that category is inefficient. Auditing a representative sample identifies the problem rate, and targeted interventions can address root causes without imposing universal burden. The statistical literature on quality control offers well-developed methods for sampling that achieves desired confidence levels at minimal cost.

**Penalty structures** matter as much as detection methods. Penalties for intentional fraud should be severe enough to deter rational actors from attempting it. Penalties for inadvertent errors should be proportionate and recoverable. When the same penalty applies to fraud and to honest mistakes, the deterrent effect on fraud is diluted while the terrorizing effect on honest claimants is amplified. Distinguishing intentional violations from inadvertent errors in penalty structures communicates that the system cares about the difference.

The goal of strategic approaches is concentration of scrutiny. Fraud prevention resources are finite. Spreading them thinly across all claims catches less fraud than concentrating them on high-probability cases. The challenge is developing indicators that accurately identify high-probability cases without embedding biases that target populations facing documentation barriers rather than populations committing fraud.

---

## Section 5: Self-Attestation Design

Self-attestation represents the most access-friendly verification approach and the most fraud-vulnerable. The question is not whether to use self-attestation but how to design self-attestation systems that maintain integrity while reducing documentation burden.

**When self-attestation makes sense** depends on the probability of fraud, the cost of fraud when it occurs, and the cost of alternative verification methods. For circumstances where fraud is rare and documentation is difficult, self-attestation may be the efficient choice. Caregiving hours for family members, volunteer activities at informal organizations, and self-employment in cash economies all present documentation challenges that formal verification struggles to address. If the alternative to self-attestation is excluding legitimate activity from qualifying hours, self-attestation serves program goals better than rigid documentation requirements.

**Penalty of perjury** as deterrent leverages legal consequences rather than documentation requirements. When people attest under penalty of perjury that their statements are true, they face criminal liability for knowingly false statements. This creates deterrent effect without creating documentation burden. The deterrent is imperfect because prosecution is rare, but it is not zero, and it applies specifically to intentional falsehood rather than to documentation capacity.

**Elevated audit rates** for high-risk attestations can calibrate scrutiny to risk. If self-attestation is permitted for caregiving hours but caregiving hours present higher fraud risk than employer-verified employment hours, the audit rate for caregiving attestations can be set higher than for employment verification. This maintains access while increasing accountability in categories where accountability is most needed.

**Community organization intermediary verification** offers a middle path between formal documentation and pure self-attestation. A community organization that knows a person is providing caregiving, volunteering, or engaging in job search activities can attest to those activities based on direct observation or ongoing relationship. The organization's attestation carries more weight than individual self-attestation because the organization has reputational stake in accuracy. This approach works particularly well in communities with strong nonprofit infrastructure and trust relationships.

**Balancing access with integrity** requires acknowledging that no verification system is perfect. Some fraud will escape detection regardless of verification stringency. Some legitimate claimants will be excluded regardless of how accessible systems are designed. The design question is where to set the tradeoff. Systems that tolerate some fraud to maximize access serve different values than systems that tolerate some exclusion to minimize fraud. Neither choice is objectively correct. Both involve normative judgments about the relative importance of preventing fraud versus ensuring access.

Oregon provides an instructive example. The state accepts applicants' attestation of eligibility information unless highly discrepant or conflicting information is uncovered through existing state systems. Internal audits have shown no increase in eligibility determination errors when the state relies on applicant self-attestation compared to more stringent documentation requirements. The feared flood of fraud from attestation-based approaches has not materialized, while the administrative burden reduction has improved processing times and reduced coverage gaps.

---

## Section 6: The Program Integrity Calculation

Program integrity is not an end in itself. It is instrumental to program goals. The purpose of Medicaid is to provide healthcare to eligible populations. Program integrity protects this purpose by ensuring resources flow to eligible rather than ineligible people. When integrity measures undermine program purpose by excluding eligible people, they have failed even if they successfully exclude some ineligible people.

**The cost of fraud** includes direct costs from payments to ineligible people and indirect costs from public trust erosion. When people believe programs are rife with fraud, support for those programs diminishes. This political cost may exceed the direct fiscal cost of fraud itself. Maintaining public confidence in program integrity has value beyond the dollars recovered.

**The cost of anti-fraud measures** includes administrative costs of verification systems, documentation burden imposed on claimants, coverage losses among eligible people who fail verification, and health consequences when coverage disruption affects care. These costs are real and quantifiable even if they appear in different budget lines than fraud recovery.

**Calculating the right balance** requires comparing these costs explicitly rather than assuming that more fraud prevention is always better. If a verification measure costs $10 million to implement and prevents $5 million in fraud while causing $20 million in coverage losses and downstream healthcare costs, it is not a good investment regardless of its effectiveness at preventing fraud. The question is not whether the measure works but whether it creates more value than it destroys.

**Political pressures toward over-enforcement** distort this calculation. Politicians face asymmetric consequences for fraud that becomes public versus for legitimate claimants who are wrongly excluded. A news story about fraud in a benefit program generates outrage and demands for action. A news story about an eligible person who lost coverage due to paperwork requirements generates less attention. This asymmetry creates incentive to over-invest in fraud prevention and under-invest in access protection.

**Some fraud tolerance may be optimal policy.** This sounds counterintuitive, but it follows directly from cost-benefit analysis. If preventing the last 1% of fraud requires measures that impose costs exceeding the cost of that fraud, tolerating that fraud is the efficient choice. Perfect fraud prevention is not the goal. Cost-effective fraud prevention is the goal. Systems designed for zero fraud tolerance will necessarily impose excessive costs on compliant populations.

The Social Security Administration provides an instructive contrast. Social Security has near-100% take-up among eligible beneficiaries. It achieves this through administrative systems that minimize documentation burden and presume eligibility based on available data. Fraud exists in Social Security, but the program's design prioritizes access for eligible people over exclusion of ineligible people. The result is a program that achieves its purpose at scale with relatively low administrative burden and relatively high public confidence.

---

## Return to Jennifer

Jennifer finishes her review of the three cases. The document mill referral is straightforward. She documents the pattern, notes the evidence, and sends it to the fraud investigation unit. This is what program integrity resources should address.

Tanya's caregiving case requires more thought. Jennifer reviews the state's qualifying activity definitions. Caregiving for a family member is permitted, but the verification requirements were written with formal caregiving arrangements in mind. Tanya does not have a formal arrangement. She has reality: an elderly mother who needs help, a daughter who provides it, and healthcare coverage at stake.

Jennifer calls Tanya. The conversation confirms what the file suggested. Tanya's mother had a stroke two years ago. Tanya moved back home to help. She cannot work traditional employment because her mother cannot be left alone for extended periods. The caregiving is real, documented in physician records, reflected in prescription patterns, observable in the living arrangement. The only thing missing is paperwork from a program her mother is not enrolled in.

Jennifer approves Tanya's case with a note recommending that the state develop alternative verification pathways for informal caregiving. The current system assumes formal arrangements that many genuine caregivers lack. This is a system design problem, not a fraud problem.

Marcus's case is the simplest and the saddest. Jennifer calls the landscaping supervisor, who enthusiastically confirms Marcus's employment. She notes the verification, restores Marcus's coverage, and flags the case for expedited processing of any future documentation from small employers lacking letterhead. But she cannot undo the 23 days Marcus went without insulin, the emergency room visit that could have been prevented, or the fear he experienced wondering whether he would lose the healthcare that keeps his diabetes managed.

Three cases. One genuine fraud operation requiring investigation and prosecution. One policy gap requiring system redesign to accommodate legitimate circumstances the system was not built for. One false positive requiring human review that arrived too late to prevent harm.

Jennifer thinks about the resources devoted to the fraud detection system that flagged all three cases identically. She thinks about the investigation capacity consumed by false positives. She thinks about the eligible people losing coverage while their cases sit in queues designed to catch fraudsters. She wonders whether the system is protecting program integrity or whether it has become a program integrity problem itself.

The answer, she suspects, depends on what you count. If you count fraud prevented, the system is working. If you count eligible people harmed, the calculation looks different. Program integrity, she realizes, is not just about preventing people from getting benefits they should not receive. It is also about ensuring people receive benefits they should get. A system that succeeds at the first while failing at the second has not achieved integrity. It has merely shifted who bears the cost of imperfection.

---

## Conclusion: Integrity Means Getting It Right

The fraud problem in work requirement systems is real but limited. Document mills exist. False claims occur. Organized schemes emerge wherever verification systems create opportunities. These problems warrant attention, investigation, and appropriate penalties.

The anti-fraud problem may be larger. Systems designed to catch fraud that treat all members as suspects, that impose universal documentation burden to identify problems in a small fraction, that cannot distinguish fraud from documentation failure, and that delay coverage for legitimate claimants while investigations proceed are systems that harm more people than they protect.

Program integrity means getting it right. Getting it right means paying benefits to eligible people and not paying benefits to ineligible people. These are two dimensions of the same goal. Systems optimized only for the second dimension, systems that measure success by fraud prevented without measuring failure by eligible people excluded, are not integrity systems. They are exclusion systems with integrity branding.

Work requirement implementation offers an opportunity to design program integrity systems that actually serve program integrity. Risk-based targeting rather than universal scrutiny. Self-attestation with strategic audit rather than universal documentation. Post-enrollment verification rather than pre-eligibility barriers. Penalty structures that distinguish fraud from error. Investigation resources concentrated where fraud actually occurs.

The alternative is repeating Arkansas. Implementing systems that lose coverage for working people because they cannot prove they are working. Measuring compliance rates that reflect documentation capacity rather than work activity. Claiming program integrity while excluding eligible populations. Counting fraud prevention while ignoring access failure.

Jennifer knows which approach serves the people the program is meant to serve. The question is whether the people designing systems will count what she counts.

---

## References

1. Centers for Medicare & Medicaid Services. "Fiscal Year 2024 Improper Payments Fact Sheet." CMS.gov. 2024.

2. Government Accountability Office. "Medicare and Medicaid: Additional Actions Needed to Enhance Program Integrity and Save Billions." GAO-24-107487. April 2024.

3. Kaiser Family Foundation. "5 Key Facts about Medicaid Program Integrity." KFF. August 2025.

4. Center on Budget and Policy Priorities. "Understanding the Medicaid Payment Error Rate Measure." CBPP. February 2025.

5. Georgetown University Center for Children and Families. "Medicaid Fraud: The Improper Use of Improper Payments." CCF. March 2025.

6. Congressional Research Service. "Supplemental Nutrition Assistance Program: Errors and Fraud." IF10860. 2025.

7. Government Accountability Office. "Improper Payments: USDA's Oversight of the Supplemental Nutrition Assistance Program." GAO-24-107461. 2024.

8. Center on Budget and Policy Priorities. "SNAP Includes Extensive Payment Accuracy System." CBPP. June 2024.

9. CLASP. "SNAP Program Integrity: How Racialized Fraud Provisions Criminalize Hunger." 2022.

10. Herd P, Moynihan DP. Administrative Burden: Policymaking by Other Means. Russell Sage Foundation. 2018.

11. Sommers BD, Goldman AL, Blendon RJ, Orav EJ, Epstein AM. "Medicaid work requirements: Results from the first year in Arkansas." New England Journal of Medicine. 2019;381(11):1073-1082.

12. Center on Budget and Policy Priorities. "How to Streamline Verification of Eligibility for Medicaid and SNAP." CBPP. July 2024.

13. CMS Medicaid and CHIP Learning Collaboratives. "Simplified, Real-Time Verification Issue Brief." Medicaid.gov.

14. Pennsylvania Department of Labor & Industry. "Self-Attestation Policy." January 2025.

15. USDA Food and Nutrition Service. "USDA Efforts to Reduce Waste, Fraud and Abuse in the Supplemental Nutrition Assistance Program." FNS.USDA.gov.

16. Hall K. "Reducing Waste and Fraud in SNAP." Mercatus Center, George Mason University. May 2025.

17. HHS Office of Inspector General. "Medicaid Fraud Control Units Annual Report: Fiscal Year 2024." OIG.HHS.gov. June 2025.

18. CMS. "Financial Eligibility Verification Requirements." November 2024.

19. Christensen J, AarÃ¸e L, Baekgaard M, Herd P, Moynihan DP. "Human capital and administrative burden: The role of cognitive resources in citizen-state interactions." Public Administration Review. 2020;80(1):127-136.

20. Herd P, Moynihan DP. "Administrative burdens in the social safety net." Journal of Economic Perspectives. 2025;39(1):129-150.

---

*Syam Adusumilli is Chief Evangelist at GroundGame.Health, a social determinants of health platform. This article is part of a comprehensive series examining Medicaid work requirements under the One Big Beautiful Bill Act.*

# Recognizing Exemptions
## When Documentation Barriers Are the Disability

*Series 19: Compliance Systems vs. Recognition Systems*
*Article 19C*

Marcus has schizophrenia. During stable periods, which might last months or years with proper medication, he works part-time stocking shelves at a hardware store three days a week. He manages his paperwork. He opens his mail. He logs into portals when required. He remembers deadlines. On medication, Marcus functions well enough that a casual observer would never know he carries a serious mental illness diagnosis.

During psychotic episodes, Marcus becomes a different person. Not a lesser person. A person whose relationship to administrative reality has been severed. He stops opening mail because the envelopes might contain messages meant for someone else. He stops answering his phone because the voices make it difficult to distinguish callers from hallucinations. He stops going to work because leaving his apartment feels dangerous in ways he cannot articulate to someone who has never experienced paranoia. He stops taking his medication because the medication is part of the conspiracy, or because he feels fine and does not understand why he ever thought he needed it.

Marcus's schizophrenia qualifies him for exemption from work requirements. His condition is well-documented in his medical records. His psychiatrist would readily attest that during episodes, Marcus cannot sustain 80 hours of monthly work activity. The exemption exists. The pathway to the exemption exists. The provider willing to document the exemption exists.

But during an episode, Marcus cannot request the exemption. He cannot open the letter telling him his work verification is due. He cannot call the Medicaid office to explain his situation. He cannot log into the portal to submit an exemption request. He cannot visit his psychiatrist to obtain documentation because he does not believe he needs a psychiatrist. The very condition that qualifies Marcus for exemption is the condition that prevents him from claiming it.

A compliance system terminates Marcus during every episode. A recognition system flags his diagnosis in claims data and maintains his coverage automatically. The difference between these two outcomes is not compassion. It is design.

## The Documentation Paradox

The exemption documentation paradox is not limited to schizophrenia. It runs through virtually every condition that qualifies someone for exemption from work requirements. The conditions that make work impossible or impractical are, with striking consistency, the same conditions that make documenting one's inability to work impossible or impractical.

Serious mental illness impairs the executive function required to navigate bureaucratic processes. Depression diminishes the motivation and energy to initiate multi-step administrative tasks. Bipolar disorder creates oscillating periods of function and dysfunction that do not align with verification deadlines. Anxiety disorders make phone calls to government agencies, interactions with unfamiliar systems, and uncertainty about outcomes physiologically unbearable. Post-traumatic stress disorder makes encounters with authority figures and institutional systems triggers for re-traumatization. Each of these conditions qualifies someone for medical exemption. Each of these conditions makes the process of obtaining that exemption feel or be impossible.

Substance use disorder creates a related paradox. Active addiction consumes cognitive resources, disrupts routine, and deprioritizes administrative tasks. Someone in the depths of opioid dependence is not opening mail from the Medicaid office. Treatment engagement, which many states accept as a qualifying activity, requires documentation that individuals in early recovery may lack the stability to assemble. The person who most needs the treatment exemption is the person least equipped to request it. And the confidentiality protections under 42 CFR Part 2 that govern substance use treatment records add another layer of complexity, as programs may be reluctant to share information without explicit patient consent that an actively using individual may not be capable of providing.

Caregiving responsibilities consume the time and attention that documentation requires. A parent caring for a child with severe disabilities is spending every available hour managing medications, attending appointments, handling behavioral crises, and navigating school systems. Adding Medicaid work requirement exemption documentation to that load is not just burdensome. It is competitive. Every hour spent gathering exemption paperwork is an hour not spent providing the care that qualifies the parent for exemption. The parent of a child on a ventilator who must be suctioned every two hours does not have time to sit on hold with the Medicaid office.

Homelessness eliminates the physical infrastructure that documentation assumes. Exemption applications require a mailing address for correspondence, a phone number for follow-up, and access to documents that may have been lost in the chaos of housing instability. A person sleeping in their car does not have a filing cabinet with their medical records. A person moving between shelters does not receive mail reliably. The documentation requirements presume a stability that homelessness, by definition, does not provide.

The logical trap is elegant and cruel. You must prove you cannot do something. But the thing you cannot do includes proving things. The documentation paradox is not an edge case. It is the central design challenge of exemption systems. Any system that relies primarily on individual self-documentation for exemptions will systematically fail the populations most in need of exemptions.

## Administrative Data for Automatic Exemption

The most effective resolution to the documentation paradox is to remove the documentation burden from the individual entirely. Administrative data systems already contain the information needed to identify most exemption-qualifying conditions. The question is whether states will build systems that use that data proactively or systems that require individuals to replicate information the state already possesses.

Claims data represents the richest source of exemption signals. A person with three or more psychiatric hospitalizations in the past twelve months almost certainly qualifies for a serious mental illness exemption. A person filling prescriptions for six or more chronic disease medications is managing a clinical burden that likely qualifies for medical frailty. A person with cancer treatment claims, chemotherapy administration codes, radiation therapy, immunotherapy infusions, is undergoing active treatment that exempts them from work requirements. Each of these signals exists in claims databases that state Medicaid agencies and MCOs already maintain.

The analytical approach involves defining clinical algorithms that identify exemption-likely conditions from claims patterns. These algorithms are not complex. Three or more inpatient psychiatric admissions in twelve months: flag for SMI exemption. Active chemotherapy claims: flag for cancer treatment exemption. Dialysis treatment claims: flag for organ failure exemption. Opioid treatment program claims: flag for SUD treatment exemption. Pregnancy diagnosis codes: flag for pregnancy exemption. Home health service utilization: flag for medical frailty review. The clinical signals are clear. The data exists. The algorithms are straightforward.

Disability program linkages provide another avenue for automatic exemption identification. Anyone receiving Supplemental Security Income has already undergone a rigorous federal disability determination finding them unable to engage in substantial gainful activity. Requiring a separate work requirement exemption application from someone who has already been determined disabled by the Social Security Administration is redundant at best and harmful at worst. Data sharing agreements between state Medicaid agencies and the Social Security Administration can automate this exemption without any individual action. SSI recipients are automatically exempt. SSDI recipients are automatically exempt. The data exchange already exists for Medicaid eligibility determination. Extending it to work requirement exemption requires only policy direction, not new infrastructure.

Hospitalization and crisis service records provide time-limited exemption triggers. Any inpatient admission should generate an automatic 30-day exemption following discharge, with longer automatic periods for psychiatric hospitalization (90 days) and surgical recovery (duration based on procedure type). Emergency department visits for mental health crises, substance use emergencies, or trauma should trigger automatic short-term exemptions. These events are already documented in claims data and reported to state systems in near real-time. Using them as exemption triggers requires adding a decision rule to existing data flows, not building new systems.

Pharmacy data provides an additional identification channel. Prescription patterns for antipsychotics, mood stabilizers, chemotherapy agents, immunosuppressants, and other medication classes serve as proxies for conditions that likely qualify for exemption. A person filling clozapine, the antipsychotic typically reserved for treatment-resistant schizophrenia, almost certainly has a condition qualifying for exemption. Pharmacy data arrives in state systems faster than diagnostic claims and provides a signal even when the person has not been seen for a clinical encounter recently.

The principle underlying all of these approaches is "recognize before they have to ask." The system identifies people who likely qualify for exemptions and either grants the exemption automatically or initiates proactive outreach to confirm eligibility. The individual does not need to know that an exemption exists, understand how to apply for it, or navigate a documentation process they may be incapable of completing. The system does the work.

## Provider Attestation Models

For conditions that administrative data cannot definitively identify, provider attestation shifts the documentation burden from patient to provider. Rather than requiring a person with debilitating chronic pain to assemble medical records, complete forms, and submit documentation to the state, the person's physician attests that the patient cannot consistently meet 80-hour monthly work requirements.

The simplest attestation model asks providers to confirm a single statement: "Due to medical conditions, this patient cannot consistently meet 80-hour monthly work requirements." No detailed diagnosis disclosure. No extensive functional assessment forms. No quantification of exactly how disabled someone is. A single checkbox and a signature from a licensed provider who knows the patient's clinical situation. This simplicity is not a shortcut. It is a design choice that respects clinical judgment while minimizing the administrative burden that reduces provider participation.

More complex attestation models produce worse outcomes. Lengthy functional assessment forms take 20 to 30 minutes to complete, far more time than most Medicaid visits allow. Providers who face lengthy paperwork are less likely to complete it, not because they do not care about their patients but because they are seeing 25 patients a day and cannot add 30-minute documentation tasks to each encounter. The more complex the form, the fewer providers will complete it, the fewer patients will receive exemptions, and the more people will lose coverage despite qualifying.

Electronic health record integration transforms attestation from an additional task to a workflow component. A primary care provider treating someone with severe rheumatoid arthritis clicks a template during a routine visit, answers three questions about the patient's functional capacity, and generates an exemption attestation that transmits directly to the state through existing data exchange infrastructure. What would otherwise require a separate appointment, a lengthy form, and manual submission becomes a five-minute addition to an existing clinical encounter.

Provider liability concerns require explicit attention. Providers who attest to exemption eligibility need assurance that good-faith attestation will not expose them to fraud liability if a patient's condition later improves. Safe harbor provisions that protect providers from liability for attestations made in reasonable clinical judgment, subject only to the expectation that attestations reflect actual clinical assessment, encourage participation. Without safe harbors, risk-averse providers will refuse to attest, and patients will be unable to obtain documentation they need.

Federally Qualified Health Centers occupy a uniquely valuable position in the attestation infrastructure. FQHCs serve the populations most likely to need exemptions. They already maintain comprehensive medical records for their patient populations. They have established relationships of trust with patients who might not engage with other providers. And their mission orientation makes them more likely to invest in exemption documentation than private practices focused on throughput. FQHCs can serve as attestation hubs for their communities, providing not just their own patients but community members who lack a regular provider with a pathway to medical exemption documentation.

Incentive alignment matters. Asking providers to complete attestation paperwork without compensation is asking them to perform unpaid labor. States that pay for attestation, even modest flat fees of $25 to $50 per attestation, dramatically increase provider participation. The math is simple: paying $35 for an attestation that prevents a $400 to $600 administrative re-enrollment cost is an investment that returns ten to fifteen times its value. States that treat provider attestation as free labor will get what they pay for.

## Trusted Intermediary Pathways

Not every exemption-qualifying circumstance can be identified through administrative data or provider attestation. Some conditions are documented only through the relationships people have with community organizations that serve them. Homeless service providers know who is experiencing homelessness. Domestic violence shelters know who is fleeing abuse. Mental health organizations know who is engaged in treatment. Recovery houses know who is in early sobriety.

These organizations can function as trusted intermediaries, entities credentialed by the state to provide exemption documentation on behalf of the individuals they serve. A homeless shelter director attesting that a person is experiencing homelessness may be more reliable and more accessible than requiring the homeless person to obtain documentation from a medical provider, a housing authority, and a state agency to prove what the shelter director already knows.

Building trusted intermediary networks requires credentialing processes that are rigorous enough to prevent fraud but accessible enough to include the organizations that actually serve vulnerable populations. Faith-based organizations, mutual aid networks, and informal community groups that serve the hardest-to-reach populations may lack the formal credentials that a state would typically require but may possess exactly the relationships and knowledge that make accurate exemption identification possible. States must balance accountability requirements against the reality that overly restrictive credentialing excludes the intermediaries most needed.

Domestic violence shelters require special consideration because the populations they serve face safety risks from documentation. A person fleeing an abusive partner may need a work requirement exemption but cannot provide documentation that might reveal their location. Confidential verification pathways that allow shelter staff to attest to a person's circumstances without disclosing identifying information that could compromise safety are not optional accommodations. They are necessities for a population that faces lethal risk from administrative processes that assume disclosure is harmless.

The trusted intermediary model works because it leverages existing relationships rather than creating new ones. A person experiencing homelessness who will not call the Medicaid office may already be in daily contact with a shelter case manager. A person with serious mental illness who cannot navigate a state portal may attend a clubhouse or psychosocial rehabilitation program three times a week. A person in early recovery who cannot assemble documentation may have a sponsor or recovery coach who sees them daily. These relationships provide access points that state systems cannot replicate.

## Exemption Continuity

The final design challenge in exemption systems is temporal. Chronic conditions do not resolve on administrative timelines. Schizophrenia does not go into remission every six months in time for exemption renewal. Progressive neurological diseases do not improve between annual redeterminations. Caregiving responsibilities for children with severe disabilities do not end when a renewal form arrives.

Yet most proposed exemption systems require periodic re-documentation, typically every six or twelve months. Each renewal cycle reintroduces the documentation paradox. A person who could not request an exemption initially does not develop the capacity to renew it simply because time has passed. The administrative burden that prevents initial documentation prevents renewal documentation with equal effectiveness.

Automatic renewal for stable exemptions resolves this problem for conditions that are chronic, progressive, or permanent. Someone receiving SSI for a permanent disability should not need to re-document their disability every six months for work requirement purposes. Someone in hospice care should not need to prove they are still dying. Someone caring for a child with severe autism should not need to re-prove the child's condition at each renewal cycle. Automatic renewal based on the persistence of the underlying condition, confirmed through ongoing claims data or disability program status, eliminates renewal burden for conditions that are not going to change.

Trigger-based review rather than calendar-based review provides a more appropriate framework for episodic conditions. Rather than reviewing Marcus's exemption on a fixed schedule, the system monitors his claims data for signals of stabilization, regular psychiatric visits suggesting medication compliance, absence of hospitalizations, evidence of part-time employment. When triggers suggest improvement, the system initiates a gentle reassessment through provider communication rather than a bureaucratic renewal demand. This approach respects the episodic nature of conditions like bipolar disorder, multiple sclerosis, and Crohn's disease while ensuring that exemptions remain appropriate.

## The Alternative

The person who most needs an exemption is often the person least able to request one. This is not an unfortunate coincidence. It is a structural feature of the conditions that qualify people for exemption. The conditions impair precisely the capacities that documentation demands.

Recognition-oriented exemption systems resolve this structural problem by using data, providers, and intermediaries to identify exemptions without requiring impossible self-advocacy. They identify people who qualify before those people miss deadlines. They shift documentation burden from individuals who cannot carry it to systems, providers, and organizations that can. They design for the reality of the conditions they are meant to accommodate rather than for an idealized beneficiary who happens to be too sick to work but not too sick to fill out forms.

The alternative is what compliance systems produce. Terminating people for being too disabled to prove they are disabled. Canceling coverage for people too mentally ill to request an exemption from a requirement they cannot meet because of their mental illness. Stripping healthcare from caregivers too busy providing care to document that they are providing care.

That alternative is not program integrity. It is system failure by design.

## References

1. Sommers BD, Goldman AL, Blendon RJ, Orav EJ, Epstein AM. "Medicaid Work Requirements: Results from the First Year in Arkansas." *New England Journal of Medicine*. 2019;381(11):1073-1082.

2. Herd P, Moynihan DP. *Administrative Burden: Policymaking by Other Means*. New York: Russell Sage Foundation. 2018.

3. Substance Abuse and Mental Health Services Administration. "Applying the Substance Abuse Confidentiality Regulations to Health Information Exchange." 2010.

4. National Alliance on Mental Illness. "Anosognosia: Understanding Lack of Awareness in Serious Mental Illness." 2024.

5. Garfield R, Rudowitz R, Damico A. "Understanding the Intersection of Medicaid and Work." Kaiser Family Foundation. February 2025.

6. U.S. Department of Housing and Urban Development. "Homeless Documentation Standards and Verification Requirements." 2024.

7. National Health Care for the Homeless Council. "Documentation Challenges for Homeless Populations in Safety Net Programs." 2023.

8. Ohio Department of Medicaid. Group VIII 1115 Demonstration Waiver Application. February 2025.

9. National Association of Community Health Centers. "FQHC Role in Social Determinants Documentation and Referral." 2024.

10. Baicker K, Allen HL, Wright BJ, Taubman SL, Finkelstein AN. "The Effect of Medicaid on Management of Depression: Evidence from the Oregon Health Insurance Experiment." *Milbank Quarterly*. 2018;96(1):29-56.

11. Moynihan D, Herd P, Harvey H. "Administrative Burden: Learning, Psychological, and Compliance Costs in Citizen-State Interactions." *Journal of Public Administration Research and Theory*. 2015;25(1):43-69.

12. National Council for Mental Wellbeing. "Provider Documentation Burden in Behavioral Health Settings." 2024.

*Syam Adusumilli is Chief Evangelist and Leader of Strategic Partnerships at GroundGame.Health, a social determinants of health platform. This article is part of a comprehensive analytical series examining Medicaid work requirements under the One Big Beautiful Bill Act.*

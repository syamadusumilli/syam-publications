---
title: "The Approximate Mind, Part 4: How Close Can We Actually Get?"
date: 2025-01-16
draft: false
weight: 4
description: "Not in theory. Not in philosophy papers. Right now, with current approaches, what can we actually model about human behavior?"
slug: "how-close-can-we-get"
tags: ["modeling", "prediction", "AI capabilities", "behavioral science"]
series: ["The Approximate Mind"]
series_order: 4
authors:
  - "Syam Adusumilli"
  - "Yagn Adusumilli"
showAuthor: true
showDate: true
showReadingTime: true
showTableOfContents: true
---

After three articles exploring how AI approaches understanding, through confidence calibration, context-aware reasoning, and the limits imposed by human irrationality, there's an obvious question: How close can cutting-edge AI actually get?

Not in theory. Not in philosophy papers. Not in what might be possible someday. But right now, with current approaches, what can we actually model about human behavior?

The answer is more nuanced than either the optimists or pessimists suggest.

## What We Can Model Well (>80% Accuracy)

**Explicit preference learning.** When people tell us what they want, we can learn it. "I prefer morning appointments." "Don't call me about routine matters." "I want my daughter involved in major decisions." Stated preferences, tracked consistently, can be learned with high reliability.

**Pattern recognition in structured domains.** Medication timing, appointment preferences, communication channel choices, behaviors with clear patterns in structured contexts can be modeled accurately. When Margaret always responds faster to text than email, that pattern is learnable.

**Basic sentiment detection.** Whether someone is frustrated, satisfied, confused, or engaged comes through in language patterns, response times, engagement metrics. Not perfect, but better than chance by a significant margin.

**Routine prediction.** Daily patterns, weekly rhythms, seasonal variations. Humans are creatures of habit, and habits are predictable.

## What We're Getting Better At (60-80% Accuracy)

**Implicit preference inference.** Reading between the lines. Margaret says she's fine with video calls, but her engagement drops and response times lengthen. The stated preference doesn't match the revealed preference. Learning to detect these gaps is improving but imperfect.

**Contextual adaptation.** Knowing that Margaret-in-the-morning differs from Margaret-in-the-evening. That Margaret-with-family differs from Margaret-alone. Context-switching is real, and AI is learning to recognize it.

**Anticipating needs from history.** If Margaret always struggles with medication adherence after stressful family events, the system can learn to offer extra support during similar future situations. Pattern-based anticipation is getting better.

**Multi-factor prediction.** Combining medical history, behavioral patterns, environmental context, and social factors to predict outcomes. More factors mean more complexity, but also potentially more accuracy when integrated well.

## What Remains Difficult (<40% Accuracy)

**Understanding unstated context.** The things Margaret assumes you know but has never said. Cultural background, family dynamics, personal history that shapes current behavior. We can infer some of this, but much remains opaque.

**Handling genuine novelty.** When Margaret faces a situation unlike anything in her history, prediction becomes guesswork. Novel situations, new diagnoses, life transitions, unprecedented events, break pattern-based models.

**Long-term consistency.** Preferences change. Values evolve. The Margaret of today might be quite different from the Margaret of five years ago. Tracking genuine change versus noise is hard.

**Multi-layered social reasoning.** Margaret wants her daughter involved, but doesn't want to burden her. She values independence, but fears isolation. She trusts her doctor, but resents being told what to do. These layered, contradictory social dynamics resist simple modeling.

**Meaning and significance.** Why does Tuesday matter to Margaret? What makes this particular request feel different from routine ones? The significance layer, what things mean to people, remains largely inaccessible.

## The Honest Assessment

If I had to give honest accuracy estimates for AI approximating human understanding:

**Surface behaviors:** 85-95% accuracy for explicit, stated, routine preferences in structured domains.

**Implicit patterns:** 65-80% accuracy for inferring unstated preferences from behavioral signals.

**Contextual adaptation:** 55-70% accuracy for knowing which context applies and adjusting accordingly.

**Anticipatory reasoning:** 45-65% accuracy for predicting needs before they're expressed.

**Deep understanding:** 20-40% accuracy for grasping meaning, significance, and the layered social dynamics of human life.

These numbers are rough estimates, not rigorous benchmarks. But they help frame realistic expectations.

## What This Means for Design

Given these limitations, how should we build AI systems that approximate human understanding?

**Be transparent about confidence.** Systems should communicate their uncertainty honestly. "I'm fairly confident you prefer morning appointments" differs from "I'm guessing you might want family involved."

**Default to human judgment for low-confidence situations.** When AI accuracy drops below acceptable thresholds, defer to humans. Don't pretend to understand what you don't.

**Design for graceful degradation.** When approximation fails, the system should fail gently, asking for clarification rather than acting on bad guesses.

**Build in feedback loops.** Continuous learning requires continuous feedback. Systems should actively seek correction when they're wrong.

**Respect the 20-40% that resists approximation.** Some aspects of human understanding will likely never be approximated computationally. Design systems that acknowledge these limits rather than pretending they don't exist.

## The Frontier

What's on the horizon? Where might the next improvements come?

**Longer context windows** allow more history to inform predictions. Andy Clark's "extended mind" thesis suggests cognition already extends into our tools. AI with longer memory might be the next step in that evolution.

**Multi-modal learning** integrates text, voice, behavior, and eventually physiological signals. More channels mean richer understanding.

**Better transfer learning** applies insights from one domain to another. What we learn about Margaret's medication preferences might inform predictions about her exercise habits.

**Improved uncertainty quantification** makes AI more honest about what it doesn't know. Calibrated confidence isn't just technically useful, it's ethically necessary.

## Conclusion

We're in the interesting middle: past obvious incompetence, not yet at obvious competence. Careful assessment matters more than blanket optimism or pessimism.

The 70-80% of human behavior that's pattern-based and context-dependent is increasingly within reach. The remaining 20-30%, contradictions, transformations, meanings, will likely remain irreducibly human.

Honest assessment of these limits matters more than either hype or despair. We can build genuinely useful AI while acknowledging genuine limits.

---

*This is the fourth in a series exploring how AI approaches understanding. Previous articles examined functional capabilities, context-dependent confidence, and human irrationality. This one provides specific accuracy estimates and explains why certain things remain out of reach.*

---

## References

**Extended Cognition:**
- Clark, A. (2008). *Supersizing the Mind*. Oxford University Press.
- Clark, A. & Chalmers, D. (1998). "The Extended Mind." *Analysis*, 58(1), 7-19.

**Machine Learning Limitations:**
- Marcus, G. & Davis, E. (2019). *Rebooting AI*. Pantheon.
- Pearl, J. & Mackenzie, D. (2018). *The Book of Why*. Basic Books.

**Uncertainty Quantification:**
- Gal, Y. (2016). "Uncertainty in Deep Learning." PhD thesis, University of Cambridge.

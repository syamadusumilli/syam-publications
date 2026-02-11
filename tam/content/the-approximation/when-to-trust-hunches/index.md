---
title: "The Approximate Mind, Part 2: When to Trust Hunches"
date: 2025-01-09
draft: false
weight: 2
description: "The computational framework captures rationality after the fact. But the phenomenology is different. It feels like spontaneity. Freedom. Like you could have chosen differently for no particular reason."
slug: "when-to-trust-hunches"
tags: ["intuition", "decision-making", "human agency", "phenomenology"]
series: ["The Approximate Mind"]
series_order: 2
authors:
  - "Syam Adusumilli"
  - "Yagn Adusumilli"
showAuthor: true
showDate: true
showReadingTime: true
showTableOfContents: true
---

You're at the grocery store. You've made chicken three times this week. You could make it again, 95% confidence it'll turn out well.

But you reach for fish instead. Never cooked this type before. Maybe 40% confident. The recipe looks complicated.

In Part 1, I might explain this as an explore-exploit algorithm: information value of trying something new outweighs low confidence given low stakes.

But is that really what's happening? Or are you simply... choosing?

Not calculating expected information gain. Not running Bayesian updates. Just deciding, in that moment, to do something different.

Maybe the computational framework captures the rationality after the fact. But the phenomenology, what it feels like from inside, is different. It feels like spontaneity. Freedom. Like you could have chosen differently for no particular reason.

Philosophers from Kant to the existentialists argued there's something about human agency that's irreducible to prior causes, including computational ones. This creates a tension. Part 1 argued AI approaches understanding through confidence calibration. But if human decision-making has this irreducible quality, then any AI model will necessarily be incomplete.

And that's okay. The goal isn't perfect prediction. It's useful approximation.

## Three Modes of Decision-Making

Let me distinguish three ways we actually make decisions:

**The Routine Life (High Confidence, Low Stakes).** Most of your day runs on autopilot. You don't reconsider which route to take to work, which coffee to order, how to greet colleagues. These are settled. Confidence is high. Stakes are low. You don't want to reinvent breakfast every morning or question whether your usual route still exists. High-confidence routines free up cognitive resources for things that actually need attention.

But if this were your entire life, you'd be stuck. You'd never discover the better coffee shop two blocks over, the colleague who could become a friend, the shortcut that saves ten minutes.

**The Experimental Life (Low Confidence, Low Stakes).** This is where you try things. New restaurants. Different conversation approaches. Alternative solutions to recurring problems. You have low confidence they'll work, maybe 30%, maybe 50%, but the stakes are low enough that failure is acceptable.

These are hypotheses you're testing on yourself. Each one is a small bet: low confidence, but low cost and high information value. Even failures teach you something.

**The Hunch Life (Intuition Without Evidence).** This is where things get genuinely strange. You can't explain why, but you just feel like you should call your friend today. This person is trustworthy (or isn't). You should take the job offer (or shouldn't). Something is wrong (or right).

Your confidence score, if you tried to calculate one, might be 25%. You have no evidence. It's just a feeling.

I could explain this as subthreshold pattern recognition, your unconscious mind detecting signals your conscious mind hasn't processed. And sometimes that's probably true. The clinician who "just knows" something is wrong is likely detecting subtle cues from thousands of prior cases.

But sometimes hunches are just... wrong. They're biases, prejudices, noise mistaken for signal. And we can't always tell the difference in advance.

## When Hunches Are Epistemically Justified

Not all hunches are created equal. Some intuitions deserve trust more than others. The question is: which ones, and how do we tell?

**Domain-specific expertise backing them.** The clinician's hunch after 20 years of emergency medicine is different from a medical student's hunch. Expertise creates pattern libraries that enable reliable intuition. As Hubert Dreyfus argued in his work on expertise, skilled practitioners develop intuitions that outperform explicit reasoning.

**Track record of accuracy.** Your hunches about your close friend's emotional state are probably more reliable than your hunches about strangers. You've been calibrated through hundreds of interactions.

**Low stakes or reversibility.** Even unreliable hunches deserve some trust when costs of being wrong are low. Try the restaurant. Start the conversation. Experiment.

**Asymmetric payoffs.** When downside is limited but upside could be large, act on hunches. The potential gain justifies the uncertainty.

**Fast-changing situations.** When you don't have time to gather evidence, intuition might be all you have. Emergency medicine, combat, financial crises, sometimes you must act on insufficient information.

## Context-Dependent Thresholds

The same confidence level justifies different actions in different contexts. Here's the crucial insight Part 1 missed:

Action justification is a function of confidence, stakes, reversibility, information gain, time pressure, and opportunity cost.

Consider 40% confidence in four scenarios:

**Try new restaurant (40% confidence it's good).** Act. Stakes are low (one mediocre meal). Reversible (leave if it's terrible). High information value (learn something either way). Time pressure is minimal. Opportunity cost is low.

**Major surgery (40% confidence it's necessary).** Don't act. Stakes are high (permanent changes to body). Irreversible. But maybe act anyway if condition is deteriorating and alternatives exhausted. Context changes everything.

**Call worried friend (40% confidence something's wrong).** Act. Asymmetric payoff: if nothing's wrong, brief awkward conversation. If something is wrong, you might help. Downside capped, upside potentially significant.

**Emergency intervention (40% confidence patient is deteriorating).** Act, even though confidence is low. Time pressure overrides uncertainty. Cost of delay exceeds cost of being wrong. This is what makes emergency medicine so cognitively demanding.

## What AI Systems Should Do Differently

This has practical implications for building AI that supports human decision-making:

**Implement context-dependent thresholds.** Not fixed confidence cutoffs, but dynamic thresholds that adjust based on stakes, reversibility, time pressure, and individual risk tolerance.

**Recognize when urgency overrides uncertainty.** Sometimes "act now with 40% confidence" is wiser than "wait for 80% confidence."

**Adjust recommendations based on individual agency.** Some people want AI to be directive. Others want it to present information and let them decide. The Human Agency Scale should calibrate how much influence the system exerts.

**Support exploration, not just optimization.** AI that only recommends high-confidence options prevents discovery. Sometimes the right recommendation is: "This is uncertain, but the stakes are low, want to try it?"

## The Wisdom of Not Knowing

The deepest insight here: epistemic humility sometimes means acting despite uncertainty.

Perfect confidence is impossible. Waiting for it is paralysis. The question isn't "how confident should I be before acting?" but "given my uncertainty, what's the wisest action?"

Sometimes wisdom means acting on a hunch. Sometimes it means gathering more information. Sometimes it means acknowledging you'll never know enough and choosing anyway.

AI that supports human flourishing needs to understand this. Not just calibrating confidence, but helping people navigate the space between knowing and acting, the space where human life actually happens.

---

*This is the second in a series exploring how AI approaches understanding. Part 1 examined functional understanding through confidence calibration. This one examines when to act despite uncertainty, and why context determines when confidence is enough.*

---

## References

**Philosophy of Action:**
- Kant, I. (1785/1998). *Groundwork of the Metaphysics of Morals*. Cambridge University Press.
- Sartre, J.-P. (1943/1956). *Being and Nothingness*. Washington Square Press.

**Expertise and Intuition:**
- Dreyfus, H. L. (2001). *On the Internet*. Routledge.
- Gigerenzer, G. (2007). *Gut Feelings: The Intelligence of the Unconscious*. Viking.
- Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press.

**Decision-Making Under Uncertainty:**
- Kahneman, D. & Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263-291.
- March, J. G. (1991). "Exploration and Exploitation in Organizational Learning." *Organization Science*, 2(1), 71-87.

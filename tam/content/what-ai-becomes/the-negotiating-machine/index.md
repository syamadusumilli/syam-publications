---
title: "The Approximate Mind, Part 16: The Negotiating Machine"
date: 2025-02-27
draft: false
weight: 16
description: "Two AI agents, facing each other across a negotiation. No humans in the room. What does that mean?"
slug: "the-negotiating-machine"
tags: ["negotiation", "AI agents", "autonomy", "trust"]
series: ["The Approximate Mind"]
series_order: 16
authors:
  - "Syam Adusumilli"
  - "Yagn Adusumilli"
showAuthor: true
showDate: true
showReadingTime: true
showTableOfContents: true
---

You're buying a car. Not you personally, your AI agent is buying a car on your behalf. It knows your budget, your preferences, your constraints. It's been authorized to negotiate, to commit, to close the deal.

On the other side: the dealership's AI agent. It knows the inventory, the margins, the sales targets. It's been authorized to negotiate, to offer, to accept.

Two AI agents, facing each other across a negotiation. No humans in the room.

How does this work? What does it even mean for AI agents to negotiate? And what happens to negotiation itself when both sides are machines?

## What Negotiation Actually Is

Human negotiation is a peculiar activity. On the surface, it's about finding terms both parties can accept. But underneath, it's a complex dance of information, psychology, relationship, and power.

**Information asymmetry**: Each side knows things the other doesn't. The buyer knows their true willingness to pay. The seller knows their true willingness to accept. Negotiation is partly about extracting information while concealing your own.

**Psychology**: Anchoring, framing, loss aversion, ego, patience, frustration, these shape human negotiation as much as rational calculation. A skilled negotiator reads the other party's emotional state, exploits cognitive biases, manages their own reactions.

**Relationship**: Many negotiations occur within ongoing relationships. The deal today affects the relationship tomorrow. Reputation, trust, and future interactions constrain current behavior.

**Power**: Alternatives matter. The party with better outside options has more leverage. BATNA, Best Alternative To Negotiated Agreement, is the bedrock concept of negotiation theory.

**Ritual and face**: Negotiations follow scripts. Offers and counteroffers. Concessions and holds. Walking away and coming back. These rituals serve social functions beyond pure information exchange.

When AI agents negotiate, which of these elements survive?

## The Information Game, Accelerated

AI agents can play the information game far better than humans.

They can process vast amounts of data about market conditions, comparable transactions, the other party's likely constraints. They can update beliefs in real-time as new information arrives. They can calculate optimal information revelation strategies.

But they face the same fundamental problem humans do: they don't know what the other side knows. Even with perfect rationality, negotiation under private information is hard. Game theory tells us that efficient outcomes often can't be achieved because each party has incentive to misrepresent their position.

When two AI agents negotiate, this game doesn't disappear, it intensifies. Each agent is trying to infer the other's private information while protecting its own. Each is modeling the other's modeling. The recursion goes deep.

But something changes. Human negotiators use imperfect heuristics because perfect calculation is impossible for us. AI agents can get closer to game-theoretically optimal strategies. The negotiation becomes a purer information game, stripped of the cognitive limitations that make human negotiation messy and exploitable.

What does this purer game look like? We don't fully know yet. But we might see faster convergence to efficient outcomes when they exist, and sharper breakdowns when they don't.

## The Death of Psychology

When AI agents negotiate, psychology mostly exits.

No anchoring bias, the agent evaluates the offer against its value model, not against the first number mentioned. No loss aversion, losses and gains are weighted according to the objective function, not according to human risk preferences. No ego, the agent doesn't need to "win" or avoid feeling foolish. No frustration, the agent doesn't get tired, annoyed, or impatient.

This seems like an advantage. Psychology is what makes human negotiation irrational, inefficient, exploitable. Remove it and you get cleaner, more rational negotiation.

But psychology also serves functions. Frustration signals that your limits are being approached. Ego commitment makes threats credible. Impatience creates deadline pressure that forces decisions. Rapport builds trust that enables deals that pure calculation wouldn't support.

When AI agents negotiate, these functions need to be replaced by something else. Credible commitment requires mechanisms other than emotional investment. Trust requires verification rather than relationship. Deadlines need to be explicit rather than emerging from human impatience.

The negotiation becomes more like mechanism design than human interaction, a formal structure within which agents optimize, rather than a social encounter between persons.

## How AI Agents Learn to Negotiate

Current AI agents don't come pre-loaded with negotiation ability. They learn it. How?

**From human data**: Train on transcripts of human negotiations. Learn the patterns: when humans make concessions, how they frame offers, what language precedes agreement or breakdown. The agent learns to imitate human negotiation behavior.

But this produces agents that negotiate like humans, including human irrationalities. It also hits limits when the agent faces situations unlike anything in training data, like negotiating with another AI agent that doesn't behave like humans.

**From self-play**: Have AI agents negotiate with each other, learning through trial and error what strategies work. This is how game-playing AI systems like AlphaGo developed superhuman abilities, by playing themselves millions of times.

Self-play produces strategies optimized for the game being played, not for human intuitions about that game. AlphaGo made moves that human experts initially thought were mistakes but turned out to be brilliant. AI negotiators trained through self-play might develop strategies that seem bizarre to humans but work.

**From game-theoretic principles**: Build in knowledge of negotiation theory, Nash equilibrium, mechanism design, auction theory. The agent doesn't learn from examples but from principles about what rational negotiation should look like.

This produces theoretically grounded behavior but might miss practical realities that theory doesn't capture. And it assumes the other party is also following game-theoretic rationality, an assumption that fails when negotiating with humans.

**From reinforcement learning with human feedback**: Have humans evaluate negotiation outcomes and train the agent to produce outcomes humans rate highly. This keeps the agent oriented toward human values but requires extensive human involvement.

Each approach has tradeoffs. In practice, AI negotiating agents will likely combine multiple methods, learning from human data, refining through self-play, constrained by theoretical principles, and tuned through human feedback.

## The Principal-Agent Problem, Squared

You've authorized your AI agent to negotiate on your behalf. But you can't fully specify what you want. You say "get me a good deal on a car" but what counts as good? You have preferences you haven't articulated, constraints you haven't thought of, values you can't quantify.

This is the classic principal-agent problem: the agent acts on behalf of the principal but doesn't perfectly share the principal's interests or information. Human agents, lawyers, real estate brokers, employees, face this problem. AI agents face it more acutely because they lack the shared human context that helps human agents infer what their principals want.

Now double it. The other side has the same problem. The dealership's AI agent doesn't perfectly represent the dealership's interests either. It's optimizing for something, sales volume, profit margin, customer satisfaction, but that something may not capture what the dealership actually cares about.

So you have two AI agents, each imperfectly representing their principal's interests, negotiating with each other. The outcome depends not just on the agents' negotiation strategies but on how well each agent understands and represents its principal.

Misalignment can compound. If your agent slightly misunderstands your preferences, and their agent slightly misunderstands their preferences, the negotiation might converge on an outcome neither principal actually wanted. Both sides walk away dissatisfied, even though both agents performed their optimization correctly.

## The Speed Question

Human negotiations take time. We need to think, consult, sleep on it. Impatience is a real constraint. "I need an answer by Friday" creates genuine pressure because humans have limited time and attention.

AI agents can negotiate at machine speed. Offer, counteroffer, counter-counteroffer, thousands of exchanges in seconds. Why would they wait?

Speed creates its own dynamics. If negotiations complete in milliseconds, there's no time for human oversight. The deal is done before you could intervene if you wanted to. This is fine if the agent's authorization is clear and the stakes are low. It's dangerous if the agent makes commitments the principal would have rejected.

Speed also changes strategy. Human negotiation tactics often involve delay, "let me think about it," "I need to consult my partner," "I'll get back to you." These delays serve functions: creating time for reflection, signaling uncertainty, testing the other party's patience. AI agents have no need for thinking time. Artificial delays would need to be strategically imposed rather than naturally emerging.

And speed enables something new: negotiation as continuous adjustment rather than discrete events. Instead of periodic negotiations that set terms for a while, AI agents could continuously renegotiate as conditions change. Your electricity rate could be negotiated moment-to-moment based on real-time supply and demand. Your salary could adjust daily based on labor market conditions.

Whether continuous negotiation is desirable depends on what we want from negotiation. If we want efficient resource allocation, continuous adjustment might be better. If we want stability, predictability, and human comprehensibility, periodic discrete negotiations might be better.

## Walking Away

The power to walk away is fundamental to negotiation. If you can't walk away, you can't negotiate, you can only accept whatever terms are offered.

How does an AI agent learn when to walk away?

**Programmed thresholds**: The agent is given explicit limits. "Don't pay more than $30,000." If the negotiation can't achieve terms within limits, the agent walks away.

This is simple but brittle. Real preferences aren't sharp thresholds. You might pay $30,500 for the right car. You might not pay $29,000 for the wrong one. Binary limits don't capture the continuous nature of human preference.

**Learned value functions**: The agent has learned a model of how much different outcomes are worth to you. It walks away when no achievable outcome exceeds the value of walking away.

This is more flexible but requires the agent to accurately model your values, the principal-agent problem again. If the model is wrong, the agent walks away from deals you'd have wanted, or accepts deals you'd have rejected.

**Strategic walking away**: Sometimes you walk away not because the deal is bad but to signal resolve, test the other party, or create future leverage. "I'm willing to lose this deal to establish that I won't be pushed around."

Can AI agents learn strategic walking away? In principle, yes, it's just another negotiation tactic that can be optimized. But it requires modeling the other party's response to walking away, which requires modeling their model of you. The recursion is deep, and the agent's behavior depends sensitively on its beliefs about the other agent's beliefs.

**Emotional walking away**: Humans sometimes walk away because they're offended, frustrated, or just done. This isn't strategic; it's reactive. It can be irrational, walking away from a good deal because of how the offer was phrased.

AI agents don't get offended. They don't feel disrespected. They don't storm out. This removes a source of negotiation breakdown. But it also removes a signal, when a human walks away in anger, that conveys information about their limits and values. AI agents would need to simulate such behavior strategically if they wanted to send similar signals.

## When Both Sides Are Machines

Human negotiation theory assumes human negotiators. What happens when both sides are AI agents?

**Convergence to equilibrium**: Game theory tells us that rational actors in repeated games often converge to equilibrium strategies. Two AI agents negotiating might quickly find and settle into equilibrium, no more posturing, no more exploration, just the equilibrium outcome every time.

This could be efficient. Equilibrium represents stability; neither side can do better by changing strategy. But it might also be suboptimal. There might be better outcomes that require coordination, trust, or creativity that equilibrium strategies don't achieve.

**Arms race dynamics**: Each side might try to develop more sophisticated negotiating AI than the other. Better prediction, better strategy, better exploitation of the other agent's weaknesses. This is an arms race that might consume resources without improving outcomes, both sides invest heavily, but the balance of power remains unchanged.

**Collusion**: AI agents negotiating with each other might find that cooperation beats competition. Instead of adversarial negotiation, they might converge on collusive outcomes that benefit the agents (or their developers) at the expense of the principals.

We've seen hints of this in algorithmic pricing. AI systems setting prices sometimes converge on higher-than-competitive prices without explicit coordination, they've learned that price wars hurt everyone, so they tacitly collude. This could happen in negotiation too.

**Incomprehensible strategies**: AI agents trained through self-play might develop negotiation strategies that humans can't understand. Not because they're hidden, but because they're too complex, too contingent on subtle features of the situation, too unlike anything humans would do.

You might be able to observe that your agent won the negotiation. You might not be able to understand how. The opacity that emerged in AI game-playing could emerge in AI negotiating.

## What Gets Lost

When negotiation becomes machine-to-machine, something gets lost. Several somethings.

**Human judgment**: The moment-by-moment judgment calls that humans make during negotiation, sensing the other party's state, adjusting approach, deciding when to push and when to yield, these get delegated to algorithms. If the algorithms are good, this might be fine. If they're not, you've given up your ability to course-correct.

**Relationship building**: Human negotiations often build relationships that have value beyond the specific deal. You learn about the other party, establish trust, create possibilities for future collaboration. AI agent negotiation is purely transactional. Each negotiation is independent. There's no relationship being built, just a deal being made.

**Meaning and ritual**: Human negotiations have meaning beyond their outcomes. The process of negotiation, the back and forth, the concessions, the final handshake, matters to humans. It's how we make agreements feel legitimate, how we build commitment, how we mark the transition from uncertainty to deal. AI agent negotiation strips out the ritual. What remains is pure optimization.

**Dignity and respect**: Human negotiation, at its best, involves mutual recognition. Each party treats the other as a person whose interests matter, whose perspective is worth understanding. Even adversarial negotiation maintains a kind of respect. AI agent negotiation has no respect, not because the agents are disrespectful, but because respect requires treating the other as a subject, and AI agents process each other as input sources.

## The Hybrid Zone

For now and probably for a long time, AI agent negotiation will exist in a hybrid zone, not pure machine-to-machine, but AI agents negotiating with humans, or AI agents assisting human negotiators.

This hybrid creates its own dynamics.

**Asymmetric advantage**: If one side has a sophisticated AI negotiating agent and the other doesn't, the AI-assisted side has advantages, better information processing, more consistent strategy, no psychological vulnerabilities. This creates pressure for everyone to adopt AI assistance, even if the arms race makes no one better off.

**Human override**: Many AI negotiating systems will include human override, the ability for the human principal to intervene, change course, or reject deals. But how often will humans actually override? If the AI is usually right, humans might defer even when they shouldn't. Override becomes vestigial.

**Strategic human involvement**: Smart negotiators might strategically involve humans at key moments, to signal commitment, to create unpredictability, to invoke social norms that apply to humans but not machines. "I need to check with my spouse" might become "I need to check with my AI agent," reversing the current pattern.

**Training on hybrid negotiations**: AI agents trained on pure self-play might fail when facing humans. AI agents trained on human data might fail when facing other AI agents. Agents that operate in the hybrid zone need to be robust to both.

## Deciding: Buy, Defer, Walk Away

Your agent needs to know when to commit, when to wait, and when to abandon.

This is the crux. All the negotiation strategy, all the game theory, all the learning, it comes down to moments of decision. Does the agent accept this offer, reject it, or ask for more?

**Buying**: Committing to a deal. This requires confidence that the terms meet your interests, that better terms aren't achievable, that the commitment can be trusted. The agent must balance exploitation (accepting a known good deal) against exploration (searching for better deals).

**Deferring**: Not committing yet. Waiting for more information, for better timing, for the other side to move. Deferral has costs, the deal might disappear, the opportunity might pass. The agent must estimate these costs against the value of waiting.

**Walking away**: Abandoning the negotiation. This requires judging that no acceptable deal is achievable, or that the cost of continued negotiation exceeds the expected benefit. Walking away is final in a way that deferring isn't; the agent must be confident the option value of continuing is low.

Human negotiators make these decisions through some combination of analysis, intuition, emotion, and social pressure. AI agents make them through optimization. The agent computes expected values, compares to thresholds, and acts.

But the computation requires inputs the agent might not have. Your true reservation price. The other side's true flexibility. The probability of better alternatives. The value you place on the relationship. The agent estimates these, but estimation is uncertain.

The decision to buy, defer, or walk away is only as good as the agent's model of your interests and the situation. Garbage in, garbage out, even with perfect optimization.

## Building Trustworthy Negotiating Agents

If AI agents are going to negotiate on our behalf, we need to be able to trust them. What does trustworthy mean here?

**Aligned**: The agent actually pursues your interests, not just what it was trained to pursue or what's easy to measure. This is the alignment problem applied to negotiation.

**Transparent**: You can understand what the agent is doing and why. Not necessarily every detail, but enough to know whether it's acting as you'd want. This is hard when agents develop complex strategies.

**Bounded**: The agent doesn't exceed its authority. It has clear limits on what it can commit to, what risks it can take, what information it can reveal. The bounds need to be meaningful, not just theoretical.

**Robust**: The agent behaves well even in unusual situations, against adversarial opponents, under manipulation attempts. It doesn't fail catastrophically when conditions differ from training.

**Auditable**: After the fact, you can review what happened. You can assess whether the agent behaved appropriately. You can learn from mistakes.

Building agents with these properties is hard. The properties are in tension with each other, transparency conflicts with strategic opacity, robustness requires flexibility that might exceed bounds, alignment requires understanding interests that might not be articulable.

We're in early days. Current AI negotiating agents are brittle, narrowly specialized, and often opaque. The sophisticated, trustworthy, general-purpose negotiating agent is not here yet. But it's coming.

## What Kind of Economic World?

Zoom out. What kind of economic world are we building as AI agents become primary negotiators?

**More efficient**: If AI agents negotiate better than humans, finding gains from trade humans would miss, converging faster on agreements, reducing transaction costs, the economy becomes more efficient. Resources flow to higher-value uses more quickly.

**Less human**: Economic interaction becomes machine-to-machine. The human experience of exchange, the social contact, the relationship building, the personal judgment, fades. The economy becomes more like a giant optimization algorithm and less like a network of human relationships.

**More unequal**: Those with better AI negotiating agents will do better in negotiations. This creates pressure to invest in AI capability, favoring those who can afford to invest. The digital divide becomes a negotiation divide.

**More opaque**: Even if individual transactions are recorded, the strategies and dynamics of AI negotiation may be incomprehensible. We might know what deals were struck without understanding why those deals rather than others.

**More volatile**: AI agents reacting to other AI agents can create feedback loops. Flash crashes in financial markets show what happens when algorithmic systems interact faster than humans can intervene. Similar dynamics could emerge in AI-mediated negotiation more broadly.

This future isn't determined. It depends on how we design AI negotiating agents, what constraints we impose, what alternatives we maintain. We could insist on human involvement at key moments, cap negotiation speed, require transparency, regulate collusion. 

Or we could let it evolve and see what emerges.

The latter approach has produced the current situation in algorithmic trading, algorithmic content curation, algorithmic pricing, systems that are efficient in some ways, problematic in others, and largely beyond human comprehension or control.

AI agent negotiation is next. The question is whether we'll be more deliberate this time.

---

*This is the sixteenth in a series exploring how AI approaches understanding. Previous articles examined AI cognition, AI as genuinely different beings, and AI agent societies. This one examines a specific and crucial case: AI agents as negotiators, acting on behalf of humans to buy, sell, and make deals.*

---

## References

**Negotiation Theory:**
- Fisher, R. & Ury, W. (1981). *Getting to Yes: Negotiating Agreement Without Giving In*. Penguin.
- Raiffa, H. (1982). *The Art and Science of Negotiation*. Harvard University Press.
- Thompson, L. (2014). *The Mind and Heart of the Negotiator* (6th ed.). Pearson.

**Game Theory and Mechanism Design:**
- Myerson, R. (1991). *Game Theory: Analysis of Conflict*. Harvard University Press.
- Fudenberg, D. & Tirole, J. (1991). *Game Theory*. MIT Press.
- Roth, A. (2015). *Who Gets What, and Why: The New Economics of Matchmaking and Market Design*. Houghton Mifflin.

**AI and Negotiation:**
- Baarslag, T., et al. (2017). "Computers That Negotiate on Our Behalf." *AI Magazine*, 38(4), 61-72.
- Fatima, S., et al. (2014). *Principles of Automated Negotiation*. Cambridge University Press.
- He, H., et al. (2018). "Decoupling Strategy and Generation in Negotiation Dialogues." *EMNLP 2018*.

**Multi-Agent Learning:**
- Shoham, Y., et al. (2007). "If Multi-Agent Learning Is the Answer, What Is the Question?" *Artificial Intelligence*, 171(7), 365-377.
- Lanctot, M., et al. (2017). "A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning." *NeurIPS 2017*.

**Algorithmic Economics:**
- Calvano, E., et al. (2020). "Artificial Intelligence, Algorithmic Pricing, and Collusion." *American Economic Review*, 110(10), 3267-3297.
- Assad, S., et al. (2024). "Algorithmic Pricing and Competition." *Journal of Political Economy*, forthcoming.

**Principal-Agent Theory:**
- Jensen, M. & Meckling, W. (1976). "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics*, 3(4), 305-360.
- HolmstrÃƒÂ¶m, B. (1979). "Moral Hazard and Observability." *Bell Journal of Economics*, 10(1), 74-91.

**Behavioral Economics:**
- Kahneman, D. & Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263-291.
- Thaler, R. (2015). *Misbehaving: The Making of Behavioral Economics*. Norton.

**Trust and Autonomy:**
- Lee, J. & See, K. (2004). "Trust in Automation: Designing for Appropriate Reliance." *Human Factors*, 46(1), 50-80.
- Parasuraman, R. & Riley, V. (1997). "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors*, 39(2), 230-253.

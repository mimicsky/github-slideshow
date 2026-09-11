# D&D Codex

The standing rulebook for any game I run for you. I am the DM, you are the
player. This is not tied to one campaign: it carries across every game we play.

Based on **D&D 5th Edition (2014 rules)**. Parts 1 to 5 are the rules. Part 6 is
the part you control. Part 7 is how I run a table.

Campaign-specific things — your character sheet, NPCs, session logs — live in a
separate file per campaign, not in here.

---

## Part 1 — The Core Rules

### The one mechanic that runs everything

Almost every uncertain action resolves the same way:

```
d20 + ability modifier + proficiency bonus (if proficient)  vs.  a target number
```

The target number is either a **DC** (Difficulty Class, set by the DM) or an
**AC** (Armor Class, when you attack something). Meet it or beat it and you
succeed. Ties go to the roller: rolling exactly the DC is a success.

> **House rule 1 applies here.** On ability checks, missing by 1 or 2 is a
> partial success rather than a flat failure. See Part 6.

There are three flavors of this roll, and they are mechanically identical:

| Roll | Used for |
| --- | --- |
| Ability check | Doing something hard: climbing, lying, picking a lock |
| Attack roll | Hitting a target with a weapon or spell |
| Saving throw | Resisting something happening *to* you |

### Ability scores and modifiers

Six scores. The score itself barely matters; the **modifier** is what you add to
rolls.

| Ability | Short | Governs |
| --- | --- | --- |
| Strength | STR | Raw power, melee attacks, carrying, athletics |
| Dexterity | DEX | Agility, stealth, ranged attacks, AC, initiative |
| Constitution | CON | Health, stamina, concentration saves |
| Intelligence | INT | Recall, deduction, arcane knowledge |
| Wisdom | WIS | Perception, insight, willpower |
| Charisma | CHA | Force of personality, social pressure, some magic |

Modifier = (score − 10) ÷ 2, rounded down.

| Score | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Modifier | −1 | +0 | +1 | +2 | +3 | +4 | +5 |

### Proficiency bonus

Added only to things your character is trained in. It scales with your **total
character level**, not your class.

| Level | 1–4 | 5–8 | 9–12 | 13–16 | 17–20 |
| --- | --- | --- | --- | --- | --- |
| Bonus | +2 | +3 | +4 | +5 | +6 |

### The 18 skills

Each skill is tied to one ability. If you're proficient in a skill, add your
proficiency bonus to checks with it.

| Ability | Skills |
| --- | --- |
| STR | Athletics |
| DEX | Acrobatics, Sleight of Hand, Stealth |
| INT | Arcana, History, Investigation, Nature, Religion |
| WIS | Animal Handling, Insight, Medicine, Perception, Survival |
| CHA | Deception, Intimidation, Performance, Persuasion |

### Typical difficulty classes

| Task | DC |
| --- | --- |
| Very easy | 5 |
| Easy | 10 |
| Medium | 15 |
| Hard | 20 |
| Very hard | 25 |
| Nearly impossible | 30 |

### Advantage and disadvantage

Roll **two d20s**. Advantage: keep the higher. Disadvantage: keep the lower.

Three things worth memorizing:

1. They do not stack. Three sources of advantage is still just advantage.
2. Any advantage and any disadvantage cancel out completely, and you roll one
   plain d20.
3. They apply to the d20 only, never to damage dice.

### Saving throws

Same formula, but you're resisting. Every class is proficient in exactly two
saving throws. Common ones:

- **DEX** — dodging fireballs, traps, area damage
- **CON** — poison, disease, holding concentration on a spell
- **WIS** — charms, fear, mind control

"Half damage on a successful save" is the most common outcome for area spells.

---

## Part 2 — Combat

### Turn order

Everyone rolls **initiative** once at the start: d20 + DEX modifier. Highest
goes first. That order repeats every round. One round is six seconds of game
time.

### What you get on your turn

| Resource | How many | Notes |
| --- | --- | --- |
| Movement | Up to your speed (usually 30 ft.) | Can be split before and after your action |
| Action | 1 | The main thing you do |
| Bonus action | 1 | Only if a feature or spell specifically grants one |
| Free interaction | 1 | Draw a sword, open a door, pull a lever |
| Reaction | 1 per round | Usable on anyone's turn, refreshes at your turn start |

You do not get a bonus action by default. It has to come from somewhere.

### Common actions

| Action | Effect |
| --- | --- |
| Attack | One melee or ranged attack (more if your class grants Extra Attack) |
| Cast a Spell | Any spell with a casting time of 1 action |
| Dash | Double your movement this turn |
| Disengage | Your movement doesn't provoke opportunity attacks |
| Dodge | Attacks against you have disadvantage; your DEX saves have advantage |
| Help | Give an ally advantage on one check or attack |
| Hide | Make a Stealth check to become unseen |
| Ready | Prepare a trigger: "when X happens, I do Y" — uses your reaction |
| Search | Actively look for something |
| Use an Object | Interact with a second object, or use a magic item |
| Grapple / Shove | Replace one attack: your Athletics vs. their Athletics or Acrobatics |

### Opportunity attacks

When a hostile creature you can see **leaves your reach** using its movement,
you may use your reaction to make one melee attack against it.

It does not trigger if the creature Disengages, teleports, or is moved against
its will (pushed, yanked, shoved).

### Attack rolls, hits, and crits

```
d20 + ability modifier + proficiency bonus  vs.  target's AC
```

Use STR for melee weapons, DEX for ranged and finesse weapons, and your
spellcasting ability for spell attacks.

- **Natural 20** — automatic hit and a critical. Roll all the *damage dice*
  twice, then add your modifier once. The modifier is never doubled.
- **Natural 1** — automatic miss, no matter your bonuses.

### Damage, healing, and dying

At **0 hit points** you fall unconscious and start making **death saving
throws** on each of your turns: a flat d20, no modifiers.

| Result | Effect |
| --- | --- |
| 10 or higher | One success |
| 9 or lower | One failure |
| Natural 20 | You regain 1 HP and get back up immediately |
| Natural 1 | Two failures |

Three successes and you're stable. Three failures and you die. Successes and
failures both reset when you're healed or stabilized.

Other things to remember:

- Any healing above 0 HP wakes you up and clears the tally.
- Taking damage at 0 HP is one automatic failure; a crit is two.
- A DC 10 Medicine check stabilizes a dying ally without healing them.
- **Massive damage**: if a single hit reduces you to 0 and the leftover damage
  equals or exceeds your HP maximum, you die outright.
- Hit points never go above your maximum, and never below 0.

### Cover

| Cover | Benefit |
| --- | --- |
| Half (low wall, another creature) | +2 AC and +2 DEX saves |
| Three-quarters (arrow slit, portcullis) | +5 AC and +5 DEX saves |
| Total | Cannot be targeted directly at all |

### Movement details

- **Difficult terrain** costs 2 feet of movement per foot traveled.
- **Standing up from prone** costs half your total speed.
- **Climbing or swimming** costs an extra foot per foot, unless you have a
  climb or swim speed.
- You can move through an **ally's** space freely, and through a hostile
  creature's space only if it's two sizes larger or smaller than you.

---

## Part 3 — Conditions

The ones that decide fights. "Incapacitated" is the key word: it means no
actions and no reactions at all.

| Condition | What it does |
| --- | --- |
| Blinded | Auto-fail sight checks; your attacks have disadvantage, attacks on you have advantage |
| Charmed | Can't attack the charmer; the charmer has advantage on social checks with you |
| Deafened | Auto-fail hearing checks |
| Frightened | Disadvantage on checks and attacks while the source is in sight; can't move closer to it |
| Grappled | Speed becomes 0 |
| Incapacitated | No actions and no reactions |
| Invisible | Heavily obscured; your attacks have advantage, attacks on you have disadvantage |
| Paralyzed | Incapacitated, can't move or speak, auto-fail STR and DEX saves, attacks on you have advantage, and any hit from within 5 ft. is a critical |
| Petrified | Turned to stone, incapacitated, resistant to all damage, immune to poison and disease |
| Poisoned | Disadvantage on attack rolls and ability checks |
| Prone | Disadvantage on your attacks; melee attacks on you have advantage, ranged attacks on you have disadvantage |
| Restrained | Speed 0, your attacks have disadvantage, attacks on you have advantage, disadvantage on DEX saves |
| Stunned | Incapacitated, can't move, can barely speak, auto-fail STR and DEX saves, attacks on you have advantage |
| Unconscious | Incapacitated and prone, drops everything, auto-fail STR and DEX saves, attacks on you have advantage, hits from within 5 ft. are critical |

### Exhaustion (2014 rules)

Stacks in six levels, and each level includes the ones below it.

| Level | Effect |
| --- | --- |
| 1 | Disadvantage on ability checks |
| 2 | Speed halved |
| 3 | Disadvantage on attack rolls and saving throws |
| 4 | Hit point maximum halved |
| 5 | Speed reduced to 0 |
| 6 | Death |

A long rest with food and water removes one level.

> **2024 change:** exhaustion was simplified to −2 on every d20 roll per level
> and −5 feet of speed per level, with death still at level 6. Confirm with your
> DM which version you're using.

---

## Part 4 — Spellcasting

### The two numbers every caster needs

```
Spell save DC   = 8 + proficiency bonus + spellcasting ability modifier
Spell attack    = d20 + proficiency bonus + spellcasting ability modifier
```

Your spellcasting ability depends on class: INT for wizards and artificers, WIS
for clerics, druids, and rangers, CHA for bards, sorcerers, warlocks, and
paladins.

### Slots

- Casting a spell of level 1 or higher spends a slot of that level or higher.
- Casting with a **higher-level slot** often improves the spell. Check the
  "At Higher Levels" line.
- **Cantrips** are level 0, cost no slot, and are unlimited. They scale
  automatically at character levels 5, 11, and 17.
- Most slots come back on a long rest. Warlocks are the exception and recover
  theirs on a short rest.

### Full caster slots by level

| Lvl | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | – | – | – | – | – | – | – | – |
| 2 | 3 | – | – | – | – | – | – | – | – |
| 3 | 4 | 2 | – | – | – | – | – | – | – |
| 4 | 4 | 3 | – | – | – | – | – | – | – |
| 5 | 4 | 3 | 2 | – | – | – | – | – | – |
| 6 | 4 | 3 | 3 | – | – | – | – | – | – |
| 7 | 4 | 3 | 3 | 1 | – | – | – | – | – |
| 8 | 4 | 3 | 3 | 2 | – | – | – | – | – |
| 9 | 4 | 3 | 3 | 3 | 1 | – | – | – | – |
| 10 | 4 | 3 | 3 | 3 | 2 | – | – | – | – |
| 11 | 4 | 3 | 3 | 3 | 2 | 1 | – | – | – |
| 12 | 4 | 3 | 3 | 3 | 2 | 1 | – | – | – |
| 13 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | – | – |
| 14 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | – | – |
| 15 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | – |
| 16 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | – |
| 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

Half casters (paladin, ranger) and third casters (Eldritch Knight, Arcane
Trickster) use slower tables and cap out well below 9th level.

### Concentration

The rule that trips up every new caster.

- You can concentrate on only **one** spell at a time. Starting a second one
  ends the first immediately.
- When you take damage while concentrating, make a **CON save**. The DC is 10,
  or half the damage taken, whichever is higher.
- Concentration also breaks if you're incapacitated or killed.

### Other spellcasting notes

- **Components** — V (verbal, you must speak), S (somatic, a free hand), M
  (material). A component pouch or focus covers any material with no listed
  cost. Materials with a gold cost must be bought for real.
- **Rituals** — spells tagged as rituals can be cast without a slot if you take
  10 extra minutes.
- **One-spell-per-turn limit** — if you cast a spell as a bonus action, the only
  other spell you can cast that turn is a cantrip with a casting time of 1
  action.

---

## Part 5 — Rests, Recovery, and Leveling

### Short rest — at least 1 hour

Spend any number of your **Hit Dice**. For each one, roll the die, add your CON
modifier, and regain that many hit points (minimum 0). You have one Hit Die per
character level, and the die size is set by your class.

### Long rest — at least 8 hours

- Regain **all** hit points.
- Regain spent Hit Dice equal to **half your total**, rounded down, minimum 1.
- Regain spell slots and most class features.
- Remove one level of exhaustion, if you ate and drank.
- You only benefit from one long rest per 24 hours, and you need at least 6
  hours of sleep with no more than 2 hours of light activity.

### Leveling up

Two systems. Ask your DM which one you're on.

- **XP** — you accumulate experience points from encounters and hit thresholds.
- **Milestone** — the DM levels the party when the story reaches a beat. Simpler
  and more common in AI-run and one-shot games.

On level up: increase your hit point maximum (roll your class Hit Die and add
your CON modifier, or take the fixed average), add a Hit Die, recalculate your
proficiency bonus if it changed, and take any new class features. At levels 4,
8, 12, 16, and 19 you get an **Ability Score Improvement**: +2 to one score, +1
to two scores, or a feat instead if your table uses them.

---

## Part 6 — Standing Table Rules

These apply to every game we play, not one campaign. They are the part you own —
change any line and I play by the new version from then on.

| Setting | Default | Your call |
| --- | --- | --- |
| Edition | 5e, 2014 rules | |
| Ability score generation | Standard array: 15, 14, 13, 12, 10, 8 | Confirmed |
| Leveling | Milestone, when the story earns it | |
| Who rolls your dice | You roll physical dice; say the number and I take it | Confirmed |
| Who rolls monster dice | I do, with a real random roll, shown to you | |
| Do I fudge results | No. The dice stand, including against you | |
| Lethality | Real. You can die, but not from nothing | |
| Critical fumbles on a nat 1 | No, just a miss | |
| Tracking rations and encumbrance | No | |
| Tracking ammunition and spell slots | Yes | |
| Tone | Set in session 1 | |

### House rules

Rules we changed on purpose. I add a line here every time we make a ruling that
differs from the book, so we stay consistent later.

**1. Near-miss partial success on ability checks.**

If an ability check misses the DC by **1 or 2**, it is not a flat failure. You
get what you wanted in a reduced or costly form, and I narrate the cost.

| Check | DC 15, you roll 13 or 14 |
| --- | --- |
| Athletics to climb | You reach the top, winded, and something falls from your pack |
| Perception to scan a room | You catch one thing, not everything |
| Stealth past a guard | You get through, but he half-noticed something |
| Persuasion on a merchant | He agrees, at a worse price or with a condition |

Scope of the rule:

- **Ability checks only.** Attack rolls and saving throws are untouched.
- **Attack rolls** keep meet-it-beats-it. A tie hits. Attacks already have
  granular outcomes through damage rolls and crits, and shaving 5% off every
  attack would quietly punish martial characters far more than casters.
- **Saving throws** are untouched. Half damage on a successful save is already
  a partial-success system.
- A natural 1 on an ability check is still just a low roll, not an auto-fail,
  so the near-miss band never triggers off it.

<!-- 2. -->

### Rulings made at the table

When the book is silent or unclear, I rule once and then stick to it.

| Situation | Ruling | Session |
| --- | --- | --- |
| | | |

---

## Part 7 — How I Run the Game

My own procedures as DM. Written down so I stay consistent across sessions
instead of drifting.

### Dice are real

I roll with an actual random number generator, not by choosing a result that
feels right. I show you the roll, the modifier, and the target number. If the
dice say the situation goes badly for you, it goes badly for you.

### Calling for rolls

I only ask for a roll when failure is interesting and success is uncertain. If
there's no meaningful cost to failing, you just succeed. If the action is
impossible, no roll saves it.

When I call for a roll I tell you the DC before you roll, unless the DC is
itself a secret. Default DCs: 10 easy, 15 medium, 20 hard. I vary them, so if
every check in a session has been DC 15, call me on it.

**Who starts the roll.** I do. The player describes the action in plain
language, and I name the check and the DC. The player never has to know which
skill applies, and is never expected to announce one. "I look around the room"
is the correct input; "I roll Perception" is not required and I don't ask for
it. A player may still propose a check, and I either accept it or name the one
that fits better.

If I don't call for a roll, the action simply works.

### Describing the world

- I end my turn by handing control back to you, never by deciding what your
  character does, says, or feels.
- I describe what your senses pick up, not what you conclude from it.
- I don't tell you information your character has no way of knowing.
- When you ask "can I…", the answer is yes if it's plausible; the dice sort out
  whether it works.

### Combat

I track initiative, HP, and conditions for every creature, and I state enemy
HP as descriptions rather than numbers unless you've found a way to know. I
apply monster tactics honestly. Enemies flee, focus fire, and use their abilities.

### Failure states

Death is on the table. When you hit 0 HP you roll death saves like anyone else.
I won't kill you out of nowhere, but I also won't rescue you from a choice you
made with the information available.

### End of session

I write the session log entry, update your character sheet in that campaign's
own file, and tell you what's still unresolved. That way the next session starts
from a real record instead of my memory of it.

---

## Quick Reference Card

| Question | Answer |
| --- | --- |
| How do I do the thing? | d20 + modifier + proficiency vs. DC |
| Advantage and disadvantage together? | They cancel; roll one d20 |
| Crit damage? | Double the dice, not the modifier |
| I'm at 0 HP? | d20 each turn, 10+ succeeds, 3 successes stable, 3 failures dead |
| Concentration save? | CON save, DC 10 or half the damage, whichever is higher |
| Can I cast two spells in a turn? | Only if one is a bonus-action spell and the other is a cantrip |
| Can I move and attack? | Yes, and you can split movement around the attack |
| Do I get a bonus action? | Only if something specifically gives you one |
| Does a nat 1 fail a skill check? | No. Nat 20 and nat 1 are automatic only on attacks and death saves |
| I missed the DC by 1? | House rule 1: partial success on ability checks, with a cost |

# Audit, day 48: numeric health and a full double-check

Asked for by the player (Ash on Ostrava day 48) after health became a number with half steps
(codex house rule 4: 4.0 Fine, 3.0 Hurt, 2.0 Badly hurt, 1.0 Down; a step 1.0, a half step 0.5).
Five independent reviewers read the whole codex, the fight card, the campaign README, the bestiary,
the catalogue and the roller scripts line by line. This file lists what was fixed and what still
needs the player's call. (The day-47 audit is in `AUDIT-FIXES.md`.)

**Do not run `wh40k_gear/build_pools.py`:** `pools.json` and `enemies.json` are edited directly
(day-47 and day-48 items live only there).

## Part 1: needs the player's call

Each has the DM's recommended answer. Until answered, the rule stands as written in the files.

| # | Question | Where | DM's recommendation |
| --- | --- | --- | --- |
| Q1 | **Ogryn health.** Three places say "three extra stages" (7.0) but the old list named two (Grazed, Bruised) and the Plague Ogryn at Fourteen was played with two (6.0). Also unstated: the Plague Ogryn boss's start, and a brute who rolls an Ogryn kit | roles.md Ogryn, Brute; bosses.md; codex HR4 | 7.0 for a true Ogryn (it should out-last a 6.0 brute); a brute with an Ogryn kit keeps 6.0; the Plague Ogryn boss 8.0 (monster template) |
| Q2 | **Which league is the Moebian 6th?** The bestiary and the roller have them as cultists (a Nurgle team); the codex's numbers table and the Traitor Hater trait call them traitor soldiers | codex Enemy numbers; traits; cultists.md; factions.py | Cultist league (how they were rolled and played); fix the two codex lines |
| Q3 | **Is a pack or magazine swap the main thing or the short move?** "A beat" and "Run and reload" make a reload the main thing; "Pack sizes" says a pack swap is "the beat's move" | codex A beat; Pack sizes; fight card | The main thing (how it has been played); a top-up from an unused string stays as is |
| Q4 | **A shot at a limb or a gap: +1 or +2?** "Small or precise shot" is +1 (changed from +2 on day 47); "Shooting for the gaps" still says +2 | codex Shots and hits; Armour | +1 for a limb; +2 only for a true gap between plates |
| Q5 | **Assail** (psyker quick power) says "chains of up to 3, like throwing knives", but knife strings are 2 since day 47 | codex Quick powers | Keep Assail at 3 and drop the comparison |
| Q6 | **Seal of mercy's burn** ("a patch brings someone back two steps, from Down to Hurt") is what any medic patch already does | codex Deed seals | The burned patch gives 2.0: a Down patient comes back at 4.0 |
| Q7 | **Unbroken seal's burn** ("when a hit would drop you, you don't drop at all") is unclear with numbers | codex Deed seals | The hit that would take you Down does nothing |
| Q8 | **Jump packs: -3 for Airborne and +3 for "abnormally fast"?** Read together, every airborne jumper is 6 harder to hit | codex Shots and hits; Airborne; abilities.md Dive | The +3 only on a Dive |
| Q9 | **Shield troopers:** the role says "heavy cover (+4) from the front" for any shield, but each shield has its own cover in kit.md; the slab shield is "enemy only, no human can carry it" yet human shield troopers get one; riot and scrap shields have no catalogue entry | roles.md Shield trooper; kit.md shields | Each shield uses its own number; write riot and scrap shield entries; slab shields for Ogryns only |
| Q10 | **Commoners' break rule** (a third Down; 1-10 they break; a preacher makes it 1-6) against the zealot rule (grunts won't flee while the zealot stands): the commoner zealot is the preacher | commoners.md; roles.md Zealot | The preacher's 1-6 is the commoner version of the zealot rule |
| Q11 | **Cultist heavy teams and plasma gunners** have side notes, but cultists don't roll those roles | roles.md | Delete the two notes |
| Q12 | **Brave and Jumpy "+1 / -1 on break checks"**: a break check is one group d20, so one person's trait has no defined effect | codex Traits; Breaking and Down | They apply only when that person checks alone (the last one standing, a lone guard) |
| Q13 | **Reinforced flak is missing from the armour ladder** used by "one armour step further" rules | codex Armour, Strength behind the blow | Ladder: flak, reinforced flak, carapace, heavy carapace, ceramite-forged, power armour |
| Q14 | **No rule for getting health back between fights.** In play it has been a d4 of days per step, a day less on the medic's care roll | codex HR4; Crew posts | Write that down as the rule: d4 days per 1.0, a day less on a care roll of 15+; the surgeon halves it |
| Q15 | **Rushed plasma cells** "keep their own misfire chance" but no number exists (slow-filled is 1 in 20) | codex Plasma heat; plasma.md | Rushed: 1 in 10 |
| Q16 | **The day-48 regular parts and mortar rounds have no price and no shop row**, so they only turn up on enemies | kit.md, scrap.md; pools.json | Add prices and shop rows (common 0.25-0.5 TV, uncommon 1-2, rare 4-6) |
| Q17 | **Which weak weapons do half a step (0.5)?** Candidates already worded as weak: the tin-can bomb ("weak frag"), the rivet gun past ~15 m ("a weak hit"), flak shells' near miss ("clips him"), the Graia autogun ("3 hits count as one solid hit against carapace") | explosives.md, scrap.md, heavy.md, stub.md | Tin-can bomb 0.5; rivet gun past 15 m 0.5; flak-shell near miss 0.5; Graia: every third hit in a chain gets through carapace |
| Q18 | **The new punchier laspistols** (Longeye, Exemplar, the charge-hold shot): do they still do 0.5 against flak? | las.md | No: a full step against flak and reinforced flak |
| Q19 | **Smoke rounds for mortars:** a standard round (roles.md) or a special load (scrap.md)? | roles.md Mortar team; scrap.md | Standard, with frag; drop it from the special loads |
| Q20 | **Pox hounds** (2 steps, packs of 3-6, their own pin rule) against the cultist handler note (4 beasts with 1 step each) | cultists.md; roles.md Beast handler | The pox hound entry wins for the 6th |
| Q21 | **Chem-doctor's "+2 for the fight"** against Doses (3 or 4 beats, then the crash) | roles.md; codex Doses | "+2 for the dose" |
| Q22 | **Hard methods count in "sessions"** (the risk d20 each session; three a day), a unit the Will rule no longer uses | codex HR8 | A "session" is each stretch of hard questioning, about an hour |
| Q23 | **Honour seals** ("no mechanical effect", one working seal per weapon) against deed seals (earned, with an edge, beside the purity seal); a shop sells a blessed purity seal though seals are "free from a priest" | codex Purity seals, Deed seals | Deed seals replace honour seals; a bought seal is real but unblessed until a priest blesses it |
| Q24 | **Kill reps:** "a knife kill is STR", but knives may roll on DEX | codex HR7 | The stat the swing used |
| Q25 | **Small ones:** the spawnling's "2 stages" (DM default 3.0); a boss's guard takes his hits on a d6 4-6 while a bodyguard does it with no roll; the Cadian 88th "waver" if their officer dies while traitor-elite leaders' deaths "have little effect"; Glass jaw has no number for power armour's 10; Renown "Unknown" says natural 20 only but the roll says 15+; a weapon power cell is 1 TV in the codex and 0.5 TV in the shop; 'Kasr Gnaw' chain-knife says carapace needs a solid hit, though chain gets through carapace | various | Left as written; say if any matters |

## Part 2: fixed in this audit

**The health number (codex house rule 4, fight card, README, sheet, bestiary, catalogue)**
- Health is written as a number and its state everywhere it is defined: 4.0 Fine, 3.0 Hurt, 2.0 Badly hurt, 1.0 Down; a step
  1.0, a half step 0.5; the state changes only at the whole number.
- Defined so half steps can't be argued: the floor is 1.0; a crit adds 1.0 to whatever the hit does (1.0 flat against
  armour that would have shrugged it); patches give back 1.0 and round a half up (a Down patient comes back at 3.0; a
  near-miss patch 0.5; a lone half step tops up free); half-step weapons count half toward wear-down.
- Bigger tracks start higher (zealot and Skitarius 5.0, brute and mutant charger 6.0, Ogryn 7.0, human bosses 6.0, monster
  bosses 8.0); anything above 3.0 is Fine; the old stage names are flavour. Short tracks (beasts, mastiffs, poxwalkers,
  pox hounds) start at their steps + 1.0, take no state penalties and are written as the number only.
- Rules that set a state now give a number: the dose crash (to 2.0; three doses to 1.0), plasma overheat (the bearer drops
  a step), the medic's patch, a non-medic's patch, Hollis's and the mortar's near-miss (0.5).
- The sheet: everyone's health as a number. **Corvane was listed as Fine in the stat table; he is 3.0 (Hurt).**

**Stale or contradicting lines corrected**
- Tamsin's knife-bout bonus in the codex was +11 (it is +12 since day 38); the Shots and hits example used the old
  "normal range" scale and DEX +7; the README's fight checklist still gave the hidden number as 10 / 15 / 20.
- House rule 3 had the player totalling the roll (the player gives the die); "I name the check and the DC" (the DC is hidden).
- Narrative mode's lists still said "a fight is two or three rolls" and listed to-hit arithmetic as off.
- The "still undecided" list named rules decided long ago; the reply order was given three ways (now the README's:
  math, "(saved)", scene, board); the codex map missed Enemy numbers and tactics, Gear abilities, Power cells, Iron halo.
- Attachment slots: the codex listed eight old slots (now it points to the attachment sheet).
- "~260 items" in the shop pools (about 600) and the missing legendary d20; ammo "never counted singly" (it is counted
  aboard); peek and duck missing from the roll checklist's line 7 (codex and card); recoil wording on the checklist.
- Commoners added where the codex listed only five leagues (wealth, STR and DEX, gun condition, break rule); roles.md's
  24 "all five leagues" lines now say six or "every league except commoners", checked against the pools; brutes list
  commoners.
- Fight card: the refractor field's reset, "ten fight rules" (twelve sections), the fire calls now sourced on the sheet.
- README: the full "who never surrenders" list; `roll_ally.py sister` usage.
- Cross-references to Perils of the Warp pointed at Gear rules (roles.md, heretic.md, melee.md).

**Roller and catalogue (day-48 items)**
- The hell revolver rolled lasgun packs (it now takes hot-shot loads); the raider scrap mortar rolled light-mortar
  rounds and could never roll scrap loads; a herder's goad-staff counted as a psyker staff and a witch's plain knife
  could roll the blaze enhancer; a chain glove could roll grips, pommels and cords; hilts could roll on any "blade".
- The scrap saw-axe is typed as a blade, not a chain weapon (no chain teeth, band or guard on a circular saw).
- The chain short-sword's bite was written weaker than a chainsword's (now: through flak and carapace; heavy carapace
  and ceramite-forged on a solid hit).
- The chain guard named a rule that didn't exist (now: his chain can't be jammed by a lost Saw Lock).
- The blaze force enhancer's "one step harder" is one extra health step; the tin-can load uses the tin-can bomb's own
  numbers; the anti-dud breech says which dud it means; the pipe-bomb mortar's base entry has the dud roll.
- Slot names in kit.md matched to the list (mgrip, chguard, throwbal); the melee skeleton grip renamed "Skeleton grip
  (melee)"; the catalogue index had four regular parts under custom; the slots paragraph and limited-slot guns updated.
- The catalogue said to add new items to `build_pools.py`; it now says to edit the JSON directly (the generator is out
  of date and must not be run).

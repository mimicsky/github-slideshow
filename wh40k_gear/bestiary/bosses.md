# Bosses

Set by the player, Ash on Ostrava day 47, after the Plague Ogryn at Fourteen went down in one beat. **Bosses are
meant to hurt.** Two kinds: **monster bosses** (bullet sponges) and **human bosses** (commanders with an honour
guard). The roster below is drawn from 40k lore; each entry is short, and the DM plays it to the templates.

A boss and its escort come **on top of** the mission's force (codex Part 8, Enemy numbers and tactics).

**Two bosses (the player: 'sometimes just challenge me').** Whenever a boss is set for a **whole-Light fight or a
regular battle**, roll a d6: **5-6, a second boss** (a different kind, or its mate: a commander and his beast, a
handler and two monsters, two of the same). The DM rolls it openly when the boss shows.

## The boss meter (set by the player, day 47)

A bar that fills over the campaign, so a boss can turn up in any fight, not only the ones the story plans.

- **At the start of every fight, roll a d100 openly: at or under the meter, a boss spawns** (the DM picks which
  from the roster for that enemy, hidden until it's seen; the two-boss d6 still applies in a big fight).
- **The meter starts at 1%.** After every fight or mission, **the DM adds 1-5%** for the size of it and what the
  Light did: about **+1** a stealth or small job, **+2** a kill-team mission, **+3** a regular battle, **+4** a
  whole-Light fight, **+5** when they kick the hornet's nest (a commander killed, a stronghold burned, the
  enemy's masters paying attention). The DM's call; never more than +5 at a time.
- **When a boss spawns from the meter, it drops back to 1%.** (DM default; the player may change it.)
- **Story bosses are separate:** a boss the story already put somewhere (a Major in his hall, a cult leader in his
  temple) is there whatever the meter says.
- **The meter is tracked on the campaign sheet**, next to the coin, where the player can see it.

## Monster boss template

- **8 health stages:** Fine, Grazed, Bruised, Hurt, Wounded, Badly hurt, Broken, Down.
- **Hide, bloat or daemon flesh:** only **solid hits** (beat the number by 3+), **crits, fire and blasts** take a
  stage off it. A plain hit does nothing. (Each entry can name its own exceptions: blessed and force weapons
  against daemons.) **Shots at a big one get +2** (it's a big target).
- **STR +6 to +10** (d5 + 5). Its blows are **heavy hits** (through carapace; the refractor field takes one on a
  d6 5-6); a crit drops two steps.
- **2 actions a beat:** move and attack, two attacks, or an attack and its special.
- **A ranged threat**, so high ground isn't safe: each entry names it (a spray, a throw, a roar, a lash).
- **Phase 2 at half (Wounded):** it changes: enrages (+2 on its attacks), or gains the trick its entry names.
- **Never alone:** it comes with its swarm, handlers or brood.

## Human boss template (a commander)

A named special character: a Major, a cult leader, a pirate captain, a renegade Inquisitor.

- **An honour guard of 4-6** of his best (bodyguards and specialists), **armour one step better** than the rest
  of his force.
- **He takes the best of everything rolled for his team**: the best gun, the best armour, the best blade,
  **plus one signature piece** (a rare: `python3 wh40k_gear/dice.py rare weapons`, or a relic with a story).
- **STR and DEX +6 to +10 each** (d5 + 5 each, rolled separately).
- **+2 health stages** (Fine, Grazed, Bruised, Hurt, Badly hurt, Down) and **Hard to kill** (+1 on his survival d6).
- **2 orders a beat** to his people (each +2, acting first).
- **Bodyguards cover him:** a guard within reach takes a hit meant for him on a **d6 4-6**.
- **Falls back at Badly hurt** to fight another day, unless he's cornered, or his faction never runs (**the
  Moebian 6th's bosses fight to the end**). A boss who gets away comes back.
- He stays behind cover and his guard (codex: leaders don't hand themselves to the Light).

## The roster (40k lore)

### Nurgle (the Moebian 6th and other plague cults)

- **Plague Ogryn** (met at Fourteen, day 47). A renegade Ogryn swollen with the rot, chained and starved, set
  loose. **Charge** (once a fight: knocks the target flat and anyone right behind; a DEX dodge to get clear).
  **Ranged threat:** tears up and **throws rubble or a body** (~15 m; a hit knocks flat). **Phase 2:** its belly
  splits: **bile spray** (~5 m cone, CON save vs 13 or the rot). **Down:** it bursts (everyone within ~3 m, CON
  vs 13). With: a walker swarm or its herders.
- **Chaos Spawn.** What's left of someone the gods loved too much: a heaving mass of flesh, mouths, tentacles and
  eyes. **Roll a d6 mutation when it shows** (1 acid blood: a hit on it in melee splashes the attacker, CON vs 13;
  2 extra maws: +1 attack a beat; 3 hide like plate: only crits and blasts count until phase 2; 4 tentacles:
  reach ~6 m and drag; 5 regrows a stage each beat it isn't hit by fire; 6 roll twice). **Ranged threat:** lashing
  tentacles (~6 m, drag the target in). **Phase 2:** it splits off a **spawnling** (a 2-stage spawn of its own).
  With: whatever made it (a cult, a sorcerer).
- **Beast of Nurgle.** A daemon: a huge, slug-bodied, idiotically affectionate thing that wants to play, and its
  play kills. **Daemon flesh:** blessed and force weapons count every hit; everything else, solid hits only.
  **Slime trail:** the ground it crosses is fouled (anyone crossing, CON vs 13 or sickened; -2 on movement).
  **Ranged threat:** it **lollops** (a bounding lunge, ~15 m, knocks flat). **Phase 2:** it **regrows a stage a
  beat** unless burned or blessed. With: a mob of nurglings or a plague cult.
- **Foetid Bloat-drone.** A Death Guard daemon engine: a rotting, buzzing, flying hulk on rusted rotors.
  **Airborne** (shots at it -3). **Ranged threat:** **plaguespitter** (a ~10 m cone of corrosive filth: a heavy
  hit, and CON vs 13). **Phase 2:** it drops low and **rams** (knocks flat). With: Death Guard or a plague cult.
- **Plague Marine (Death Guard), the apex.** A Heretic Astartes of the Plague God: two and a half metres of
  rotting power armour, bolter and plague knife. **Power armour:** only heavy hits get through (plasma, melta,
  power, chain, krak, heavy weapons) and las and stub never do. **Disgustingly resilient:** a stage that would
  come off is ignored on a d6 5-6. **Ranged threat:** **bolter** (a string of 3, recoil 2, heavy hits) and a
  **blight grenade**. **Phase 2:** the stench: everyone within ~5 m -1. Rare: a campaign-level enemy.

### Chaos cults (any god)

- **Daemonhost.** A human body bound around a daemon by a cult or a renegade Inquisitor; it floats, burns cold,
  and whispers. **Daemon flesh** (as the Beast). **Ranged threat:** **warp blast** (~30 m, a heavy hit) or
  **hurls** someone (~10 m, knocks flat). **Phase 2:** its bindings slip: **2 extra actions this beat**, then it
  may turn on its own (d6 1-2). With: its binder.
- **Cult champion** (a human boss). The god's chosen: a Blood Pact butcher-lord, a Tzeentchian sorcerer-adept, a
  Volscani cataphract commander. Human boss template, plus **one gift of his god** (Khorne: +2 in melee and no
  pain until Down; Tzeentch: a warp blast as the Daemonhost; Slaanesh: +2 dodging; Nurgle: disgustingly
  resilient as the Plague Marine).
- **Mutant rager.** A cult's war-beast: a hulking mutant packed with stimms and rage. Monster template, **no
  ranged threat but a leap** (~10 m into melee); **phase 2:** berserk (attacks the nearest, friend or foe, +2).

### Raiders

- **Raider warlord** (a human boss) **and his brute**: the warlord's honour guard is his gang; the **mutant brute**
  is a monster boss on a chain (monster template, ranged threat: thrown wreckage ~15 m).
- **Scavvy king.** A mutant overlord of the underhive and the wastes: human boss template, **plague-ridden**
  (bites carry the rot) and a **horde of plague zombies** (walkers, poor numbers) driven ahead of him.
- **Ambull.** A burrowing death-world predator the size of a groundcar: monster template; **comes up out of the
  ground** (surprise on whoever it surfaces under); **ranged threat:** none, but it **tunnels** (gone a beat,
  then surfaces ~20 m away). Raiders keep them in pits.

### Pirates

- **Reaver captain** (a human boss). A void-pirate lord with a stolen signature piece and an honour guard of
  boarders. **Ranged threat:** his ship (a boarding torpedo or a gunship on call, once a fight).
- **Boarding servitor.** A pirate's combat servitor: a lobotomised hulk of armour and heavy weapons. Monster
  template, **no fear**, **ranged threat:** its arm-mounted heavy stubber or flamer; **phase 2:** its limiter
  burns out: it attacks anything that moves.

### Traitor elites

- **Traitor storm trooper captain** (a human boss). The best of the best: hot-shot and plasma, a Tempestus
  honour guard, carapace a step better (power-armoured plates).
- **Renegade Inquisitor** (a human boss) **with a Daemonhost**: the classic pair; the second boss comes with him
  whether the d6 says so or not.
- **Renegade Astartes, the apex.** A Chaos Space Marine (any god): as the Plague Marine, with his god's gift.

### Commoners

- **Militia captain** (a human boss, lightly): the honour guard is his best men in whatever they have; **no
  signature piece** unless the story gives one; **he can be talked down** like his people.

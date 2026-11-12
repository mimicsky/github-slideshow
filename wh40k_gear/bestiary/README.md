# Bestiary: table of contents

Enemy forces the Light can meet. For the DM: read this index; open a team's entry
when it shows up.

**How enemies are rolled** (`../roll_enemy.py TYPE COUNT [WEALTH] [GOD]`; roll the faction's wealth first with `../roll_enemy.py wealth TYPE`, codex Part 8): every group
is one of six **basic types** (cultists, raiders, pirates, traitor soldiers,
traitor elites, and commoners: a militia of ordinary people, with no named teams). Before the fight, **2d20 added**: **2-30** a basic group, **31-40** a
**named special team** of that type (below), about 1 fight in 7. A special team
gets **+5 STR and DEX levels** (+1 on other rolls), **armour one step better**, **+3 to their
better-armed d20**, and half their guns are the team's favoured weapons. Their
look and tactics are in their entry, and the DM plays them that way. Every enemy
also rolls its own STR and DEX (ranges in `DND_CODEX.md` Part 8); no per-book bonuses.

**Team units (set by the player, day 47).** A special team has its own units. **When one of its members rolls grunt, roll a d6: 1-2 makes them one of the team's units instead** (listed in `factions.py` and in the team's entry); **3-6 a regular grunt.** The roller does it. A team with no units listed yet gets its list the first time it shows up. **When the story already says who they are** (the 6th at a place of theirs), force the team: `../roll_enemy.py TYPE COUNT [WEALTH] team=moebian`.

**Special teams fit the mission (set by the player, day 47).** When the mission's enemy is a named team (the 6th on Gallowmere), **every group of theirs rolls as that team** (`team=NAME`: its bonuses and its units), never a random one. When the 2d20 rolls a special team that doesn't fit the mission (e.g. the Urdeshi Deserter Storm Troops turning up in the 6th's own compound, as happened at Fourteen), **reroll the pick until it fits** (same type, and for cultists the same god), **or make a story of it** (never just ignore the tag). **A story** means the team is there for a reason, written in the DM notes: a rival warband hunting the main faction (Khorne berserkers in a Nurgle sector, come to take skulls off the plague-cult), mercenaries someone hired, a schism inside the faction, an ally of convenience, a third party with its own aims. **The DM's call; if unsure, a d6: 1-3 reroll, 4-6 a story.** A mission can also be built around a special team from the start, because of what the mission is.

## [Enemy roles: personalities and tendencies](roles.md)

Every grunt and specialist role, how it tends to think and fight, and its rules.
The DM decides; these are tendencies.

**Specialist kits (set by the player, day 47): a coin flip.** **Preset:** the role's own kit from the roller's list.
**Random:** a gun and a melee weapon from the type's lists, plus the role's tool if it has one (a medic's med-kit, a
jumper's pack); he still fights as his role. Roles that are their kit (Ogryn, herder, heavy team, mortar team, bomb
zealot, psyker, beast handler, mutant charger) always take the preset. The roller prints PRESET or RANDOM KIT.

## [Mini bosses](bosses.md)

Mini bosses (renamed day 47; real bosses not built yet): monster mini bosses (bullet sponges: 8 stages, 2 actions, a ranged threat, a phase 2) and human bosses (commanders with an honour guard, the best kit, STR and DEX +6 to +10), a roster from 40k lore, and the two-boss roll (set by the player, day 47).

## [Enemy attachments](../catalogue/attachments.md#enemy-attachments)

Each enemy weapon (guns and melee) rolls a d100 for an attachment or special ammo by the faction's wealth (poor 20% up to wealthy 50%; special teams +10%; a hit rolls again; it must fit; custom builds roll by rarity, as the enemy smith's own version; `roll_enemy.py` rolls them from `attachments.py`) (set by the player, day 47).

## [Vehicles](vehicles.md)

Light vehicles, APCs and tanks: when they show up (by mission type and wealth), hull points, what gets through their armour, the damage d6, and what the Light can answer them with (set by the player, day 47).

## [Commoners (militia)](commoners.md)

Ordinary people under arms: Poor, Steady, or Good in rich places. Brittle; can be talked down.

## [Cultists](cultists.md)

- [The Moebian 6th](cultists.md#the-moebian-6th) (Nurgle)
- [The Volscani Cataphracts](cultists.md#the-volscani-cataphracts) (Undivided)
- [The Blood Pact](cultists.md#the-blood-pact) (Khorne)
- [The Sons of Sek](cultists.md#the-sons-of-sek) (Khorne)
- [The Prospero Spireguard](cultists.md#the-prospero-spireguard) (Tzeentch)
- [The Adorned](cultists.md#the-adorned) (Slaanesh)
- [The Cohort of the Enraptured](cultists.md#the-cohort-of-the-enraptured) (Slaanesh)

## [Traitor soldiers](traitors.md)

- [The Vraksian Renegade Militia](traitors.md#the-vraksian-renegade-militia)
- [The Renegade 14th Volpone 'Bluebloods'](traitors.md#the-renegade-14th-volpone-bluebloods)
- [The Urdeshi Deserter Storm Troops](traitors.md#the-urdeshi-deserter-storm-troops)

## [Pirates](pirates.md)

- [Renegade Privateers](pirates.md#renegade-privateers)
- [The Kanak Skull Takers (renegade)](pirates.md#the-kanak-skull-takers-renegade)
- [The Savlar Chem-Dog deserters](pirates.md#the-savlar-chem-dog-deserters)
- [Red Corsair reavers](pirates.md#red-corsair-reavers)

## [Raiders](raiders.md)

- [Renegade Void-Raiders](raiders.md#renegade-void-raiders)
- [Crangor's Buccaneers](raiders.md#crangors-buccaneers)
- [The Fallen Maelstrom Wardens](raiders.md#the-fallen-maelstrom-wardens)
- [Chaos Cultist Scavengers](raiders.md#chaos-cultist-scavengers)

## [Traitor elites](traitor-elites.md)

- [The Lost 88th Cadian (fallen company)](traitor-elites.md#the-lost-88th-cadian-fallen-company)
- [The Unburied, Death Korps of Krieg (fallen company)](traitor-elites.md#the-unburied-death-korps-of-krieg-fallen-company)
- [The Sand-Ghosts, Tallarn (fallen company)](traitor-elites.md#the-sand-ghosts-tallarn-fallen-company)
- [The Disowned, Vostroyan Firstborn (fallen company)](traitor-elites.md#the-disowned-vostroyan-firstborn-fallen-company)
- [The Green Hell deserters, Catachan (fallen company)](traitor-elites.md#the-green-hell-deserters-catachan-fallen-company)
- [The Broken Badge, renegade Arbites (fallen precinct)](traitor-elites.md#the-broken-badge-renegade-arbites-fallen-precinct)

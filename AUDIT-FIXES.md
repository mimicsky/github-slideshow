# Audit fixes: Ash on Ostrava + wh40k_gear (day 47)

A list of every problem found in the audit, what the player decided, and what to change.
Base: branch `claude/ash-ostrava-campaign-closeout-ma000x`.
All of **Part A** and **Part B** is already done on branch `claude/intelligent-mayer-ccf8rv`. To bring it in:
- **Easiest:** merge or cherry-pick that branch's commits.
- **By hand:** apply each change below.

**Part C** lists problems found but **not fixed yet**. **Part D** lists new item ideas (optional).

**If you edit the shop list by hand:** `wh40k_gear/pools.json` no longer matches `build_pools.py`. Running `python3 build_pools.py` reorders `pools.json` and drops ~250 lines from `enemies.json`. **Don't regenerate.** Edit the item names in both `build_pools.py` and `pools.json`.

---

## Part A: Gear catalogue (`wh40k_gear/catalogue/`)

| # | File | Problem | Change (player's call) |
| --- | --- | --- | --- |
| A1 | `stub.md`, Stub and autogun rounds table, **Flat-tip** row | Said "(Armour: every 3 drop a step)"; the codex changed wear-down to every 6 on day 47 | Now "(Armour, wear-down: every 6 drop a step). **Ceramite-forged and power armour: no wear-down at all** (stub is too weak to matter: codex, Armour)". **Flat-tip must never wear down power armour.** |
| A2 | `stub.md`: Shredder autopistol, Hammerfall auto-revolver, Hunting rifle 'Kasr Stag' | Said autogun rounds go "through carapace on a solid hit"; the codex says carapace shrugs autoguns and stub | Changed to "carapace shrugs it; a crit gets through" (the Shredder also notes "AP and CAP loads do better"). Rule: stub and auto only get through up to a set armour; **crits get through one more armour step** |
| A3 | `explosives.md`, Grenades: standard types, **Krak** | Said it "goes through carapace"; the codex says krak gets through power armour | Now "goes through **power armour** (and anything lighter; codex, Armour)" |
| A4 | `kit.md`, Gun-skull, and `drugs.md`, "Servo-skull, gun" | The same item twice: `kit.md` fires at d20+3, `drugs.md` at +0 | **Keep the kit.md Gun-skull (+3).** The drugs.md entry now points to it. The `Servo-skull, gun (built-in laspistol)` row is removed from `build_pools.py` and `pools.json` (the burner skull stays) |
| A5 | `kit.md`, Extended magazine kits + the attachment list's "Extended magazine" | Two prices (1.5 TV and 1 TV); the bolt/plasma version was cheaper than a tuned plasma cell | Both are now **uncommon, 1.5 TV, autogun and stub only**, +50% rounds. Las uses the extended las pack; plasma uses the tuned cell. Pools: renamed `Extended magazine kit, autogun or stub (+50% rounds)` and removed the bolt/plasma kit row |
| A6 | `kit.md`, Power weapon tuning kit | Gave "through power armour on any hit", which power weapons already have, so it did nothing | Now **+1 to parry with the tuned weapon, and its power cell lasts twice as long (60 power-mode swings, not 30)**. Pools name updated |
| A7 | `bows.md` + `melee.md` | "Kasr Talon" was the name of both a compound bow and a power claw | **Bow renamed 'Kasr Kestrel'** (heading, entry, README link and anchor, build_pools, pools.json). The power claw keeps Talon |
| A8 | `heavy.md`, Las-cannon, medium tripod emplacement (35 TV) | Weaker than the smaller man-portable lascannon | Rewritten (pools name updated too): <ul><li>Man-portable lascannon punch: through anything a person wears, APCs, and tanks from the front</li><li>**+2 on every shot** (steady mount); can't move once set up</li><li>**One beam a beat** on a coupling or battery pack; every other beat on a plain pack</li></ul> |
| A9 | `assassinorum.md`, Nemesii blade (legendary, 150 TV) | Weaker than a 28 TV power falchion | **Buffed** (pools name updated): <ul><li>+2 to strike first and to parry</li><li>Light blade, chains of 4</li><li>Power edge (through power armour); **a solid hit drops two steps**</li><li>**Can't be disarmed**</li><li>A parry won by 5+ gives a free riposte</li></ul> |
| A10 | `melee.md`, Mono-knife (3 TV) | Worse than the 2 TV injector stiletto | Now **through carapace on a solid hit, heavy carapace on a raw 19-20**. Also updated on Brenner's row of the campaign sheet |
| A11 | `kit.md`, attachment list, Custom barrel (1.5 TV) | Did the 10 TV range-finder's job (+1 past 30 m), plus more, with no downside | Now **+1 on aimed shots only**. Pools name updated |
| A12 | `kit.md`, Forged shield (6 TV) | Worse than the 1.5 TV scrap cogitator shield | Added: **no DEX penalty** (balanced), and it **doesn't break from heavy hits** (only Field Burst or melta ruins it). Also fixed its escaped apostrophe |
| A13 | `stub.md`, Needle rifle, Needle pistol, Needle darts | The rifle was weaker than the pistol and had no save number | **The save lives on the dart, not the gun.** <ul><li>Standard dart: CON 15 or Down (paralysed, alive)</li><li>Rifle: **effective to ~150 m, +2 aimed, +1 more past ~30 m**; a hit drops a step plus the dart's toxin</li><li>Pistol and darts text updated to match; pools name updated</li></ul> |
| A14 | `kit.md`, Catachan shotgun | Compared to a real-world "Baikal MP-155"; "breach" typo | Now "it fires as fast as the trigger can be pulled"; "breach" changed to **breech** |
| A15 | `stub.md`, Macragge service pistol | Real-world calibre "M.45" | Now "**Heavy stub rounds**". Pools name updated |
| A16 | `explosives.md`, Sticky vortex grenade | The player's own design, but in 40k a vortex grenade is a matter-erasing warp hole | **Renamed "Sticky warp-shock grenade (Mechanicus)"**, with the same rules (heading, README link and anchor, build_pools, pools.json) |
| A17 | `explosives.md`, Mining charges; Six Bells | No price | Mining charges **uncommon, 2 TV each** (Munitorum, mining guilds, black market; added to pools as `Mining charge`, U, MBF, 2). Six Bells **rare, ~12 TV** (Munitorum, Free Traders; not added to pools: it's Hollis's) |
| A18 | `heavy.md`, Valkyrie bolt-rocket pods | No aiming or reload rules | Added (DM default): the pilot rolls d20 + DEX like a grenade throw; a miss by 1-2 still bursts close at half effect. **Reload: 6 rockets, 12 TV**; takes a landing and ~10 minutes |
| A19 | `melee.md`, Great chain axe | Gets through power armour on a raw 18+; the codex says chain never gets through power armour | **Kept as-is (player's call).** No change |

## Part B: Campaign files (`campaigns/ash-on-ostrava/`)

| # | File | Problem | Change |
| --- | --- | --- | --- |
| B1 | `fight-card.md`, 12. Will checks | Old bands: 0-2 / 5-10 / 10-15 / 15-20% | Now the codex bands: **1-2 / 3-5 / 6-8 / 9-10%** |
| B2 | `fight-card.md` §10 and `README.md` (knife bouts) | Tamsin's knife-bout bonus was +11 (7 DEX) | **+12** (8 DEX + 4 prof; DEX +8 since day 38) |
| B3 | `dm-notes.md`, IX assault, before "Fight checklist, before beat 5" | Beats 1-4 used ally bonuses that were too high | Added an **AUDIT** note: <ul><li>Bonus used vs correct: Brenner beat 1 +10 vs +6; Sorel beat 1 +11 vs +4; Nessa beat 1 +12 vs +8; Tavi beat 2 +9 vs +5; Kell beats 1 and 3 +9 vs +5</li><li>Cause: the checklist was skipped. It wasn't orders: only Brenner, Tey, Corvane, Varga and Hollis had them, and Kell's +1 was already counted</li><li>**Results stand as played**</li></ul> |
| B4 | `ash-on-ostrava-campaign-sheet.md`, before "The Light's standing modifiers" | Isk's +2 long-shot specialty and Varga's +2 aimed specialty kept being dropped | Added **Fixed shooting lines** (add Kell +1 and orders +2 on top): <ul><li>**Isk, Patience, aimed:** +9 inside ~30 m, **+13 past it** (with the Scion helmet)</li><li>**Varga, Mercy, aimed:** +12 inside ~30 m, +11 past it</li><li>**Varga, Mercy, not aimed:** +5 inside ~30 m, +6 past it; airborne -1</li></ul> |
| B5 | Sheet, Nessa's row | The black-tip save was rolled at 15 (it's 17), and her count wasn't reduced | Black-tip **6** (2 fired at IX). Use **17** from now on |
| B6 | Sheet, Sallow's Bag | 10 stimms | **8** (one each on the Major and Vosk, day 47) |
| B7 | Sheet, Tavi's row | Demo satchel still listed | Struck: **spent on Fourteen's barns, day 47**; the detonator kept |
| B8 | Sheet, Kell's and Isk's rows | The Scion helmets issued on day 47 weren't recorded | Both now wear a **Scion-pattern helmet** (+2 Perception, +1 shooting, built-in rebreather; pict lens moved onto it) |
| B9 | `inventory.md`, the hostel roof's rocket tube | Still said 3 rockets | **0 rockets: all 3 fired by Hollis at IX**; the empty tube is container stock |
| B10 | `inventory.md`, Complex XIV, "Still there" | "~140 walkers behind the vault doors", but the vaults were cleared and burned | That phrase deleted |
| B11 | Sheet, "Where we stopped" and the "Current state" heading | Stuck at dawn of day 46 / "day 41" | Now **day 47, ~1830, Kettle Ford** (H-hour 1900, four cells, 3 of 35 down, Wil hidden, house 3), plus a short day-47 summary; heading now "Current state (day 47)" |
| B12 | Sheet, Coin | Still 7,419 Thrones | **14,228** (+6,809: IX 983, Fourteen's bodies 3,676, main hall 90, pay strongbox 2,000, final search 60) |
| B13 | Sheet, Prisoners | "Prisoners (now, day 37)", with Thask and Ilsabet aboard | New "Prisoners (now, day 47)": <ul><li>**Cell 1:** Mordane, the plague-priest, Kreel, Quint</li><li>**Cell 2:** Vosk (in the medicae, restrained), Drayle, IX's preacher, Bell man C</li><li>**The hold:** ~25-30 more (worth a head count)</li></ul>The old list is kept, labelled history |
| B14 | `world.md`, the Pell, Ilsabet and Maren rows; the Gallowmere target row | Old locations; Gallowmere still "Rumoured (8)" | <ul><li>Pell and Maren: in Kesh's house on the Rest</li><li>Ilsabet: handed to Kesh, day 41</li><li>Gallowmere: **Active**</li><li>Added a **Gallowmere (days 46-47)** NPC table: Corrow, Quint, Mordane, Vosk, Varrow, Vael</li></ul> |
| B15 | Ammo and cells (Vigil, Last Word, power cells, Kell's plasma cell) | Looked stale | **No change, by design:** Ollin rekits everything rechargeable after each fight, so the next fight starts full |

## Part C: Found but NOT fixed yet

**Catalogue**
1. **Heavy stub punch is inconsistent.**
   - Macragge pistol (`stub.md`): through carapace on a solid hit.
   - Orlock heavy SMG: through carapace only on a raw 19-20.
   - Pick one rule.
2. **Needlespine blaster** (`assassinorum.md`, legendary, 140 TV) is about a needle rifle +2.
3. **Needle SMG** (`stub.md`) is legendary but only ~40 TV. It's Assassinorum gear but not filed in `assassinorum.md`.
4. **Psyker overload grenade** (`explosives.md`): friendly psykers roll d20 + CON, enemies a flat d20. The codex says enemies roll CON saves as d20 + STR bonus.
5. **Psykana force stave** (`melee.md`) says Perils "1-2 becomes 1". The codex baseline is 1-3 (so: "1-3 becomes 1-2").
6. **Kasr Rain** (`las.md`) is called "the most efficient las pack made" at 100 shots, but the eco pack and the backpack cell hold 120.
7. `heretic.md`: the "As loot: useless to anyone but a psyker…" lines sit under the daemons paragraph; they belong under the Chaos psyker staff.
8. Missing stats:
   - **No chain class (light, medium or heavy):** Power falchion and Omnissian power sword (`melee.md`).
   - **No warp-fire effect:** Blaze force sword (`melee.md`).
   - **No shot count:** Sterl las-SMG (`las.md`).
9. `kit.md` still has escaped apostrophes (`defender\'s`) on the Boarding shield, Storm shield, Slab shield, Makeshift shield and Improvised shield entries.
10. **Arbitrator shield** says "+2 to block"; every other shield says "block or parry".
11. Abilities lines sit sometimes before the entry text and sometimes after. Pick one.
12. `catalogue/README.md`, "Heavy and vehicle weapons" section, lists flamer fuels, bolt rounds and stub guns and shells. They belong in their own sections.
13. **Hellstrike missile price:** ~8 TV each in `heavy.md`. The pools' "Valkyrie rocket pod (2 Hellstrike)" costs 20 (that may include the pod).
14. **Gaps, no entries:**
    - Weapons: heavy bolter, man-portable lascannon, missile launcher, autocannon, meltagun, flamer, heavy flamer (all in the pools)
    - Armour: flak, reinforced flak, carapace, heavy carapace, ceramite-forged
    - Kit: rebreather, gas mask, void-suit, refractor field, conversion field, medkit, vox-caster, magnoculars, chameleoline cloak, grapnel
    - Explosives: melta bombs, demo charges
    - Kits: a hot-shot conversion kit entry
    - Nothing xenos at all

**Campaign**
1. `day-log.md`: day 47 is filed under `## Day 46`. Add a `## Day 47` heading.
2. `dm-notes.md`: "Live now" still points at the Torvane's Mart mission.
3. Sheet, Health block: still from day 38. Dace was Hurt at Quay 4 on day 47.
4. Sheet, Owed list, stale:
   - Ferro's warding rite (done day 44)
   - Brenner's mat time (both "postponed" and "DONE")
   - Shameholder's first cut (kept day 47; "both their rages sated" is still owed)
5. `inventory.md`:
   - Varga's lift pack "2 left" (refilled)
   - Isk "flies the stolen jump pack" (he has the IX one now)
   - The hand flamer, Mezoa long-las and shotlas marked "no catalogue entry" (entries exist)
   - ~24 crate frags (a box of 12 went to Tavi's mines)
   - Hollis handed 2 spec flashes he doesn't have
6. Tey's pistol focus: probably due +3 (one drill day a day from day 36 puts the next +1 around day 45). Confirm the drill days.

## Part D: New item ideas (optional; the player decides)

Written in the catalogue's style (TV prices, steps, chains, solid hits).

**Weapons**
- **Purgation flamer, 'Kasr Cleanse' pattern** (rare, ~12 TV):
  - Cone ~8 m, no roll to hit; DEX 13 for half.
  - Poxwalkers who fail can't get back up.
  - Heat 1 a burst, vent at 3; 6 bursts a tank.
- **Meltagun, 'Kasr Ember' pattern** (rare, ~25 TV):
  - Inside ~10 m: through anything. Past 10 m: carapace.
  - 4 shots a canister.
- **Rad-carbine, Skitarii pattern** (rare, ~20 TV):
  - A hit: CON 14 or -1 on all rolls (stacks to -3).
  - Nurgle-touched targets take -2 on the save.
  - Chains of 2.
- **Arc pistol** (uncommon, ~10 TV):
  - Hits on machines, servitors and power packs drop two steps.
  - A hit stops a refractor field for a beat.
- **Bolt pistol with Kraken rounds** (rare, ~18 TV):
  - Strings of 2; 8 a magazine.
  - Kraken: carapace on any hit, power armour on a solid hit.
- **Sanctified chainsword, 'Blessed Edge' pattern** (uncommon, ~8 TV):
  - Ignores Nurgle daemons' and blessed cultists' shrug-off.
  - The oil lasts one fight.
- **Grain-hook, 'Gallowmere' pattern** (common, 0.3 TV):
  - Two-handed, chains of 2.
  - A hit: STR contest to drag the target 2 m or knock them down.
- **Shuriken pistol** (xenos, epic, ~45 TV; off a corpse or from Drex's *Sweet Abundance*):
  - Strings of 3, silent, carapace on a solid hit.
  - No reloads but scavenged discs.

**Gear**
- **Medicae kit** (3 TV, 10 uses): brings a Hurt ally back a step outside a fight; +2 on a plague or fester save.
- **Krieg sealed rebreather** (2 TV): immune to spores and gas for 1 hour a filter; -2 to talk or persuade.
- **Chameleoline cloak** (12 TV): +3 to hide when still, +1 moving.
- **Melta bomb** (6 TV): takes a beat to stick on; then through anything.
- **Geller ward-charm** (Ferro makes one a week): +2 on saves against Nurgle mind effects; cracks on a raw 1.
- **Plague-scrubber field kit** (4 TV): bags and proves tainted grain (Silo Row 3).

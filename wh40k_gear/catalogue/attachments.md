# Attachments

The Light's attachment sheet (set by the player, Ash on Ostrava day 47). Three parts:
1. **[Fitted and working](#fitted-and-working-every-attachment)** and **[Enemy attachments](#enemy-attachments):** when one counts, and how enemies roll them.
2. **[The rollable list](#the-rollable-list):** every traditional attachment and part, for the roller (step 3: being built).
3. **[Custom builds](#custom-builds):** every part the Light designed and built themselves. **Custom, not traditional: no
   trader carries these.**

**The paper trail:** traditional attachments keep their full entries in [kit.md](kit.md) (and [las.md](las.md),
[plasma.md](plasma.md)); custom builds are written here in full, each gun linked to the schematic that made it, and
**every schematic on the campaign's [`schematics.md`](../../campaigns/ash-on-ostrava/schematics.md) links back here.**

## Fitted and working (every attachment)

**An attachment only does anything while it's fully fitted and working** (the player, day 47). Half on, loose, broken
or still in a pouch, it gives nothing. **Fitting or taking off a quick one in a fight (a bayonet) takes the beat's
move;** everything else is fitted at the bench (an hour or two: [kit.md](kit.md#pistol-and-gun-attachments-player-designs-ash-on-ostrava-session-10)).
Tamsin's scorched-tip knife rides on his belt and only gives Vigil a bayonet once it's fixed on the lug.

## Enemy attachments

**Set by the player, day 47.** When an enemy is rolled, **each of his guns rolls a d100 for an attachment,** by his
faction's wealth:

| Wealth | Chance of an attachment |
| --- | --- |
| Poor | 20% |
| Steady | 25% |
| Good | 30% |
| Rich | 40% |
| Wealthy | 50% |

- **Special teams +10%.**
- **On a hit, roll again at the same chance for another;** keep going until a roll misses.
- **It has to fit the gun:** the right slot and the right kind of gun (no silencer on a las, one optic per gun). If it
  doesn't fit, roll again on the list.
- **What a gun comes with doesn't count** (a kit's listed scope, a gun's built-in parts): the roll only adds.
- **Custom builds roll too, by their rarity** (the player, day 47): **simple fixes are common** (swapped springs, cut
  barrels, grips, slings, stocks), **real bench work is uncommon** (a new motor, a twin tray, a matched cell), and
  **the interesting ones are rare** (new mechanisms and modes: the Super V, an energy selector, a charge trigger, a
  heartbeat scanner). Rarity follows the faction's wealth as for any loot (`roll_enemy.py`: rich C40/U45/R15,
  wealthy C25/U50/R25). **An enemy's custom part is his own smith's version, not Tamsin's design:** no trader carries
  it, someone built it (a story hook). Numbers written for one of the Light (Tamsin's +1 string) use the base.
- The DM uses what's rolled in the fight like any other kit, and it's there to loot afterwards.

## The rollable list

*(Step 3, next: every traditional attachment and schematic part with its slot and which guns it fits, wired into
`roll_enemy.py`.)*

## Custom builds

**Custom, not traditional: no trader carries these.** Designed by Tamsin (or the Light) and built by the Light's own
smiths (Dace, Ferro-Ashe, Ottrick before them) from a schematic. They're never sold or found in a shop:
**no trader carries them.** Enemies roll their own smiths' versions by rarity ([Enemy attachments](#enemy-attachments)). **The rulings are the schematics' own** (with the day-36 cleanup); the full sheet, costs and
Tamsin's notes stay on [`schematics.md`](../../campaigns/ash-on-ostrava/schematics.md). Each gun says whether it's built yet; parts on paper aren't
on the gun until the build is done. **Traditional parts** on the same gun (bought, with catalogue entries) are named
under each gun, not repeated here.


### Stinger (Tamsin)

**Built** (Dace, done day 27). Source: [inventory.md, Tamsin's weapons](../../campaigns/ash-on-ostrava/inventory.md#tamsins-weapons-in-detail-history-blessings-spirits).

- **New bolt and heavy buffer spring** (action; **common**) *(Custom, not traditional: no trader carries this.)*: the Hornet **jams only from the 25th straight round** (a stock Hornet jams from the 13th).
- **New frame with top and under rails** (frame; **common**) *(Custom, not traditional: no trader carries this.)*: 1/2 plasteel; gives the Hornet **an optic slot on top and an under-barrel slot below**. No rule of its own.
- *Traditional parts on it:* custom barrel, hair trigger, pressure-pin safety (kit.md).

### Shameholder's overdrive (Tamsin)

**Built** (Ottrick, season one). Source: [inventory.md, Tamsin's weapons](../../campaigns/ash-on-ostrava/inventory.md#tamsins-weapons-in-detail-history-blessings-spirits).

- **Overdrive** (melee motor; **rare**) *(Custom, not traditional: no trader carries this.)*: **once a mission, ~30 s:** armour counts **one step lighter** against it and **advantage in mob pushes**; then it can't be used again that fight; **a natural 1 while it's running burns out the motor.**

### Dace's autopistol (schematic 1)

On paper (8th in the build order). Source: [schematic 1](../../campaigns/ash-on-ostrava/schematics.md#schematic-1-daces-autopistol-rebuilt).

- **Heavy ergonomic tower grip** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: soaks the faster slide's kick: **recoil stays 0.**
- **Lightened slide** (action; **common**) *(Custom, not traditional: no trader carries this.)*: faster cycling: **strings up to 5.**
- **Three-way selector with the rapid feeder** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **not drop-prone. SAFE / BURST** (strings up to 5, normal chain bonuses) **/ AUTO** (strings **up to 8**, the fast-gun rule: **no hit bonuses in the chain, misses still -1**; **from the 13th straight round of continuous fire, a shot die of 1-3 jams**).
- **Top and bottom rails** (frame; **common**) *(Custom, not traditional: no trader carries this.)*: an optic slot on top, an under-barrel slot below. No rule of its own.
- *Traditional parts on it:* pistol drum (kit.md).

### Hollis's hand flamer (schematic 2)

On paper (15th). Source: [schematic 2](../../campaigns/ash-on-ostrava/schematics.md#schematic-2-holliss-hand-flamer-rebuilt).

- **Long flamer barrel** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: reach **~10 m** (not ~6); rides a chest or thigh rig: **-1 on quick-draws.**
- **Tuned igniter** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: a **wider spread:** the gout opens to **~2 m across** at the far end and catches anyone standing close together.
- **Heavy-burst switch** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **one pull spends 2 bursts:** everyone it hits **drops one extra step;** the igniter needs **a beat to clear** (no flame the next beat).
- **Dual angled canister cradle** (magazine; **uncommon**) *(Custom, not traditional: no trader carries this.)*: two canisters: **8 bursts before a reload.**

### Morcant's heavy stubber (schematic 3)

On paper (14th). Source: [schematic 3](../../campaigns/ash-on-ostrava/schematics.md#schematic-3-morcants-heavy-stubber-rebuilt).

- **Heavy grip and recoil stock** (stock and grip; **common**) *(Custom, not traditional: no trader carries this.)*: **recoil 0 braced.**
- **Angled side grip** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: **recoil 1 on the move.**
- **Open-bolt feeder** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: goes **Dirty after ~60 shots,** not ~30, and **a Dirty stubber doesn't jam** (Neglected still does).
- **Light reciprocating parts and plasteel spring** (action; **common**) *(Custom, not traditional: no trader carries this.)*: **NORMAL: strings up to 10,** no hit bonuses in the string.
- **Rate selector (HIGH)** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: his choice each beat: **HIGH: strings up to 12;** on HIGH it goes **Dirty at ~30,** a **Dirty gun jams on a natural 1,** and **recoil is 1 braced, 2 on the move** (0 on the tripod).
- **Traverse tripod with spade grips** (mount; **rare**) *(Custom, not traditional: no trader carries this.)*: setting it up or folding it is **a main thing;** on it he **can't move** and fires with **no recoil.** **ARC fire** (tripod only): spend the string spraying an arc (a doorway, a corridor, a group): everyone in it not behind hard cover takes **-2 on their shots next beat,** and anyone who breaks cover in the arc **draws a free shot.**
- **Twin feed tray** (magazine; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **twice the rounds before a reload;** **two belt types loaded,** switched with a lever; doesn't raise the string.
- **Walking plate** (muzzle; **rare**) *(Custom, not traditional: no trader carries this.)*: **one string spread across up to 3 enemies standing abreast;** the swap's -1 is paid once per extra target; each shot still checks one target; enemies stacked one behind another: only the front one.

### Tey's hellpistol (schematic 4)

On paper (7th). Source: [schematic 4](../../campaigns/ash-on-ostrava/schematics.md#schematic-4-teys-hellpistol-tuned).

- **One-piece crossdraw rig** (holster; **common**) *(Custom, not traditional: no trader carries this.)*: cut down and fitted to his pistols, with a slicked slide: **+1 on quick-draws, both guns;** both pistols and both chain knives out in one motion.
- **Bridged double-cell belt pack** (power pack; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **60 shots** on the same short cable; nothing added to the gun, **no quick-draw penalty.**
- *Traditional parts on it:* hair trigger, pressure-pin safety, laser sight (kit.md).

### Kell's chain axe (schematic 5)

On paper (10th). Source: [schematic 5](../../campaigns/ash-on-ostrava/schematics.md#schematic-5-kells-chain-axe-rebuilt).

- **Better motor** (melee motor; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **crits on 19-20;** **a natural 1 on a swing throws the chain** (a beat to reseat it).
- **Plasteel teeth** (melee teeth; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **through heavy carapace on any hit, ceramite-forged on a solid hit;** power armour still shrugs it; wear-down applies.
- **Curved hardwood grip** (melee grip; **common**) *(Custom, not traditional: no trader carries this.)*: **can't be knocked from his hand by a solid hit** (still drops if he goes Down).
- **Bite switch** (melee motor; **rare**) *(Custom, not traditional: no trader carries this.)*: **BITE: one swing a beat instead of two, but a hit that lands drops one extra step** (a crit in bite: three steps); flipping it is free (before the swing, never during).

### Varga's Mercy (schematic 6)

On paper (5th). Source: [schematic 6](../../campaigns/ash-on-ostrava/schematics.md#schematic-6-vargas-mercy-rebuilt).

- **Long barrel (Mercy)** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: **+1 on aimed shots past ~30 m;** **-1 inside ~5 m.**
- **Custom long-range scope** (optic; **uncommon**) *(Custom, not traditional: no trader carries this.)*: telescopic: **+2 on aimed shots past ~30 m;** stacks with her eye's rangefinder.
- **Dual riser mount, 45° offset** (optic mount; **uncommon**) *(Custom, not traditional: no trader carries this.)*: the long scope on top, the reflex **canted at 45°** beside it: roll the rifle a quarter-turn to switch; **the scope's close-range penalty never applies;** one optic at a time; **-1 on quick-draws.**
- **Energy selector, LIGHT / MED / HEAVY** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **LIGHT:** a normal hellgun. **MED:** 2 shots of pack per shot, **through heavy carapace at any range,** **+1 heat per string.** **HEAVY:** 3 shots of pack per shot, **through ceramite-forged,** **+2 heat per shot.** Heat on Vigil's scale: vent a beat at 3; firing anyway at 3: d20, 1-5 cracks the emitter. Power armour still shrugs it.
- *Traditional parts on it:* reflex sight (kit.md).

### Isk's Patience (schematic 7)

On paper (12th). Source: [schematic 7](../../campaigns/ash-on-ostrava/schematics.md#schematic-7-isks-patience-rebuilt).

- **Custom range-finder** (optic, rides the scope; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **+2 on aimed shots past ~30 m** (the traditional range-finder sight is +1).
- **Heavy long barrel** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: **+2 on aimed shots;** **-1 on hip and snap shots and when firing on the move.**
- **Custom bipod** (under-barrel; **common**) *(Custom, not traditional: no trader carries this.)*: **braced or prone, a miss doesn't cost the chain's -1;** a beat to set up; useless on the move (not the traditional bipod's +2).
- **Intensified laser generator** (action, permanent; **rare**) *(Custom, not traditional: no trader carries this.)*: **every shot draws 3 shots of pack:** **+1 on aimed shots** and **through ceramite-forged at any distance;** **a string of 3 adds 1 heat** (vent at 3); a 30-shot pack gives 10 shots. Power armour still shrugs it.
- *Traditional parts on it:* low-light scope, finer focusing lens (his kit).

### Kell's Officer (schematic 8)

On paper (13th). Source: [schematic 8](../../campaigns/ash-on-ostrava/schematics.md#schematic-8-kells-officer-rebuilt-as-a-close-quarters-carbine).

- **Short barrel (cut down)** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: **+1 inside ~15 m, -1 past ~30 m.**
- **Skeleton grip** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: **no swap penalty;** **-1 on aimed shots past ~30 m.**
- **Stock magazine slot** (stock; **common**) *(Custom, not traditional: no trader carries this.)*: a spare pack rides in the tube stock: **the first reload each fight costs no beat.**
- **Twin-shot switch, SINGLE / TWIN** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **TWIN:** two bolts on one target from one roll: **a hit drops one step, hits one armour tier harder** (heavy carapace at any range) **and counts as 2 hits toward wear-down;** **2 shots of pack per shot.**
- *Traditional parts on it:* reflex sight, hair trigger, pressure-pin safety (kit.md). Also on it: **the Steady blessing** (a rite, not a part: once a mission, reroll one attack with Officer).

### Tavi's Tiny (schematic 9)

On paper (16th). Source: [schematic 9](../../campaigns/ash-on-ostrava/schematics.md#schematic-9-tavis-tiny-rebuilt).

- **Underslung krak launcher** (under-barrel; **rare**) *(Custom, not traditional: no trader carries this.)*: **kraks only:** **one krak a beat (the main thing) out to ~60 m,** rolled like a throw (**d20 + DEX, +2 demolitions** against a door, wall or vehicle); **a beat to reload** from the stock loops; its cover doubles as a foregrip: **no -1 on aimed shots.**
- **Stub barrel** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: **+1 inside ~15 m, -1 past ~30 m.**
- **Heavy shotgun stock with krak loops** (stock; **common**) *(Custom, not traditional: no trader carries this.)*: **+1 on aimed shots, -1 on swapping;** **3 krak loops** strapped flush (a drop spills them, it doesn't set them off).
- *Traditional parts on it:* reflex sight, laser sight (kit.md).

### Sallow's carbine (schematic 10)

**On the bench** (2nd; just started, day 45). Source: [schematic 10](../../campaigns/ash-on-ostrava/schematics.md#schematic-10-sallows-lascarbine-rebuilt-as-a-medics-carbine).

- **Quick-release sling** (sling; **common**) *(Custom, not traditional: no trader carries this.)*: dropping it to hang on her chest, or bringing it back up, **costs nothing.**
- **Hollow skeleton stock (medicine cabinet)** (stock; **common**) *(Custom, not traditional: no trader carries this.)*: **3 compartments: a stimm, a bandage, a tourniquet;** **-1 on aimed shots past ~30 m.**
- **Hollow pop-lock grip** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: one more stimm, bandage or anything that size. With the stock: **she can patch from the gun without the Bag** (a stimm: Down to Hurt; a bandage or tourniquet: Hurt to Fine).
- **Tuned charger** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **strings up to 7,** no extra pack cost; the fast-gun rule: **no hit bonuses in the string,** misses still -1.
- *Traditional parts on it:* holo sight, laser sight (kit.md).

### Corvane's shotlas (schematic 11)

On paper (6th). Source: [schematic 11](../../campaigns/ash-on-ostrava/schematics.md#schematic-11-corvanes-shotlas-rebuilt-as-a-duelling-hand-gun).

- **Ergonomic grip cover (stock removed)** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: a true one-hand gun: **+1 on quick-draws,** fits a holster.
- **Charge trigger and capacitor** (trigger and action; **rare**) *(Custom, not traditional: no trader carries this.)*: a second trigger offset to the side. **Pressing it is his shot for the beat:** it draws **up to 30 shots** from the pack; **next beat he fires one charged bolt** (one roll; -2 past ~15 m still applies). **25-30:** plasma punch (through ceramite; power armour on a solid hit). **20-24:** hellgun punch, through heavy carapace at any range. **10-19:** hellgun punch. **9 or less:** a normal shot. **He must fire it the next beat or the charge bleeds off** (the pack spent anyway). **After any 20+ charge: a vent beat** (no shot; the sword still swings).
- *Traditional parts on it:* laser sight, extended las packs (kit.md, las.md).

### Brenner's Accatran (schematic 12)

On paper (4th). Source: [schematic 12](../../campaigns/ash-on-ostrava/schematics.md#schematic-12-brenners-accatran-rebuilt-as-a-scanner-carbine).

- **Heartbeat scanner on a 90° hinge side rail** (side rail; **rare**) *(Custom, not traditional: no trader carries this.)*: in full at [kit.md, Heartbeat scanner](kit.md#heartbeat-scanner-side-rail-screen): heartbeats only, through walls, **~30 m, sharper the closer;** while it's out and he's watching, **nobody with a heartbeat inside ~30 m can surprise him or his team.**
- *Traditional parts on it:* holo sight, tac stock, ergo foregrip, extended hot-shot packs (kit.md, las.md); **a repeater crystal** (bought, ~8 TV; no catalogue entry yet: **strings up to 7,** the fast-gun rule; goes on the rollable list in step 3).

### Nessa's needle pistol (schematic 13)

On paper (9th). Source: [schematic 13](../../campaigns/ash-on-ostrava/schematics.md#schematic-13-nessas-needle-pistol-tuned).

- **Long needle barrel** (barrel; **common**) *(Custom, not traditional: no trader carries this.)*: reach **~35 m;** **+1 on aimed shots;** **-1 on quick-draws.**
- *Traditional parts on it:* ergo grip sleeve, pistol reflex sight (kit.md); better darts (stub.md).

### Sorel's hellgun (schematic 14)

On paper (3rd). Source: [schematic 14](../../campaigns/ash-on-ostrava/schematics.md#schematic-14-sorels-hellgun-rebuilt-as-a-burst-rifle-plus-a-trackers-helm).

- **Adjustable tube skeleton stock** (stock; **common**) *(Custom, not traditional: no trader carries this.)*: Six Bells' design, bent to his length, **with the notched strip from his old lasgun set in;** rules as the light rifle stock (**+2 on swapping, -1 on aimed shots**).
- **Three-round burst, the only setting** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **his string is 2 bursts;** each burst is one roll, three bolts on one target, 3 shots of pack: **a hit drops one step, hits one armour tier harder** (heavy carapace at any range) **and counts as 3 hits toward wear-down;** normal chain rules across the 2 bursts.
- **Tower grip (burst)** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: holds the burst flat: **the burst takes no penalty.**
- **Helm-linked ammo counter** (helm link; **uncommon**) *(Custom, not traditional: no trader carries this.)*: silent: a tap behind the ear and a glow at the visor's edge: **he always knows his count, never caught dry by surprise.**
- **Blacklight tracking visor** (helm; **rare**) *(Custom, not traditional: no trader carries this.)*: in full at [kit.md, Blacklight tracking visor](kit.md#blacklight-tracking-visor): **+2 on tracking and finding traces** in a ~10 m cone; the emitter glows violet in the dark.
- *Traditional parts on it:* holo sight (kit.md).

### Ferro's Ryza plasma pistol (schematic 15)

**On the bench** (1st; about a third done, day 45). Source: [schematic 15](../../campaigns/ash-on-ostrava/schematics.md#schematic-15-ferros-ryza-plasma-pistol-rebuilt).

- **Third vent channel** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **sheds 1 heat at the end of every beat,** fired or not.
- **Matched fill** (cell; **uncommon**) *(Custom, not traditional: no trader carries this.)*: a tuned plasma cell ([plasma.md](plasma.md#tuned-plasma-cell): 12 shots) matched to Ferro's reclamator: **no misfire,** but **a refill takes 3 days, not 2.**
- **Charge (hold the trigger)** (trigger; **rare**) *(Custom, not traditional: no trader carries this.)*: **quick charge:** the beat's string becomes one charged shot: **a hit drops 1 step, +2 heat, 2 shots of cell.** **Full charge:** hold through a whole beat (no firing), fire the next: **a hit drops 2 steps, +3 heat, 3 shots of cell.** Plasma punch on both; a crit adds a step.
- *Traditional parts on it:* holo sight, laser sight wired in (kit.md); tuned plasma cells (plasma.md).

### Hollis's Six Bells (schematic 16)

On paper (11th). Source: [schematic 16](../../campaigns/ash-on-ostrava/schematics.md#schematic-16-holliss-six-bells-rebuilt).

- **Plasteel spring and gas-piston trigger** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: **2 grenades a string;** the second shot takes **-1 for the kick.**
- **Angled handguard grip (fitted)** (grip; **common**) *(Custom, not traditional: no trader carries this.)*: **cancels the kick: no -1 on the second shot.** (The grip itself is bought; the fitting and the rule are the schematic's.)
- **Adjustable tube skeleton stock** (stock; **common**) *(Custom, not traditional: no trader carries this.)*: light and set to his length; rules as the light rifle stock (**+2 on swapping, -1 on aimed shots**).
- **Arc calculator** (optic; **rare**) *(Custom, not traditional: no trader carries this.)*: in full at [kit.md, Arc calculator](kit.md#arc-calculator-launcher-sight): **+3 on launcher shots past ~30 m** on the first shot, and on a second at the same spot; in smoke or dust the two beams show.
- *Traditional parts on it:* holo sight (kit.md); grenade bandolier and belt pouches (kit.md).

### Tamsin's Kasr Frontier (schematic 17)

On paper (17th). Source: [schematic 17](../../campaigns/ash-on-ostrava/schematics.md#schematic-17-tamsins-kasr-frontier-rebuilt).

- **New lever linkage** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: **single lever chains up to 7 (Tamsin 8), double lever up to 4 (Tamsin 5);** a lever string above 6 runs with **no hit bonuses.**
- **Twin side-by-side tubes** (magazine; **uncommon**) *(Custom, not traditional: no trader carries this.)*: two extended tubes: **2 x 18 = 36 rounds;** the weight up front: **-1 on swapping.**
- **Tube selector** (action; **uncommon**) *(Custom, not traditional: no trader carries this.)*: by the thumb, **flicking it costs nothing:** **each tube holds its own load** (HP in one, HV in the other).
- **Plasteel tube springs** (magazine; **common**) *(Custom, not traditional: no trader carries this.)*: the long tubes **feed clean to the last round.**
- **Push-loaders (2)** (kit; **common**) *(Custom, not traditional: no trader carries this.)*: brass tubes pushed onto a tube's mouth: **refill a tube in the beat's move** (by hand it's the main thing).
- *Traditional parts on it:* extended tube kits, muzzle brake, telescopic sight, padded sling, light rifle stock, ergo grip sleeve, ergo foregrip (kit.md).

### Tamsin's Columnus (schematic 18)

On paper (18th). Source: [schematic 18](../../campaigns/ash-on-ostrava/schematics.md#schematic-18-tamsins-columnus-rebuilt-as-a-different-gun).

- **Magwell cut for Stinger's sticks** (magazine well; **common**) *(Custom, not traditional: no trader carries this.)*: takes **Stinger's straight 40-round sticks:** one mag fits both guns.
- **100-round box mags** (magazine; **uncommon**) *(Custom, not traditional: no trader carries this.)*: a squat canvas-covered box with a Stinger-stick neck and a plasteel spring; swapped like any mag (the beat's move); **a loaded box: -1 on swapping and -1 on quick-draw.**
- **The Super V** (action; **rare**) *(Custom, not traditional: no trader carries this.)*: an off-axis weighted slider and delayed blowback: **auto strings up to 12 (Tamsin 13), recoil 0;** auto still has no hit bonuses, misses still -1. **Gas tube removed:** cleans in ~20 min.
- **Short finned barrel** (barrel; **uncommon**) *(Custom, not traditional: no trader carries this.)*: a bought heavy short barrel with fins machined by Dace: **+1 within ~10 m, -2 past ~30 m** (single loses its +1 past 30 m); **strings of 8+ build 1 heat,** vent a beat at 3; **the fins shed 1 heat after any beat it doesn't fire;** **-1 more on swapping.**
- *Traditional parts on it:* standard silencer, hair trigger, laser sight, reflex sight, skeleton pistol grip (kit.md).

### Varga's drop rig and lanyard autopistol (schematic 19)

On paper (19th). Source: [schematic 19](../../campaigns/ash-on-ostrava/schematics.md#schematic-19-vargas-drop-rig-and-lanyard-autopistol).

- **Drop rig** (chest rig; **rare**) *(Custom, not traditional: no trader carries this.)*: **six impact frags on short ripcords;** on a jump pass she drops **one to six:** each is a **drop,** d20 + DEX against the spot, **+2 when directly above it;** impact frags burst on landing (no dive, no throwing back); pulled from under ~10 m she's inside her own blast.
- **Jump-harness lanyard** (sling; **common**) *(Custom, not traditional: no trader carries this.)*: the drum autopistol on a lanyard clipped to the harness: **fire one-handed on the way down (-2 in the air),** and it **suppresses** (whoever she fires at takes -1 on their shots that beat); **let go to work the controls; picking it back up costs no beat.**
- *Traditional parts on it:* pistol drum (kit.md); impact frags (Ottrick's method).

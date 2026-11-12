# Attachments

The Light's attachment sheet (set by the player, Ash on Ostrava day 47). Three parts:
1. **[Fitted and working](#fitted-and-working-every-attachment)** and **[Enemy attachments](#enemy-attachments):** when one counts, and how enemies roll them.
2. **[The rollable list](#the-rollable-list):** every traditional attachment, melee part, special ammo load and custom part an enemy can roll, with its slot and what it fits (the roller rolls it).
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

**Set by the player, day 47.** When an enemy is rolled, **each of his weapons (guns and melee, day 47) rolls a d100 for an attachment,** by
his faction's wealth:

| Wealth | Chance of an attachment |
| --- | --- |
| Poor | 20% |
| Steady | 25% |
| Good | 30% |
| Rich | 40% |
| Wealthy | 50% |

- **Special teams +10%.**
- **On a hit, roll again at the same chance for another;** keep going until a roll misses.
- **It has to fit the weapon:** the right slot and the right kind of weapon (no silencer on a las, one optic per gun,
  a chain motor only on a chain weapon). If it doesn't fit, roll again on the list.
- **Special ammo rolls too** (the player, day 47): a gun's special load (HP, AP, HV, belts, darts) is one more slot.
  **Special ammo is uncommon: it's easy to get. Armour-piercing loads are rare** (AP, CAP, tungsten-core belts, shard
  darts, man-stopper shells, Kraken bolts, and for las **the hot-shot conversion with hot-shot packs** and **the Mechanicus
  hot-shot pack**, which hit a step harder): they're better.
  **AP, CAP and man-stopper shells are rare only in the enemy roll; in shops they stay uncommon** (the player, day 47). The rest keep their catalogue rarity (hellfire belts, widow and truth darts are rare).
- **What a gun comes with doesn't count** (a kit's listed scope, a gun's built-in parts): the roll only adds.
- **Custom builds roll too, by their rarity** (the player, day 47): **simple fixes are common** (swapped springs, cut
  barrels, grips, slings, stocks), **real bench work is uncommon** (a new motor, a twin tray, a matched cell), and
  **the interesting ones are rare** (new mechanisms and modes: the Super V, an energy selector, a charge trigger, a
  heartbeat scanner). Rarity follows the faction's wealth as for any loot (`roll_enemy.py`: rich C40/U45/R15,
  wealthy C25/U50/R25). **An enemy's custom part is his own smith's version, not Tamsin's design:** no trader carries
  it, someone built it (a story hook). Numbers written for one of the Light (Tamsin's +1 string) use the base.
- The DM uses what's rolled in the fight like any other kit, and it's there to loot afterwards.

## The rollable list

**Set by the player, day 47. The roller rolls it:** `python3 wh40k_gear/roll_enemy.py ...` prints an
**++ ATTACHMENTS** line under any enemy whose guns got something (the d100s shown). The list lives in
[`wh40k_gear/attachments.py`](../attachments.py); this table is printed from it (`python3 wh40k_gear/attachments.py md`),
so the two always match. Each row links to the full entry; **custom rows** link to their gun under
[Custom builds](#custom-builds) below.

**How a gun rolls:** d100 against the chance above; on a hit, the rarity comes from the faction's wealth (as loot:
poor C80/U20, steady C70/U25/R5, good C55/U35/R10, rich C40/U45/R15, wealthy C25/U50/R25; **poor never rare**), then
**one attachment of that rarity that fits the gun and a free slot** (one per slot; a gun's own scope, drum, silencer
or bayonet already fills its slot). Then roll again. A part that needs another (an offset sight needs a scope, a
pressure pin needs a hair trigger) only comes once the first is on. **Every weapon rolls** (a gunslinger's pair, a
rifle and a sidearm, a machete and a shield). **Melee weapons roll too** (the player, day 47); the melee list is
thin for now, so plain blades and clubs mostly draw the hardwood grip, the whetstone or the shock-coil.

**Slots:** optic, optic2 (a second sight that rides a scope), laser, trigger, pin, limiter, under (under-barrel),
bayonet, stock, stockmag, muzzle, mag, grip, sleeve, barrel, coil, action, selector, bolt, slide, igniter, feeder,
tripod, holster, generator, sling, siderail, counter, vent, arc, tubesel, loader, **load** (special ammo); melee:
field, hone, spikes, slot, overdrive, motor, teeth, mgrip, mselector.

| Attachment | Rarity | Slot | Fits | What it does | Full entry |
| --- | --- | --- | --- | --- | --- |
| **Las auto-fire crystal** | rare | action | las rifles (only: ^(?!.*(hot-shot or hellgun)).*(lasgun or lascarbine)) | strings up to 12; no hit bonuses in the string, misses still -1; strings of 8+ build 1 heat, vent at 3 | [kit.md](kit.md#las-auto-fire-crystal) |
| **Repeater crystal** | rare | action | las pistols, las rifles | strings up to 7; no chain bonuses in the string, misses still -1 | [kit.md](kit.md#repeater-crystal) |
| **Custom barrel** | uncommon | barrel | SMGs, stub pistols | +1 aimed, +1 past ~30 m | [kit.md](kit.md#custom-barrel-stub-pistols-and-smgs-barrel-slot) |
| **Bayonet (fixed)** | common | bayonet | autoguns and stub rifles, las rifles | a spear thrust in melee: chains 2, +1 to strike first; Bayonet Charge | [kit.md](kit.md#bayonet) |
| **Underslung chain-bayonet** | rare | bayonet | autoguns and stub rifles, las rifles | fights as a chainsword (-1 block/parry); -1 hip snap shots; Bayonet Charge | [kit.md](kit.md#underslung-chain-bayonet) |
| **Shock-coil kit** | rare | coil | SMGs, autoguns and stub rifles, blades, blunt weapons, bolt pistols, boltguns, chain weapons, heavy stubbers, heavy weapons, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, power weapons, shotguns, stub pistols | after a hit, +1 on his next roll against that target (6 charges a fight) | [kit.md](kit.md#shock-coil-kit) |
| **Power weapon tuning kit** | rare | field | power weapons | a steady field: through power armour on any hit | [kit.md](kit.md#power-weapon-tuning-kit) |
| **Weighted grip** | common | grip | SMGs, autoguns and stub rifles, bolt pistols, boltguns, shotguns, stub pistols | recoil -1; -1 quick-draw | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Diamantine whetstone** | uncommon | hone | blades | honed before the fight: +1 pierce on its next 2 hits (~10 uses) | [kit.md](kit.md#diamantine-whetstone) |
| **Laser and lumen combo** | uncommon | laser | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | both, switched on alone or together | [kit.md](kit.md#laser-sight-under-mount-lumen-or-both) |
| **Laser sight** | uncommon | laser | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | +1 hip inside ~20 m, or +1 after a swap inside ~30 m (not both); the beam shows | [kit.md](kit.md#laser-sight-under-mount-lumen-or-both) |
| **Under-mount lumen** | common | laser | SMGs, autoguns and stub rifles, bolt pistols, boltguns, flamers, heavy stubbers, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | no darkness penalty in the beam; he's lit up too | [kit.md](kit.md#laser-sight-under-mount-lumen-or-both) |
| **Burst limiter** | common | limiter | SMGs, autoguns and stub rifles, boltguns, heavy stubbers | recoil -1; strings capped at 3 | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **AP rounds (armour-piercing)** | rare | load | SMGs, autoguns and stub rifles, stub pistols | flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m; against no armour a crit drops just one step | [stub.md](stub.md#stub-and-autogun-rounds-special-loads) |
| **Astartes melta canister** | rare | load | meltaguns | a hit on a vehicle takes 2 hull points, not 1; the kick: -1 on his next melta shot | [plasma.md](plasma.md#melta-canisters-special-loads) |
| **Black-tip darts** | uncommon | load | needle pistols, needle rifles | the toxin's save is vs 17; a pass is still -1 on their next roll | [stub.md](stub.md#needle-darts-special-loads) |
| **CAP rounds (ceramite-tipped AP)** | rare | load | SMGs, autoguns and stub rifles, stub pistols (only: autogun or autopistol or autorifle or auto-revolver or hammerfall or submachine or rattler or machine pistol or chain-fed) | flak and reinforced flak don't shrug it; through carapace on a solid hit at any range; against no armour a crit drops just one step | [stub.md](stub.md#stub-and-autogun-rounds-special-loads) |
| **Cut phosphex** | rare | load | flamers, hand flamers | can't be beaten out: burns 2 beats, a step each, unless smothered; the ground burns 2 beats; a natural 1 splashes the flamer | [scrap.md](scrap.md#flamer-tanks-and-fuels-special-loads) |
| **Dragon's breath shells** | uncommon | load | shotguns | shot at, the target is flashed: -1 on his next shot; hit, -2 instead; a hit on a raw 17+ sets him alight | [stub.md](stub.md#shotgun-shells-special-loads) |
| **Flak shells (autocannon)** | uncommon | load | heavy weapons (only: autocannon) | airborne targets: ignore the -3, a miss by 1-3 still clips; on the ground no extra step | [heavy.md](heavy.md#autocannon-shells-special-loads) |
| **Flat-tip rounds** | uncommon | load | autoguns and stub rifles, stub pistols (only: (?<!auto-)revolver or stub pistol or stub automatic or hand cannon or lever or hunting or stub rifle or boarding pistol) | a shrugged hit counts as 2 toward wear-down | [stub.md](stub.md#stub-and-autogun-rounds-special-loads) |
| **HP rounds (hollow point)** | uncommon | load | SMGs, autoguns and stub rifles, stub pistols | flak doesn't shrug it even at range; against no armour or flak a solid hit drops two steps; reinforced flak and heavier shrug it | [stub.md](stub.md#stub-and-autogun-rounds-special-loads) |
| **HV rounds (high velocity)** | uncommon | load | SMGs, autoguns and stub rifles, stub pistols | +1 aimed past ~30 m; flak doesn't shrug it at range; each shot counts 2 toward Dirty | [stub.md](stub.md#stub-and-autogun-rounds-special-loads) |
| **Hellfire belt** | rare | load | heavy stubbers | a hit that gets through: CON save vs 10 or one more step | [heavy.md](heavy.md#heavy-stubber-belts-special) |
| **Hellfire shells** | rare | load | shotguns | a hit that gets through: CON save vs 10 or one more step | [stub.md](stub.md#shotgun-shells-special-loads) |
| **Hollow point stubber belt** | uncommon | load | heavy stubbers | against flak or less a solid hit drops an extra step; carapace and heavier shrug it | [heavy.md](heavy.md#heavy-stubber-belts-special) |
| **Hot-shot conversion and hot-shot packs** | rare | load | las pistols, las rifles (only: ^(?!.*(hellgun or hellpistol or hot-shot or volley gun)).*) | hits one step harder (a lasgun hits like a hellgun); packs drain twice as fast; +1 heat a chain on a gun that builds heat | [../../DND_CODEX.md](../../DND_CODEX.md#hot-shot-conversion) |
| **Incinerator canister** | rare | load | meltaguns | inside ~8 m a hit drops 3 steps; vehicles 2 hull points; sets alight, melts light cover; a crit puts anyone straight to Down (enemies -1 on survival); the kick -2; 3 shots | [plasma.md](plasma.md#melta-canisters-special-loads) |
| **Inferno belt** | uncommon | load | heavy stubbers | a hit on a raw 17+ sets the target alight | [heavy.md](heavy.md#heavy-stubber-belts-special) |
| **Kraken bolt rounds** | rare | load | bolt pistols, boltguns, heavy weapons (only: bolt) | through an APC's armour; +1 aimed past ~30 m | [bolt.md](bolt.md#bolt-rounds-special-loads) |
| **Las eco pack** | common | load | las pistols, las rifles (only: ^(?!.*(hellgun or hellpistol or hot-shot or volley gun)).*) | 120 shots; flak shrugs it past ~15 m, reinforced flak always | [las.md](las.md#las-eco-pack) |
| **Man-stopper shells (armour-piercing slug)** | rare | load | shotguns | one slug, one target, no spread; flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m | [stub.md](stub.md#shotgun-shells-special-loads) |
| **Mechanicus lascannon pack** | rare | load | heavy weapons (only: lascannon or las-cannon) | a hit on a vehicle takes 2 hull points; +1 heat a shot, vent at 3 | [heavy.md](heavy.md#lascannon-packs-special-loads) |
| **Mechanicus melta canister** | rare | load | meltaguns | inside ~8 m a hit drops 3 steps; the kick: -1 on his next melta shot; 4 shots | [plasma.md](plasma.md#melta-canisters-special-loads) |
| **Mechanicus pattern hot-shot pack** | rare | load | las pistols, las rifles (only: hellgun or hellpistol or hot-shot or volley gun) | one armour tier harder (heavy carapace at any range, ceramite-forged inside ~15 m); 20 shots a pack | [las.md](las.md#hot-shot-pack-mechanicus-pattern) |
| **Meltacore bolt rounds** | rare | load | bolt pistols, boltguns, heavy weapons (only: bolt) | through a tank's armour from any side; +1 heat a string, vent at 3; +1 recoil | [bolt.md](bolt.md#bolt-rounds-special-loads) |
| **Off-brand bolt rounds** | common | load | bolt pistols, boltguns, heavy weapons (only: bolt) | heavy carapace and ceramite only on a solid hit; power armour shrugs them; a crit drops just one step | [bolt.md](bolt.md#bolt-rounds-special-loads) |
| **Panic darts** | uncommon | load | needle pistols, needle rifles | CON vs 15 or drops what's in hand and runs or hides 2 beats | [stub.md](stub.md#needle-darts-special-loads) |
| **Penetrator shells (autocannon)** | rare | load | heavy weapons (only: autocannon) | through a tank's side or rear; keeps the extra step on people; +1 recoil | [heavy.md](heavy.md#autocannon-shells-special-loads) |
| **Shard darts** | rare | load | needle pistols, needle rifles | through carapace on any hit, heavy carapace on a solid hit | [stub.md](stub.md#needle-darts-special-loads) |
| **Storm bolt rounds** | uncommon | load | bolt pistols, boltguns, heavy weapons (only: bolt) | a miss by 1-3 still hits; every hit lands like a frag (flak; carapace on a solid hit; heavier shrugs) | [bolt.md](bolt.md#bolt-rounds-special-loads) |
| **Sulphur fuel** | uncommon | load | flamers, hand flamers | everyone hit drops an extra step; fumes: -1 on the next roll in the burned area without a mask | [scrap.md](scrap.md#flamer-tanks-and-fuels-special-loads) |
| **Thermite fuel** | rare | load | flamers, hand flamers | +1 step on a hit; through carapace to ceramite-forged on any hit, power armour on a solid hit; burns through light cover; half the reach | [scrap.md](scrap.md#flamer-tanks-and-fuels-special-loads) |
| **Tracker darts** | uncommon | load | needle pistols, needle rifles | a pinger, not a toxin: followed on an auspex ~1 km for a day | [stub.md](stub.md#needle-darts-special-loads) |
| **Truth darts** | rare | load | needle pistols, needle rifles | CON vs 15 or ~10 minutes of loose tongue | [stub.md](stub.md#needle-darts-special-loads) |
| **Tungsten-core belt** | rare | load | heavy stubbers | through heavy carapace at any range | [heavy.md](heavy.md#heavy-stubber-belts-special) |
| **Vengeance bolt rounds** | rare | load | bolt pistols, boltguns, heavy weapons (only: bolt) | against power armour a hit drops an extra step; through an APC's armour; a natural 1 cooks off: he drops a step, the gun is out | [bolt.md](bolt.md#bolt-rounds-special-loads) |
| **Widow darts** | rare | load | needle pistols, needle rifles | a failed save is dead, no survival roll | [stub.md](stub.md#needle-darts-special-loads) |
| **Ancient plasma cell** | rare | mag | plasma guns, plasma pistols | through power armour on any hit; a hit drops an extra step; 1 heat a shot; 8 shots, can't be refilled | [plasma.md](plasma.md#ancient-plasma-cell) |
| **Big flamer tank** | uncommon | mag | flamers, hand flamers | twice the bursts; -1 on dodges; the tank is a target (a 1-4 burst also catches anyone within ~3 m) | [scrap.md](scrap.md#flamer-tanks-and-fuels-special-loads) |
| **Big melta canister** | uncommon | mag | meltaguns | 14 shots, not 6; -1 on quick-draws and swapping | [plasma.md](plasma.md#melta-canisters-special-loads) |
| **Extended lascannon pack** | uncommon | mag | heavy weapons (only: lascannon or las-cannon) | 10 shots, not 6; -1 on swapping | [heavy.md](heavy.md#lascannon-packs-special-loads) |
| **Extended magazine** | common | mag | SMGs, autoguns and stub rifles, las pistols, las rifles, shotguns, stub pistols | +50% shots | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Extended magazine kit (bolt or plasma)** | rare | mag | bolt pistols, boltguns, plasma guns, plasma pistols | +50% shots | [kit.md](kit.md#extended-magazine-kits) |
| **Lascannon battery pack** | uncommon | mag | heavy weapons (only: lascannon or las-cannon) | 40 shots; set down and cabled (the beat's move), the gunner stays within ~3 m; a solid hit on it kills it | [heavy.md](heavy.md#lascannon-packs-special-loads) |
| **Pistol drum** | uncommon | mag | SMGs, las pistols, stub pistols | twice the shots; no quick-draw holster, -1 quick-draw | [kit.md](kit.md#pistol-drums) |
| **Tuned plasma cell** | rare | mag | plasma guns, plasma pistols | 12 shots, not 8 | [plasma.md](plasma.md#tuned-plasma-cell) |
| **Compensator** | uncommon | muzzle | SMGs, autoguns and stub rifles, bolt pistols, boltguns, heavy stubbers, shotguns, stub pistols | recoil -2; +1 more after each hit; -1 aimed | [kit.md](kit.md#muzzles) |
| **Flash hider** | common | muzzle | SMGs, autoguns and stub rifles, bolt pistols, boltguns, heavy stubbers, shotguns, stub pistols | his shots don't give him away in the dark | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Heavy suppressor** | uncommon | muzzle | SMGs, autoguns and stub rifles, stub pistols | near-silent; recoil -2; -1 quick-draw and swapping; Dirty after ~20 shots | [kit.md](kit.md#muzzles) |
| **Muzzle brake** | uncommon | muzzle | SMGs, autoguns and stub rifles, bolt pistols, boltguns, heavy stubbers, shotguns, stub pistols | a chain miss costs no -1; the flash places him after his first string | [kit.md](kit.md#muzzles) |
| **Standard silencer** | uncommon | muzzle | SMGs, autoguns and stub rifles, stub pistols | quieter; recoil -1; -1 quick-draw; Dirty after ~20 shots | [kit.md](kit.md#muzzles) |
| **Holo sight** | uncommon | optic | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | +1 aimed inside ~50 m; -1 hip shots | [kit.md](kit.md#holo-sight) |
| **Low-light optic** | uncommon | optic | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | no darkness penalty through it; a flash blinds him a beat | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Range-finder sight** | rare | optic | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns | +1 past ~30 m | [kit.md](kit.md#range-finder-sight) |
| **Reflex sight** | uncommon | optic | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | +2 aimed inside ~30 m; -1 past ~30 m | [kit.md](kit.md#pistol-reflex-sight) |
| **Telescopic sight** | uncommon | optic | autoguns and stub rifles, boltguns, heavy stubbers, las rifles, needle rifles, plasma guns | +2 long shots; -1 hip/snap and inside ~15 m | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Offset backup sight** | uncommon | optic2 | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns (needs a scope) | cancels the scope's close penalty; -1 quick-draw | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Pressure-pin safety** | uncommon | pin | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols (needs Hair trigger) | the hair trigger isn't drop-prone while pinned | [kit.md](kit.md#pressure-pin-safety-hair-triggers) |
| **Ergo grip sleeve** | common | sleeve | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | never slips from his hand; disarms against him -2 | [kit.md](kit.md#ergo-grip-sleeve) |
| **Shield viewing slot** | uncommon | slot | shields | sees and shoots a pistol through it without leaving cover; planted, slot fire -2 | [kit.md](kit.md#shield-viewing-slot-mod) |
| **Spiked shield** | uncommon | spikes | shields | +3 on a shield-first charge, then +1 attacking with the shield | [kit.md](kit.md#spiked-shield-mod) |
| **Folding stock** | common | stock | SMGs, autoguns and stub rifles, las rifles, shotguns | +1 quick-draw; -1 aimed | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Light rifle stock** | common | stock | autoguns and stub rifles, boltguns, las rifles, shotguns | +2 on swapping; -1 aimed | [kit.md](kit.md#rifle-stocks-autogun-lasgun-stub-rifle) |
| **Tac rifle stock** | uncommon | stock | autoguns and stub rifles, boltguns, las rifles, shotguns | +1 first shot, +1 aimed; -2 more on swapping | [kit.md](kit.md#rifle-stocks-autogun-lasgun-stub-rifle) |
| **Hair trigger** | uncommon | trigger | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | +1 on the first shot of every string; drop-prone | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Match trigger** | uncommon | trigger | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | +1 aimed; -1 hip/snap | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Bipod** | common | under | autoguns and stub rifles, boltguns, heavy stubbers, las rifles, needle rifles, plasma guns | +2 aimed braced or prone; a beat to set up | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Ergo foregrip** | common | under | SMGs, autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns, shotguns | +1 on the first shot | [kit.md](kit.md#foregrips-under-barrel-slot) |
| **Handstop foregrip** | uncommon | under | SMGs, autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns, shotguns | +2 on the first shot; swapping costs nothing; -1 aimed | [kit.md](kit.md#foregrips-under-barrel-slot) |
| **Heavy foregrip** | uncommon | under | SMGs, autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns, shotguns | +2 aimed; a chain miss costs -2; -1 more on swapping | [kit.md](kit.md#foregrips-under-barrel-slot) |
| **Underslung grenade launcher** | rare | under | autoguns and stub rifles, boltguns, las rifles | one grenade shot without swapping; -1 aimed; a beat to reload | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **Underslung shotgun (masterkey)** | uncommon | under | autoguns and stub rifles, boltguns, las rifles | one or two shotgun blasts; -1 aimed | [kit.md](kit.md#more-attachments-player-picks-ash-on-ostrava-session-10) |
| **New lever linkage** *(Custom)* | uncommon | action | autoguns and stub rifles (only: lever) | single lever chains up to 7, double up to 4; above 6, no hit bonuses | [attachments.md](attachments.md#tamsins-kasr-frontier-schematic-17) |
| **Plasteel spring and gas-piston trigger** *(Custom)* | rare | action | grenade launchers | 2 grenades a string; the second -1 for the kick | [attachments.md](attachments.md#holliss-six-bells-schematic-16) |
| **The Super V** *(Custom)* | rare | action | autoguns and stub rifles (only: autogun or columnus) | auto strings up to 12, recoil 0; auto still no hit bonuses | [attachments.md](attachments.md#tamsins-columnus-schematic-18) |
| **Tuned charger** *(Custom)* | uncommon | action | las pistols, las rifles | strings up to 7; no hit bonuses in the string, misses still -1 | [attachments.md](attachments.md#sallows-carbine-schematic-10) |
| **Arc calculator** *(Custom)* | rare | arc | grenade launchers, mortars | +3 on launcher shots past ~30 m, the first shot or a repeat on the same spot; the beams show in smoke | [attachments.md](attachments.md#holliss-six-bells-schematic-16) |
| **Cut-down short barrel** *(Custom)* | common | barrel | autoguns and stub rifles, las rifles | +1 inside ~15 m; -1 past ~30 m | [attachments.md](attachments.md#kells-officer-schematic-8) |
| **Heavy long barrel** *(Custom)* | common | barrel | autoguns and stub rifles, las rifles, needle rifles | +2 aimed; -1 hip, snap and on the move | [attachments.md](attachments.md#isks-patience-schematic-7) |
| **Long barrel** *(Custom)* | common | barrel | las rifles | +1 aimed past ~30 m; -1 inside ~5 m | [attachments.md](attachments.md#vargas-mercy-schematic-6) |
| **Long flamer barrel** *(Custom)* | common | barrel | hand flamers | reach ~10 m; -1 quick-draw | [attachments.md](attachments.md#holliss-hand-flamer-schematic-2) |
| **Long needle barrel** *(Custom)* | common | barrel | needle pistols | reach ~35 m; +1 aimed; -1 quick-draw | [attachments.md](attachments.md#nessas-needle-pistol-schematic-13) |
| **Short finned barrel** *(Custom)* | uncommon | barrel | autoguns and stub rifles (only: autogun or columnus) | +1 inside ~10 m, -2 past ~30 m; strings of 8+ build 1 heat, the fins shed 1 when it doesn't fire; -1 swapping | [attachments.md](attachments.md#tamsins-columnus-schematic-18) |
| **Heavy buffer spring and new bolt** *(Custom)* | common | bolt | SMGs | jams only from the 25th straight round | [attachments.md](attachments.md#stinger-tamsin) |
| **Light reciprocating parts and plasteel spring** *(Custom)* | common | bolt | heavy stubbers | strings up to 10, no hit bonuses in the string | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Helm-linked ammo counter** *(Custom)* | uncommon | counter | SMGs, autoguns and stub rifles, bolt pistols, boltguns, flamers, hand flamers, heavy stubbers, heavy weapons, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | he always knows his count: never caught dry | [attachments.md](attachments.md#sorels-hellgun-schematic-14) |
| **Open-bolt feeder** *(Custom)* | uncommon | feeder | heavy stubbers | Dirty after ~60 shots; a Dirty stubber doesn't jam | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Intensified laser generator** *(Custom)* | rare | generator | las rifles | 3 pack a shot: +1 aimed, through ceramite-forged; a string of 3 adds 1 heat | [attachments.md](attachments.md#isks-patience-schematic-7) |
| **Angled handguard grip (fitted)** *(Custom)* | common | grip | grenade launchers (needs Plasteel spring and gas-piston trigger) | no -1 on the second grenade | [attachments.md](attachments.md#holliss-six-bells-schematic-16) |
| **Angled side grip** *(Custom)* | common | grip | heavy stubbers | recoil 1 on the move | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Hollow pop-lock grip** *(Custom)* | common | grip | SMGs, autoguns and stub rifles, bolt pistols, boltguns, las pistols, las rifles, meltaguns, needle pistols, needle rifles, plasma guns, plasma pistols, shotguns, stub pistols | one more stimm or bandage inside | [attachments.md](attachments.md#sallows-carbine-schematic-10) |
| **Skeleton grip** *(Custom)* | common | grip | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns | no swap penalty; -1 aimed past ~30 m | [attachments.md](attachments.md#kells-officer-schematic-8) |
| **One-piece crossdraw rig** *(Custom)* | common | holster | bolt pistols, las pistols, needle pistols, plasma pistols, stub pistols | +1 quick-draw | [attachments.md](attachments.md#teys-hellpistol-schematic-4) |
| **Tuned igniter** *(Custom)* | uncommon | igniter | flamers, hand flamers | the gout opens ~2 m wide at the far end and catches anyone close together | [attachments.md](attachments.md#holliss-hand-flamer-schematic-2) |
| **Push-loaders** *(Custom)* | common | loader | autoguns and stub rifles, shotguns (only: lever or pump) | refill a tube in the beat's move | [attachments.md](attachments.md#tamsins-kasr-frontier-schematic-17) |
| **100-round box mags** *(Custom)* | uncommon | mag | autoguns and stub rifles (only: autogun or columnus) | 100 rounds; a loaded box -1 swapping and quick-draw | [attachments.md](attachments.md#tamsins-columnus-schematic-18) |
| **Bridged double-cell belt pack** *(Custom)* | uncommon | mag | las pistols (only: hellpistol) | 60 shots on the cable | [attachments.md](attachments.md#teys-hellpistol-schematic-4) |
| **Dual canister cradle** *(Custom)* | uncommon | mag | hand flamers | 8 bursts before a reload | [attachments.md](attachments.md#holliss-hand-flamer-schematic-2) |
| **Twin feed tray** *(Custom)* | uncommon | mag | heavy stubbers | twice the rounds; two belt types, switched with a lever | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Twin side-by-side tubes** *(Custom)* | uncommon | mag | autoguns and stub rifles (only: lever) | 36 rounds; -1 swapping | [attachments.md](attachments.md#tamsins-kasr-frontier-schematic-17) |
| **Curved hardwood grip** *(Custom)* | common | mgrip | blades, blunt weapons, chain weapons, power weapons | can't be knocked from his hand by a solid hit | [attachments.md](attachments.md#kells-chain-axe-schematic-5) |
| **Better motor** *(Custom)* | uncommon | motor | chain weapons | crits on 19-20; a natural 1 on a swing throws the chain (a beat to reseat) | [attachments.md](attachments.md#kells-chain-axe-schematic-5) |
| **Bite switch** *(Custom)* | rare | mselector | chain weapons | BITE: one swing a beat, a hit drops an extra step; flipped before the swing | [attachments.md](attachments.md#kells-chain-axe-schematic-5) |
| **Walking plate** *(Custom)* | rare | muzzle | heavy stubbers | one string across up to 3 standing abreast; the swap's -1 once per extra target | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Custom long-range scope** *(Custom)* | uncommon | optic | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns | +2 aimed past ~30 m (telescopic: -1 hip/snap and inside ~15 m) | [attachments.md](attachments.md#vargas-mercy-schematic-6) |
| **Custom range-finder** *(Custom)* | uncommon | optic2 | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns (needs a scope) | +2 aimed past ~30 m (rides the scope) | [attachments.md](attachments.md#isks-patience-schematic-7) |
| **Dual riser mount with a canted reflex** *(Custom)* | uncommon | optic2 | autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns (needs a scope) | the scope's close penalty never applies (the reflex: +2 aimed inside ~30 m); one optic at a time; -1 quick-draw | [attachments.md](attachments.md#vargas-mercy-schematic-6) |
| **Overdrive** *(Custom)* | rare | overdrive | chain weapons | once a mission, ~30 s: armour a step lighter against it, advantage in mob pushes; then done for the fight; a natural 1 while running burns the motor | [attachments.md](attachments.md#shameholders-overdrive-tamsin) |
| **Charge trigger and capacitor** *(Custom)* | rare | selector | las pistols, las rifles | a charge beat draws up to 30 pack, next beat one bolt: 25-30 plasma punch, 20-24 hellgun + heavy carapace, 10-19 hellgun; fire it next beat or lose it; 20+: a vent beat | [attachments.md](attachments.md#corvanes-shotlas-schematic-11) |
| **Energy selector (LIGHT / MED / HEAVY)** *(Custom)* | rare | selector | las rifles (only: hellgun or hot-shot) | MED: 2 pack a shot, heavy carapace at any range, +1 heat a string; HEAVY: 3 pack a shot, through ceramite-forged, +2 heat a shot; vent at 3 | [attachments.md](attachments.md#vargas-mercy-schematic-6) |
| **Heavy-burst switch** *(Custom)* | rare | selector | flamers, hand flamers | one pull spends 2 bursts: everyone hit drops an extra step; no flame the next beat | [attachments.md](attachments.md#holliss-hand-flamer-schematic-2) |
| **Plasma charge (hold the trigger)** *(Custom)* | rare | selector | plasma guns, plasma pistols | quick: one shot, +1 extra step, +2 heat, 2 cell; full: hold a beat, +2 extra steps, +3 heat, 3 cell | [attachments.md](attachments.md#ferros-ryza-plasma-pistol-schematic-15) |
| **Rate selector (HIGH)** *(Custom)* | rare | selector | heavy stubbers | HIGH: strings up to 12; Dirty at ~30 and jams on a natural 1; recoil 1 braced, 2 moving | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Three-round burst with its tower grip** *(Custom)* | rare | selector | las rifles | a string is 2 bursts, each one roll of 3 bolts: a hit drops a step, one armour tier harder, 3 hits toward wear-down; 3 pack a burst | [attachments.md](attachments.md#sorels-hellgun-schematic-14) |
| **Three-way selector with a rapid feeder** *(Custom)* | rare | selector | stub pistols (only: autopistol) | SAFE / BURST (strings up to 5) / AUTO (strings up to 8, no hit bonuses; from the 13th straight round a shot die of 1-3 jams); not drop-prone | [attachments.md](attachments.md#daces-autopistol-schematic-1) |
| **Twin-shot switch** *(Custom)* | rare | selector | las rifles | TWIN: a hit drops a step, one armour tier harder, 2 hits toward wear-down; 2 pack a shot | [attachments.md](attachments.md#kells-officer-schematic-8) |
| **Heartbeat scanner** *(Custom)* | rare | siderail | SMGs, autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns | heartbeats through walls to ~30 m; while he watches it, nobody with a heartbeat surprises him | [attachments.md](attachments.md#brenners-accatran-schematic-12) |
| **Lightened slide and tower grip** *(Custom)* | common | slide | stub pistols (only: autopistol) | strings up to 5; recoil stays 0 | [attachments.md](attachments.md#daces-autopistol-schematic-1) |
| **Quick-release sling** *(Custom)* | common | sling | SMGs, autoguns and stub rifles, boltguns, las rifles, needle rifles, plasma guns, shotguns | dropping it to his chest or bringing it up costs nothing | [attachments.md](attachments.md#sallows-carbine-schematic-10) |
| **Ergonomic grip cover (stock removed)** *(Custom)* | common | stock | SMGs, shotguns | +1 quick-draw; fits a holster | [attachments.md](attachments.md#corvanes-shotlas-schematic-11) |
| **Heavy grip and recoil stock** *(Custom)* | common | stock | heavy stubbers | recoil 0 braced | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Heavy shotgun stock with grenade loops** *(Custom)* | common | stock | autoguns and stub rifles, las rifles, shotguns | +1 aimed; -1 swapping; 3 grenade loops | [attachments.md](attachments.md#tavis-tiny-schematic-9) |
| **Hollow medicine-cabinet stock** *(Custom)* | common | stock | autoguns and stub rifles, las rifles | a stimm, a bandage and a tourniquet inside: he patches from the gun; -1 aimed past ~30 m | [attachments.md](attachments.md#sallows-carbine-schematic-10) |
| **Stock magazine slot** *(Custom)* | common | stockmag | las rifles | the first reload each fight costs no beat | [attachments.md](attachments.md#kells-officer-schematic-8) |
| **Plasteel teeth** *(Custom)* | uncommon | teeth | chain weapons | through heavy carapace on any hit, ceramite-forged on a solid hit | [attachments.md](attachments.md#kells-chain-axe-schematic-5) |
| **Traverse tripod (ARC fire)** *(Custom)* | rare | tripod | heavy stubbers | set up as a main thing, no recoil; ARC: everyone in the arc -2 on their shots next beat, breaking cover draws a free shot | [attachments.md](attachments.md#morcants-heavy-stubber-schematic-3) |
| **Tube selector** *(Custom)* | uncommon | tubesel | autoguns and stub rifles (only: lever) (needs Twin side-by-side tubes) | each tube its own load; flicking it is free | [attachments.md](attachments.md#tamsins-kasr-frontier-schematic-17) |
| **Custom bipod** *(Custom)* | common | under | autoguns and stub rifles, boltguns, heavy stubbers, las rifles, needle rifles, plasma guns | braced or prone, a chain miss costs no -1; a beat to set up | [attachments.md](attachments.md#isks-patience-schematic-7) |
| **Underslung krak launcher** *(Custom)* | rare | under | autoguns and stub rifles, las rifles | one krak a beat out to ~60 m, rolled like a throw; a beat to reload | [attachments.md](attachments.md#tavis-tiny-schematic-9) |
| **Third vent channel** *(Custom)* | uncommon | vent | plasma guns, plasma pistols | sheds 1 heat at the end of every beat | [attachments.md](attachments.md#ferros-ryza-plasma-pistol-schematic-15) |

**Custom parts not in the roll:**
- **Stinger's frame rails; Dace's top and bottom rails:** no rule of their own.
- **Sorel's and Six Bells' adjustable tube stocks:** they rule as the light rifle stock, which is on the list.
- **Ferro's matched fill:** it's matched to Ferro's own reclamator.
- **The Columnus magwell cut:** it takes Stinger's sticks: Tamsin's guns only.
- **The Frontier's plasteel tube springs:** no rule of their own.
- **Sorel's blacklight visor:** helm gear, not a gun part: the DM gives it to a tracker.
- **Varga's drop rig and harness lanyard:** jumper gear, not gun parts: the DM gives them to a jumper.

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
- **Charge (hold the trigger)** (trigger; **rare**) *(Custom, not traditional: no trader carries this.)*: **quick charge:** the beat's string becomes one charged shot: **a hit drops 1 extra step (2 in all), +2 heat, 2 shots of cell.** **Full charge:** hold through a whole beat (no firing), fire the next: **a hit drops 2 extra steps (3 in all), +3 heat, 3 shots of cell.** (Extra steps: the player, day 47.) Plasma punch on both; a crit adds a step.
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

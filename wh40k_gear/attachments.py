"""The rollable attachment list (set by the player, Ash on Ostrava day 47).

Every traditional attachment (kit.md, las.md, plasma.md), melee part, special ammo load (stub.md, heavy.md) and
every custom build part (catalogue/attachments.md, Custom builds) that can be on an enemy's weapon, with its slot,
the weapons it fits, and its rarity. roll_enemy.py calls describe() for every weapon an enemy carries (guns and
melee, day 47). The rules for the roll:
  - each weapon rolls a d100: poor 20%, steady 25%, good 30%, rich 40%, wealthy 50%; special teams +10%
  - a hit picks an attachment (rarity by the faction's wealth, as loot) that fits the gun and a free slot,
    then rolls again at the same chance; a miss, or nothing left that fits, stops it
  - what the gun already has (a scope, a drum, a silencer, a bayonet) fills its slot: the roll only adds
  - Poor factions never get rares
  - custom parts roll like the rest: an enemy's custom part is his own smith's version
  - special ammo is one more slot ('load'): uncommon, armour-piercing loads rare (the player, day 47)
Print the list for the sheet: python3 attachments.py md
"""
import random, re

CHANCE = {"poor": 20, "steady": 25, "good": 30, "rich": 40, "wealthy": 50}

# Gun types: lp las pistol, lr las rifle/carbine, sp stub pistol, smg, sr stub rifle/autogun, sg shotgun,
# bp bolt pistol, br boltgun, pp plasma pistol, pg plasma gun, np needle pistol, nr needle rifle,
# hf hand flamer, fl flamer, hs heavy stubber, hv other heavy weapon, gl grenade launcher, mo mortar, mg meltagun.
PIST = {"lp", "sp", "bp", "pp", "np"}
RIFLE = {"lr", "sr", "br", "pg", "nr"}
SIGHT = PIST | RIFLE | {"smg", "sg", "mg"}
RECOIL = {"sp", "smg", "sr", "sg", "bp", "br", "hs"}
HAND = SIGHT  # guns a hand holds and a grip sleeve fits
# Melee (day 47): ch chain, pw power, bl edged blade, bt blunt, sh shield.
MELEE = {"ch", "pw", "bl", "bt"}
STUBCAL = r"(?<!auto-)revolver|stub pistol|stub automatic|hand cannon|lever|hunting|stub rifle|boarding pistol"
AUTOCAL = r"autogun|autopistol|autorifle|auto-revolver|hammerfall|submachine|rattler|machine pistol|chain-fed"
NAMES = {"lp": "las pistols", "lr": "las rifles", "sp": "stub pistols", "smg": "SMGs", "sr": "autoguns and stub rifles",
         "sg": "shotguns", "bp": "bolt pistols", "br": "boltguns", "pp": "plasma pistols", "pg": "plasma guns",
         "np": "needle pistols", "nr": "needle rifles", "hf": "hand flamers", "fl": "flamers", "hs": "heavy stubbers",
         "hv": "heavy weapons", "gl": "grenade launchers", "mo": "mortars", "mg": "meltaguns",
         "ch": "chain weapons", "pw": "power weapons", "bl": "blades", "bt": "blunt weapons", "sh": "shields"}

K = "kit.md#"
MORE = K + "more-attachments-player-picks-ash-on-ostrava-session-10"
C = "attachments.md#"  # custom builds, same folder
# (key, name, rarity, slot, fits, keyword the gun's name must have or None, needs key or None, custom, rule, link)
A = [
 # --- traditional ---
 ("reflex", "Reflex sight", "U", "optic", SIGHT, None, None, 0, "+2 aimed inside ~30 m; -1 past ~30 m", K + "pistol-reflex-sight"),
 ("holo", "Holo sight", "U", "optic", SIGHT, None, None, 0, "+1 aimed inside ~50 m; -1 hip shots", K + "holo-sight"),
 ("tele", "Telescopic sight", "U", "optic", RIFLE | {"hs"}, None, None, 0, "+2 long shots; -1 hip/snap and inside ~15 m", MORE),
 ("lowlight", "Low-light optic", "U", "optic", SIGHT, None, None, 0, "no darkness penalty through it; a flash blinds him a beat", MORE),
 ("rangef", "Range-finder sight", "R", "optic", RIFLE, None, None, 0, "+1 past ~30 m", K + "range-finder-sight"),
 ("offset", "Offset backup sight", "U", "optic2", RIFLE, None, "scope", 0, "cancels the scope's close penalty; -1 quick-draw", MORE),
 ("laser", "Laser sight", "U", "laser", SIGHT, None, None, 0, "+1 hip inside ~20 m, or +1 after a swap inside ~30 m (not both); the beam shows", K + "laser-sight-under-mount-lumen-or-both"),
 ("lumen", "Under-mount lumen", "C", "laser", SIGHT | {"hs", "fl"}, None, None, 0, "no darkness penalty in the beam; he's lit up too", K + "laser-sight-under-mount-lumen-or-both"),
 ("combo", "Laser and lumen combo", "U", "laser", SIGHT, None, None, 0, "both, switched on alone or together", K + "laser-sight-under-mount-lumen-or-both"),
 ("match", "Match trigger", "U", "trigger", PIST | RIFLE | {"smg", "sg"}, None, None, 0, "+1 aimed; -1 hip/snap", MORE),
 ("hair", "Hair trigger", "U", "trigger", PIST | RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot of every string; drop-prone", MORE),
 ("pin", "Pressure-pin safety", "U", "pin", PIST | RIFLE | {"smg", "sg"}, None, "hair", 0, "the hair trigger isn't drop-prone while pinned", K + "pressure-pin-safety-hair-triggers"),
 ("limiter", "Burst limiter", "C", "limiter", {"smg", "sr", "br", "hs"}, None, None, 0, "recoil -1; strings capped at 3", MORE),
 ("ergofg", "Ergo foregrip", "C", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot", K + "foregrips-under-barrel-slot"),
 ("heavyfg", "Heavy foregrip", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+2 aimed; a chain miss costs -2; -1 more on swapping", K + "foregrips-under-barrel-slot"),
 ("handstop", "Handstop foregrip", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+2 on the first shot; swapping costs nothing; -1 aimed", K + "foregrips-under-barrel-slot"),
 ("bipod", "Bipod", "C", "under", RIFLE | {"hs"}, None, None, 0, "+2 aimed braced or prone; a beat to set up", MORE),
 ("ugl", "Underslung grenade launcher", "R", "under", {"lr", "sr", "br"}, None, None, 0, "one grenade shot without swapping; -1 aimed; a beat to reload", MORE),
 ("masterkey", "Underslung shotgun (masterkey)", "U", "under", {"lr", "sr", "br"}, None, None, 0, "one or two shotgun blasts; -1 aimed", MORE),
 ("bayonet", "Bayonet (fixed)", "C", "bayonet", {"lr", "sr"}, None, None, 0, "a spear thrust in melee: chains 2, +1 to strike first; Bayonet Charge", K + "bayonet"),
 ("chainbay", "Underslung chain-bayonet", "R", "bayonet", {"lr", "sr"}, None, None, 0, "fights as a chainsword (-1 block/parry); -1 hip snap shots; Bayonet Charge", K + "underslung-chain-bayonet"),
 ("tacstock", "Tac rifle stock", "U", "stock", {"lr", "sr", "br", "sg"}, None, None, 0, "+1 first shot, +1 aimed; -2 more on swapping", K + "rifle-stocks-autogun-lasgun-stub-rifle"),
 ("lightstock", "Light rifle stock", "C", "stock", {"lr", "sr", "br", "sg"}, None, None, 0, "+2 on swapping; -1 aimed", K + "rifle-stocks-autogun-lasgun-stub-rifle"),
 ("foldstock", "Folding stock", "C", "stock", {"lr", "sr", "smg", "sg"}, None, None, 0, "+1 quick-draw; -1 aimed", MORE),
 ("silencer", "Standard silencer", "U", "muzzle", {"sp", "smg", "sr"}, None, None, 0, "quieter; recoil -1; -1 quick-draw; Dirty after ~20 shots", K + "muzzles"),
 ("suppressor", "Heavy suppressor", "U", "muzzle", {"sp", "smg", "sr"}, None, None, 0, "near-silent; recoil -2; -1 quick-draw and swapping; Dirty after ~20 shots", K + "muzzles"),
 ("comp", "Compensator", "U", "muzzle", RECOIL | {"bp", "br"}, None, None, 0, "recoil -2; +1 more after each hit; -1 aimed", K + "muzzles"),
 ("brake", "Muzzle brake", "U", "muzzle", RECOIL, None, None, 0, "a chain miss costs no -1; the flash places him after his first string", K + "muzzles"),
 ("flashhider", "Flash hider", "C", "muzzle", RECOIL, None, None, 0, "his shots don't give him away in the dark", MORE),
 ("extmag", "Extended magazine", "C", "mag", {"lp", "lr", "sp", "smg", "sr", "sg"}, None, None, 0, "+50% shots", MORE),
 ("extbp", "Extended magazine kit (bolt or plasma)", "R", "mag", {"bp", "br", "pp", "pg"}, None, None, 0, "+50% shots", K + "extended-magazine-kits"),
 ("drum", "Pistol drum", "U", "mag", {"sp", "smg", "lp"}, None, None, 0, "twice the shots; no quick-draw holster, -1 quick-draw", K + "pistol-drums"),
 ("tunedcell", "Tuned plasma cell", "R", "mag", {"pp", "pg"}, None, None, 0, "12 shots, not 8", "plasma.md#tuned-plasma-cell"),
 ("weighted", "Weighted grip", "C", "grip", {"sp", "smg", "sr", "sg", "bp", "br"}, None, None, 0, "recoil -1; -1 quick-draw", MORE),
 ("sleeve", "Ergo grip sleeve", "C", "sleeve", HAND, None, None, 0, "never slips from his hand; disarms against him -2", K + "ergo-grip-sleeve"),
 ("cbarrel", "Custom barrel", "U", "barrel", {"sp", "smg"}, None, None, 0, "+1 aimed, +1 past ~30 m", K + "custom-barrel-stub-pistols-and-smgs-barrel-slot"),
 ("shockcoil", "Shock-coil kit", "R", "coil", HAND | {"hs", "hv"} | MELEE, None, None, 0, "after a hit, +1 on his next roll against that target (6 charges a fight)", K + "shock-coil-kit"),
 ("repeater", "Repeater crystal", "R", "action", {"lp", "lr"}, None, None, 0, "strings up to 7; no chain bonuses in the string, misses still -1", K + "repeater-crystal"),
 # melee (day 47)
 ("tuning", "Power weapon tuning kit", "R", "field", {"pw"}, None, None, 0, "a steady field: through power armour on any hit", K + "power-weapon-tuning-kit"),
 ("whetstone", "Diamantine whetstone", "U", "hone", {"bl"}, None, None, 0, "honed before the fight: +1 pierce on its next 2 hits (~10 uses)", K + "diamantine-whetstone"),
 ("spikes", "Spiked shield", "U", "spikes", {"sh"}, None, None, 0, "+3 on a shield-first charge, then +1 attacking with the shield", K + "spiked-shield-mod"),
 ("viewslot", "Shield viewing slot", "U", "slot", {"sh"}, None, None, 0, "sees and shoots a pistol through it without leaving cover; planted, slot fire -2", K + "shield-viewing-slot-mod"),
 # ammo (day 47): one special load per gun ('load' slot); a magazine holds one load at a time.
 # The player: special ammo is easy to get (uncommon); armour-piercing is better (rare).
 ("a_hp", "HP rounds (hollow point)", "U", "load", {"sp", "smg", "sr"}, None, None, 0, "flak doesn't shrug it even at range; against no armour or flak a solid hit drops two steps; reinforced flak and heavier shrug it", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_ap", "AP rounds (armour-piercing)", "R", "load", {"sp", "smg", "sr"}, None, None, 0, "flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m; against no armour a crit drops just one step", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_hv", "HV rounds (high velocity)", "U", "load", {"sp", "smg", "sr"}, None, None, 0, "+1 aimed past ~30 m; flak doesn't shrug it at range; each shot counts 2 toward Dirty", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_flat", "Flat-tip rounds", "U", "load", {"sp", "sr"}, STUBCAL, None, 0, "a shrugged hit counts as 2 toward wear-down", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_cap", "CAP rounds (ceramite-tipped AP)", "R", "load", {"sp", "smg", "sr"}, AUTOCAL, None, 0, "flak and reinforced flak don't shrug it; through carapace on a solid hit at any range; against no armour a crit drops just one step", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_hotshot", "Hot-shot conversion and hot-shot packs", "R", "load", {"lp", "lr"}, r"^(?!.*(hellgun|hellpistol|hot-shot|volley gun)).*", None, 0, "hits one step harder (a lasgun hits like a hellgun); packs drain twice as fast; +1 heat a chain on a gun that builds heat", "../../DND_CODEX.md#hot-shot-conversion"),
 ("a_manstopper", "Man-stopper shells (armour-piercing slug)", "R", "load", {"sg"}, None, None, 0, "one slug, one target, no spread; flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m", "stub.md#shotgun-shells-special-loads"),
 ("a_dragon", "Dragon's breath shells", "U", "load", {"sg"}, None, None, 0, "shot at, the target is flashed: -1 on his next shot; hit, -2 instead; a hit on a raw 17+ sets him alight", "stub.md#shotgun-shells-special-loads"),
 ("a_hellshell", "Hellfire shells", "R", "load", {"sg"}, None, None, 0, "a hit that gets through: CON save vs 10 or one more step", "stub.md#shotgun-shells-special-loads"),
 ("a_hpbelt", "Hollow point stubber belt", "U", "load", {"hs"}, None, None, 0, "against flak or less a solid hit drops an extra step; carapace and heavier shrug it", "heavy.md#heavy-stubber-belts-special"),
 ("a_inferno", "Inferno belt", "U", "load", {"hs"}, None, None, 0, "a hit on a raw 17+ sets the target alight", "heavy.md#heavy-stubber-belts-special"),
 ("a_tungsten", "Tungsten-core belt", "R", "load", {"hs"}, None, None, 0, "through heavy carapace at any range", "heavy.md#heavy-stubber-belts-special"),
 ("a_hellfire", "Hellfire belt", "R", "load", {"hs"}, None, None, 0, "a hit that gets through: CON save vs 15 or one more step", "heavy.md#heavy-stubber-belts-special"),
 ("a_blacktip", "Black-tip darts", "U", "load", {"np", "nr"}, None, None, 0, "the toxin's save is vs 17; a pass is still -1 on their next roll", "stub.md#needle-darts-special-loads"),
 ("a_panic", "Panic darts", "U", "load", {"np", "nr"}, None, None, 0, "CON vs 15 or drops what's in hand and runs or hides 2 beats", "stub.md#needle-darts-special-loads"),
 ("a_tracker", "Tracker darts", "U", "load", {"np", "nr"}, None, None, 0, "a pinger, not a toxin: followed on an auspex ~1 km for a day", "stub.md#needle-darts-special-loads"),
 ("a_shard", "Shard darts", "R", "load", {"np", "nr"}, None, None, 0, "through carapace on any hit, heavy carapace on a solid hit", "stub.md#needle-darts-special-loads"),
 ("a_widow", "Widow darts", "R", "load", {"np", "nr"}, None, None, 0, "a failed save is dead, no survival roll", "stub.md#needle-darts-special-loads"),
 ("a_truth", "Truth darts", "R", "load", {"np", "nr"}, None, None, 0, "CON vs 15 or ~10 minutes of loose tongue", "stub.md#needle-darts-special-loads"),
 # --- custom (an enemy's is his own smith's version) ---
 ("c_overdrive", "Overdrive", "R", "overdrive", {"ch"}, None, None, 1, "once a mission, ~30 s: armour a step lighter against it, advantage in mob pushes; then done for the fight; a natural 1 while running burns the motor", C + "shameholders-overdrive-tamsin"),
 ("c_motor", "Better motor", "U", "motor", {"ch"}, None, None, 1, "crits on 19-20; a natural 1 on a swing throws the chain (a beat to reseat)", C + "kells-chain-axe-schematic-5"),
 ("c_teeth", "Plasteel teeth", "U", "teeth", {"ch"}, None, None, 1, "through heavy carapace on any hit, ceramite-forged on a solid hit", C + "kells-chain-axe-schematic-5"),
 ("c_hardgrip", "Curved hardwood grip", "C", "mgrip", MELEE, None, None, 1, "can't be knocked from his hand by a solid hit", C + "kells-chain-axe-schematic-5"),
 ("c_bite", "Bite switch", "R", "mselector", {"ch"}, None, None, 1, "BITE: one swing a beat, a hit drops an extra step; flipped before the swing", C + "kells-chain-axe-schematic-5"),
 ("c_buffer", "Heavy buffer spring and new bolt", "C", "bolt", {"smg"}, None, None, 1, "jams only from the 25th straight round", C + "stinger-tamsin"),
 ("c_slide", "Lightened slide and tower grip", "C", "slide", {"sp"}, "autopistol", None, 1, "strings up to 5; recoil stays 0", C + "daces-autopistol-schematic-1"),
 ("c_select3", "Three-way selector with a rapid feeder", "R", "selector", {"sp"}, "autopistol", None, 1, "SAFE / BURST (strings up to 5) / AUTO (strings up to 8, no hit bonuses; from the 13th straight round a shot die of 1-3 jams); not drop-prone", C + "daces-autopistol-schematic-1"),
 ("c_flbarrel", "Long flamer barrel", "C", "barrel", {"hf"}, None, None, 1, "reach ~10 m; -1 quick-draw", C + "holliss-hand-flamer-schematic-2"),
 ("c_igniter", "Tuned igniter", "U", "igniter", {"hf", "fl"}, None, None, 1, "the gout opens ~2 m wide at the far end and catches anyone close together", C + "holliss-hand-flamer-schematic-2"),
 ("c_hburst", "Heavy-burst switch", "R", "selector", {"hf", "fl"}, None, None, 1, "one pull spends 2 bursts: everyone hit drops an extra step; no flame the next beat", C + "holliss-hand-flamer-schematic-2"),
 ("c_cradle", "Dual canister cradle", "U", "mag", {"hf"}, None, None, 1, "8 bursts before a reload", C + "holliss-hand-flamer-schematic-2"),
 ("c_hstock", "Heavy grip and recoil stock", "C", "stock", {"hs"}, None, None, 1, "recoil 0 braced", C + "morcants-heavy-stubber-schematic-3"),
 ("c_sidegrip", "Angled side grip", "C", "grip", {"hs"}, None, None, 1, "recoil 1 on the move", C + "morcants-heavy-stubber-schematic-3"),
 ("c_openbolt", "Open-bolt feeder", "U", "feeder", {"hs"}, None, None, 1, "Dirty after ~60 shots; a Dirty stubber doesn't jam", C + "morcants-heavy-stubber-schematic-3"),
 ("c_recip", "Light reciprocating parts and plasteel spring", "C", "bolt", {"hs"}, None, None, 1, "strings up to 10, no hit bonuses in the string", C + "morcants-heavy-stubber-schematic-3"),
 ("c_rate", "Rate selector (HIGH)", "R", "selector", {"hs"}, None, None, 1, "HIGH: strings up to 12; Dirty at ~30 and jams on a natural 1; recoil 1 braced, 2 moving", C + "morcants-heavy-stubber-schematic-3"),
 ("c_tripod", "Traverse tripod (ARC fire)", "R", "tripod", {"hs"}, None, None, 1, "set up as a main thing, no recoil; ARC: everyone in the arc -2 on their shots next beat, breaking cover draws a free shot", C + "morcants-heavy-stubber-schematic-3"),
 ("c_twintray", "Twin feed tray", "U", "mag", {"hs"}, None, None, 1, "twice the rounds; two belt types, switched with a lever", C + "morcants-heavy-stubber-schematic-3"),
 ("c_walk", "Walking plate", "R", "muzzle", {"hs"}, None, None, 1, "one string across up to 3 standing abreast; the swap's -1 once per extra target", C + "morcants-heavy-stubber-schematic-3"),
 ("c_rig", "One-piece crossdraw rig", "C", "holster", PIST, None, None, 1, "+1 quick-draw", C + "teys-hellpistol-schematic-4"),
 ("c_bridged", "Bridged double-cell belt pack", "U", "mag", {"lp"}, "hellpistol", None, 1, "60 shots on the cable", C + "teys-hellpistol-schematic-4"),
 ("c_longbarrel", "Long barrel", "C", "barrel", {"lr"}, None, None, 1, "+1 aimed past ~30 m; -1 inside ~5 m", C + "vargas-mercy-schematic-6"),
 ("c_lrscope", "Custom long-range scope", "U", "optic", RIFLE, None, None, 1, "+2 aimed past ~30 m (telescopic: -1 hip/snap and inside ~15 m)", C + "vargas-mercy-schematic-6"),
 ("c_dualmount", "Dual riser mount with a canted reflex", "U", "optic2", RIFLE, None, "scope", 1, "the scope's close penalty never applies (the reflex: +2 aimed inside ~30 m); one optic at a time; -1 quick-draw", C + "vargas-mercy-schematic-6"),
 ("c_energy", "Energy selector (LIGHT / MED / HEAVY)", "R", "selector", {"lr"}, "hellgun|hot-shot", None, 1, "MED: 2 pack a shot, heavy carapace at any range, +1 heat a string; HEAVY: 3 pack a shot, through ceramite-forged, +2 heat a shot; vent at 3", C + "vargas-mercy-schematic-6"),
 ("c_rangef", "Custom range-finder", "U", "optic2", RIFLE, None, "scope", 1, "+2 aimed past ~30 m (rides the scope)", C + "isks-patience-schematic-7"),
 ("c_hbarrel", "Heavy long barrel", "C", "barrel", {"lr", "sr", "nr"}, None, None, 1, "+2 aimed; -1 hip, snap and on the move", C + "isks-patience-schematic-7"),
 ("c_bipod", "Custom bipod", "C", "under", RIFLE | {"hs"}, None, None, 1, "braced or prone, a chain miss costs no -1; a beat to set up", C + "isks-patience-schematic-7"),
 ("c_generator", "Intensified laser generator", "R", "generator", {"lr"}, None, None, 1, "3 pack a shot: +1 aimed, through ceramite-forged; a string of 3 adds 1 heat", C + "isks-patience-schematic-7"),
 ("c_short", "Cut-down short barrel", "C", "barrel", {"lr", "sr"}, None, None, 1, "+1 inside ~15 m; -1 past ~30 m", C + "kells-officer-schematic-8"),
 ("c_skelgrip", "Skeleton grip", "C", "grip", RIFLE, None, None, 1, "no swap penalty; -1 aimed past ~30 m", C + "kells-officer-schematic-8"),
 ("c_stockmag", "Stock magazine slot", "C", "stockmag", {"lr"}, None, None, 1, "the first reload each fight costs no beat", C + "kells-officer-schematic-8"),
 ("c_twin", "Twin-shot switch", "R", "selector", {"lr"}, None, None, 1, "TWIN: a hit drops a step, one armour tier harder, 2 hits toward wear-down; 2 pack a shot", C + "kells-officer-schematic-8"),
 ("c_krak", "Underslung krak launcher", "R", "under", {"lr", "sr"}, None, None, 1, "one krak a beat out to ~60 m, rolled like a throw; a beat to reload", C + "tavis-tiny-schematic-9"),
 ("c_shotstock", "Heavy shotgun stock with grenade loops", "C", "stock", {"lr", "sr", "sg"}, None, None, 1, "+1 aimed; -1 swapping; 3 grenade loops", C + "tavis-tiny-schematic-9"),
 ("c_sling", "Quick-release sling", "C", "sling", RIFLE | {"smg", "sg"}, None, None, 1, "dropping it to his chest or bringing it up costs nothing", C + "sallows-carbine-schematic-10"),
 ("c_medstock", "Hollow medicine-cabinet stock", "C", "stock", {"lr", "sr"}, None, None, 1, "a stimm, a bandage and a tourniquet inside: he patches from the gun; -1 aimed past ~30 m", C + "sallows-carbine-schematic-10"),
 ("c_popgrip", "Hollow pop-lock grip", "C", "grip", HAND, None, None, 1, "one more stimm or bandage inside", C + "sallows-carbine-schematic-10"),
 ("c_charger", "Tuned charger", "U", "action", {"lp", "lr"}, None, None, 1, "strings up to 7; no hit bonuses in the string, misses still -1", C + "sallows-carbine-schematic-10"),
 ("c_gripcover", "Ergonomic grip cover (stock removed)", "C", "stock", {"smg", "sg"}, None, None, 1, "+1 quick-draw; fits a holster", C + "corvanes-shotlas-schematic-11"),
 ("c_charge", "Charge trigger and capacitor", "R", "selector", {"lp", "lr"}, None, None, 1, "a charge beat draws up to 30 pack, next beat one bolt: 25-30 plasma punch, 20-24 hellgun + heavy carapace, 10-19 hellgun; fire it next beat or lose it; 20+: a vent beat", C + "corvanes-shotlas-schematic-11"),
 ("c_heartbeat", "Heartbeat scanner", "R", "siderail", RIFLE | {"smg"}, None, None, 1, "heartbeats through walls to ~30 m; while he watches it, nobody with a heartbeat surprises him", C + "brenners-accatran-schematic-12"),
 ("c_needlebarrel", "Long needle barrel", "C", "barrel", {"np"}, None, None, 1, "reach ~35 m; +1 aimed; -1 quick-draw", C + "nessas-needle-pistol-schematic-13"),
 ("c_burst3", "Three-round burst with its tower grip", "R", "selector", {"lr"}, None, None, 1, "a string is 2 bursts, each one roll of 3 bolts: a hit drops a step, one armour tier harder, 3 hits toward wear-down; 3 pack a burst", C + "sorels-hellgun-schematic-14"),
 ("c_counter", "Helm-linked ammo counter", "U", "counter", HAND | {"hs", "hv", "hf", "fl"}, None, None, 1, "he always knows his count: never caught dry", C + "sorels-hellgun-schematic-14"),
 ("c_vent", "Third vent channel", "U", "vent", {"pp", "pg"}, None, None, 1, "sheds 1 heat at the end of every beat", C + "ferros-ryza-plasma-pistol-schematic-15"),
 ("c_pcharge", "Plasma charge (hold the trigger)", "R", "selector", {"pp", "pg"}, None, None, 1, "quick: one shot, +1 extra step, +2 heat, 2 cell; full: hold a beat, +2 extra steps, +3 heat, 3 cell", C + "ferros-ryza-plasma-pistol-schematic-15"),
 ("c_gaspiston", "Plasteel spring and gas-piston trigger", "R", "action", {"gl"}, None, None, 1, "2 grenades a string; the second -1 for the kick", C + "holliss-six-bells-schematic-16"),
 ("c_angled", "Angled handguard grip (fitted)", "C", "grip", {"gl"}, None, "c_gaspiston", 1, "no -1 on the second grenade", C + "holliss-six-bells-schematic-16"),
 ("c_arc", "Arc calculator", "R", "arc", {"gl", "mo"}, None, None, 1, "+3 on launcher shots past ~30 m, the first shot or a repeat on the same spot; the beams show in smoke", C + "holliss-six-bells-schematic-16"),
 ("c_lever", "New lever linkage", "U", "action", {"sr"}, "lever", None, 1, "single lever chains up to 7, double up to 4; above 6, no hit bonuses", C + "tamsins-kasr-frontier-schematic-17"),
 ("c_twintubes", "Twin side-by-side tubes", "U", "mag", {"sr"}, "lever", None, 1, "36 rounds; -1 swapping", C + "tamsins-kasr-frontier-schematic-17"),
 ("c_tubesel", "Tube selector", "U", "tubesel", {"sr"}, "lever", "c_twintubes", 1, "each tube its own load; flicking it is free", C + "tamsins-kasr-frontier-schematic-17"),
 ("c_pushload", "Push-loaders", "C", "loader", {"sr", "sg"}, "lever|pump", None, 1, "refill a tube in the beat's move", C + "tamsins-kasr-frontier-schematic-17"),
 ("c_box100", "100-round box mags", "U", "mag", {"sr"}, "autogun|columnus", None, 1, "100 rounds; a loaded box -1 swapping and quick-draw", C + "tamsins-columnus-schematic-18"),
 ("c_superv", "The Super V", "R", "action", {"sr"}, "autogun|columnus", None, 1, "auto strings up to 12, recoil 0; auto still no hit bonuses", C + "tamsins-columnus-schematic-18"),
 ("c_finned", "Short finned barrel", "U", "barrel", {"sr"}, "autogun|columnus", None, 1, "+1 inside ~10 m, -2 past ~30 m; strings of 8+ build 1 heat, the fins shed 1 when it doesn't fire; -1 swapping", C + "tamsins-columnus-schematic-18"),
]
KEYS = {a[0] for a in A}
# Custom parts that don't go in the gun roll, and why (shown on the sheet).
NOT_ROLLED = [
 ("Stinger's frame rails; Dace's top and bottom rails", "no rule of their own"),
 ("Sorel's and Six Bells' adjustable tube stocks", "they rule as the light rifle stock, which is on the list"),
 ("Ferro's matched fill", "it's matched to Ferro's own reclamator"),
 ("The Columnus magwell cut", "it takes Stinger's sticks: Tamsin's guns only"),
 ("The Frontier's plasteel tube springs", "no rule of their own"),
 ("Sorel's blacklight visor", "helm gear, not a gun part: the DM gives it to a tracker"),
 ("Varga's drop rig and harness lanyard", "jumper gear, not gun parts: the DM gives them to a jumper"),
]

SKIP = re.compile(r"web pistol|bolt-pipe|rivet gun|harpoon|turret|gauntlet|hellstrike|flare|^'")
TYPES = [("pp", r"plasma pistol"), ("pg", r"plasma gun"), ("bp", r"bolt pistol"),
         ("hv", r"heavy bolter|autocannon|lascannon|multi-laser"), ("hs", r"heavy stubber"), ("br", r"boltgun"),
         ("hf", r"hand flamer"), ("fl", r"flamer|torch-thrower|promethium sprayer"), ("mg", r"meltagun|melta gun"),
         ("gl", r"grenade launcher"), ("mo", r"mortar"), ("np", r"needle pistol"), ("nr", r"needle rifle"),
         ("lr", r"shotlas"), ("smg", r"submachine|machine pistol|rattler|\bsmg\b|chain-fed autopistol"),
         ("lp", r"laspistol|las pistol|hellpistol"),
         ("sp", r"autopistol|revolver|stub pistol|stub automatic|hand cannon|boarding pistol|hammerfall|pipe pistol"),
         ("sg", r"shotgun|sawn-off|scattergun|nailer|ripper gun"),
         ("lr", r"lasgun|lascarbine|hellgun|long-las|las-box|las-lmg|volley gun|battery las"),
         ("sr", r"autogun|autorifle|stub rifle|lever-action|pipe rifle|hunting rifle")]
MTYPES = [("sh", r"shield"), ("pw", r"power (sword|axe|maul|knife|fist|mace|blade|odachi)|thunder hammer|relic blade"),
          ("ch", r"chainsword|chain axe|chain-axe|chain knife|chain glaive|chain blade|eviscerator"),
          ("bl", r"knife|machete|cutlass|sabre|sword|cleaver|axe|shank|blade|stiletto|shovel"),
          ("bt", r"club|maul|mace|hammer|flail|baton|prod|knuckle|girder|pick\b")]
BUILTIN = [("optic", r"scope|range-finder|sprinter|kasr lance"), ("mag", r"drum|100-shot box"),
           ("muzzle", r"silenced|suppressed"), ("bayonet", r"bayonet|krieg"), ("tripod", r"tripod"),
           ("barrel", r"heavy barrel|long barrel|long-barrel|stub barrel"), ("stock", r"folding stock")]


def guns_in(text):
    """The weapons in a kit string (guns, then melee): [(type, label, count, builtins, src)]."""
    out = []
    for chunk in text.split(" | "):
        for piece in chunk.split(" + "):
            found = []
            for sub in piece.split(" and "):
                for frag in sub.split(", "):  # one weapon per fragment; turrets, odd scrap guns, 'X' pattern skipped
                    low = re.sub(r"^.*?: ", "", frag.lower())
                    if SKIP.search(low):
                        continue
                    t = next((t for t, p in TYPES if re.search(p, low)), None) or \
                        next((t for t, p in MTYPES if re.search(p, low) and "bayonet" not in low), None)
                    if t:
                        found.append((t, frag))
            for t, sub in found:
                src = (piece if len(found) == 1 else sub).lower()
                taken = {s for s, p in BUILTIN if re.search(p, src)}
                label = re.sub(r"^.*?: ", "", sub).split(",")[0].split(" (")[0].split(" with ")[0].strip()
                label = re.sub(r"^(two|a|an) ", "", label)
                n = 2 if re.search(r"\btwo\s", sub.lower()) else 1  # 'two pistols', not a two-man team
                out.append((t, label, n, taken, src))
    return out


def roll_gun(gtype, src, taken, level, team, weights):
    """Roll one gun's attachments. Returns (d100 rolls, [attachment rows])."""
    chance = CHANCE[level] + (10 if team else 0)
    taken, have, got, rolls = set(taken), set(), [], []
    if "optic" in taken and re.search(r"scope|sprinter|kasr lance", src):
        have.add("scope")
    for _ in range(8):
        d = random.randint(1, 100)
        rolls.append(d)
        if d > chance:
            break
        cands = [a for a in A if gtype in a[4] and a[3] not in taken and a[0] not in have
                 and (a[5] is None or re.search(a[5], src)) and (a[6] is None or a[6] in have)
                 and not (level == "poor" and a[2] == "R")]
        if not cands:
            break
        tiers = [t for t in weights if weights[t] and any(a[2] == t for a in cands)]
        if not tiers:
            break
        tier = random.choices(tiers, weights=[weights[t] for t in tiers])[0]
        a = random.choice([a for a in cands if a[2] == tier])
        got.append(a)
        taken.add(a[3])
        have.add(a[0])
        if a[0] in ("tele", "c_lrscope"):
            have.add("scope")
    return rolls, got


def describe(text, level, team, weights):
    """One line listing what every weapon in this kit rolled, or '' if nothing."""
    parts = []
    for t, label, n, taken, src in guns_in(text):
        for i in range(n):
            rolls, got = roll_gun(t, src, taken, level, team, weights)
            if got:
                name = label + (f" #{i + 1}" if n > 1 else "")
                bits = "; ".join(f"{'CUSTOM ' if a[7] else ''}{a[1]} ({a[2]}: {a[8]})" for a in got)
                parts.append(f"{name}: {bits} [d100 {', '.join(map(str, rolls))}]")
    return " || ".join(parts)


def md():
    rar = {"C": "common", "U": "uncommon", "R": "rare"}
    print("| Attachment | Rarity | Slot | Fits | What it does | Full entry |")
    print("| --- | --- | --- | --- | --- | --- |")
    for key, name, r, slot, fits, kw, needs, custom, rule, link in sorted(A, key=lambda a: (a[7], a[3], a[1])):
        f = ", ".join(sorted(NAMES[x] for x in fits))
        if kw:
            f += f" (only: {kw.replace('|', ' or ')})"
        if needs:
            f += f" (needs {'a scope' if needs == 'scope' else next(a[1] for a in A if a[0] == needs)})"
        tag = " *(Custom)*" if custom else ""
        print(f"| **{name}**{tag} | {rar[r]} | {slot} | {f} | {rule} | [{link.split('#')[0]}]({link}) |")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "md":
        md()
    else:  # quick test: python3 attachments.py "kit text" LEVEL
        w = {"poor": {"C": 80, "U": 20, "R": 0}, "steady": {"C": 70, "U": 25, "R": 5}, "good": {"C": 55, "U": 35, "R": 10},
             "rich": {"C": 40, "U": 45, "R": 15}, "wealthy": {"C": 25, "U": 50, "R": 25}}
        lvl = sys.argv[2] if len(sys.argv) > 2 else "good"
        print(guns_in(sys.argv[1]))
        print(describe(sys.argv[1], lvl, False, w[lvl]))

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

# bw bow (day 47: only arrows roll; see catalogue/bows.md).
# Gun types: lp las pistol, lr las rifle/carbine, sp stub pistol, smg, sr stub rifle/autogun, sg shotgun,
# bp bolt pistol, br boltgun, pp plasma pistol, pg plasma gun, np needle pistol, nr needle rifle,
# hf hand flamer, fl flamer, hs heavy belt stubber, hv other heavy weapon, gl grenade launcher, mo mortar, mg meltagun.
PIST = {"lp", "sp", "bp", "pp", "np"}
RIFLE = {"lr", "sr", "br", "pg", "nr"}
SIGHT = PIST | RIFLE | {"smg", "sg", "mg"}
RECOIL = {"sp", "smg", "sr", "sg", "bp", "br", "hs"}
HAND = SIGHT  # guns a hand holds and a grip sleeve fits
# Melee (day 47): ch chain, pw power, bl edged blade, bt blunt, sh shield.
MELEE = {"ch", "pw", "bl", "bt", "st"}  # st: psyker staffs and staves (day 48)
NOGLOVE = r"^(?!.*(glove|fist|knuckle|claws)).*"  # worn weapons take no grip, strap, pommel or length parts (day 48 audit)
STUBCAL = r"(?<!auto-)revolver|stub pistol|stub automatic|hand cannon|lever|hunting stub|stub rifle|boarding pistol"
AUTOCAL = r"autogun|autopistol|autorifle|auto-revolver|hammerfall|submachine|rattler|machine pistol|chain-fed|solid stag|burst pistol"
NAMES = {"lp": "las pistols", "lr": "las rifles", "sp": "stub pistols", "smg": "SMGs", "sr": "autoguns and stub rifles",
         "sg": "shotguns", "bp": "bolt pistols", "br": "boltguns", "pp": "plasma pistols", "pg": "plasma guns",
         "np": "needle pistols", "nr": "needle rifles", "hf": "hand flamers", "fl": "flamers", "hs": "heavy belt stubbers",
         "hv": "heavy weapons", "gl": "grenade launchers", "mo": "mortars", "mg": "meltaguns",
         "bw": "bows", "ch": "chain weapons", "pw": "power weapons", "bl": "blades", "bt": "blunt weapons", "sh": "shields", "st": "psyker staffs"}

K = "kit.md#"
MORE = K + "more-attachments-player-picks-ash-on-ostrava-session-10"
C = "attachments.md#"  # custom builds, same folder
# (key, name, rarity, slot, fits, keyword the gun's name must have or None, needs key or None, custom, rule, link)
A = [
 # --- traditional ---
 ("reflex", "Reflex sight", "U", "optic", SIGHT, None, None, 0, "+2 aimed inside ~30 m; -1 past ~30 m", K + "pistol-reflex-sight"),
 ("holo", "Holo sight", "U", "optic", SIGHT, None, None, 0, "+1 aimed inside ~50 m; -1 hip shots", K + "holo-sight"),
 ("tele", "10x scope", "U", "optic", RIFLE | {"hs"}, None, None, 0, "+2 long shots, +1 more past ~150 m; -1 hip/snap and inside ~15 m", MORE),
 ("lowlight", "Low-light optic", "U", "optic", SIGHT, None, None, 0, "no darkness penalty through it; a flash blinds him a beat", MORE),
 ("rangef", "Range-finder sight", "R", "mount", RIFLE, None, None, 0, "+1 past ~30 m; a box on the side rail: stacks with the optic on top", K + "range-finder-sight"),
 ("offset", "Offset backup sight", "U", "mount", RIFLE, None, "scope", 0, "cancels the scope's close penalty; -1 quick-draw", MORE),
 ("laser", "Laser sight", "U", "laser", SIGHT, None, None, 0, "+1 hip inside ~20 m, or +1 after a swap inside ~30 m (not both); the beam shows", K + "laser-sight-under-mount-lumen-or-both"),
 ("tapedlight", "Taped flashlight", "C", "tape", SIGHT | {"hs", "hf", "fl"}, None, None, 0, "a lumen on any gun, slot or not; the beat's move to flick on or off; can't blind", K + "taped-flashlight"),
 ("floodbeam", "Floodbeam lumen", "U", "laser", SIGHT | {"hs", "fl"}, None, None, 0, "no darkness penalty to ~50 m; in a face inside ~15 m: -3 on their next roll; strobe: -1 on shots in the beam inside ~10 m; seen from ~200 m", K + "floodbeam-lumen"),
 ("lumen", "Under-mount lumen", "C", "laser", SIGHT | {"hs", "fl"}, None, None, 0, "no darkness penalty in the beam; he's lit up too; in a face inside ~5 m in the dark: -2 on their next roll", K + "laser-sight-under-mount-lumen-or-both"),
 ("combo", "Laser and lumen combo", "U", "laser", SIGHT, None, None, 0, "both, switched on alone or together; the lumen can blind (in a face inside ~5 m in the dark: -2 on their next roll)", K + "laser-sight-under-mount-lumen-or-both"),
 ("match", "Match trigger", "U", "trigger", PIST | RIFLE | {"smg", "sg"}, None, None, 0, "+1 aimed; -1 hip/snap", MORE),
 ("hair", "Hair trigger", "U", "trigger", PIST | RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot of every string; drop-prone", MORE),
 ("pin", "Pressure-pin safety", "U", "pin", PIST | RIFLE | {"smg", "sg"}, None, "hair", 0, "the hair trigger isn't drop-prone while pinned", K + "pressure-pin-safety-hair-triggers"),
 ("limiter", "Burst limiter", "C", "limiter", {"smg", "sr", "br", "hs"}, None, None, 0, "recoil -1; strings capped at 3", MORE),
 ("ergofg", "Ergo foregrip", "C", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot", K + "foregrips-under-barrel-slot"),
 ("heavyfg", "Heavy foregrip", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+2 aimed; a chain miss costs -2; Handling -1", K + "foregrips-under-barrel-slot"),
 ("lumengrip", "Lumen foregrip", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot; a lumen (no darkness penalty in the beam, can blind); the switch is free", K + "foregrips-under-barrel-slot"),
 ("handstop", "Handstop foregrip", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+2 on the first shot; Handling +1; -1 aimed", K + "foregrips-under-barrel-slot"),
 ("bipod", "Bipod", "C", "under", RIFLE | {"hs"}, None, None, 0, "+2 aimed braced or prone; a beat to set up", MORE),
 ("ugl", "Underslung grenade launcher", "R", "under", {"lr", "sr", "br"}, None, None, 0, "one grenade shot without swapping; -1 aimed; a beat to reload", MORE),
 ("masterkey", "Underslung shotgun (masterkey)", "U", "under", {"lr", "sr", "br"}, None, None, 0, "one or two shotgun blasts; -1 aimed", MORE),
 ("bayonet", "Bayonet (fixed)", "C", "bayonet", {"lr", "sr"}, None, None, 0, "a spear thrust in melee: chains 2, +1 to strike first; Bayonet Charge", K + "bayonet"),
 ("chainbay", "Underslung chain-bayonet", "R", "bayonet", {"lr", "sr"}, None, None, 0, "fights as a chainsword (-1 block/parry); -1 hip snap shots; Bayonet Charge", K + "underslung-chain-bayonet"),
 ("tacstock", "Tac rifle stock", "U", "stock", {"lr", "sr", "br", "sg"}, None, None, 0, "+1 first shot, +1 aimed; Handling -2", K + "rifle-stocks-autogun-lasgun-stub-rifle"),
 ("lightstock", "Light rifle stock", "C", "stock", {"lr", "sr", "br", "sg"}, None, None, 0, "Handling +2; -1 aimed", K + "rifle-stocks-autogun-lasgun-stub-rifle"),
 ("foldstock", "Folding stock", "C", "stock", {"lr", "sr", "smg", "sg"}, None, None, 0, "+1 quick-draw; -1 aimed", MORE),
 ("silencer", "Standard silencer", "U", "muzzle", {"sp", "smg", "sr"}, None, None, 0, "quieter; recoil -1; -1 quick-draw; Dirty after ~20 shots", K + "muzzles"),
 ("suppressor", "Heavy suppressor", "U", "muzzle", {"sp", "smg", "sr"}, None, None, 0, "near-silent; recoil -2; -1 quick-draw; Handling -1; Dirty after ~20 shots", K + "muzzles"),
 ("comp", "Compensator", "U", "muzzle", RECOIL | {"bp", "br"}, None, None, 0, "recoil -2; +1 more after each hit; -1 aimed", K + "muzzles"),
 ("brake", "Muzzle brake", "U", "muzzle", RECOIL, None, None, 0, "a chain miss costs no -1; the flash places him after his first string", K + "muzzles"),
 ("flashhider", "Flash hider", "C", "muzzle", RECOIL, None, None, 0, "his shots don't give him away in the dark", MORE),
 ("extmag", "Extended magazine", "U", "mag", {"sp", "smg", "sr"}, None, None, 0, "+50% rounds (autogun and stub only; audit A5)", K + "extended-magazine-kits"),
 ("extlas", "Extended las pack", "U", "mag", {"lp", "lr"}, r"^(?!.*(hellgun|hellpistol|hell revolver|hell shotgun|hot-shot|volley gun)).*", None, 0, "60 shots, not 45", "las.md#extended-las-pack"),
 ("exths", "Extended hot-shot pack", "U", "mag", {"lp", "lr"}, r"hellgun|hellpistol|hell revolver|hell shotgun|hot-shot|volley gun", None, 0, "40 shots, not 30", "las.md#extended-hot-shot-pack"),
 ("drum", "Pistol drum", "U", "mag", {"sp", "smg", "lp"}, None, None, 0, "twice the shots; no quick-draw holster, -1 quick-draw", K + "pistol-drums"),
 ("tunedcell", "Tuned plasma cell", "R", "mag", {"pp", "pg"}, None, None, 0, "12 shots, not 8", "plasma.md#tuned-plasma-cell"),
 ("weighted", "Weighted grip", "C", "grip", {"sp", "smg", "sr", "sg", "bp", "br"}, None, None, 0, "recoil -1; -1 quick-draw", MORE),
 ("sleeve", "Ergo grip sleeve", "C", "sleeve", HAND, None, None, 0, "never slips from his hand; disarms against him -2", K + "ergo-grip-sleeve"),
 ("cbarrel", "Custom barrel", "U", "barrel", {"sp", "smg"}, None, None, 0, "+1 on aimed shots", K + "custom-barrel-stub-pistols-and-smgs-barrel-slot"),
 ("shockcoil", "Shock-coil kit", "R", "coil", HAND | {"hs", "hv"} | MELEE, None, None, 0, "after a hit, +1 on his next roll against that target (6 charges a fight)", K + "shock-coil-kit"),
 ("autocrystal", "Las auto-fire crystal", "R", "action", {"lr"}, r"^(?!.*(hot-shot|hellgun)).*(lasgun|lascarbine)", None, 0, "strings up to 12; no hit bonuses in the string, misses still -1; strings of 8+ build 1 heat, vent at 3", K + "las-auto-fire-crystal"),
 ("sweep", "Sweep emitter", "U", "muzzle", {"hv", "lr"}, r"multi-laser|multilaser|las-box|las-lmg|kasr rain", None, 0, "one string across up to 3 standing abreast; the swap's -1 once per extra target", K + "sweep-emitter"),
 ("repeater", "Repeater crystal", "R", "action", {"lp", "lr"}, None, None, 0, "strings up to 7; no chain bonuses in the string, misses still -1", K + "repeater-crystal"),
 # melee (day 47)
 ("tuning", "Power weapon tuning kit", "R", "field", {"pw"}, None, None, 0, "+1 to parry with it; its power cell lasts twice as long (60 power-mode swings)", K + "power-weapon-tuning-kit"),
 ("whetstone", "Diamantine whetstone", "U", "hone", {"bl"}, None, None, 0, "honed before the fight: +1 pierce on its next 2 hits (~10 uses)", K + "diamantine-whetstone"),
 ("spikes", "Spiked shield", "U", "spikes", {"sh"}, None, None, 0, "+3 on a shield-first charge, then +1 attacking with the shield", K + "spiked-shield-mod"),
 ("viewslot", "Shield viewing slot", "U", "slot", {"sh"}, None, None, 0, "sees and shoots a pistol through it without leaving cover; planted, slot fire -2", K + "shield-viewing-slot-mod"),
 ("extender", "Shield extender", "U", "extender", {"sh"}, None, None, 0, "bolt-on wings and a skirt: the shield gives one more level of cover (light to half, half to heavy, heavy to full from the front)", "kit.md#melee-attachments-day-48"),
 # melee, more (the player, day 48): regular and custom; full entries in kit.md, Melee attachments (day 48)
 ("leather", "Leather-wrap grip", "C", "mgrip", MELEE, NOGLOVE, None, 0, "never slips in wet or bloody hands; disarms against him -2", "kit.md#melee-attachments-day-48"),
 ("pstrap", "Wrist pommel strap", "C", "strap", {"bl", "bt", "pw"}, NOGLOVE, None, 0, "knocked from his hand, it's back in it next beat, free", "kit.md#melee-attachments-day-48"),
 ("basket", "Basket hilt", "U", "guard", {"bl", "pw", "bt"}, r"sword|sabre|cutlass|rapier|jian", None, 0, "+1 to parry", "kit.md#melee-attachments-day-48"),
 ("serrated", "Serrated edge", "U", "edge", {"bl"}, None, None, 0, "against no armour a hit drops an extra step; anyone it downs is -2 on the survival d6 after the fight", "kit.md#melee-attachments-day-48"),
 ("flanged", "Flanged head", "U", "head", {"bt"}, None, None, 0, "on a solid hit, through one armour step further than it normally gets", "kit.md#melee-attachments-day-48"),
 ("rim", "Sharpened rim", "U", "rim", {"sh"}, None, None, 0, "a shield bash counts as a blade hit", "kit.md#melee-attachments-day-48"),
 ("scrapspikes", "Scrap spikes", "C", "head", {"bt"}, None, None, 0, "dents and bites: a solid hit when he beats the number by 2+, not 3+", "kit.md#melee-attachments-day-48"),
 ("tristand", "Tri-stand", "U", "stand", {"sh"}, None, None, 0, "planting or lifting the shield is the beat's short move (plant and shoot, or lift and shoot; no other move); planted: full cover from the front, hands free: he shoots from it by peek and duck", "kit.md#melee-attachments-day-48"),
 ("widehilt", "Wide hilt", "C", "guard", {"bl", "pw", "bt"}, r"sword|sabre|cutlass|rapier|jian", None, 0, "+1 to parry; -1 on the first swing of a chain", "kit.md#melee-attachments-day-48"),
 ("spikepommel", "Spiked pommel", "U", "pommel", {"bl", "bt", "pw", "ch"}, r"^(?!.*(two-handed|great|eviscerator|shovel|glaive|sledge|headsman|glove|fist|knuckle)).*", None, 0, "one more swing at the end of every chain: a pommel strike; a hit drops no health step, it only staggers (-1 on their next roll) and counts 2 toward wear-down", "kit.md#melee-attachments-day-48"),
 ("regulator", "Staff regulator", "R", "regulator", {"st"}, None, None, 0, "every charged power takes 1 more beat to charge, but no Perils roll while it's fitted", "kit.md#melee-attachments-day-48"),
 ("c_blazeenh", "Blaze force enhancer", "R", "enhancer", {"bl", "st"}, r"force (sword|greatsword|staff|stave|blade)|blaze force|scrap force|witch-knife|\bstaff\b|\bstave\b", None, 1, "imbued (a psyker's hands): a hit drops one extra health step (1.0); a raw 1-3 on an imbued swing and the warp flings it out of his hands (~d6 m; a beat to fetch)", "kit.md#melee-attachments-day-48"),
 ("longreach", "Longer grip or blade", "U", "length", {"bl", "bt", "pw", "ch"}, NOGLOVE, None, 0, "longer reach: moving mid-chain, up to 7 m a beat between swings, not 5", "kit.md#melee-attachments-day-48"),
 ("tsuka", "Tsuka grip", "R", "mgrip", {"bl", "pw", "bt"}, r"sword|sabre|cutlass|odachi|katana|jian", None, 0, "leverage, blade control, some shock absorption: +1 on swings, +1 to parry, +1 on his disarm attempts", "kit.md#melee-attachments-day-48"),
 # melee handling parts (the player, day 48): full entries in kit.md, Melee Handling and handling parts
 ("fuller", "Fullered blade", "U", "fuller", {"bl", "pw"}, r"^(?!.*(glove|fist|knuckle|shovel|cleaver)).*", None, 0, "Handling +1; -1 to parry", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 ("skelhaft", "Skeletonized haft", "U", "haft", {"bl", "bt", "pw"}, r"axe|hammer|mace|maul|pick\b|morning star", None, 0, "Handling +2; a natural 1 on a swing or parry cracks it (Handling 0, -1 on swings till fixed)", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 ("shorthaft", "Shortened haft", "C", "haft", {"bl", "bt", "pw", "ch"}, r"two-handed|great|eviscerator|glaive|sledge|headsman|thunder hammer|crusher|war hammer", None, 0, "Handling +2; Strength behind the blow needs STR 60+, not 50+", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 ("cwpommel", "Counterweight pommel", "C", "pommel", {"bl", "ch", "pw"}, r"^(?!.*(glove|fist|knuckle|axe|shovel)).*(sword|sabre|cutlass|rapier|jian|knife|dagger|blade|machete|stiletto|odachi|katana|wakizashi)", None, 0, "Handling +1", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 ("wtdhead", "Weighted head", "U", "head", {"bt"}, None, None, 0, "Handling -2; Strength behind the blow at STR 40+, not 50+", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 ("lightbar", "Lightened chain bar", "U", "bar", {"ch"}, None, None, 0, "Handling +1; -1 on Saw Lock's STR contest", "kit.md#melee-handling-and-handling-parts-the-player-day-48"),
 # flamers and mortars, more (the player, day 48): full entries in scrap.md, Flamer and mortar parts (day 48)
 ("sglong", "Long shotgun barrel", "U", "barrel", {"sg", "lr"}, r"^(?!.*(sawn-off|pipe|junk|nailer)).*(shotgun|scattergun|shotlas|ripper)", None, 0, "the close blast reaches ~20 m, not ~15; -1 on quick-draws", "stub.md#long-shotgun-barrel"),
 ("tubestock", "Tube stock", "C", "stock", {"lr", "sr", "br", "smg", "sg"}, None, None, 0, "Handling +2; +1 on shots inside ~10 m; +1 recoil", "kit.md#gun-parts-day-48"),
 ("c_accel", "Shot accelerator", "R", "barrel", {"sp", "smg", "sr", "sg", "hs"}, None, None, 1, "one armour step further (gets through and dents); range half as far again; inside ~15 m a shrugged hit counts 2 toward wear-down and a hit that gets through drops an extra step; +1 heat every 6 shots, vent at 3", "kit.md#gun-parts-day-48"),
 # optics, lasers, grips and sleeves (the player, day 48): full entries in kit.md
 ("cheek", "Cheek rest", "C", "cheek", {"lr", "sr", "br", "sg"}, None, None, 0, "+1 aimed with an optic on the gun; with iron sights -1 aimed", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("acog", "Combat scope (3.5x)", "U", "optic", RIFLE | {"smg", "sg", "hs"}, None, None, 0, "+1 aimed past ~15 m; -1 hip inside ~10 m", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("cqcscope", "CQC scope (1.5x)", "U", "optic", RIFLE | {"smg", "sg"}, None, None, 0, "+1 aimed inside ~30 m and +1 on the first shot after a swap; -1 aimed past ~60 m", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("var6", "Variable scope (1-6x)", "C", "optic", RIFLE | {"smg", "sg", "hs"}, None, None, 0, "1x: +1 aimed inside ~30 m; 6x: +1 aimed past ~30 m, -1 hip and inside ~15 m; switching uses the short move; -1 quick-draw", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("var7", "Variable scope (1-7x)", "U", "optic", RIFLE | {"smg", "sg", "hs"}, None, None, 0, "1x: +1 aimed inside ~30 m; 7x: +2 aimed past ~30 m, -1 hip and inside ~15 m; switching uses the short move; -1 quick-draw", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("var9", "Variable scope (1-9x)", "R", "optic", RIFLE | {"smg", "sg", "hs"}, None, None, 0, "1x: +2 aimed inside ~30 m; 9x: +2 aimed past ~30 m, +1 more past ~150 m, -1 hip inside ~15 m; switching is free; -1 quick-draw", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("monopod", "Grip monopod", "U", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 aimed braced; the leg drops in the beat's move, no set-up beat; Handling -1 while it's down", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("irlaser", "IR laser", "R", "laser", SIGHT, None, None, 0, "+1 hip inside ~20 m, only with a low-light optic or night goggles; only that kind of gear sees the beam", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("greenlaser", "Green laser", "U", "laser", SIGHT, None, None, 0, "+2 hip inside ~30 m, day or night; spotted easily: anyone looking for him +2", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("bluelaser", "Blue laser", "U", "laser", SIGHT, None, None, 0, "+1 hip inside ~20 m; in the dark or smoke +2 out to ~30 m; nothing in bright daylight; the beam shows like a normal laser", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("scrapscope", "Scrap scope", "C", "optic", RIFLE | {"sg", "hs"}, None, None, 0, "+1 long shots; -1 hip and inside ~15 m; slips on a natural 1: no bonus until half a beat re-seating it", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("scrapvert", "Scrap vertical grip", "C", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 on the first shot; works loose on a natural 1: -1 on shots until half a beat tightening it", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("scrapv", "Scrap V grip", "C", "under", RIFLE | {"smg", "sg"}, None, None, 0, "+1 hip; snaps off for good on a natural 1", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("scrapcush", "Scrap cushioned stock", "C", "stock", {"lr", "sr", "br", "smg", "sg"}, None, None, 0, "recoil -1; -1 aimed past ~30 m", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("roundsleeve", "Rifle round sleeve", "C", "saddle", {"sr"}, r"lever|hunting|pipe rifle|bolt-action|break-action", None, 0, "holds 10 rounds; every top-up from it loads 2 more", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("shellsleeve", "Shotgun shell sleeve", "C", "saddle", {"sg"}, r"^(?!.*(sawn-off|pistol)).*", None, 0, "holds 7 shells; every top-up from it loads 2 more (4 a half beat becomes 6)", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("skelguard", "Skeleton handguard", "C", "handguard", {"lr", "sr", "br", "smg", "sg"}, None, None, 0, "Handling +2; +1 recoil", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("c_biopin", "Bio-scanner firing pin", "R", "biolock", SIGHT | {"hs"}, None, None, 1, "bonded to one owner's hands: nobody else can fire it until it's hacked (INT tech vs 15, a bench, an hour; fail by 5+ fries the pin); bloody or gloved hands: a natural 1 doesn't read, half a beat to wipe and regrip; picked up mid-fight it's hidden (half a beat and Perception vs 13 to spot), fired blind the shooting that beat is gone", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("c_intsupp", "Full-barrel suppressor", "R", "barrel", {"sp", "smg", "sr"}, None, None, 1, "blocks the muzzle slot; silent; recoil -1; jams on a natural 1; heat 1 at 10 shots, 2 at 20, -1 each beat not firing; fired past heat 2 it jams on 1-5; then after the fight a d6: 1-2 broken (a day at a bench), 3 minor adjustments (30 min at a bench, or -1 next fight), 4-6 fine", "kit.md#optics-lasers-grips-and-sleeves-the-player-day-48"),
 ("sprayer", "Sprayer barrel", "U", "barrel", {"fl", "hf"}, None, None, 0, "an open funnel: the gout reaches half as far but spreads twice as wide at its end (a hand flamer's line becomes a ~3 m fan)", "scrap.md#flamer-and-mortar-parts-day-48"),
 ("mortarbarrel", "Reinforced mortar barrel", "U", "barrel", {"mo"}, None, None, 0, "half as far again: a light mortar to ~450 m, a pipe-bomb mortar to ~60 m", "scrap.md#flamer-and-mortar-parts-day-48"),
 ("c_chamber", "Extra shot chamber", "U", "chamber", {"mo"}, None, None, 1, "a fold-out chamber holding one round: swung in, it fires a second round the same beat (same spot or one within ~10 m); refilling it is the loader's beat", "scrap.md#flamer-and-mortar-parts-day-48"),
 ("antidud", "Anti-dud breech", "U", "breech", {"mo"}, None, None, 0, "fewer duds: a dud happens only if a d6 after it shows 1-3; a dud in the tube is lifted out safely (a beat, no dive)", "scrap.md#flamer-and-mortar-parts-day-48"),
 # mortar rounds (the player, day 48): a rolled load means about half the team's rounds are that type
 ("m_smoke", "Smoke rounds (mortar)", "C", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "as a smoke grenade where it lands", "scrap.md#mortar-rounds-day-48"),
 ("m_flare", "Flare rounds (mortar)", "C", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "lights ~50 m for 3 beats: no darkness penalty for anyone in it", "scrap.md#mortar-rounds-day-48"),
 ("m_incend", "Incendiary rounds (mortar)", "U", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "everyone within ~5 m catches fire; the ground burns 2 beats", "scrap.md#mortar-rounds-day-48"),
 ("m_choke", "Choke gas rounds (mortar)", "U", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "an ~8 m cloud for 3 beats: -2 without a mask or rebreather", "scrap.md#mortar-rounds-day-48"),
 ("m_airburst", "Airburst rounds (mortar)", "U", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "bursts overhead over ~8 m: a step; only a solid roof helps; duds on a d6 of 1", "scrap.md#mortar-rounds-day-48"),
 ("m_krak", "Krak rounds (mortar)", "R", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "one target or vehicle, hits like a krak; -2 to land it", "scrap.md#mortar-rounds-day-48"),
 ("m_cluster", "Cluster rounds (mortar)", "R", "load", {"mo"}, r"^(?!.*(pipe|lobber|scrap)).*mortar", None, 0, "bomblets over ~15 m: everyone in it rolls a d6, 4-6 drops a step; duds on a d6 of 1", "scrap.md#mortar-rounds-day-48"),
 ("m_firebottle", "Fire-bottle loads (scrap mortar)", "C", "load", {"mo"}, r"pipe-bomb mortar|tube lobber|lobber|scrap mortar", None, 0, "a ~2 m pool of fire where it lands; duds on a d6 of 1", "scrap.md#mortar-rounds-day-48"),
 ("m_tincan", "Tin-can loads (scrap mortar)", "C", "load", {"mo"}, r"pipe-bomb mortar|tube lobber|lobber|scrap mortar", None, 0, "as a tin-can bomb (~3 m; half a step; flak and heavier shrug it); duds on a d6 of 1", "scrap.md#mortar-rounds-day-48"),
 ("m_cracker", "Cracker-bundle loads (scrap mortar)", "C", "load", {"mo"}, r"pipe-bomb mortar|tube lobber|lobber|scrap mortar", None, 0, "a flashbang: -2 within ~4 m; duds on a d6 of 1-2", "scrap.md#mortar-rounds-day-48"),
 ("c_chargehold", "Charge-hold trigger", "U", "selector", {"lp"}, None, None, 1, "hold the trigger through one shot of a string (it doesn't fire): the next shot gets through one more armour step, up to carapace, for a full step (1.0); once a string", "las.md#charge-hold-trigger-custom"),
 # chain weapons, more (the player, day 48): teeth material, band, tooth shape, spike guard; kit.md, Chain weapon parts (day 48)
 ("ceramteeth", "Ceramite teeth", "R", "material", {"ch"}, None, None, 0, "through ceramite-forged on any hit; power armour on a raw 18+", "kit.md#chain-weapon-parts-day-48"),
 ("adamteeth", "Adamantium teeth", "R", "material", {"ch"}, None, None, 0, "through ceramite-forged on any hit; power armour on a solid hit", "kit.md#chain-weapon-parts-day-48"),
 ("doubleband", "Double band", "U", "band", {"ch"}, None, None, 0, "a hit drops one more health step; less control: -2 on swings", "kit.md#chain-weapon-parts-day-48"),
 ("spiketeeth", "Long spike teeth", "U", "shape", {"ch"}, None, None, 0, "against no armour or flak a hit drops an extra step; it gets through one armour step less than it otherwise would", "kit.md#chain-weapon-parts-day-48"),
 ("flatteeth", "Flat teeth", "U", "shape", {"ch"}, None, None, 0, "it gets through one armour step further than it otherwise would; against no armour or flak only a solid hit drops a step", "kit.md#chain-weapon-parts-day-48"),
 ("spikeguard", "Spike guard", "U", "chguard", {"ch"}, None, None, 0, "one more swing at the end of every chain: a guard punch; a hit drops no health step, it staggers (-1 on their next roll); one end-of-chain strike a chain", "kit.md#chain-weapon-parts-day-48"),
 ("c_cord", "Chain-linked cord", "U", "pommel", {"bl", "bt", "pw", "ch"}, r"^(?!.*(two-handed|great|eviscerator|shovel|glaive|sledge|headsman|glove|fist|knuckle)).*", None, 1, "+1 on the first swing; thrown on its chain ~5 m, back in his hand next beat; the chain caps every throw at 5 m (a throwing balance too)", "kit.md#melee-attachments-day-48"),
 ("c_balance", "Smith-balanced blade", "U", "balance", {"bl"}, None, None, 1, "+1 on every swing", "kit.md#melee-attachments-day-48"),
 ("throwbal", "Throwing balance", "U", "throwbal", {"bl"}, r"^(?!.*(two-handed|heavy|great|headsman|huge)).*(knife|machete|hatchet|cleaver|axe)", None, 0, "can be thrown once like a throwing knife (~10 m)", "kit.md#melee-attachments-day-48"),
 ("c_wristblade", "Leather wrist-sheath (hidden blade)", "U", "rig", {"bl"}, r"knife|dagger|stiletto|shank", None, 1, "can't be disarmed; +5 to keep it hidden; +3 on the first swing against each target (the surprise), even mid-melee", "kit.md#melee-attachments-day-48"),
 ("c_chguard", "Chain guard", "U", "chguard", {"ch"}, None, None, 1, "+1 to parry; his chain can't be jammed by a lost Saw Lock", "kit.md#melee-attachments-day-48"),
 ("c_tritip", "Triangle-tipped point", "U", "point", {"bl", "pw"}, r"knife|dagger|stiletto|sword|sabre|cutlass|shank|blade|spear", None, 1, "a hit that lands: -1 on their next swing; downed by it: -3 on the survival d6", "kit.md#melee-attachments-day-48"),
 ("c_tunedfield", "Tuned field", "U", "field", {"pw"}, None, None, 1, "its cell holds +5 power-mode swings", "kit.md#melee-attachments-day-48"),
 ("10deg", "10-degree edge", "U", "edge", {"bl"}, None, None, 0, "against no armour a hit drops an extra step; a hit on armour, d6: 5 the edge dulls (no bonus till re-sharpened), 6 the blade breaks", "kit.md#melee-attachments-day-48"),
 ("cappedhead", "Ceramite-capped head", "R", "head", {"bt"}, None, None, 0, "a hit the armour shrugs still counts 2 toward wear-down", "kit.md#melee-attachments-day-48"),
 ("skeleton", "Skeleton grip (melee)", "U", "mgrip", MELEE, NOGLOVE, None, 0, "lighter and quicker: Handling +2 and +1 on parries; disarms against him +2", "kit.md#melee-attachments-day-48"),
 ("c_promethium", "Promethium can and blade line", "R", "coil", {"bl", "ch"}, None, None, 1, "heavy: -2 to parry with it, Handling -1; lit (on/off free): -1 on swings, a hit sets the target alight on a d6 5-6; 1 charge a lit beat, 6 to a can (a fire bottle or a flamer canister refills it)", "kit.md#melee-attachments-day-48"),
 # ammo (day 47): one special load per gun ('load' slot); a magazine holds one load at a time.
 # The player: special ammo is easy to get (uncommon); armour-piercing is better (rare).
 ("a_hp", "HP rounds (hollow point)", "U", "load", {"sp", "smg", "sr"}, None, None, 0, "flak doesn't shrug it even at range; against no armour or flak a solid hit drops two steps; reinforced flak and heavier shrug it", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_ap", "AP rounds (armour-piercing)", "R", "load", {"sp", "smg", "sr"}, None, None, 0, "flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m; against no armour a crit drops just one step", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_hv", "HV rounds (high velocity)", "U", "load", {"sp", "smg", "sr"}, None, None, 0, "+1 aimed past ~30 m; flak doesn't shrug it at range; each shot counts 2 toward Dirty", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_flat", "Flat-tip rounds", "U", "load", {"sp", "sr"}, STUBCAL, None, 0, "a shrugged hit counts as 2 toward wear-down", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_cap", "CAP rounds (ceramite-tipped AP)", "R", "load", {"sp", "smg", "sr"}, AUTOCAL, None, 0, "flak and reinforced flak don't shrug it; through carapace on a solid hit at any range; against no armour a crit drops just one step", "stub.md#stub-and-autogun-rounds-special-loads"),
 ("a_hotshot", "Hot-shot conversion and hot-shot packs", "R", "load", {"lp", "lr"}, r"^(?!.*(hellgun|hellpistol|hell revolver|hell shotgun|hot-shot|volley gun)).*", None, 0, "it becomes a hellgun-type gun: one step harder; hot-shot packs only, at the normal rate", "las.md#hot-shot-conversion-kit"),
 ("a_mechpack", "Mechanicus pattern hot-shot pack", "R", "load", {"lp", "lr"}, r"hellgun|hellpistol|hell revolver|hell shotgun|hot-shot|volley gun", None, 0, "one armour tier harder (heavy carapace at any range, ceramite-forged inside ~15 m); 20 shots a pack", "las.md#hot-shot-pack-mechanicus-pattern"),
 ("a_ancient", "Ancient plasma cell", "R", "mag", {"pp", "pg"}, None, None, 0, "through power armour on any hit; a hit drops an extra step; 1 heat a shot; 8 shots, can't be refilled", "plasma.md#ancient-plasma-cell"),
 ("a_bigtank", "Big flamer tank", "U", "mag", {"hf", "fl"}, None, None, 0, "twice the bursts; -1 on dodges; the tank is a target (a 1-4 burst also catches anyone within ~3 m)", "scrap.md#flamer-tanks-and-fuels-special-loads"),
 ("a_sulphur", "Sulphur fuel", "U", "load", {"hf", "fl"}, None, None, 0, "everyone hit drops an extra step; fumes: -1 on the next roll in the burned area without a mask", "scrap.md#flamer-tanks-and-fuels-special-loads"),
 ("a_thermite", "Thermite fuel", "R", "load", {"hf", "fl"}, None, None, 0, "+1 step on a hit; through carapace to ceramite-forged on any hit, power armour on a solid hit; burns through light cover; half the reach", "scrap.md#flamer-tanks-and-fuels-special-loads"),
 ("a_phosphex", "Cut phosphex", "R", "load", {"hf", "fl"}, None, None, 0, "can't be beaten out: burns 2 beats, a step each, unless smothered; the ground burns 2 beats; a natural 1 splashes the flamer", "scrap.md#flamer-tanks-and-fuels-special-loads"),
 ("a_astmelta", "Astartes melta canister", "R", "load", {"mg"}, None, None, 0, "a hit on a vehicle takes 2 hull points, not 1; the kick: -1 on his next melta shot", "plasma.md#melta-canisters-special-loads"),
 ("a_bigmelta", "Big melta canister", "U", "mag", {"mg"}, None, None, 0, "14 shots, not 6; -1 on quick-draws; Handling -1", "plasma.md#melta-canisters-special-loads"),
 ("a_mechmelta", "Mechanicus melta canister", "R", "load", {"mg"}, None, None, 0, "inside ~8 m a hit drops 3 steps; the kick: -1 on his next melta shot; 4 shots", "plasma.md#melta-canisters-special-loads"),
 ("a_incin", "Incinerator canister", "R", "load", {"mg"}, None, None, 0, "inside ~8 m a hit drops 3 steps; vehicles 2 hull points; sets alight, melts light cover; a crit puts anyone straight to Down (enemies -1 on survival); the kick -2; 3 shots", "plasma.md#melta-canisters-special-loads"),
 ("a_offbolt", "Off-brand bolt rounds", "C", "load", {"bp", "br", "hv"}, r"bolt", None, 0, "heavy carapace and ceramite only on a solid hit; power armour shrugs them; a crit drops just one step", "bolt.md#bolt-rounds-special-loads"),
 ("a_meltacore", "Meltacore bolt rounds", "R", "load", {"bp", "br", "hv"}, r"bolt", None, 0, "through a tank's armour from any side; +1 heat a string, vent at 3; +1 recoil", "bolt.md#bolt-rounds-special-loads"),
 ("a_storm", "Storm bolt rounds", "U", "load", {"bp", "br", "hv"}, r"bolt", None, 0, "a miss by 1-3 still hits; every hit lands like a frag (flak; carapace on a solid hit; heavier shrugs)", "bolt.md#bolt-rounds-special-loads"),
 ("a_vengeance", "Vengeance bolt rounds", "R", "load", {"bp", "br", "hv"}, r"bolt", None, 0, "against power armour a hit drops an extra step; through an APC's armour; a natural 1 cooks off: he drops a step, the gun is out", "bolt.md#bolt-rounds-special-loads"),
 ("a_eco", "Las eco pack", "C", "load", {"lp", "lr"}, r"^(?!.*(hellgun|hellpistol|hell revolver|hell shotgun|hot-shot|volley gun)).*", None, 0, "120 shots; flak shrugs it past ~15 m, reinforced flak always", "las.md#las-eco-pack"),
 ("a_mechlas", "Mechanicus lascannon pack", "R", "load", {"hv"}, r"lascannon|las-cannon", None, 0, "a hit on a vehicle takes 2 hull points; +1 heat a shot, vent at 3", "heavy.md#lascannon-packs-special-loads"),
 ("a_extlas", "Extended lascannon pack", "U", "mag", {"hv"}, r"lascannon|las-cannon", None, 0, "10 shots, not 6; Handling -1", "heavy.md#lascannon-packs-special-loads"),
 ("a_battlas", "Lascannon battery pack", "U", "mag", {"hv"}, r"lascannon|las-cannon", None, 0, "40 shots; set down and cabled (the beat's move), the gunner stays within ~3 m; a solid hit on it kills it", "heavy.md#lascannon-packs-special-loads"),
 ("a_flak", "Flak shells (autocannon)", "U", "load", {"hv"}, r"autocannon", None, 0, "airborne targets: ignore the -3, a miss by 1-3 still clips him for half a step (0.5); on the ground no extra step", "heavy.md#autocannon-shells-special-loads"),
 ("a_penetrator", "Penetrator shells (autocannon)", "R", "load", {"hv"}, r"autocannon", None, 0, "through a tank's side or rear; keeps the extra step on people; +1 recoil", "heavy.md#autocannon-shells-special-loads"),
 ("a_incendhe", "Incendiary HE shells (autocannon)", "U", "load", {"hv"}, r"autocannon", None, 0, "splash: within ~2 m of a hit, DEX dodge or drop a step; a raw 17+ sets alight; no extra step on the target; APCs shrug it", "heavy.md#autocannon-shells-special-loads"),
 ("a_overml", "Overcharged multi-laser pack", "R", "load", {"hv"}, r"multi-laser|multilaser", None, 0, "one armour tier harder (heavy carapace at any range, ceramite-forged inside ~15 m); 6 shots a pack, not 12", "heavy.md#multi-laser-packs-special-loads"),
 ("a_extml", "Extended multi-laser pack", "U", "mag", {"hv"}, r"multi-laser|multilaser", None, 0, "36 shots, not 12; Handling -1", "heavy.md#multi-laser-packs-special-loads"),
 ("bowstring", "Heavy bowstring", "U", "string", {"bw"}, None, None, 0, "the -2 starts 20 m later; a bow needs 5 more STR to draw (a crossbow none)", "bows.md#bow-parts-day-48"),
 ("bowsight", "Bow sight", "C", "bowsight", {"bw"}, None, None, 0, "+1 on aimed shots past ~20 m", "bows.md#bow-parts-day-48"),
 ("c_arctracker", "Arc tracker (bow)", "U", "tracker", {"bw"}, r"^(?!.*condemnor)", None, 1, "no -2 at long range, out to twice the reach; arcs over cover: one level lighter; no beams", "bows.md#bow-parts-day-48"),
 ("a_seekerarrow", "Seeker arrows, Mechanicus pattern", "R", "load", {"bw"}, None, None, 0, "lock onto heat: +3 on warm targets; light and half cover do not count; burst: through carapace, the target 2 steps, ~2 m dive or 0.5", "bows.md#explosive-arrows-day-48"),
 ("a_scrapboom", "Scrap explosive arrows", "C", "load", {"bw"}, None, None, 0, "a tin-can bomb on a shaft: -2 and half the reach; goes off as a tin-can bomb with its d6 timing", "bows.md#explosive-arrows-day-48"),
 ("a_scraparrow", "Scrap arrows", "C", "load", {"bw"}, None, None, 0, "through no armour; flak and up shrug them (no wear-down) and they break", "bows.md#arrows"),
 ("a_metalarrow", "Metal arrows", "C", "load", {"bw"}, None, None, 0, "through no armour; dent flak and reinforced flak; can break on carapace and up", "bows.md#arrows"),
 ("a_steelarrow", "Steel arrows", "U", "load", {"bw"}, None, None, 0, "through flak; dent reinforced flak and carapace; can break on reinforced flak and up", "bows.md#arrows"),
 ("a_manstopper", "Man-stopper shells (armour-piercing slug)", "R", "load", {"sg"}, None, None, 0, "one slug, one target, no spread; flak and reinforced flak don't shrug it; through carapace on a solid hit inside ~15 m", "stub.md#shotgun-shells-special-loads"),
 ("a_dragon", "Dragon's breath shells", "U", "load", {"sg"}, None, None, 0, "shot at, the target is flashed: -1 on his next shot; hit, -2 instead; a hit on a raw 17+ sets him alight", "stub.md#shotgun-shells-special-loads"),
 ("a_hellshell", "Hellfire shells", "R", "load", {"sg"}, None, None, 0, "a hit that gets through: CON save vs 10 or one more step", "stub.md#shotgun-shells-special-loads"),
 ("a_kraken", "Kraken bolt rounds", "R", "load", {"bp", "br", "hv"}, r"bolt", None, 0, "through an APC's armour; +1 aimed past ~30 m", "bolt.md#bolt-rounds-special-loads"),
 ("a_hpbelt", "Hollow point stubber belt", "U", "load", {"hs"}, None, None, 0, "against flak or less a solid hit drops an extra step; carapace and heavier shrug it", "heavy.md#heavy-belt-stubber-belts-special"),
 ("a_inferno", "Inferno belt", "U", "load", {"hs"}, None, None, 0, "a hit on a raw 17+ sets the target alight", "heavy.md#heavy-belt-stubber-belts-special"),
 ("a_tungsten", "Tungsten-core belt", "R", "load", {"hs"}, None, None, 0, "through heavy carapace at any range", "heavy.md#heavy-belt-stubber-belts-special"),
 ("a_hellfire", "Hellfire belt", "R", "load", {"hs"}, None, None, 0, "a hit that gets through: CON save vs 10 or one more step", "heavy.md#heavy-belt-stubber-belts-special"),
 ("a_blacktip", "Black-tip darts", "U", "load", {"np", "nr"}, None, None, 0, "the toxin's save is vs 17; a pass is still -1 on their next roll", "stub.md#needle-darts-special-loads"),
 ("a_panic", "Panic darts", "U", "load", {"np", "nr"}, None, None, 0, "CON vs 15 or drops what's in hand and runs or hides 2 beats", "stub.md#needle-darts-special-loads"),
 ("a_tracker", "Tracker darts", "U", "load", {"np", "nr"}, None, None, 0, "a pinger, not a toxin: followed on an auspex ~1 km for a day", "stub.md#needle-darts-special-loads"),
 ("a_shard", "Shard darts", "R", "load", {"np", "nr"}, None, None, 0, "through carapace on any hit, heavy carapace on a solid hit", "stub.md#needle-darts-special-loads"),
 ("a_widow", "Widow darts", "R", "load", {"np", "nr"}, None, None, 0, "a failed save is dead, no survival roll", "stub.md#needle-darts-special-loads"),
 ("a_truth", "Truth darts", "R", "load", {"np", "nr"}, None, None, 0, "CON vs 15 or ~10 minutes of loose tongue", "stub.md#needle-darts-special-loads"),
 # --- custom (an enemy's is his own smith's version) ---
 ("c_overdrive", "Overdrive", "R", "overdrive", {"ch"}, None, None, 1, "once a mission, ~30 s: armour a step lighter against it, advantage in mob pushes; then done for the fight; a natural 1 while running burns the motor", C + "shameholders-overdrive-tamsin"),
 ("c_motor", "Better motor", "U", "motor", {"ch"}, None, None, 1, "crits on 19-20; a natural 1 on a swing throws the chain (a beat to reseat)", C + "kells-chain-axe-schematic-5"),
 ("c_teeth", "Plasteel teeth", "U", "material", {"ch"}, None, None, 1, "through heavy carapace on any hit, ceramite-forged on a solid hit", C + "kells-chain-axe-schematic-5"),
 ("c_hardgrip", "Curved hardwood grip", "C", "mgrip", MELEE, NOGLOVE, None, 1, "can't be knocked from his hand by a solid hit", C + "kells-chain-axe-schematic-5"),
 ("c_bite", "Bite switch", "R", "mselector", {"ch"}, None, None, 1, "BITE: one swing a beat, a hit drops an extra step; flipped before the swing", C + "kells-chain-axe-schematic-5"),
 ("c_buffer", "Heavy buffer spring and new bolt", "C", "bolt", {"smg"}, None, None, 1, "jams only from the 25th straight round", C + "stinger-tamsin"),
 ("c_slide", "Lightened slide and tower grip", "C", "slide", {"sp"}, "autopistol", None, 1, "strings up to 5; recoil stays 0", C + "daces-autopistol-schematic-1"),
 ("c_select3", "Three-way selector with a rapid feeder", "R", "selector", {"sp"}, "autopistol", None, 1, "SAFE / BURST (strings up to 5) / AUTO (strings up to 8, no hit bonuses; from the 13th straight round a shot die of 1-3 jams); not drop-prone", C + "daces-autopistol-schematic-1"),
 ("c_flbarrel", "Long flamer barrel", "C", "barrel", {"hf"}, None, None, 1, "reach ~10 m; -1 quick-draw", C + "holliss-hand-flamer-schematic-2"),
 ("c_igniter", "Tuned igniter", "U", "igniter", {"hf", "fl"}, None, None, 1, "the gout opens ~2 m wide at the far end and catches anyone close together", C + "holliss-hand-flamer-schematic-2"),
 ("c_hburst", "Heavy-burst switch", "R", "selector", {"hf", "fl"}, None, None, 1, "one pull spends 2 bursts: everyone hit drops an extra step; no flame the next beat", C + "holliss-hand-flamer-schematic-2"),
 ("c_cradle", "Dual canister cradle", "U", "mag", {"hf"}, None, None, 1, "8 bursts before a reload", C + "holliss-hand-flamer-schematic-2"),
 ("c_hstock", "Heavy grip and recoil stock", "C", "stock", {"hs"}, None, None, 1, "recoil 0 braced", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_sidegrip", "Angled side grip", "C", "grip", {"hs"}, None, None, 1, "recoil 1 on the move", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_openbolt", "Open-bolt feeder", "U", "feeder", {"hs"}, None, None, 1, "Dirty after ~60 shots; a Dirty stubber doesn't jam", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_recip", "Light reciprocating parts and plasteel spring", "C", "bolt", {"hs"}, None, None, 1, "strings up to 10, no hit bonuses in the string", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_rate", "Rate selector (HIGH)", "R", "selector", {"hs"}, None, None, 1, "HIGH: strings up to 12; Dirty at ~30 and jams on a natural 1; recoil 1 braced, 2 moving", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_tripod", "Traverse tripod (ARC fire)", "R", "tripod", {"hs"}, None, None, 1, "set up as a main thing, no recoil; ARC: everyone in the arc -2 on their shots next beat, breaking cover draws a free shot", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_twintray", "Twin feed tray", "U", "mag", {"hs"}, None, None, 1, "twice the rounds; two belt types, switched with a lever", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_walk", "Walking plate", "R", "muzzle", {"hs"}, None, None, 1, "one string across up to 3 standing abreast; the swap's -1 once per extra target", C + "morcants-heavy-belt-stubber-schematic-3"),
 ("c_rig", "One-piece crossdraw rig", "C", "holster", PIST, None, None, 1, "+1 quick-draw", C + "teys-hellpistol-schematic-4"),
 ("c_bridged", "Bridged double-cell belt pack", "U", "mag", {"lp"}, "hellpistol", None, 1, "60 shots on the cable", C + "teys-hellpistol-schematic-4"),
 ("c_longbarrel", "Long barrel", "C", "barrel", {"lr"}, None, None, 1, "+1 aimed past ~30 m; -1 inside ~5 m", C + "vargas-mercy-schematic-6"),
 ("c_lrscope", "Custom long-range scope", "U", "optic", RIFLE, None, None, 1, "+2 aimed past ~30 m (as the 10x scope: -1 hip/snap and inside ~15 m)", C + "vargas-mercy-schematic-6"),
 ("c_dualmount", "Dual riser mount with a canted reflex", "U", "mount", RIFLE, None, "scope", 1, "the scope's close penalty never applies (the reflex: +2 aimed inside ~30 m); one optic at a time; -1 quick-draw", C + "vargas-mercy-schematic-6"),
 ("c_energy", "Energy selector (LIGHT / MED / HEAVY)", "R", "selector", {"lr"}, "hellgun|hot-shot", None, 1, "MED: 2 pack a shot, heavy carapace at any range, +1 heat a string; HEAVY: 3 pack a shot, through ceramite-forged, +2 heat a shot; vent at 3", C + "vargas-mercy-schematic-6"),
 ("c_rangef", "Custom range-finder", "U", "mount", RIFLE, None, "scope", 1, "+2 aimed past ~30 m (rides the scope)", C + "isks-patience-schematic-7"),
 ("c_hbarrel", "Heavy long barrel", "C", "barrel", {"lr", "sr", "nr"}, None, None, 1, "+2 aimed; -1 hip, snap and on the move", C + "isks-patience-schematic-7"),
 ("c_bipod", "Custom bipod", "C", "under", RIFLE | {"hs"}, None, None, 1, "braced or prone, a chain miss costs no -1; a beat to set up", C + "isks-patience-schematic-7"),
 ("c_generator", "Intensified laser generator", "R", "generator", {"lr"}, None, None, 1, "3 pack a shot: +1 aimed, through ceramite-forged; a string of 3 adds 1 heat", C + "isks-patience-schematic-7"),
 ("c_short", "Cut-down short barrel", "C", "barrel", {"lr", "sr"}, None, None, 1, "+1 inside ~15 m; -1 past ~30 m", C + "kells-officer-schematic-8"),
 ("c_skelgrip", "Skeleton grip", "C", "grip", RIFLE, None, None, 1, "Handling +1; -1 aimed past ~30 m", C + "kells-officer-schematic-8"),
 ("c_stockmag", "Stock magazine slot", "C", "stockmag", {"lr"}, None, None, 1, "the first reload each fight costs no beat", C + "kells-officer-schematic-8"),
 ("c_twin", "Twin-shot switch", "R", "selector", {"lr"}, None, None, 1, "TWIN: a hit drops a step, one armour tier harder, 2 hits toward wear-down; 2 pack a shot", C + "kells-officer-schematic-8"),
 ("c_krak", "Underslung krak launcher", "R", "under", {"lr", "sr"}, None, None, 1, "one krak a beat out to ~60 m, rolled like a throw; a beat to reload", C + "tavis-tiny-schematic-9"),
 ("c_shotstock", "Heavy shotgun stock with grenade loops", "C", "stock", {"lr", "sr", "sg"}, None, None, 1, "+1 aimed; Handling -1; 3 grenade loops", C + "tavis-tiny-schematic-9"),
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
 ("c_lever", "New lever linkage", "U", "action", {"sr"}, "lever", None, 1, "single lever chains up to 7, double up to 4; above 6, no hit bonuses", C + "tamsins-ironside-frontier-schematic-17"),
 ("c_twintubes", "Twin side-by-side tubes", "U", "mag", {"sr"}, "lever", None, 1, "36 rounds; Handling -1", C + "tamsins-ironside-frontier-schematic-17"),
 ("c_tubesel", "Tube selector", "U", "tubesel", {"sr"}, "lever", "c_twintubes", 1, "each tube its own load; flicking it is free", C + "tamsins-ironside-frontier-schematic-17"),
 ("c_pushload", "Push-loaders", "C", "loader", {"sr", "sg"}, "lever|pump|ironclad|harrow", None, 1, "refill a tube in the beat's move", C + "tamsins-ironside-frontier-schematic-17"),
 ("c_box100", "100-round box mags", "U", "mag", {"sr"}, "autogun|columnus", None, 1, "100 rounds; a loaded box: Handling -1 and -1 quick-draw", C + "tamsins-columnus-schematic-18"),
 ("c_superv", "The Super V", "R", "action", {"sr"}, "autogun|columnus", None, 1, "auto strings up to 12, recoil 0; auto still no hit bonuses", C + "tamsins-columnus-schematic-18"),
 ("c_finned", "Short finned barrel", "U", "barrel", {"sr"}, "autogun|columnus", None, 1, "+1 inside ~10 m, -2 past ~30 m; strings of 8+ build 1 heat, the fins shed 1 when it doesn't fire; Handling -1", C + "tamsins-columnus-schematic-18"),
]
KEYS = {a[0] for a in A}
BLOCKS = {"c_intsupp": {"muzzle"}}  # parts that fill a second slot (the full-barrel suppressor, day 48)
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

# Guns with limited attachment slots (day 47): only these slots roll (special ammo always can).
SLOTLIMIT = [(re.compile(r"farmer's pump|three-shooter|harrow|trinity|holdout|cutpurse|las luger"), {"load", "tape"}),
             (re.compile(r"service stub pistol|steadfast"), {"load", "muzzle", "tape"}),
             (re.compile(r"turnstile"), {"optic", "under", "load", "tape"}),
             (re.compile(r"twinstack"), {"optic", "muzzle", "load", "tape"}),
             (re.compile(r"thresher"), {"optic", "laser", "under", "stock", "muzzle", "load", "tape"}),
             (re.compile(r"magistrate"), {"optic", "laser", "sleeve", "load", "tape"}),
             (re.compile(r"jackknife"), {"load"}),
             (re.compile(r"ironhound"), {"optic", "laser", "load", "tape"}),
             (re.compile(r"outrider"), {"laser", "muzzle", "load", "tape"}),
             (re.compile(r"siege ping"), {"trigger", "barrel", "grip", "sleeve", "load"}),  # internal mods only (day 48)
             (re.compile(r"siege hinge"), {"optic", "sling", "load", "tape"}),
             (re.compile(r"gutter smg|grease gun"), {"load", "tape"}),
             (re.compile(r"hell complete"), {"load"}),  # a full setup: no attachments (day 48)  # scrap SMGs (day 48)
             (re.compile(r"magnum firebrand"), {"muzzle", "laser", "load", "tape"}),
             (re.compile(r"condemnor"), {"string", "bowsight"}),  # stakes, not arrows (day 48)  # the stockless lever shotgun (day 48)  # the line shotgun (day 48)  # the folding breacher: no slots (day 48)  # the officer's shell revolver (day 48)  # the drum auto-shotgun (day 48)  # over-under pump: optic and muzzles only (day 48)  # the revolving shotgun: optic and under-barrel only (day 48)
             (re.compile(r"breach latchkey"), {"laser", "sleeve", "load", "tape"}),  # the standoff breacher: no stock, the standoff is the muzzle (day 48)
             (re.compile(r"hell revolver"), {"optic", "laser", "load", "tape"})]  # top and bottom slots only (day 48)  # tape needs no slot
SKIP = re.compile(r"web pistol|bolt-pipe|rivet gun|harpoon|turret|gauntlet|hellstrike|flare|^'")
TYPES = [("bw", r"\b(recurve|compound|long|short|hunting)?\s?bow\b|crossbow"), ("pp", r"plasma pistol"), ("pg", r"plasma gun|plasma carbine"), ("bp", r"bolt pistol"),
         ("hv", r"heavy bolter|autocannon|lascannon|multi-laser"), ("hs", r"heavy belt stubber(?! pistol)|heavy stubber"), ("br", r"bolt marksman|boltgun|storm bolter|combi-flamer|combi-melta|combi-plasma|bolt carbine"),
         ("hf", r"hand flamer|wrist flamer"), ("fl", r"flamer|torch-thrower|promethium sprayer"), ("mg", r"meltagun|melta gun|multi-melta|inferno pistol|melta-cutter|improvised melta"),
         ("gl", r"grenade launcher"), ("mo", r"mortar"), ("np", r"needle pistol"), ("nr", r"needle rifle"),
         ("lr", r"shotlas|hell shotgun|las shotgun|hailstorm"), ("smg", r"submachine|machine pistol|rattler|\bsmg\b|chain-fed autopistol"),
         ("lp", r"laspistol|las pistol|las-shot pistol|hellpistol|las luger|hell revolver"),
         ("sp", r"heavy belt stubber pistol|autopistol|revolver|stub pistol|stub automatic|hand cannon|boarding pistol|hammerfall|pipe pistol|three-shooter|burst pistol"),
         ("sg", r"shotgun|sawn-off|scattergun|nailer|ripper gun"),
         ("lr", r"lasgun|lascarbine|hellgun|long-las|las-box|las-lmg|volley gun|battery las"),
         ("sr", r"autogun|autorifle|stub rifle|lever-action|pipe rifle|hunting rifle|anti-materiel|battle rifle|break-action rifle|commissar's carbine|lieutenant's carbine|semi-auto carbine|bullpup autogun|marksman rifle(?!.*twinshot)|light machine gun|sniper rifle|heavy carbine")]
MTYPES = [("sh", r"shield"), ("pw", r"power (sword|axe|maul|knife|fist|mace|blade|odachi)|(?<!scrap )thunder hammer|relic blade"),
          ("ch", r"chainsword|chain axe|chain-axe|chain knife|chain glaive|chain blade|eviscerator|chain glove|chain short-sword"),
          ("bl", r"knife|machete|cutlass|sabre|sword|cleaver|axe|shank|blade|stiletto|shovel|dagger|dirk|kukri|karambit|gladius|ninjato|falchion|scimitar|tiger claws|billhook|sickle|\bkama\b|\bsai\b|tanto|katana|wakizashi|bardiche|glaive|zweihander"),
          ("bt", r"club|maul|mace|hammer|flail|baton|prod|knuckle|girder|pick\b|pry-bar|crowbar|truncheon|cosh|morning star|pernach|\bbat\b|quarterstaff"),
          ("st", r"^(?!.*goad).*(\bstaff\b|\bstave\b)")]
BUILTIN = [("mount", r"range-finder"), ("optic", r"scope|sprinter|kasr lance|exemplar|cognis|kasr sentinel|kasr augur|hell complete|rampart longwatch"), ("mag", r"drum|100-shot box|las luger|hell revolver"),
           ("laser", r"kasr tether|cognis"), ("counter", r"exemplar"),
           ("muzzle", r"silenced|suppressed|breach hush"), ("bayonet", r"bayonet|krieg"), ("tripod", r"tripod"),
           ("barrel", r"heavy barrel|long barrel|long-barrel|stub barrel"), ("stock", r"folding stock"),
           ("load", r"arrows|mortar.*(smoke|krak)"),
           ("mgrip", r"pernach"), ("pommel", r"pernach"), ("stock", r"hailstorm|switchback|carousel"), ("under", r"breakwater|kasr augur|thunder' pattern|thunder pattern"), ("bayonet", r"solid stripper"), ("sleeve", r"magnum universal"), ("trigger", r"magnum centurion"), ("mag", r"lieutenant's carbine"),
           ("optic", r"rampart halberd|rampart dragoon|rampart overwatch"), ("mount", r"rampart halberd"), ("muzzle", r"rampart halberd|rampart overwatch|breach latchkey"),
           ("stock", r"solid frost|breach cyclone"), ("cheek", r"solid frost"), ("guard", r"forge corsair")]  # the player's gun list, day 48: issued scopes, cans and built-in stocks  # the pernach's built-in ergo grip and banner (day 48)  # a kit that names its arrows has its load


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
    chance = CHANCE[level] + (10 if team else 0) + (25 if re.search(r"solid patriot", src) else 0)  # the M4-style Patriot: +25% (the player, day 48)
    taken, have, got, rolls = set(taken), set(), [], []
    if "optic" in taken and re.search(r"scope|sprinter|kasr lance", src):
        have.add("scope")
    for _ in range(8):
        d = random.randint(1, 100)
        rolls.append(d)
        if d > chance:
            break
        cands = [a for a in A if gtype in a[4] and a[3] not in taken and a[0] not in have
                 and all(a[3] in ok for rx, ok in SLOTLIMIT if rx.search(src))
                 and (a[5] is None or re.search(a[5], src)) and (a[6] is None or a[6] in have)
                 and not (level == "poor" and a[2] == "R") and not (BLOCKS.get(a[0], set()) & taken)]
        if not cands:
            break
        tiers = [t for t in weights if weights[t] and any(a[2] == t for a in cands)]
        if not tiers:
            break
        tier = random.choices(tiers, weights=[weights[t] for t in tiers])[0]
        a = random.choice([a for a in cands if a[2] == tier])
        got.append(a)
        taken.add(a[3])
        taken |= BLOCKS.get(a[0], set())
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

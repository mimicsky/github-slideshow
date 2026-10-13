# Builds pools.json. Each item: name, TV price, category, rarity, sellers.
# Rarity: C common, U uncommon, R rare, X exotic (exotic only via the natural-20 roll).
# Sellers: M Munitorum/fleet stores, B black market/chandlers, A Adeptus Mechanicus shrine,
#          F Free Trader / Void Exchange, E Ecclesiarchy / shrine-world sellers.
import json
I = []
def add(cat, rarity, sellers, rows):
    for name, price in rows:
        I.append({"name": name, "tv": price, "cat": cat, "rarity": rarity, "sellers": sellers})

# --- Las ---
add("las","C","MBF",[("Lasgun, Kantrael M36",1),("Lasgun, Lucius No.98 (hotter, eats packs)",1.5),("Laspistol, Kantrael",0.5),("Lascarbine, Accatran Mk IV",1.5)])
add("las","U","MBF",[("Lasgun, Accatran Mk XIV (short, fast)",2),("Heavy laspistol",2),("Lasgun, Agripinaa (sturdy, slow)",1.5),("Recon lascarbine, folding stock",2.5),("Lasgun, Mezoa 'Lucius' long-barrel",2.5)])
add("las","U","MAF",[("Hellgun, Ryza pattern",5),("Hellpistol, Kantrael",4),("Hellgun, Accatran (compact)",5.5)])
add("las","R","MAF",[("Long-las, Mezoa (sniper)",6),("Long-las, Helbore (heavy, single-shot)",8),("Hot-shot volley gun",12),("Lasgun, Mars pattern (Skitarii, galvanic-ready)",6)])
add("las","U","MBF",[("Lascarbine, Accatran Mk VI (burst fire)",2)])
add("las","R","MBF",[("Las-scattergun 'shotlas' (wide spread, short range)",4)])
add("las","R","MF",[("Multi-laser, man-portable (braced, drains packs fast)",15)])
# Player designs (session 8). Full rules in the notes below and in DND_CODEX Part 8.
add("las","U","MBF",[("Las-SMG, 'Sterl' pattern (side-mounted pack; 6-shot chains, misses don't penalise the chain; 2 hits = 1 vs carapace; eats packs)",3)])
add("las","R","MF",[("Las-box, 'Kasr Barr' pattern light las-LMG (box pack; 6-shot chains; through carapace on a solid hit; heat: chain of 4+ = 1 heat, vent at 3; bipod)",8)])
add("ammo","U","MF",[("Las-box pack (for the Kasr Barr)",0.75)])
add("las","R","BF",[("Duelling laspistol, noble-house pattern",8),("Archeotech lasgun 'sunfire' (worn, works)",30)])
# --- Solid shot ---
add("stub","C","MB",[("Autogun, Agripinaa",1),("Autopistol",1),("Stub revolver",0.5),("Stub automatic",0.75),("Combat shotgun, pump",1.5)])
add("stub","U","MBF",[("Combat shotgun, semi-auto",2),("Ripper gun / drum-fed shotgun",3),("Braced autogun (heavy barrel)",2.5),("Sawn-off shotgun",1),("Hand cannon (big-bore stubber)",2),("Scrap autogun with drum",1.5)])
add("stub","U","B",[("Silenced stub pistol",2.5),("Holdout stub pistol",1),("Hive-gang 'scattergun'",1),("Ganger's chain-fed autopistol",2)])
add("stub","R","MBF",[("Vraks-pattern sniper autorifle",7),("Lucius-pattern 'Ironclad' shotgun",4),("Arbites combat shotgun (shock shells)",6)])
# --- Bolt ---
add("bolt","U","MF",[("Bolt pistol, Godwyn-Deaz (officer)",12)])
add("bolt","R","MF",[("Boltgun, Godwyn pattern",25),("Boltgun, Phobos pattern",28),("Bolt pistol, Ryza pattern",14)])
add("bolt","R","MF",[("Boltgun, Locke Mk IIb 'Spearhead' (Darktide)",26)])
add("bolt","R","MBF",[("Bolt-shotgun, 'Breacher' pattern (single-shot breech, loose bolt rounds; 1-2 shots a beat by recoil)",10)])
add("bolt","R","EF",[("Sororitas bolt pistol (Godwyn-De'az)",16),("Sororitas boltgun",30)])
add("bolt","R","B",[("Bolt pistol, rebored (unstable)",8)])
# --- Plasma / melta / flame ---
add("plasma","R","MAF",[("Plasma pistol, Ryza pattern",25),("Plasma gun, Mars pattern",30),("Plasma gun, Ryza pattern",32)])
add("plasma","U","MAF",[("Plasma cell",6)])
add("plasma","R","AF",[("Tuned plasma cell (12 shots, not 8)",10)])
add("plasma","R","AF",[("Plasma blaster, twin-cell 'Lumen' pattern (2 cells; chains up to 4; heat 1 per 4 shots; pistol punch)",35)])
add("plasma","R","MAF",[("Plasma pistol, 'Needle' pattern (compact, long barrel; slow heat: 1 per 4 shots; 12 shots a cell; lighter punch)",18)])
add("melta","R","MAF",[("Meltagun",35),("Inferno pistol (Sororitas)",40)])
add("melta","U","MF",[("Melta charge (spare)",5)])
add("flame","U","MBEF",[("Flamer, Ryza pattern",8),("Hand flamer",6),("Promethium canister",1),("Ecclesiarchy 'cleansing' flamer",9)])
add("flame","R","MF",[("Heavy flamer",20),("Incinerator (blessed fuel)",25)])
# --- Launchers / heavy ---
add("launcher","U","MF",[("Underslung grenade launcher, Ryza",6),("Grenade launcher, stand-alone",5),("Grenade launcher, revolver-drum",8)])
add("heavy","U","MBF",[("Heavy stubber",4),("Heavy stubber, tripod",5),("Mortar with 6 rounds",12)])
add("heavy","R","MF",[("Heavy bolter, 1 belt",40),("Missile launcher (2 frag, 1 krak)",25),("Autocannon",35),("Lascannon",45),("Multilaser (crew)",30),("Rocket-propelled grenade tube (2 rounds)",10)])
# --- Explosives ---
add("explosive","C","MBF",[("Frag grenade",1),("Smoke grenade",1)])
add("explosive","U","MBF",[("Krak grenade",2),("Photon flash grenade",2),("Choke gas grenade",1.5),("Breaching charge",2),("Det-tape (5 m)",1),("Demolition charge, satchel",4),("Incendiary grenade",2)])
add("explosive","R","MAF",[("Melta bomb",8),("Plasma grenade",6),("Haywire grenade (machine-killer)",8),("Stun grenade (Arbites)",2.5)])
add("explosive","R","BF",[("Phosphex canister (forbidden)",15),("Shrapnel mine",3)])
# --- Ammunition ---
add("ammo","C","MBF",[("Las pack",0.25),("Stub/auto rounds (box)",0.5),("Shotgun shells (box)",0.5),("Heavy stubber belt",1)])
add("ammo","U","MAF",[("Hot-shot pack (Guard)",1),("Hot-shot pack (Mechanicus pattern)",3),("Bolt rounds (10)",8),("Stubber drum magazine",1.5),("Man-stopper shells (box)",1),("Inferno shells (box)",2),("Extended las pack",0.75)])
add("ammo","R","MF",[("Kraken-pattern bolt rounds (10, Astartes)",20),("Hellfire shells (box)",4)])
# --- Melee ---
add("melee","C","MB",[("Combat knife",0.25),("Bayonet",0.25),("Entrenching tool",0.25),("Trench club",0.25),("Cadian machete",0.5)])
add("melee","U","MBF",[("Navy cutlass",2),("Chainsword",6),("Chain axe",8),("Shock maul",7),("Mono-knife",3),("Krieg trench shovel (sharpened)",0.5),("Officer's sabre",3),("Chain knife",3),("Shock baton (Arbites)",4)])
add("melee","R","MAF",[("Power maul",25),("Power sword",30),("Power axe",30),("Power knife",15),("Chainsword, Lucius heavy",10),("Eviscerator (two-handed chainsword)",22),("Thunder hammer (damaged)",40)])
add("melee","R","E",[("Blessed power maul (Ecclesiarchy)",28),("Sororitas power sword",32)])
add("melee","R","B",[("Assassin's mono-wire garrotte",6),("Needle-blade (toxin)",8)])
# --- Armour ---
add("armour","C","MB",[("Flak vest",0.5),("Flak armour set",1),("Flak helmet",0.25),("Gas mask / rebreather",0.5)])
add("armour","U","MBF",[("Carapace armour set",8),("Carapace chest plate",4),("Mesh armour (light, quiet)",5),("Boarding shield",4),("Void-suit, Navy",4),("Hazard suit (plague-rated)",5),("Arbites carapace",10)])
add("armour","R","MAF",[("Storm trooper carapace set",15),("Storm shield (power field)",30),("Refractor field",25),("Conversion field (damaged)",35),("Skitarii armour (augmetic fit)",18)])
add("armour","R","E",[("Sororitas power armour, damaged",50),("Rosarius (blessed field, small)",30)])
# --- Optics / sights / mods ---
add("mod","U","MBF",[("Reflex sight",3),("Telescopic sight",3),("Photo-visor (low-light)",2),("Magnoculars",1.5),("Bipod",0.5),("Weapon sling, padded",0.25),("Quick-draw holster",0.5),("Silencer (stub/auto)",2),("Extended magazine",1),("Bayonet lug kit",0.25),("Laser designator",3)])
add("mod","R","MAF",[("Hot-shot conversion kit (lasgun)",5),("Overcharge capacitor (las)",8),("Mechanicus focusing lens",10),("Auto-targeter (augur sight)",12),("Heat-sink shroud (las)",4),("Chainsword teeth, adamantium (set)",12),("Motor housing, high-tolerance",9)])
# --- Gear / tech ---
add("gear","C","MB",[("Micro-bead",0.5),("Chrono",0.5),("Lumen (torch)",0.25),("Field rations (crate)",0.5),("Water purifier",0.5),("Rope (20 m)",0.25),("Lho-sticks (carton)",0.25),("Imperial Infantryman's Uplifting Primer",0.1)])
add("gear","U","MBF",[("Map-slate",1),("Auspex (hand)",6),("Vox-caster (manpack)",5),("Flares (box of 10)",0.5),("Grav-chute",6),("Climbing rig and grapnel",1.5),("Demolitions kit / bag",1.5),("Large field pack",1),("Drag harness",0.5),("Multi-key / lockbreaker",2),("Cutting torch",3),("Med-kit",3),("Stimm (dose)",0.5),("Antitoxin (dose)",1),("Combat drug 'slaught' (dose)",1)])
add("gear","U","B",[("Forged Munitorum ID chits",2),("Lock-picks, hive pattern",1),("Spoof-tag (fakes a transponder)",6),("Black-market data-slate",1)])
add("gear","R","MAF",[("Cogitator spike",4),("Servo-skull (utility, used)",20),("Servo-skull (medicae)",25),("Bio-scanner",8),("Psy-occulus (warp detector)",15),("Jump pack (Guard pattern)",30),("Chameleoline cloak",12),("Medicae servitor (old)",30)])
add("gear","R","E",[("Purity seal (blessed)",2),("Aquila rosary",1),("Reliquary fragment",10),("Blessed sacred oils (flask)",2),("Vial of shrine water",1)])
# --- Augmetics ---
add("augmetic","U","AB",[("Augmetic eye (basic)",8),("Augmetic hand (basic)",8),("Respirator implant",6)])
add("augmetic","R","A",[("Augmetic arm, Mechanicus",20),("Bionic eye with targeter",18),("Subdermal armour",25),("Augmetic legs (pair)",30),("Mind-impulse link",22)])
# --- Salvage / parts ---
add("salvage","C","MBA",[("Scrap metal (crate)",0.5),("Plasteel ingot",2)])
add("salvage","U","ABF",[("Ceramite plate",3),("Servo-motor",3),("Machine-core",6),("Mechanicus sacred oils (flask)",1),("Spare coupling (Mechanicus)",2),("Power cell (station)",0.5),("Adamantium shard",6)])
add("salvage","R","A",[("Cogitator relic",12),("Machine-spirit core (old weapon)",15),("Promethium crucible charge",10)])
# --- Vehicle / ship ---
add("vehicle","U","MF",[("Valkyrie multilaser charge pack",3),("Valkyrie fuel (load)",2),("Chimera spare track section",3)])
add("vehicle","R","MF",[("Valkyrie rocket pod (2 Hellstrike)",20),("Valkyrie heavy bolter door-guns (pair)",45),("Void-shield emitter (salvage)",40),("Augur array (small ship)",30)])
# --- Luxury / trade goods ---
add("goods","C","BFE",[("Amasec (case)",2),("Recaff (sack)",0.5)])
add("goods","U","BF",[("Spire wine (case)",2),("Off-world spice",3),("Noble's signet (fence)",4),("Silk bolt",2),("Grox-hide leather",1)])
add("goods","R","BF",[("Gemstones (pouch)",10),("Ancient coin hoard",15)])

# --- Exotic: only on a natural 20 ---
add("exotic","X","BFAEM",[
 ("Ork 'shoota' (confiscated, crude, loud)",3),("Ork 'choppa' (crude cleaver)",2),("Eldar shuriken pistol (1 magazine)",40),
 ("Eldar shuriken catapult (no ammo)",35),("Tau pulse carbine (half charge)",35),("Tau pulse rifle (no charge)",30),
 ("Kroot rifle (bladed stocks)",12),("Dark Eldar splinter pistol (poison, 1 mag)",35),("Necron gauss flayer fragment (inert)",50),
 ("Archeotech laspistol (Dark Age, unknown maker)",60),("Astartes combat knife (Space Marine)",15),("Astartes bolt pistol (huge, heavy)",45),
 ("Sororitas inferno pistol (no charge)",30),("Needle pistol (noble's, 6 darts)",20),("Exitus-pattern round (single, Assassin)",50),
 ("Digital weapon ring (one shot, Jokaero)",60),("Webber (Mechanicus, rare)",20),("Arc rifle (Skitarii)",25),
 ("Radium carbine (Skitarii, toxic)",20),("Volkite serpenta (Dark Age pistol)",70),("Grav-pistol (no charge)",55),
 ("Ork 'burna' (flamer, leaks)",8),("Genestealer cult mining laser (heavy)",15),("Hrud fusil (temporal, unstable)",50),
 ("Squat plasma axe (heirloom)",45),("Inquisitorial hexagrammic ward",25),("Tarot of the Emperor (deck, psychic)",30),
 ("Xenos crystal shard (Eldar, warm)",40),("Rogue Trader's warrant fragment (forged)",20),("Mechadendrite (single, salvage)",15),
])
json.dump(I, open("pools.json","w"), indent=1)
print(len(I), "items")

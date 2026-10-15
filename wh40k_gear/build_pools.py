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
add("las","R","FA",[("Heavy laspistol, 'Nocturne Ember' pattern (side pack, long barrel; ignites on a raw 17+; heavy trigger: -1 quick-draw, chains of 3 max)",14)])
add("las","R","MFA",[("Lasgun, 'Kasr Duet' twin-focus pattern (two crystals, one barrel: a hit lands like a hellgun; 2 charge a pull; chains of 2; braced pad stock; rail)",7)])
add("las","U","MBF",[("Long-las, 'Kasr Sprinter' stripped pattern (skeleton stock and grip, 3x sight; +1 aimed 20-60 m; move and aim; light trigger, NO SAFETY: drop-prone)",4.5)])
add("las","R","BF",[("Duelling laspistol, noble-house pattern",8),("Archeotech lasgun 'sunfire' (worn, works)",30)])
# --- Solid shot ---
add("stub","C","MB",[("Autogun, Agripinaa",1),("Autopistol",1),("Stub revolver",0.5),("Stub automatic",0.75),("Combat shotgun, pump",1.5)])
add("stub","U","MBF",[("Combat shotgun, semi-auto",2),("Ripper gun / drum-fed shotgun",3),("Sawn-off shotgun",1),("Hand cannon (big-bore stubber)",2),("Scrap autogun with drum",1.5)])
add("stub","U","B",[("Silenced stub pistol",2.5),("Holdout stub pistol",1),("Hive-gang 'scattergun'",1),("Ganger's chain-fed autopistol",2)])
# Player design (session 8): auto-revolver. Full rules in DND_CODEX Part 8.
add("stub","U","MBF",[("Auto-revolver, 'Hammerfall' pattern, stub barrel (8-round cylinder, autogun rounds; hold-trigger chains up to 8, no hit bonuses in the chain)",2),("Auto-revolver, 'Hammerfall' pattern, long barrel (as stub; +1 on single aimed shots past 20 m)",2.5)])
add("gear","C","MBF",[("Speedloader (auto-revolver)",0.25)])
# Darktide-inspired autoguns, player-detailed (session 8). Full rules in DND_CODEX Part 8.
add("stub","C","MBF",[("Infantry autogun, 'Columnus' pattern (30-round curved mag; single/burst/auto)",1.25)])
add("stub","U","MBF",[("Braced autogun, 'Graia' pattern (60-round box, bipod; full auto chains of 8; suppression braced; heat)",2.5)])
add("stub","U","MBF",[("Vigilante autogun, 'Kasr Warden' pattern (20-round straight mag; semi-auto chains of 4; light trigger, drop-prone; vented; threaded muzzle; rails)",2)])
add("stub","U","MBF",[("Shredder autopistol, Ius pattern (Darktide; 30-round mag; full-auto chains of 8, no hit bonuses; autopistol punch)",1.5)])
add("stub","U","MBF",[("Headhunter autogun, Agripaa pattern (Darktide; 15-round mag; semi-auto marksman; +2 aimed past 30 m; chains of 2)",3)])
add("stub","U","MBF",[("Combat shotgun, 'Kasr Sweeper' duckbill pattern (one-piece metal body; 8-shell tube; semi-auto chains of 4; flat spread hits up to 3 abreast within 10 m; -2 past 15 m)",3)])
add("stub","U","BF",[("Machine pistol, 'Kasr Hornet' pattern (autogun rounds, 40-round mag; chains of 10, no hit bonuses; hair trigger; jams on shot dice 1-4 from the 13th continuous round; dumps the mag when dropped)",2.5)])
add("mod","U","MBF",[("Muzzle brake (threaded muzzles: a miss in a chain gives no -1)",1.5)])
add("stub","R","MB",[("Web pistol, Arbites pattern (entangles, no damage; 4 shots a canister)",8)])
add("ammo","U","MB",[("Web canister (4 shots)",1)])
add("stub","R","BF",[("Needle rifle (silent toxin darts, 8-dart magazine; CON save or drop a health step)",18)])
add("ammo","U","BF",[("Needle rifle toxin darts (8)",2)])
add("stub","R","MBF",[("Vraks-pattern sniper autorifle",7),("Lucius-pattern 'Ironclad' shotgun",4),("Arbites combat shotgun (shock shells)",6)])
# --- Bolt ---
add("bolt","U","MF",[("Bolt pistol, Godwyn-Deaz (officer)",12)])
add("bolt","R","MF",[("Boltgun, Godwyn pattern",25),("Boltgun, Phobos pattern",28),("Bolt pistol, Ryza pattern",14)])
add("bolt","R","MF",[("Boltgun, Locke Mk IIb 'Spearhead' (Darktide)",26)])
add("bolt","R","MBF",[("Bolt-shotgun, 'Breacher' pattern (single-shot breech, loose bolt rounds; 1-2 shots a beat by recoil)",10)])
add("bolt","R","EF",[("Sororitas bolt pistol (Godwyn-De'az)",16),("Sororitas boltgun",30)])
add("bolt","R","B",[("Bolt pistol, rebored (unstable)",8)])
# Player designs (session 8): Astartes bolters. Too big for a human (DND_CODEX Part 8).
# X = epic/exotic (natural-20 only); L = legendary (natural 20, then a second d20 of 18-20).
add("bolt","X","BF",[("Astartes bolt carbine (Space Marine; human: braced only, -4)",55),("Astartes bolt rifle (Space Marine; human: braced only, -4)",60),("Astartes auto bolt rifle (Space Marine; human: braced only, -4)",65)])
add("bolt","L","BF",[("Astartes heavy bolt rifle (Space Marine; human: braced only, -4)",90),("Astartes heavy bolter (Space Marine; human: mounted only, -4)",120)])
# Officio Assassinorum gear (player-set: all epic or legendary). Rules: catalogue/assassinorum.md.
add("stub","X","BF",[("Exitus pistol (Vindicare; silent, +1; may self-destruct when first picked up)",60),("Exitus rounds: shield-breaker (each)",10),("Exitus rounds: turbo-penetrator (each)",10),("Exitus rounds: hellfire (each)",10)])
add("stub","L","BF",[("Exitus rifle (Vindicare; +3 aimed, no range or weather penalty)",150),("Neural shredder (Callidus; 10 m cone, CON save or two health steps)",180),("Executioner pistol (Eversor; bolt pistol + toxin needler)",150),("Needlespine blaster (Adamus; silent, +2 at range, toxin)",140)])
add("melee","X","BF",[("Poison blades, concealed (Callidus; toxin, hidden on a search)",50)])
add("melee","L","BF",[("Phase sword (Callidus; C'tan blade, ignores armour and shields)",200),("Neuro gauntlet (Eversor; stun + CON save or two health steps)",160),("Nemesii blade (Adamus; +2 strike first and parry)",150)])
add("explosive","X","BF",[("Psyk-out grenade (Culexus; no powers for 2 turns in the burst)",20)])
add("gear","L","BF",[("Animus speculum (Culexus; pariah only)",250),("Venenum toxin kit (injectors and poison globes)",120)])
# --- Plasma / melta / flame ---
add("plasma","R","MAF",[("Plasma pistol, Ryza pattern",25),("Plasma gun, Mars pattern",30),("Plasma gun, Ryza pattern",32)])
add("plasma","U","MAF",[("Plasma cell",6)])
add("plasma","R","AF",[("Plasma repeater, 'Kasr Furnace' break-action lever pattern (one plasma cell in the breech: 8 shots, 12 tuned; 2 lever actions a beat (shot or pump, any mix), up to 3 pumps for a charged shot, each pump uses a shot; held charge builds heat)",30)])
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
add("explosive","R","MAF",[("Plasma tripwire mine (laser trip, plasma-cell charge)",10)])
add("explosive","U","MBF",[("Thrown demo satchel with paired detonator (mag-clamp, throw or set; beeps when armed)",5)])
add("explosive","U","MBF",[("Air-frag 'blender' grenade (heavy shrapnel, 2-second fuse, ricochets)",2)])
add("explosive","R","BF",[("Phosphex canister (forbidden)",15),("Shrapnel mine",3)])
# --- Ammunition ---
add("ammo","C","MBF",[("Las pack",0.25),("Stub/auto rounds (box)",0.5),("Shotgun shells (box)",0.5),("Heavy stubber belt",1)])
add("ammo","U","MAF",[("Hot-shot pack (Guard)",1),("Hot-shot pack (Mechanicus pattern)",3),("Bolt rounds (10)",8),("Stubber drum magazine",1.5),("Man-stopper shells (box)",1),("Inferno shells (box)",2),("Extended las pack",0.75)])
add("ammo","R","MF",[("Kraken-pattern bolt rounds (10, Astartes)",20),("Hellfire shells (box)",4)])
# --- Melee ---
add("melee","C","MB",[("Combat knife",0.25),("Bayonet",0.25),("Entrenching tool",0.25),("Trench club",0.25),("Cadian machete",0.5)])
add("melee","U","MBF",[("Navy cutlass",2),("Chainsword",6),("Chain axe",8),("Shock maul",7),("Mono-knife",3),("Krieg trench shovel (sharpened)",0.5),("Officer's sabre",3),("Chain knife",3),("Shock baton (Arbites)",4)])
add("melee","R","MAF",[("Power maul",25),("Power sword",30),("Power axe",30),("Power knife",15),("Chainsword, Lucius heavy",10),("Eviscerator (two-handed chainsword)",22),("Thunder hammer (damaged)",40)])
# Player design (session 8): plasteel throwing knives. Full rules in DND_CODEX Part 8.
add("melee","U","MBF",[("Combat chain-knife, 'Kasr Gnaw' pattern (combat-knife frame, chain blade, spine motor, hilt lever; +1 strike first; chainsword bite)",3)])
add("melee","U","MBF",[("Injector stiletto, 'Kasr Sting' pattern (straight stiletto blade with an injection channel; pommel vial, 1 dose; skeleton hilt, green cord wrap; throwable)",2)])
add("gear","U","BF",[("Injector vial: toxin (1 dose; CON save or drop a health step)",1),("Injector vial: paralytic (1 dose; CON save or can't move or act next beat)",1.5)])
add("gear","X","EF",[("Psy-ward amulet (blessed parchment; burns to take one hit that would hurt the wearer)",45)])
add("goods","R","B",[("Chaos ward-mark (cult charm; takes one hit, the god's way, at a price)",15)])
add("goods","R","B",[("Chaos psyker staff (cultist witch's focus; psyker only; touching it is dangerous)",25)])
add("goods","R","B",[("Chaos grimoire (forbidden book; the DM decides what it does; the Inquisition wants it)",12)])
add("explosive","U","B",[("Cult gas bottle (glass, plastek cage and sealed cap; shatters on impact; gas by cult: plague, rage, euphoria or visions)",1.5)])
add("melee","R","MAF",[("Power fist, Guard pattern (human-sized; through power armour; slow, +2 to block or parry it)",35)])
add("melee","X","BF",[("Astartes power fist (Space Marine; too big for a human hand: trade or trophy)",70),("Neo Scar scimitar (White Scars neophyte training blade, one-handed; ceramite edge, +1 strike first, no hilt)",45)])
add("melee","R","AF",[("Las-fist, 'Kasr Knuckle' pattern (power fist with a lasgun barrel and crystal; trigger in the fist; -3 to shoot, none point-blank)",40)])
add("melee","X","BF",[("Power claw, 'Kasr Talon' pattern (four curved power blades; charge and expel into a stabbed target)",60)])
add("melee","R","F",[("Force wakizashi, 'Kasr Veil' pattern (psyker only; skeleton grip, no guard; warp-shield intake, Perils 1-3 each beat)",35)])
add("melee","R","BF",[("Plasteel throwing knives, 'Callidus' pattern, wavy blade (set of 6; through carapace on a solid hit; wound -2 to treat)",4)])
add("melee","C","MB",[("Hive shank (scrap knife)",0.1),("Scrap throwing knives (set of 4)",0.4),("Combat axe, Rashad pattern (fast, light)",1)])
add("melee","R","MAF",[("Thunder hammer, Crucis pattern (intact; heavy, slow)",50),("Power falchion (duelling blade)",28),("Omnissian power sword (Mechanicus)",32),("Transonic blades, paired (Skitarii)",30)])
add("melee","R","F",[("Blaze force sword (psyker only)",45),("Blaze force greatsword (psyker only)",60)])
add("melee","R","E",[("Blessed power maul (Ecclesiarchy)",28),("Sororitas power sword",32)])
add("melee","R","B",[("Assassin's mono-wire garrotte",6),("Needle-blade (toxin)",8)])
# --- Armour ---
add("armour","C","MB",[("Flak vest",0.5),("Flak armour set",1),("Flak helmet",0.25),("Gas mask / rebreather",0.5)])
add("armour","U","MBF",[("Carapace armour set",8),("Carapace chest plate",4),("Mesh armour (light, quiet)",5),("Boarding shield",4),("Void-suit, Navy",4),("Hazard suit (plague-rated)",5),("Arbites carapace",10)])
add("armour","C","MB",[("Makeshift shield (wood and scrap; +1 block, 1/3 cover, breaks after 2-3 heavy hits)",1)])
add("armour","U","MBF",[("Forged shield (+2 block, half cover)",6)])
add("mod","U","MBF",[("Shield viewing slot (shoot a pistol through without losing cover)",1.5),("Shield spikes (charge shield-first: +3 on the charge, +1 shield melee after)",2)])
add("armour","R","MB",[("Arbitrator shield (Adeptus Arbites riot shield; +2 block, portable cover, pistol notch)",10)])
add("armour","R","MAF",[("Storm trooper carapace set",15),("Storm shield (power field)",30),("Refractor field",25),("Conversion field (damaged)",35),("Skitarii armour (augmetic fit)",18)])
add("armour","R","MF",[("Tempestus Scion helmet (rebreather, auspex; +2 Perception, +1 shooting)",25)])
add("gear","U","MBF",[("Back gun-scabbard / heavy sling mount (carry a second long gun or a heavy on the back)",1)])
add("gear","C","MBF",[("Mag belt / bandolier (+4 packs or mags ready)",0.5),("Melee sheath / scabbard (fits the weapon)",0.25),("Belt side-pouch (2 grenades or small kit)",0.25),("Pistol holster (hip or chest)",0.25)])
add("armour","R","E",[("Sororitas power armour, damaged",50),("Rosarius (blessed field, small)",30)])
# --- Optics / sights / mods ---
add("mod","U","MBF",[("Reflex sight",3),("Telescopic sight",3),("Photo-visor (low-light)",2),("Magnoculars",1.5),("Bipod",0.5),("Weapon sling, padded",0.25),("Quick-draw holster",0.5),("Silencer (stub/auto)",2),("Extended magazine",1),("Bayonet lug kit",0.25),("Laser designator",3)])
add("mod","U","MBF",[("Extended magazine kit, las or stub (+50% shots)",1.5)])
add("mod","U","MBF",[("Diamantine whetstone (any edged blade: +1 pierce for the next 2 hits; ~10 uses)",1)])
add("mod","R","MF",[("Underslung chain-bayonet (rifle-mounted chainsword)",10)])
add("mod","R","MAF",[("Extended magazine kit, bolt or plasma housing (+50% shots)",6),("Range-finder sight (+1 shooting past ~30 m)",10),("Power weapon tuning kit (steadies the field, through power armour on any hit)",12),("Shock-coil kit (any weapon: +1 on your next roll against a target you hit, +2 for heavy weapons; 6 charges a fight)",8)])
add("mod","R","MAF",[("Hot-shot conversion kit (lasgun)",5),("Overcharge capacitor (las)",8),("Mechanicus focusing lens",10),("Auto-targeter (augur sight)",12),("Heat-sink shroud (las)",4),("Chainsword teeth, adamantium (set)",12),("Motor housing, high-tolerance",9)])
# --- Gear / tech ---
add("gear","C","MB",[("Micro-bead",0.5),("Chrono",0.5),("Lumen (torch)",0.25),("Field rations (crate)",0.5),("Water purifier",0.5),("Rope (20 m)",0.25),("Lho-sticks (carton)",0.25),("Imperial Infantryman's Uplifting Primer",0.1)])
add("gear","U","MBF",[("Map-slate",1),("Auspex (hand)",6),("Vox-caster (manpack)",5),("Flares (box of 10)",0.5),("Grav-chute",6),("Climbing rig and grapnel",1.5),("Demolitions kit / bag",1.5),("Large field pack",1),("Drag harness",0.5),("Multi-key / lockbreaker",2),("Cutting torch",3),("Med-kit",3),("Stimm (dose)",0.5),("Antitoxin (dose)",1),("Combat drug 'slaught' (dose)",1)])
add("gear","R","B",[("Spook (dose; wakes latent psychic power, Perils 1-6)",6)])
add("gear","C","B",[("Obscura (dose; hive narcotic, trade value)",0.5),("Spur (dose; ganger stimulant, +1 everything, early crash)",0.5)])
add("gear","U","MB",[("Kalma (dose; nerve calmer, fearless, -1 strike first)",1),("Morphia (dose; painkiller, one health step better)",1)])
add("gear","U","B",[("Onslaught (dose; two moves a turn, -2 shooting)",1.5)])
add("gear","R","AF",[("Glanding implant (needs an augmetic surgeon; one combat-drug effect a fight)",20)])
add("gear","R","MAF",[("Concentrated stimm (dose)",2),("Concentrated antitoxin (dose)",4),("Combat drug 'Frenzon', concentrated (+3 melee; backfire 1-2)",4)])
add("gear","U","MB",[("Combat drug 'Quicksilver' (speed: +2 Athletics and moving)",1.5),("Combat drug 'Deadeye' (focus: +2 shooting)",1.5),("Combat drug 'Frenzon' (rage: +2 melee)",1.5),("Combat drug 'Slaught' (reflexes: +2 strike first and dodge, +1 STR)",1.5),("Combat drug 'Adrenaline' (senses: +4 Perception, +1 shooting)",1.5)])
add("gear","R","MAF",[("Servo-skull, gun (built-in laspistol)",30),("Servo-skull, burner (built-in micro-flamer)",35)])
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
add("vehicle","R","MF",[("Valkyrie bolt-rocket pods, pair (6 rockets that burst into bolt rounds)",35)])
add("heavy","R","MF",[("Las-cannon, medium tripod emplacement (one heavy beam every other beat)",35)])
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

# --- Enemy loot pools (session 8, player-set) ---
# What each enemy type carries when killed or looted. Rolled per enemy by roll_enemy.py.
# Each slot lists (item, rarity). "Found or made" items are homemade or scavenged
# pieces that only enemies carry; they can have quirks.
E = {
 "cultist": {
  "weapon": [("Autogun, Agripinaa","C"),("Stub automatic","C"),("Stub revolver","C"),("Autopistol","C"),("Lasgun, Kantrael M36 (stolen)","C"),
             ("Scrap autogun with drum","U"),("Sawn-off shotgun","U"),("Hive-gang 'scattergun'","U"),("Lasgun, Lucius No.98 (stolen)","U"),
             ("Hellgun, Ryza pattern (stolen Guard issue)","R"),("Flamer, Ryza pattern (stolen)","R")],
  "melee":  [("Hive shank (scrap knife)","C"),("Trench club","C"),("Cadian machete","C"),("Scrap throwing knives (set of 4)","C"),
             ("Chain knife","U"),("Combat axe, Rashad pattern","U"),("Chainsword","U"),("Needle-blade (toxin)","R")],
  "armour": [("Rags, no armour","C"),("Flak vest","C"),("Gas mask / rebreather","C"),("Flak armour set","U"),("Carapace chest plate (stolen)","R")],
  "extra":  [("Nothing","C"),("Frag grenade","C"),("Black candles and chalk","C"),("Crude iron cult amulet","C"),("Stimm (dose)","U"),
             ("Combat drug 'Frenzon' (dose)","U"),("Choke gas grenade","U"),("Cult gas bottle (gas of their god)","U"),("Cult prayer-book","R")],
  "found":  [("Cult-forged blade (crude, sharp; +1 vs flesh, breaks on a natural 1)","U"),("Jury-rigged autogun (fires full chains; jams on a 1-2)","U"),
             ("Pipe-bomb (frag, short fuse; a natural 1 goes off in hand)","U"),("Cult gas bottle x2 (gas of their god)","U"),("Stolen officer's laspistol","U"),
             ("Desecrated chainsword (spiked, roars; -1 to parry with it)","R"),("Krak grenade (stolen)","R"),("Plasma pistol, Ryza pattern (stolen, slow-filled cell)","R"),("Chaos grimoire (forbidden book)","R"),("Chaos ward-mark (takes one hit, the god's way)","R")],
 },
 "raider": {
  "weapon": [("Autogun, Agripinaa","C"),("Autopistol","C"),("Stub automatic","C"),("Combat shotgun, pump","C"),
             ("Ganger's chain-fed autopistol","U"),("Hive-gang 'scattergun'","U"),("Auto-revolver, 'Hammerfall' pattern, stub barrel","U"),("Braced autogun (heavy barrel)","U"),
             ("Hand cannon (big-bore stubber)","U"),("Ripper gun / drum-fed shotgun","R"),("Heavy stubber","R")],
  "melee":  [("Hive shank (scrap knife)","C"),("Combat knife","C"),("Combat axe, Rashad pattern","C"),("Scrap throwing knives (set of 4)","C"),
             ("Chain knife","U"),("Shock baton (Arbites, stolen)","U"),("Mono-knife","U"),("Chain axe","R")],
  "armour": [("Leathers, no armour","C"),("Flak vest","C"),("Flak armour set","U"),("Mesh armour (light, quiet)","U"),("Arbites carapace (stolen)","R")],
  "extra":  [("Nothing","C"),("Frag grenade","C"),("Lho-sticks (carton)","C"),("Lock-picks, hive pattern","U"),("Combat drug 'slaught' (dose)","U"),
             ("Combat drug 'Quicksilver' (dose)","U"),("Stimm (dose)","U"),("Forged Munitorum ID chits","R")],
  "found":  [("Bolted-together drum autogun (heavy; +1 suppression, -1 from the hip)","U"),("Spiked knuckle-duster blade","U"),("Speedloader and spare Hammerfall cylinder","U"),
             ("Demo satchel (stolen)","U"),("Silenced stub pistol","R"),("Auto-revolver, 'Hammerfall' pattern, long barrel","R"),("Bolt pistol, rebored (unstable)","R")],
 },
 "pirate": {
  "weapon": [("Combat shotgun, pump","C"),("Autopistol","C"),("Stub revolver","C"),("Lascarbine, Accatran Mk IV","C"),
             ("Combat shotgun, semi-auto","U"),("Auto-revolver, 'Hammerfall' pattern, long barrel","U"),("Heavy laspistol","U"),("Las-scattergun 'shotlas'","U"),
             ("Ripper gun / drum-fed shotgun","U"),("Boltgun, Godwyn pattern (stolen)","R"),("Plasma pistol, Ryza pattern (stolen)","R")],
  "melee":  [("Navy cutlass","C"),("Combat knife","C"),("Boarding axe","C"),("Officer's sabre","U"),("Chainsword","U"),("Shock maul","U"),("Power knife","R"),("Power sword (taken from a captain)","R")],
  "armour": [("Deck coat, no armour","C"),("Flak armour set","C"),("Void-suit, Navy (patched)","U"),("Boarding shield","U"),("Carapace armour set","R")],
  "extra":  [("Nothing","C"),("Frag grenade","C"),("Amasec (bottle)","C"),("Grav-chute","U"),("Spoof-tag (fakes a transponder)","U"),
             ("Off-world spice","U"),("Gemstones (pouch)","R"),("Breaching charge","R")],
  "found":  [("Twin-barrel boarding pistol (2 shotgun shells, one beat to reload)","U"),("Weighted grapple-cutlass","U"),("Captain's flintlock-pattern las pistol (ornate; +1 on single shots)","U"),
             ("Melta bomb (stolen)","R"),("Refractor field (salvaged, flickers)","R"),("Plasteel throwing knives, 'Callidus' pattern (set of 6)","R")],
 },
}
E["traitor"] = {
  "weapon": [("Lasgun, Kantrael M36","C"),("Lasgun, Lucius No.98","C"),("Lascarbine, Accatran Mk IV","C"),("Autogun, Agripinaa","C"),
             ("Infantry autogun, 'Columnus' pattern","U"),("Hellgun, Ryza pattern","U"),("Lasgun, Accatran Mk XIV","U"),("Combat shotgun, semi-auto","U"),
             ("Hellgun, Accatran (compact)","R"),("Lasgun, 'Kasr Duet' twin-focus pattern","R")],
  "melee":  [("Bayonet (fixed)","C"),("Combat knife","C"),("Entrenching tool","C"),("Cadian machete","C"),
             ("Krieg trench shovel (sharpened)","U"),("Chain knife","U"),("Chainsword","U"),("Power knife","R")],
  "armour": [("Flak armour set","C"),("Flak vest and helmet","C"),("Carapace chest plate","U"),("Carapace armour set","U"),("Storm trooper carapace (looted)","R")],
  "extra":  [("Nothing","C"),("Frag grenade","C"),("Spare las packs (3)","C"),("Smoke grenade","C"),("Stimm (dose)","U"),
             ("Krak grenade","U"),("Ration pack and lho","C"),("Defaced regimental insignia","U")],
  "found":  [("Officer's laspistol","U"),("Bolt pistol, Godwyn-Deaz (officer, few rounds)","R"),("Hot-shot packs (2)","U"),
             ("Shotgun with the eagle scratched off","U"),("Plasma pistol, Ryza pattern (taken from a dead officer)","R"),("Melta bomb","R"),
             ("Commissar's power sword (trophy)","R")],
}
# Specialist kits (player-set, session 8): rolled on 16-20 on the enemy's role d20.
# Each role: (main kit, rarity) options; the specialist also rolls armour and an extra.
SPEC = {
 "cultist": {
  "sniper":      [("Long-las, Mezoa (stolen) + laspistol","U"),("Scoped autogun + stub revolver","C"),("Vraks-pattern sniper autorifle","R")],
  "grenadier":   [("Bag of 4 frags + autopistol","C"),("4 pipe-bombs + stub revolver","C"),("Grenade launcher (stolen) + 6 frag rounds","R")],
  "heavy":       [("Heavy stubber + 2 belts","U"),("Braced autogun with drum","C"),("Heavy bolter, Guard pattern (stolen, 1 belt)","R")],
  "assassin":    [("Silenced stub pistol + mono-knife","U"),("Needle-blade (toxin) + throwing knives","U"),("Garrotte + chain knife","C")],
  "flamer":      [("Hand flamer + 1 canister","U"),("Flamer, Ryza pattern (stolen) + 2 canisters","R"),("Promethium sprayer (homemade; short reach, leaks on a 1)","C")],
  "demolitions": [("Demo satchel + detonator","U"),("3 krak grenades (stolen)","R"),("Mining charges x2 + stub pistol","C")],
  "medic":       [("Med-kit + 3 stimms + autopistol","C"),("Cult 'blessings' (stimms and drugs) + knife","C")],
  "leader":      [("Chainsword + laspistol (cult preacher)","U"),("Desecrated chainsword + autopistol","U"),("Bolt pistol (stolen) + power knife","R")],
  "psyker":      [("Witch: rogue psyker, crude staff + knife (warp power; Perils on a natural 1)","C"),("Witch with a Chaos psyker staff + knife (fire, lightning, force; Perils 1-3 a beat)","U")],
 },
 "raider": {
  "sniper":      [("Scoped autogun + autopistol","C"),("Long-las, Mezoa + heavy laspistol","U"),("Vraks-pattern sniper autorifle","R")],
  "grenadier":   [("Bandolier of 4 frags + 2 smoke + autopistol","C"),("Grenade launcher + 6 rounds","U")],
  "heavy":       [("Heavy stubber + 2 belts","U"),("Ripper gun / drum-fed shotgun","U"),("Bolted-together drum autogun","C")],
  "assassin":    [("Silenced stub pistol + mono-knife","U"),("Throwing knives + chain knife","C"),("Needle-blade (toxin)","R")],
  "flamer":      [("Hand flamer + 1 canister","U"),("Flamer + 2 canisters","R")],
  "demolitions": [("Demo satchel + detonator","U"),("Breaching charges x2","U"),("Melta bomb (stolen)","R")],
  "medic":       [("Med-kit + 3 stimms + autopistol","C"),("Combat drugs (slaught, Quicksilver) + stimm","U")],
  "leader":      [("Gang boss: chain axe + hand cannon","U"),("Hammerfall long barrel + chainsword","U"),("Bolt pistol, rebored + power knife","R")],
  "breacher":    [("Boarding shield + sawn-off shotgun","U"),("Combat shotgun, semi-auto + shock baton","U")],
 },
 "pirate": {
  "sniper":      [("Long-las, Mezoa + laspistol","U"),("Scoped lascarbine + stub revolver","C"),("Long-las, Helbore","R")],
  "grenadier":   [("Bag of 4 frags + 2 smoke + autopistol","C"),("Grenade launcher + 6 rounds","U")],
  "heavy":       [("Heavy stubber + 2 belts","U"),("Ripper gun / drum-fed shotgun","U"),("Multi-laser, man-portable","R")],
  "assassin":    [("Silenced stub pistol + mono-knife","U"),("Plasteel throwing knives, 'Callidus' (set of 6) + cutlass","R"),("Garrotte + combat knife","C")],
  "flamer":      [("Hand flamer + 1 canister","U"),("Flamer + 2 canisters","U")],
  "demolitions": [("Breaching charges x2 + pump shotgun","U"),("Demo satchel + detonator","U"),("Melta bomb","R")],
  "medic":       [("Ship's surgeon: med-kit, 3 stimms, autopistol","C"),("Med-kit + antitoxin + laspistol","U")],
  "leader":      [("Pirate captain: power sword + heavy laspistol","R"),("Bosun: chainsword + Hammerfall long barrel","U"),("Officer's sabre + boarding pistol","C")],
  "breacher":    [("Boarding shield + combat shotgun, semi-auto","U"),("Boarding shield + shock maul","U"),("Void-suited boarder: boarding axe + shotgun","C")],
  "vox":         [("Vox-caster + spoof-tag + autopistol","U"),("Auspex + lascarbine","U")],
 },
}
SPEC["traitor"] = {
  "sniper":      [("Long-las, Mezoa + laspistol","U"),("Scoped lasgun + laspistol","C"),("Long-las, Helbore","R")],
  "grenadier":   [("Grenade launcher + 6 frag, 2 krak rounds","U"),("Bag of 4 frags + 2 kraks + lasgun","C")],
  "heavy":       [("Heavy stubber + 2 belts (two-man team)","U"),("Heavy bolter, Guard pattern (two-man team)","R"),("Braced autogun, 'Graia' pattern","C")],
  "plasma gunner": [("Plasma gun, Mars pattern (slow-filled cell) + laspistol","R"),("Meltagun + laspistol","R"),("Hellgun with hot-shot packs","U")],
  "flamer":      [("Flamer, Ryza pattern + 2 canisters","U"),("Hand flamer + lasgun","U")],
  "demolitions": [("Demo satchel + detonator + lasgun","U"),("Breaching charges x2 + 2 kraks","U")],
  "medic":       [("Med-kit + 3 stimms + laspistol","C"),("Med-kit, antitoxin, 2 stimms + lascarbine","U")],
  "leader":      [("Renegade sergeant: chainsword + laspistol","U"),("Renegade officer: power sword + bolt pistol","R"),("Renegade sergeant: shotgun + combat knife","C")],
  "vox":         [("Vox-caster + lascarbine (calls in the rest)","U"),("Vox-caster + auspex + laspistol","U")],
}
# Shared roles added (player-set): rogue psyker, breacher, vox/auspex for every type;
# plasma gunner for raiders and pirates too.
PSY = [("Rogue psyker: crude staff + knife (unsanctioned; basic warp powers, Perils 1-3 a beat)","C"),("Rogue psyker with a stolen force staff (stronger powers, Perils 1-3 a beat)","R")]
BREACH = [("Boarding shield + sawn-off shotgun","U"),("Combat shotgun, semi-auto + shock baton","U"),("Breaching charge + pump shotgun","C")]
VOX = [("Vox-caster + autopistol (calls in the rest)","U"),("Auspex + lascarbine (sees through walls)","U")]
PLASMA = [("Plasma pistol, Ryza pattern (slow-filled cell) + autopistol","R"),("Plasma gun, Mars pattern (stolen, rushed cell)","R"),("Hot-shot hellgun","U")]
for k in ("raider","pirate","traitor"): SPEC[k].setdefault("psyker", PSY)
for k in ("cultist","traitor"): SPEC[k].setdefault("breacher", BREACH)
for k in ("cultist","raider"): SPEC[k].setdefault("vox", VOX)
for k in ("raider","pirate"): SPEC[k].setdefault("plasma gunner", PLASMA)
# Traitor elites: traitor storm troopers, renegade Inquisition kill-teams. Rolled with
# the elite weights (common 25 / uncommon 50 / rare 25) every time.
E["traitor_elite"] = {
  "weights": {"C": 25, "U": 50, "R": 25},
  "weapon": [("Hellgun, Ryza pattern","C"),("Hellgun, Accatran (compact)","C"),("Hot-shot volley gun","U"),("Lasgun, 'Kasr Duet' twin-focus pattern","U"),
             ("Boltgun, Godwyn pattern","R"),("Plasma gun, Mars pattern","R"),("Combat shotgun, 'Kasr Sweeper' duckbill pattern","U")],
  "melee":  [("Combat knife","C"),("Chain knife","C"),("Chainsword","U"),("Shock maul","U"),("Power knife","U"),("Power sword","R")],
  "armour": [("Storm trooper carapace","C"),("Storm trooper carapace and Scion-pattern helmet","U"),("Storm trooper carapace with a refractor field","R")],
  "extra":  [("Frag and krak grenades","C"),("Hot-shot packs (3)","C"),("Photon flash grenade","U"),("Stimm and med-kit","U"),
             ("Melta bomb","R"),("Grav-chute","U"),("Ordo seal (forged or stolen)","R")],
  "found":  [("Hellpistol","U"),("Bolt pistol with a full magazine","U"),("Inferno pistol","R"),("Refractor field","R"),
             ("Psy-ward amulet (stolen from the Ordo)","R"),("Power fist, Guard pattern","R")],
}
SPEC["traitor_elite"] = {
  "sniper":      [("Long-las, Helbore + hellpistol","U"),("Hot-shot long-las with range-finder","R")],
  "grenadier":   [("Grenade launcher with krak and frag + hellgun","U"),("Melta bombs x2 + hellgun","R")],
  "heavy":       [("Heavy bolter (two-man team)","U"),("Multi-laser, man-portable","U"),("Lascannon, man-portable (two-man team)","R")],
  "plasma gunner": [("Plasma gun, Mars pattern (proper cell) + hellpistol","U"),("Meltagun + hellpistol","U")],
  "flamer":      [("Heavy flamer","U"),("Flamer + hand flamer","U")],
  "demolitions": [("Demo satchels x2 + detonator","U"),("Breaching charges x3 + melta bomb","R")],
  "medic":       [("Medicae kit, concentrated stimms + hellpistol","U")],
  "leader":      [("Renegade storm-trooper captain: power sword + plasma pistol","R"),("Renegade Interrogator: bolt pistol + power sword + forged rosette","R"),("Sergeant: chainsword + hellpistol","U")],
  "vox":         [("Vox-caster + auspex + hellgun","U")],
  "breacher":    [("Storm shield + bolt pistol","R"),("Boarding shield + duckbill shotgun","U")],
  "psyker":      [("Renegade sanctioned psyker: force staff + laspistol","R")],
  "assassin":    [("Silenced hellpistol + mono-knife","U"),("Needle rifle + power knife","R")],
}
# Heavy gunner (player-set): one soldier carrying a heavy gun, like Morcant. Traitor
# "heavy" stays the two-man team, renamed; cultists, raiders and pirates' heavies
# were already one-man.
for k in ("traitor","traitor_elite"):
    SPEC[k]["heavy team"] = SPEC[k].pop("heavy")
SPEC["traitor"]["heavy gunner"] = [("Heavy stubber + 2 belts, carried","C"),("Braced autogun, 'Graia' pattern","C"),("Ripper gun / drum-fed shotgun","U"),("Las-box, 'Kasr Barr' light las-LMG","R")]
SPEC["traitor_elite"]["heavy gunner"] = [("Las-box, 'Kasr Barr' light las-LMG","U"),("Hot-shot volley gun","U"),("Heavy stubber with drum mag, carried","C"),("Multi-laser, man-portable, carried","R")]
for k in ("cultist","raider","pirate"):
    SPEC[k]["heavy gunner"] = SPEC[k].pop("heavy")
# Heavy team for raiders and pirates too; berserker for every type (player-set).
SPEC["raider"]["heavy team"] = [("Heavy stubber on a tripod (two-man team)","C"),("Autocannon, salvaged (two-man team)","R"),("Mortar with 6 rounds (two-man team)","U")]
SPEC["pirate"]["heavy team"] = [("Heavy stubber on a tripod (two-man team)","C"),("Heavy bolter, stolen (two-man team)","R"),("Multi-laser on a deck mount (two-man team)","U")]
BERSERK = {
  "cultist": [("Chain axe + 4 doses of Frenzon (frothing, chanting)","U"),("Cleaver and spiked club + 3 doses of slaught","C"),("Chainsword + 4 doses of Frenzon","U"),("Eviscerator + 5 doses of Frenzon","R")],
  "raider":  [("Chain axe + 3 doses of slaught","U"),("Two hive shanks + 4 doses of Frenzon","C"),("Spiked knuckle-duster blades + 3 doses of Frenzon","C"),("Chainsword + 5 doses of slaught","R")],
  "pirate":  [("Boarding axe + 3 doses of slaught","C"),("Chain axe + 4 doses of Frenzon","U"),("Two cutlasses + 3 doses of Frenzon","C"),("Power axe + 4 doses of slaught","R")],
  "traitor": [("Chainsword + 3 doses of Frenzon (a broken penal trooper)","U"),("Sharpened trench shovel + 3 doses of slaught","C"),("Chain axe + 4 doses of Frenzon","U")],
  "traitor_elite": [("Power axe + 4 doses of concentrated Frenzon","R"),("Chainsword and power knife + 4 doses of Frenzon","U"),("Eviscerator + 5 doses of Frenzon","R")],
}
for k,v in BERSERK.items(): SPEC[k]["berserker"] = v
# New roles (player-set, session 8): brute, icon bearer, beast handler, tech-adept,
# infiltrator, enforcer, bomb zealot, gunslinger, chem-doctor, bodyguard.
# Behaviour and rules for every role: bestiary/roles.md.
NEW = {
 "brute": {
  "cultist": [("Mutant brute: huge rusted cleaver, slab of scrap armour","C"),("Mutant brute: chained engine-block flail","U"),("Mutant brute: two-handed eviscerator","R")],
  "raider":  [("Brute: sledgehammer and a door for a shield","C"),("Brute: chain axe in each hand","U"),("Brute: stolen Ogryn ripper gun and a club","R")],
  "traitor": [("Renegade Ogryn: ripper gun and slab shield","U"),("Renegade Ogryn: grenadier gauntlet","R"),("Penal brute: maul and a stolen trench club","C")],
  "traitor_elite": [("Renegade Ogryn bodyguard: power maul and slab shield","R"),("Renegade Ogryn: heavy stubber, carried","U")],
 },
 "icon bearer": {
  "cultist": [("Cult icon: a chalk gate on a pole of bones + autopistol","C"),("Daemon-touched icon that whispers + chain knife","R"),("God-banner of stitched skin + stub revolver","U")],
  "raider":  [("Gang banner of trophies + autopistol","C"),("War-horn and skull standard + chain knife","U")],
  "pirate":  [("Captain's black flag on a boarding pike + heavy laspistol","C"),("Brass ship's icon + cutlass","U")],
  "traitor": [("Defaced regimental colours + laspistol","C"),("Traitor icon of the eight-pointed star + chainsword","U")],
  "traitor_elite": [("Fallen company colours, the old honours burned + bolt pistol","U"),("Their regiment's real standard, stolen + power sword","R")],
 },
 "beast handler": {
  "cultist": [("Handler with 4 mutant hounds + goad and autopistol","C"),("Handler with 4 warp-hounds (daemon-touched) + whip","R")],
  "raider":  [("Handler with 4 fighting dogs + stub revolver","C"),("Handler with 4 chained mutant beasts + shock prod","U")],
  "pirate":  [("Handler with 2 void-rats the size of dogs + autopistol","C"),("Handler with a cyber-mastiff (stolen Arbites) + shotgun","U")],
  "traitor": [("Dog-handler with 2 war dogs + lasgun","C"),("Handler with 2 cyber-mastiffs + laspistol","U")],
  "traitor_elite": [("Handler with 2 cyber-mastiffs + hellpistol","U"),("Handler with 3 cyber-mastiffs + hellgun","R")],
 },
 "tech-adept": {
  "cultist": [("Heretek: scrap-built auto-turret, cutting torch, autopistol","U"),("Heretek: daemon-bound vox-jammer + servo-arm","R")],
  "raider":  [("Tech-scav: deployable stubber turret + lock-breaker","U"),("Tech-scav: vox jammer + multi-key + autopistol","C")],
  "pirate":  [("Ship's mechanic: door-locker, auto-turret, laspistol","U"),("Ship's mechanic: cutting torch, spoof-tags, shotgun","C")],
  "traitor": [("Renegade enginseer: auto-turret, repair kit, lasgun","U"),("Renegade enginseer: vox jammer, servo-skull, laspistol","R")],
  "traitor_elite": [("Renegade tech-priest: heavy auto-turret, servo-arm, hellpistol","R"),("Combat engineer: vox jammer, auspex, demo charge, hellgun","U")],
 },
 "infiltrator": {
  "raider":  [("Infiltrator: silenced stub pistol, mono-knife, dark rags","U"),("Infiltrator: crossbow-quiet needle pistol, garrotte","R")],
  "traitor": [("Infiltrator: silenced stub pistol, combat knife, chameleoline scraps","U"),("Infiltrator: suppressed Kasr Warden autogun, knife","U")],
  "traitor_elite": [("Infiltrator: silenced hellpistol, power knife, chameleoline cloak","R"),("Infiltrator: needle rifle, mono-knife, chameleoline cloak","R"),("Infiltrator: suppressed Kasr Warden autogun, knife, cloak","U")],
 },
 "enforcer": {
  "traitor": [("Renegade commissar: bolt pistol and chainsword, greatcoat","U"),("Enforcer: laspistol and power maul, the old Commissariat cap","U")],
  "traitor_elite": [("Fallen commissar: bolt pistol, power sword, carapace greatcoat","R"),("Enforcer: plasma pistol and chainsword","R")],
 },
 "bomb zealot": {
  "cultist": [("Bomb zealot: vest of mining charges, a dead-man's grip","C"),("Bomb zealot: promethium tanks strapped on, a flare","U"),("Bomb zealot: a stolen melta bomb on a chest rig","R")],
  "raider":  [("Bomb-runner: a captured hiver, charges chained to their chest","C"),("Bomb-runner: a gang coward in a vest of pipe-bombs","C"),("Bomb-runner: a prisoner wired with a stolen krak charge","U")],
  "pirate":  [("Bomb-runner: a captured deckhand with mining charges lashed on","C"),("Bomb-runner: a crew coward in a promethium-tank harness","C"),("Bomb-runner: a prisoner with a melta bomb strapped to their back","R")],
 },
 "gunslinger": {
  "raider": [("Gunslinger: two Hammerfall stub revolvers","U"),("Gunslinger: two autopistols","C"),("Gunslinger: Headhunter autogun","U"),("Gunslinger: Kasr Warden autogun","C")],
  "pirate": [("Gunslinger: two heavy laspistols","U"),("Gunslinger: two Hammerfall long revolvers","C"),("Gunslinger: Kasr Sprinter long-las","U"),("Gunslinger: semi-auto shotgun","C")],
  "traitor": [("Gunslinger: two Kantrael laspistols","C"),("Gunslinger: two heavy laspistols","U"),("Gunslinger: Mezoa long-las","C"),("Gunslinger: Ryza hellgun (stolen Guard issue)","U"),("Gunslinger: two Hammerfall stub revolvers","C"),("Gunslinger: two plasma pistols","R"),("Gunslinger: two autopistols","C"),("Gunslinger: Accatran Mk XIV recon lasgun (short, fast)","U"),("Gunslinger: Agripinaa autogun","C")],
 },
 "chem-doctor": {
  "cultist": [("Plague-doctor: rot-stimms, 3 doses of slaught, a jar of the god's 'medicine', autopistol","U"),("Chem-witch: injector stiletto (paralytic), drug satchel, heretic charms","R")],
  "raider":  [("Chem-doc: 4 stimms, 3 combat drugs, injector stiletto, autopistol","C"),("Chem-doc: concentrated stimms, Frenzon, a forbidden tonic, laspistol","U")],
  "pirate":  [("Ship's chem-doc: stimms, slaught, Quicksilver, a heretic cure-all, shotgun","C"),("Chem-doc: concentrated stimm, injector stiletto (toxin), ward-mark","U")],
 },
 "bodyguard": {t: [("Bodyguard: boarding shield and shock maul","C"),("Bodyguard: heavy carapace, combat shotgun and a shield","U"),("Bodyguard: storm shield and power maul","R")] for t in ("cultist","raider","pirate","traitor","traitor_elite")},
}
for role, per in NEW.items():
    for t, kits in per.items(): SPEC[t][role] = kits
for k in E: E[k]["specialists"] = SPEC[k]
json.dump(E, open("enemies.json","w"), indent=1)
print(len(E), "enemy pools")

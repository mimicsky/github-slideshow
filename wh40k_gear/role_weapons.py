"""Role weapons (set by the player, Ash on Ostrava day 47).

When a specialist rolls a RANDOM KIT (the 50/50 in roll_enemy.py), his guaranteed weapon or tool is drawn from his
role's list here, by the faction's wealth (the same C/U/R weights as all gear; poor factions never get rares), and his
off weapon is random. Roles that are their kit (ogryn, herder, heavy team, mortar team, bomb zealot, psyker, beast
handler, mutant charger) always take their preset and aren't listed.
Print the lists for the bestiary: python3 role_weapons.py md
"""

QUIET = [("Silenced stub pistol", "C"), ("Suppressed autopistol", "C"),
         ("Recurve bow, 'Reedhawk' pattern, and a quiver of metal arrows", "C"),
         ("Service stub pistol, 'Steadfast' pattern, suppressed", "C"), ("Suppressed Agripinaa autogun", "U"),
         ("Hunting rifle, 'Kasr Stag' pattern, suppressed, with an old scope", "U"),
         ("Suppressed stamped SMG, 'Munitorum Mk I' pattern", "U"), ("Infantry autogun, 'Columnus' pattern, suppressed", "U"),
         ("Needle pistol", "U"), ("Compound bow, 'Kasr Kestrel' pattern, and a quiver of steel arrows", "U"),
         ("Burst pistol, 'Kasr Trice' pattern, suppressed", "U"), ("Needle rifle", "R"),
         ("Suppressed Kasr Warden autogun with a scope", "R"), ("Vraks-pattern sniper autorifle, suppressed", "R"),
         ("Crossbow-quiet needle pistol", "R"), ("Assassin's mono-wire garrotte", "R"), ("Injector stiletto, 'Kasr Sting' pattern", "U"), ("Collapsing spear, 'Ordo Sicarius' pattern", "R"), ("Silenced submachine gun, 'Kasr Whisper' pattern", "U"), ("Seeker shurikens, Mechanicus pattern", "R")]

ROLE_WEAPONS = {
 "assassin": QUIET,
 "infiltrator": QUIET,
 "sniper": [("Scoped lasgun", "C"), ("Scoped autogun", "C"), ("Hunting rifle, 'Kasr Stag' pattern, with a scope", "C"),
            ("Hunting stub rifle with an old scope", "C"), ("Long-las, Mezoa", "U"), ("Long-las, 'Kasr Sprinter' stripped pattern", "U"),
            ("Compound bow, 'Kasr Kestrel' pattern, and a quiver of steel arrows", "U"), ("Long-las, Helbore", "R"),
            ("Vraks-pattern sniper autorifle", "R"), ("Hot-shot long-las with range-finder", "R"),
            ("Charge long-las, 'Kasr Lance' pattern", "R"), ("Anti-materiel rifle, 'Kasr Breaker' pattern", "R"), ("Headhunter autogun, Agripaa pattern", "U")],
 "flamer": [("Torch-thrower (scrap flamer)", "C"), ("Promethium sprayer (homemade)", "C"), ("Hand flamer", "U"),
            ("Flamer, Ryza pattern + 2 canisters", "U"), ("Heavy flamer", "R"), ("Ecclesiarchy 'cleansing' flamer", "U")],
 "heavy gunner": [("Heavy stubber", "C"), ("Braced autogun with drum", "C"), ("Heavy stubber with drum mag", "U"),
                  ("Multi-laser, man-portable", "U"), ("Las-LMG, 'Kasr Rain' suppression pattern", "U"),
                  ("Las-box, 'Kasr Barr' light las-LMG", "R"), ("Heavy bolter, Guard pattern", "R"), ("Missile launcher", "R"), ("Rocket-propelled grenade tube", "R")],
 "plasma gunner": [("Hellgun with hot-shot packs", "C"), ("Plasma pistol, Ryza pattern", "U"),
                   ("Plasma gun, Mars pattern (slow-filled cell)", "U"), ("Plasma gun, Mars pattern", "R"), ("Meltagun", "R"),
                   ("Inferno pistol", "R"), ("Plasma gun, Ryza pattern", "R"), ("Plasma blaster, twin-cell 'Lumen' pattern", "R"), ("Plasma SMG, 'Kasr Spark' pattern", "R"), ("Plasma repeater, 'Kasr Furnace' break-action lever pattern", "R")],
 "gunslinger": [("Two autopistols", "C"), ("Two stub revolvers", "C"), ("Two laspistols", "C"),
                ("Two Hammerfall auto-revolvers", "U"), ("Two hellpistols", "U"), ("Two heavy laspistols", "U"),
                ("Two burst pistols, 'Kasr Trice' pattern", "U"), ("Bolt pistol and a duelling laspistol", "R"),
                ("Two plasma pistols", "R"), ("Two shot-revolvers, 'Kasr Magistrate' officer's pattern", "R"), ("Las-scattergun 'shotlas' and a stub revolver", "U"), ("Twin-barrel autopistol, 'Kasr Hydra' pattern", "U"), ("Combi-pistol, 'Kasr Trident' pattern", "R"), ("Shredder autopistol, Ius pattern", "U"), ("Machine pistol, 'Kasr Hornet' pattern", "U"), ("Submachine gun, 'Kasr Scorpion' pattern", "R")],
 "grenadier": [("Bag of 4 frags", "C"), ("Bandolier of 4 frags and 2 smoke", "C"), ("Tin-can bombs x4", "C"),
               ("Cracker bundles x3 and 2 frags", "C"), ("Grenade launcher + 6 rounds", "U"),
               ("Grenade launcher with krak and frag", "R"), ("Grenade launcher, stand-alone", "U"), ("Grenade launcher, revolver-drum", "U"), ("Thumper (Catachan grenade launcher)", "U")],
 "demolitions": [("2 breaching charges", "C"), ("Mining charges x2", "C"), ("Tin-can bombs x3", "C"),
                 ("Demo satchel and a detonator", "U"), ("3 krak grenades", "U"), ("Melta bomb", "R"), ("Shrapnel mines (2)", "R"), ("Plasma tripwire mine", "R"), ("Thrown demo satchel with paired detonator", "U")],
 "breacher": [("Combat shotgun, pump, and a breaching charge", "C"), ("Folding breaching shotgun, 'Kasr Jackknife' pattern", "U"), ("Pump shotgun, 'Harrow' pattern, and 2 breaching charges", "C"),
              ("Sawn-off shotgun and a breaching charge", "C"), ("Combat shotgun, 'Kasr Sweeper' duckbill pattern", "U"),
              ("Tactical breaching axe, 'Kasr Sapper' pattern", "U"), ("Lucius-pattern 'Ironclad' shotgun", "R"),
              ("Bolt-shotgun, 'Breacher' pattern", "R"), ("Arbites combat shotgun (shock shells)", "U"), ("Hydraulic push axe, 'Kasr Ram' pattern", "R"), ("Las-SMG, 'Sterl' pattern", "U"), ("Compact autogun, 'Kasr Hive' pattern", "U"), ("Bullpup SMG, 'Kasr Adder' pattern", "U")],
 "bodyguard": [("Combat shotgun, pump, and a boarding shield", "C"), ("Boarding shield and a shock maul", "C"),
               ("Combat shotgun, semi-auto, and a boarding shield", "U"), ("Boarding shield and a hellpistol", "U"),
               ("Storm shield and a power maul", "R"), ("Lucius-pattern 'Ironclad' shotgun", "R"), ("Heavy SMG, 'Orlock' pattern", "U"), ("Rotary SMG, 'Hive Spinner' pattern", "U")],
 "shield trooper": [("Boarding shield", "C"), ("Riot shield", "C"), ("Scrap shield", "C"), ("Cogitator shield (scrap)", "U"),
                    ("Forged shield", "U"), ("Storm shield", "R"), ("Arbites suppression shield and an Arbites combat shotgun (shock shells)", "R")],
 "arbitrator": [("Combat shotgun, pump, and a shock baton", "C"), ("Shock maul and a suppression shield", "C"),
                ("Arbites combat shotgun (shock shells)", "U"), ("Web pistol and a shock maul", "U"),
                ("Power maul and a suppression shield", "R"), ("Riot SMG, Arbites pattern", "R")],
 "enforcer": [("Shock maul", "C"), ("Shock baton and a stub revolver", "C"), ("Combat shotgun, pump", "C"), ("Bolt pistol", "U"),
              ("Laspistol and a power maul", "R"), ("Plasma pistol and a chainsword", "R"),
              # one-handed swords and pistols (the player, day 48)
              ("Laspistol and an officer's sabre", "C"), ("Stub revolver and a naval sabre", "C"),
              ("Service stub pistol, 'Steadfast' pattern, and a cutlass", "C"), ("Laspistol and a chainsword", "C"),
              ("Hellpistol and an officer's sabre", "U"), ("Hellpistol and a chainsword", "U"),
              ("Bolt pistol and an officer's sabre", "U"), ("Bolt pistol and a chainsword", "U"),
              ("Bolt pistol and a power sword", "R"), ("Hellpistol and a power sword", "R"),
              ("Plasma pistol and a power sword", "R"),
              ("Bolt pistol and a thunder hammer, one-handed officer's pattern", "R"), ("Shot-revolver, 'Kasr Magistrate' officer's pattern", "R"), ("Arbites combat shotgun (shock shells)", "U"), ("Riot SMG, Arbites pattern", "R"), ("Bolt pistol, Ryza pattern", "R")],  # made for commissars (the player's session-9 design; added day 48)
 "sister novitiate": [("Autopistol and a chainsword", "C"), ("Autogun", "C"), ("Autopistol and a novitiate's mace", "C"),
                      ("Laspistol and a chainsword", "C"), ("Sacred banner and an autopistol", "U"), ("Hand flamer and an autopistol", "U"),
                      ("Bolt pistol and a chainsword", "U"), ("Sororitas bolt pistol (Godwyn-De'az) and a blessed power maul", "R"),
                      ("Inferno pistol (Sororitas) and a chainsword", "R"), ("Sororitas power sword and a bolt pistol", "R")],
                      # allies only (the player, Ash on Ostrava day 48)
 "veteran": [("Lasgun", "C"), ("Autogun", "C"), ("Combat shotgun, pump", "C"), ("Hunting rifle with an old scope", "C"),
             ("Lascarbine", "U"), ("Hellgun", "U"), ("Scoped autogun", "U"), ("Hellgun with a holo sight", "R"),
             ("Long-las with a scope", "R"), ("Lucius-pattern 'Ironclad' shotgun", "R"), ("Catachan shotgun", "R"), ("Lasgun, Agripinaa", "U"), ("Lascarbine, Accatran Mk VI", "U"), ("Lasgun, Krieg pattern", "U"), ("Chainsword, Lucius heavy", "R"), ("Las bullpup SMG, 'Kasr Volt' pattern", "U")],  # the player, day 48
 "berserker": [("Chainsword", "C"), ("Chain axe", "C"), ("Heavy scrap axe", "C"), ("Saw-cleaver", "C"), ("Two chain axes", "U"),
               ("Eviscerator", "R"), ("Great chain axe, 'Butcher' pattern", "R"), ("Power axe", "R"), ("Chainsword, Lucius heavy", "R"), ("Combat chain-knife, 'Kasr Gnaw' pattern", "U")],
 "mauler": [("Heavy scrap axe", "C"), ("Two-handed boarding axe", "C"), ("Headsman's axe (two-handed)", "U"), ("Chain glaive (two-handed)", "U"),
            ("Great chain axe, 'Butcher' pattern", "R"), ("Power axe (two-handed)", "R"), ("Heavy war axe, 'Kasr Gate' pattern", "U"), ("Hydraulic push axe, 'Kasr Ram' pattern", "R"), ("Thunder hammer, Crucis pattern", "R")],
 "brute": [("Sledgehammer", "C"), ("Heavy scrap axe", "C"), ("Two-handed scrap great-axe", "C"), ("Trench club and a door for a shield", "C"),
           ("Chain axe", "U"), ("Stolen Ogryn ripper gun and a club", "R"), ("Brute stubber, 'Kasr Deddog' pattern", "R")],
 "duelist": [("Naval sabre", "C"), ("Chainsword", "C"), ("Cutlass and a stub revolver", "C"),
             ("Officer's sabre and a duelling laspistol", "U"), ("Paired mono-knife blades", "U"), ("Power sword", "R"), ("Shot-revolver, 'Kasr Magistrate' officer's pattern, and an officer's sabre", "R"), ("Las-scattergun 'shotlas' and a naval sabre", "U"), ("Power falchion", "R"), ("Power odachi, 'Eversor' pattern", "R")],
 "zealot": [("Chainsword", "C"), ("Chain axe", "C"), ("Flamer-torch", "U"), ("Crusher, two-handed mace", "U"), ("Power maul", "R"), ("Eviscerator", "R"), ("Ecclesiarchy 'cleansing' flamer", "U"), ("Incinerator", "R")],
 "commander": [("Chainsword and a command vox", "C"), ("Shot-revolver, 'Kasr Magistrate' officer's pattern, and a command vox", "R"), ("Laspistol and a command vox", "C"), ("Bolt pistol and a command vox", "U"),
               ("Hellpistol and a command vox", "U"), ("Power sword and a command vox", "R"), ("Plasma pistol and a command vox", "R"), ("Boltgun, Phobos pattern", "R"), ("Las-fist, 'Kasr Knuckle' pattern", "R")],
 "leader": [("Chainsword and a command vox", "C"), ("Shot-revolver, 'Kasr Magistrate' officer's pattern, and a command vox", "R"), ("Laspistol and a command vox", "C"), ("Bolt pistol and a command vox", "U"),
            ("Hellpistol and a command vox", "U"), ("Power sword and a command vox", "R"), ("Plasma pistol and a command vox", "R"), ("Bolt pistol, Ryza pattern", "R"), ("Boltgun, Locke Mk IIb 'Spearhead'", "R"), ("Hellpistol, Kantrael, and a command vox", "U")],
 "medic": [("Med-kit and 3 stimms", "C"), ("Field dressings and two stimms", "C"), ("Med-kit, antitoxin and 2 stimms", "U"),
           ("Medicae kit and concentrated stimms", "R")],
 "chem-doctor": [("Drug satchel: stimms, slaught and Frenzon", "C"), ("Syringe spike and a drug satchel", "U"),
                 ("Injector stiletto (toxin) and concentrated stimms", "R"), ("Injector stiletto, 'Kasr Sting' pattern, and a drug satchel", "U")],
 "vox": [("Vox-caster", "C"), ("Vox-caster and an auspex", "U"), ("Vox-caster and a spoof-tag", "U"), ("Vox jammer", "R"), ("Vox-caster and a recon lascarbine, folding stock", "U")],
 "spotter": [("Magnoculars", "C"), ("Range-finder magnoculars", "U"), ("Auspex", "U"), ("Vox-caster and range-finder magnoculars", "R"), ("Magnoculars and a recon lascarbine, folding stock", "U")],
 "tracker": [("Two war dogs on leashes", "C"), ("Magnoculars and a hunting rifle", "C"), ("Auspex", "U"), ("Bio-scanner", "R"), ("Catachan shotgun and magnoculars", "U"), ("Catachan butcher knife", "U"), ("Tactical hand axe, 'Fenris' pattern", "U")],
 "tech-adept": [("Servo-arm and a repair kit", "C"), ("Scrap-built auto-turret and a cutting torch", "U"),
                ("Vox jammer and a servo-skull", "U"), ("Heavy auto-turret and a servo-arm", "R"), ("Servo-arm and an Omnissian axe", "R"), ("Omnissian power sword and a repair kit", "R"), ("Phosphor blast pistol and a servo-arm", "R"), ("Lasgun, Ryza Mechanicus cable pattern, and a backpack cell", "R"), ("Lasgun, Mars pattern, and a repair kit", "R")],
 "jumper": [("Scrap jump pack (homemade; sputters on a 1)", "C"), ("Stolen grav-chute rigged to hop", "C"), ("Boarders' lift pack", "U"),
            ("Guard jump pack", "U"), ("Kasrkin-pattern jump pack", "R")],
 "icon bearer": [("The faction's icon on a pole", "C"), ("Defaced regimental colours", "U"), ("Daemon-touched icon that whispers", "R")],
 "fighter pilot": [("Flight suit and an autopistol", "C"), ("Flight suit and a laspistol", "C"), ("Flight suit and a hot-shot laspistol", "U"), ("Flight suit and a las machine pistol, 'Kasr Wasp' pattern", "U"), ("Flight suit and a boarding SMG, Navy 'Gyre' pattern", "U")],
}


def md():
    rar = {"C": "common", "U": "uncommon", "R": "rare"}
    for role in sorted(ROLE_WEAPONS):
        rows = ROLE_WEAPONS[role]
        if role == "infiltrator":
            print(f"- **{role}:** the same quiet list as the assassin")
            continue
        print(f"- **{role}:** " + "; ".join(f"{n} ({rar[r]})" for n, r in rows))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "md":
        md()

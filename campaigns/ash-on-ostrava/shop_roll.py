import random
pool = [
("Lasgun (Kantrael M36)","1 TV"),("Lascarbine (Accatran)","1.5 TV"),("Long-las (sniper)","6 TV"),
("Hellgun (Ryza-pattern)","5 TV"),("Hellpistol","4 TV"),("Laspistol","0.5 TV"),("Heavy laspistol","2 TV"),
("Autogun","1 TV"),("Autopistol","1 TV"),("Stub revolver","0.5 TV"),("Combat shotgun (semi-auto)","2 TV"),
("Ripper/drum-fed shotgun","3 TV"),("Bolt pistol","12 TV"),("Boltgun (Godwyn pattern)","25 TV"),
("Plasma gun (Mars pattern, 1 cell)","30 TV"),("Plasma cell","6 TV"),("Meltagun (2 charges)","35 TV"),
("Flamer (2 canisters)","8 TV"),("Hand flamer","6 TV"),("Promethium canister (flamer fuel)","1 TV"),
("Grenade launcher (Ryza, underslung)","6 TV"),("Grenade launcher (stand-alone)","5 TV"),
("Heavy stubber","4 TV"),("Heavy bolter (crew, 1 belt)","40 TV"),("Missile launcher (2 frag, 1 krak)","25 TV"),
("Autocannon (crew)","35 TV"),("Lascannon (crew)","45 TV"),("Mortar (crew, 6 rounds)","12 TV"),
("Frag grenade","1 TV"),("Krak grenade","2 TV"),("Smoke grenade","1 TV"),("Photon flash grenade","2 TV"),
("Melta bomb","8 TV"),("Demolition/breaching charge","2 TV"),("Det-tape (5 m)","1 TV"),("Choke gas grenade","1.5 TV"),
("Hot-shot pack (Mechanicus pattern)","3 TV"),("Las pack","0.25 TV"),("Bolt rounds (10)","8 TV"),("Heavy stubber belt","1 TV"),
("Stubber drum magazine","1.5 TV"),("Combat knife","0.25 TV"),("Bayonet","0.25 TV"),("Navy cutlass","2 TV"),
("Chainsword","6 TV"),("Chain axe","8 TV"),("Shock maul","7 TV"),("Power maul","25 TV"),("Power sword","30 TV"),
("Entrenching tool","0.25 TV"),("Flak armour set","1 TV"),("Carapace armour set","8 TV"),("Storm trooper carapace set","15 TV"),
("Storm shield (power field)","30 TV"),("Boarding shield","4 TV"),("Rebreather","0.5 TV"),("Void-suit (Navy)","4 TV"),
("Photo-visor (low-light)","2 TV"),("Magnoculars","1.5 TV"),("Auspex (hand)","6 TV"),("Vox-caster (manpack)","5 TV"),
("Micro-bead","0.5 TV"),("Chrono","0.5 TV"),("Map-slate","1 TV"),("Cogitator spike","4 TV"),("Flares (box of 10)","0.5 TV"),
("Medi-kit","3 TV"),("Stimm (dose)","0.5 TV"),("Antitoxin (dose)","1 TV"),("De-tox / counter-plague (dose)","2 TV"),
("Drag harness","0.5 TV"),("Grav-chute","6 TV"),("Climbing rig + grapnel","1.5 TV"),("Demolitions kit / bag","1.5 TV"),
("Large field pack","1 TV"),("Quick-draw holster","0.5 TV"),("Weapon sling (padded)","0.25 TV"),("Red-dot / reflex sight","3 TV"),
("Telescopic sight","3 TV"),("Bipod","0.5 TV"),("Silencer (stub/auto)","2 TV"),("Hot-shot conversion kit (lasgun)","5 TV"),
("Servo-skull (utility, used)","20 TV"),("Mechanicus sacred oils (flask)","1 TV"),("Plasteel ingot","2 TV"),("Ceramite plate (salvage)","3 TV"),
("Machine-core (salvage)","6 TV"),("Servo-motor (salvage)","3 TV"),("Rations (crate)","0.5 TV"),("Amasec (case)","2 TV"),
("Lho-sticks (carton)","0.25 TV"),("Imperial Infantryman's Uplifting Primer","0.1 TV"),("Valkyrie rocket pod (Hellstrike missile x2)","20 TV"),
("Valkyrie multilaser charge pack","3 TV"),("Spare coupling (Mechanicus)","2 TV"),("Mono-knife","3 TV"),("Kantrael lasgun bayonet lug kit","0.25 TV"),
]
rare = [
("Ork 'shoota' (confiscated, crude, loud)","3 TV"),("Eldar shuriken pistol (confiscated, 1 magazine)","40 TV"),
("Tau pulse carbine (confiscated, half charge)","35 TV"),("Archeotech laspistol (Dark Age, unknown maker)","60 TV"),
("Astartes combat knife (Space Marine, huge)","15 TV"),("Sororitas inferno pistol (no charge)","30 TV"),("Needle pistol (noble's)","20 TV"),
]
n = random.randint(14,18)
items = random.sample(pool, n)
out=[]
for it,price in items:
    qty = random.choice([1,1,1,2,2,3,4,5,10])
    out.append((it,price,qty))
r = random.randint(1,20)
print("rare d20:", r)
if r==20:
    print("RARE:", random.choice(rare))
for it,p,q in out: print(f"{q} x {it} — {p}")

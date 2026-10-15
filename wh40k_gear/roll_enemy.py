"""Roll an enemy group's roles and gear, from enemies.json.

Usage: python3 roll_enemy.py TYPE COUNT [BOOK] [GOD]
  TYPE:  cultist, raider, pirate, traitor (renegade Guard), traitor_elite
         (traitor storm troopers, renegade Inquisition teams: always elite weights)
  COUNT: how many enemies in the group (a named enemy alone: 1)
  BOOK:  which book of the campaign (default 2); difficulty scales by book
  GOD:   cultists only: khorne, nurgle, slaanesh, tzeentch, undivided (default random)

Role, one d20 per enemy (player-set, session 8):
  1-15  grunt: a coin flip (traitors 75/25) makes them RANGED (main gun + melee backup)
        or MELEE (melee weapon + a sidearm or nothing)
  16-20 specialist: a random role from this type's list (sniper, grenadier,
        heavy, assassin, flamer, demolitions, medic, leader, and so on)
Specialists carry their role kit, and 1 in 4 also has a melee backup.
Every enemy also rolls armour and one extra. Gear is weighted
common 70 / uncommon 25 / rare 5.

Better-armed, one open d20 for the group:
  1-9 none; 10-11 one; 12-13 two; 14-15 three; 16-18 four (capped at the group);
  natural 19-20 (on the die itself, never from bonuses) ELITE TEAM: everyone rolls one rarity step better
  (common 25 / uncommon 50 / rare 25) and each carries a 'found or made' item.
A natural 20 also adds one rare find to the group's loot (DND_CODEX Part 8, Loot).
Book scaling (campaign sheet, DM threads): better-armed d20 +2 per book after the
first; specialist role starts 1 lower per book (book 1: 16-20, book 2: 15-20).
Blessed cultists: "blessed" is one of the cultist specialist types. A cultist who
rolls specialist and draws "blessed" rolls the role d20 again: grunt or
specialist as normal; if specialist, draw a type again; drawing "blessed" a
second time makes them a blessed grunt
(wh40k_gear/catalogue/heretic.md, Blessed cultists).
Special teams (player-set): before the fight, 2d20 added; 33-40 means the group is
a named special team of this type (factions.py; bestiary/): +1 on all their rolls,
armour one step better, +8 to the better-armed d20, and half their guns are the
team's favoured weapons. Their look and tactics are in the bestiary.
"""
import json, random, sys, os
here = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(here, "enemies.json")))
kind = (sys.argv[1] if len(sys.argv) > 1 else "cultist").lower()
count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
book = int(sys.argv[3]) if len(sys.argv) > 3 else 2
god = (sys.argv[4].lower() if len(sys.argv) > 4 else random.choice(["khorne", "nurgle", "slaanesh", "tzeentch", "undivided"]))
P = E[kind]
sys.path.insert(0, here)
from factions import F
team_roll = random.randint(1, 20) + random.randint(1, 20)
team = None
if team_roll >= 33:
    opts = [f for f in F if f["type"] == kind and (kind != "cultist" or len(sys.argv) <= 4 or f.get("god") == god)] or [f for f in F if f["type"] == kind]
    team = random.choice(opts)
    if team.get("god"): god = team["god"]
raw = random.randint(1, 20)
d20 = min(20, raw + 2 * (book - 1) + (8 if team else 0))
elite = raw >= 19  # only the natural die makes an elite team; bonuses never do
better = 0 if d20 < 10 else 1 if d20 < 12 else 2 if d20 < 14 else 3 if d20 < 16 else 4
if elite: better = count
better = min(better, count)
w = {"C": 25, "U": 50, "R": 25} if elite else P.get("weights", {"C": 70, "U": 25, "R": 5})
def pick(rows):
    tier = random.choices(list(w), weights=list(w.values()))[0]
    opts = [r for r in rows if r[1] == tier] or rows
    return random.choice(opts)[0]
sidearms = [r for r in P["weapon"] if any(x in r[0].lower() for x in ("pistol", "revolver", "stub automatic", "sawn-off"))] or [("Hellpistol" if kind == "traitor_elite" else "Laspistol", "C")]
ranged_share = 0.75 if kind.startswith("traitor") else 0.5  # soldiers mostly fight with guns
print(f"SPECIAL TEAM: {team['name']} (2d20 {team_roll}): +1 on all rolls, armour one step better, +8 better-armed" if team else f"(2d20 {team_roll}: a basic group)")
print(f"{kind} x{count}, book {book}" + (f", god {god}" if kind == "cultist" else "") + f", group d20: {raw} (+{2*(book-1) + (8 if team else 0)} = {d20})" + ("  ELITE TEAM" if elite else f"  better-armed: {better}") + ("  + RARE FIND (natural 20)" if raw == 20 else ""))
lucky = set(random.sample(range(count), better))
for n in range(count):
    role_d20 = random.randint(1, 20)
    blessed = False
    roles = list(P["specialists"]) + (["blessed"] if kind == "cultist" else [])
    if role_d20 >= 17 - book:
        role = random.choice(roles)
        if role == "blessed":
            blessed = True
            role_d20 = random.randint(1, 20)  # roll again: grunt or specialist
            if role_d20 >= 17 - book:
                role = random.choice(roles)
                if role == "blessed":
                    role_d20 = 1  # blessed again: a blessed grunt
    if role_d20 >= 17 - book:
        backup = f" | {pick(P['melee'])}" if random.random() < 0.25 else ""  # 25% carry a melee backup
        kit = pick(P['specialists'][role])
        if "two-man team" in kit:
            kit += " [counts as two: gunner + loader with a lasgun and the ammo]"
        head = f"SPECIALIST {role.upper()} (d20 {role_d20}): {kit}{backup}"
    elif random.random() < ranged_share:
        head = f"grunt, ranged (d20 {role_d20}): {pick(P['weapon'])} | {pick(P['melee'])}"
    else:
        side = pick(sidearms) if random.random() < 0.5 else "no sidearm"
        head = f"grunt, melee (d20 {role_d20}): {pick(P['melee'])} | {side}"
    if team and head.startswith("grunt, ranged") and random.random() < 0.5:
        g = random.choice(team["favoured"])
        head = head.split("): ", 1)[0] + "): " + g + " | " + head.split(" | ", 1)[1]
    armour = pick(P['armour'])
    if team:  # one step better: draw the armour from the top of the list
        armour = random.choice([r[0] for r in P['armour'] if r[1] in ("U", "R")] or [armour])
    line = f"{n+1}. {head} | {armour} | {pick(P['extra'])}"
    if n in lucky:
        line += f"  ** FOUND/MADE: {random.choice(P['found'])[0]}"
    if blessed:
        line = line.replace(f"{n+1}. ", f"{n+1}. !! BLESSED by {god}, rerolled: ", 1)
    print(line)

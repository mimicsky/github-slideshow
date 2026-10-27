"""Roll an enemy group's roles and gear, from enemies.json.

Usage: python3 roll_enemy.py TYPE COUNT [WEALTH] [GOD]
       python3 roll_enemy.py wealth TYPE   (roll a faction's wealth at mission start)
  TYPE:  cultist, raider, pirate, traitor (renegade Guard), traitor_elite
         (traitor storm troopers, renegade Inquisition teams)
  WEALTH: poor, steady, good, rich, wealthy (the faction's level, rolled d100 at mission
         start; default steady, traitors good)
  COUNT: how many enemies in the group (a named enemy alone: 1)
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
  1-8 none; 9-10 one; 11-12 two; 13-14 three; 15-16 four; 17-18 five; 19+ six (capped at the group);
  natural 19-20 (on the die itself, never from bonuses) ELITE TEAM: everyone rolls one rarity step better
  (common 25 / uncommon 50 / rare 25) and each carries a 'found or made' item.
A natural 20 means one of them carries and uses a rare weapon or gear in the fight (rare roll 1;
the looting d20 afterwards is rare roll 2, for stashed items; DND_CODEX Part 8, Loot).
No per-book bonuses (removed by the player, session 9): later books bring more
enemies and smarter tactics, not bigger numbers.
Fight stats (player-set, session 9): each enemy rolls STR and DEX levels (1-100) in
its type's range; +1 to rolls per full 10. A specialist gets +5 levels in the stat
its role uses; a special team gets +5 levels to both.
Faction wealth (player-set, session 9): rolled d100 once per mission or world (or the
first meeting with that faction there). Cultists, raiders, pirates: 1-30 Poor, 31-60
Steady, 61-80 Good, 81-95 Rich, 96-100 Wealthy. Traitors and traitor elites (Good and up):
1-50 Good, 51-85 Rich, 86-100 Wealthy. Gear C/U/R: Poor 80/20/0 (found items never rare,
lots of scrap guns), Steady 70/25/5 (some scrap), Good 55/35/10, Rich 40/45/15 and
Wealthy 25/50/25 (armour one step better). Epic items: each enemy of a Rich faction has a
2% chance, of a Wealthy faction 5%, to carry one (no Assassinorum gear). An elite team is
one level richer.
Gun condition (player-set, session 9): cultists and raiders Dirty or Neglected, pirates Dirty,
traitors Clean (codex Part 8, Gun condition and jams).
Skitarii (player-set, session 9): a traitor or traitor-elite tech-adept rolls a second d20;
18-20 makes it a corrupted Skitarius (kind d6: 1-3 Ranger, 4-5 Vanguard, 6 Sicarian).
Blessed cultists: "blessed" is one of the cultist specialist types. A cultist who
rolls specialist and draws "blessed" rolls the role d20 again: grunt or
specialist as normal; if specialist, draw a type again; drawing "blessed" a
second time makes them a blessed grunt
(wh40k_gear/catalogue/heretic.md, Blessed cultists).
Special teams (player-set): before the fight, 2d20 added; 31-40 means the group is
a named special team of this type (factions.py; bestiary/): +5 STR and DEX levels, +1 on other rolls,
armour one step better, +3 to the better-armed d20, and half their guns are the
team's favoured weapons. Their look and tactics are in the bestiary.
"""
import json, random, sys, os
here = os.path.dirname(os.path.abspath(__file__))
LEVELS = ["poor", "steady", "good", "rich", "wealthy"]
WEIGHTS = {"poor": {"C": 80, "U": 20, "R": 0}, "steady": {"C": 70, "U": 25, "R": 5}, "good": {"C": 55, "U": 35, "R": 10},
           "rich": {"C": 40, "U": 45, "R": 15}, "wealthy": {"C": 25, "U": 50, "R": 25}}
if len(sys.argv) > 1 and sys.argv[1].lower() == "wealth":  # roll a faction's wealth at mission start
    t = (sys.argv[2] if len(sys.argv) > 2 else "cultist").lower()
    d = random.randint(1, 100)
    if t.startswith("traitor"):
        lvl = "good" if d <= 50 else "rich" if d <= 85 else "wealthy"
    else:
        lvl = "poor" if d <= 30 else "steady" if d <= 60 else "good" if d <= 80 else "rich" if d <= 95 else "wealthy"
    print(f"{t} faction wealth: d100 {d} = {lvl.upper()}")
    sys.exit()
E = json.load(open(os.path.join(here, "enemies.json")))
kind = (sys.argv[1] if len(sys.argv) > 1 else "cultist").lower()
count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
rest = [a for a in sys.argv[3:] if not a.isdigit() and a.lower() not in LEVELS]  # an old BOOK number is accepted and ignored
given = [a.lower() for a in sys.argv[3:] if a.lower() in LEVELS]
level = given[0] if given else ("good" if kind.startswith("traitor") else "steady")
if kind.startswith("traitor") and LEVELS.index(level) < 2: level = "good"  # traitors are Good and up
god_given = bool(rest)
god = (rest[0].lower() if rest else random.choice(["khorne", "nurgle", "slaanesh", "tzeentch", "undivided"]))
STATS = {"cultist": ((10, 30), (10, 25)), "raider": ((15, 35), (15, 30)), "pirate": ((15, 35), (20, 35)),
         "traitor": ((20, 35), (25, 40)), "traitor_elite": ((25, 45), (35, 50))}
STR_ROLES = {"brute", "berserker", "breacher", "bodyguard", "enforcer", "duelist", "zealot", "bomb zealot"}
DEX_ROLES = {"sniper", "grenadier", "assassin", "flamer", "demolitions", "jumper", "spotter", "tracker", "fighter pilot",
             "heavy gunner", "heavy team", "plasma gunner", "infiltrator", "gunslinger"}
def stats(role, skitarius=False):
    (s0, s1), (d0, d1) = ((30, 45), (35, 50)) if skitarius else ((60, 80), (10, 20)) if role == "ogryn" else STATS[kind]
    st, dx = random.randint(s0, s1), random.randint(d0, d1)
    if role in STR_ROLES and role != "ogryn": st += 5
    if role in DEX_ROLES: dx += 5
    if team: st, dx = st + 5, dx + 5
    return f"STR {st} (+{st // 10}) DEX {dx} (+{dx // 10})"
P = E[kind]
sys.path.insert(0, here)
from factions import F
team_roll = random.randint(1, 20) + random.randint(1, 20)
team = None
if team_roll >= 31:
    opts = [f for f in F if f["type"] == kind and (kind != "cultist" or not god_given or f.get("god") == god)] or [f for f in F if f["type"] == kind]
    team = random.choice(opts)
    if team.get("god"): god = team["god"]
raw = random.randint(1, 20)
d20 = min(20, raw + (3 if team else 0))
elite = raw >= 19  # only the natural die makes an elite team; bonuses never do
better = 0 if d20 < 9 else 1 if d20 < 11 else 2 if d20 < 13 else 3 if d20 < 15 else 4 if d20 < 17 else 5 if d20 < 19 else 6
if elite: better = count
better = min(better, count)
if elite: level = LEVELS[min(4, LEVELS.index(level) + 1)]  # an elite team is one level richer
poor = level == "poor"
w = WEIGHTS[level]
better_armour = bool(team) or level in ("rich", "wealthy")
EPIC_CHANCE = {"rich": 0.02, "wealthy": 0.05}.get(level, 0)  # epic (exotic) items, player-set session 9
EPICS = [i["name"] for i in json.load(open(os.path.join(here, "pools.json"))) if i["rarity"] == "X"
         and not any(x in i["name"] for x in ("Exitus", "Callidus", "Culexus", "Vindicare"))]
def pick(rows):
    if team or level not in ("poor", "steady") or (level == "steady" and random.random() < 0.5):
        rows = [r for r in rows if "(scrap" not in r[0]] or rows  # scrap guns: Poor, and some Steady
    tier = random.choices(list(w), weights=list(w.values()))[0]
    opts = [r for r in rows if r[1] == tier] or [r for r in rows if not (poor and r[1] == "R")] or rows
    return random.choice(opts)[0]
sidearms = [r for r in P["weapon"] if any(x in r[0].lower() for x in ("pistol", "revolver", "stub automatic", "sawn-off"))] or [("Hellpistol" if kind == "traitor_elite" else "Laspistol", "C")]
# Bomb zealots (player-set): their extra is always 3-5 explosives, all strapped on.
BOMBS = [("Frag grenade","C"),("Pipe-bomb","C"),("Fire bomb (promethium)","C"),("Mining charge","C"),
         ("Krak grenade","U"),("Choke gas grenade","U"),("Cult gas bottle (gas of their god)","U"),("Melta bomb","R")]
ranged_share = 0.75 if kind.startswith("traitor") else 0.5  # soldiers mostly fight with guns
print(f"SPECIAL TEAM: {team['name']} (2d20 {team_roll}): +5 STR/DEX levels, +1 other rolls, armour one step better, +3 better-armed" if team else f"(2d20 {team_roll}: a basic group)")
print(f"{kind} x{count}, wealth {level.upper()}" + ("" if given else " (default; roll it: roll_enemy.py wealth TYPE)") + (f", god {god}" if kind == "cultist" else "") + f", group d20: {raw} (+{3 if team else 0} = {d20})" + ("  ELITE TEAM" if elite else f"  better-armed: {better}") + ("  + RARE GEAR IN USE (natural 20)" if raw == 20 else ""))
lucky = set(random.sample(range(count), better))
for n in range(count):
    role_d20 = random.randint(1, 20)
    role = None
    blessed = False
    roles = list(P["specialists"]) + (["blessed"] if kind == "cultist" else [])
    if role_d20 >= 16:
        role = random.choice(roles)
        if role == "blessed":
            blessed = True
            role_d20 = random.randint(1, 20)  # roll again: grunt or specialist
            if role_d20 >= 16:
                role = random.choice(roles)
                if role == "blessed":
                    role_d20 = 1  # blessed again: a blessed grunt
    if role_d20 >= 16:
        backup = f" | {pick(P['melee'])}" if random.random() < 0.25 else ""  # 25% carry a melee backup
        skit = None
        if role == "tech-adept" and kind.startswith("traitor"):
            sk = random.randint(1, 20)
            if sk >= 18:
                k6 = random.randint(1, 6)
                skit = ("RANGER: galvanic rifle" if k6 <= 3 else "VANGUARD: radium carbine (rad-sickness within ~5 m)" if k6 <= 5 else "SICARIAN: paired transonic blades")
                skit = f"corrupted SKITARIUS (tech-adept d20 {sk}, kind d6 {k6}), {skit}; augmetic eyes, machine body (extra stage), shock-weak; see roles.md"
        kit = skit or pick(P['specialists'][role])
        if "two-man team" in kit:
            kit += " [counts as two: gunner + loader with a lasgun and the ammo]"
        if role == "herder":  # player design, session 10: cultists only; the herd follows their god
            n_d = random.randint(1, 4) + 1
            herd = {"nurgle": f"a swarm of {sum(random.randint(1, 10) for _ in range(2)) + 10} POXWALKERS",
                    "khorne": f"{n_d} BLOODLETTERS (lesser daemons of Khorne)",
                    "slaanesh": f"{n_d} DAEMONETTES (lesser daemons of Slaanesh)",
                    "tzeentch": f"{n_d} PINK HORRORS (lesser daemons of Tzeentch)"}.get(god, f"{n_d} FURIES (lesser daemons, undivided)")
            kit += f" [HERD: {herd}; kill the herder and the herd loses its march]"
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
    if better_armour:  # one step better: draw the armour from the top of the list
        armour = random.choice([r[0] for r in P['armour'] if r[1] in ("U", "R")] or [armour])
    extra = pick(P['extra'])
    if head.startswith("SPECIALIST BOMB ZEALOT"):
        extra = "STRAPPED ON: " + ", ".join(pick(BOMBS) for _ in range(random.randint(3, 5)))
    cond = random.choice(["Dirty", "Neglected"]) if kind in ("cultist", "raider") else "Dirty" if kind == "pirate" else "Clean"
    line = f"{n+1}. {head} | {armour} | {extra} | {stats(role if role_d20 >= 16 else None, "SKITARIUS" in head)} | guns {cond}"
    if n in lucky:
        line += f"  ** FOUND/MADE: {random.choice([f for f in P['found'] if not poor or f[1] != 'R'] or P['found'])[0]}"
    if EPIC_CHANCE and random.random() < EPIC_CHANCE:
        line += f"  ** EPIC: {random.choice(EPICS)}"
    if blessed:
        line = line.replace(f"{n+1}. ", f"{n+1}. !! BLESSED by {god}, rerolled: ", 1)
    print(line)

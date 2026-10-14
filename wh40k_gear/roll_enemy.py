"""Roll an enemy group's roles and gear, from enemies.json.

Usage: python3 roll_enemy.py TYPE COUNT
  TYPE:  cultist, raider, pirate
  COUNT: how many enemies in the group (a named enemy alone: 1)

Role, one d20 per enemy (player-set, session 8):
  1-15  grunt: a coin flip makes them RANGED (main gun + melee backup)
        or MELEE (melee weapon + a sidearm or nothing)
  16-20 specialist: a random role from this type's list (sniper, grenadier,
        heavy, assassin, flamer, demolitions, medic, leader, and so on)
Every enemy also rolls armour and one extra. Gear is weighted
common 70 / uncommon 25 / rare 5.

Better-armed, one open d20 for the group:
  1-9 none; 10-11 one; 12-13 two; 14-15 three; 16-18 four (capped at the group);
  19-20 ELITE TEAM: everyone rolls one rarity step better
  (common 25 / uncommon 50 / rare 25) and each carries a 'found or made' item.
A natural 20 also adds one rare find to the group's loot (DND_CODEX Part 8, Loot).
"""
import json, random, sys, os
here = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(here, "enemies.json")))
kind = (sys.argv[1] if len(sys.argv) > 1 else "cultist").lower()
count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
P = E[kind]
d20 = random.randint(1, 20)
elite = d20 >= 19
better = 0 if d20 < 10 else 1 if d20 < 12 else 2 if d20 < 14 else 3 if d20 < 16 else 4 if d20 < 19 else count
better = min(better, count)
w = {"C": 25, "U": 50, "R": 25} if elite else {"C": 70, "U": 25, "R": 5}
def pick(rows):
    tier = random.choices(list(w), weights=list(w.values()))[0]
    opts = [r for r in rows if r[1] == tier] or rows
    return random.choice(opts)[0]
sidearms = [r for r in P["weapon"] if any(x in r[0].lower() for x in ("pistol", "revolver", "stub automatic", "sawn-off"))] or P["weapon"]
print(f"{kind} x{count}, group d20: {d20}" + ("  ELITE TEAM" if elite else f"  better-armed: {better}") + ("  + RARE FIND (natural 20)" if d20 == 20 else ""))
lucky = set(random.sample(range(count), better))
for n in range(count):
    role_d20 = random.randint(1, 20)
    if role_d20 >= 16:
        role = random.choice(list(P["specialists"]))
        kit = pick(P["specialists"][role])
        head = f"SPECIALIST {role.upper()} (d20 {role_d20}): {kit}"
    elif random.random() < 0.5:
        head = f"grunt, ranged (d20 {role_d20}): {pick(P['weapon'])} | {pick(P['melee'])}"
    else:
        side = pick(sidearms) if random.random() < 0.5 else "no sidearm"
        head = f"grunt, melee (d20 {role_d20}): {pick(P['melee'])} | {side}"
    line = f"{n+1}. {head} | {pick(P['armour'])} | {pick(P['extra'])}"
    if n in lucky:
        line += f"  ** FOUND/MADE: {random.choice(P['found'])[0]}"
    print(line)

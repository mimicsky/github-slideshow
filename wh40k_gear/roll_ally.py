"""Ally roller (set by the player, Ash on Ostrava day 48): every new ally gets the full roll, as a friendly.

Recruits, allied soldiers or units met in the field, Sisters, NPCs who matter: the same rolls as enemies
(role d20, stats, kit, armour, extra), read as loyal, plus their traits (codex house rule 9).
Rules: bestiary/roles.md, 'Rolling new people' and 'Sister Novitiate'.

Usage:
  python3 roll_ally.py TYPE COUNT [WEALTH] [join]     allied soldiers through the enemy roller, + traits
      TYPE: commoner (militia, civilians), traitor (Guard and PDF troopers),
            traitor_elite (storm troopers, Scions, Ordo teams)
  python3 roll_ally.py sister [COUNT] [WEALTH] [join] [vows]   Sisters Novitiate
      vows: close to her vows (elite-trained stats)
  join: they join the Light (its named people): 3 traits at 75/25 good, Lho habit rerolled.
        Otherwise grunts roll 1 trait and specialists 2, at 50/50.
"""
import os, random, re, subprocess, sys, json

here = os.path.dirname(os.path.abspath(__file__))
LEVELS = ["poor", "steady", "good", "rich", "wealthy"]
WEIGHTS = {"poor": {"C": 80, "U": 20, "R": 0}, "steady": {"C": 70, "U": 25, "R": 5}, "good": {"C": 55, "U": 35, "R": 10},
           "rich": {"C": 40, "U": 45, "R": 15}, "wealthy": {"C": 25, "U": 50, "R": 25}}

# --- traits (codex house rule 9), read straight from the codex so the tables stay in one place ---
def trait_tables():
    text = open(os.path.join(here, "..", "DND_CODEX.md")).read()
    out = {}
    for kind, head in (("good", "**Good traits (d36)**"), ("bad", "**Bad traits (d36)**")):
        block = text[text.index(head):].split("\n\n", 2)[1]
        rows = {}
        for line in block.splitlines():
            m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if m:
                eff = re.sub(r"\s*\((added|changed|set|was|name)[^()]*(\([^()]*\)[^()]*)*\)", "", m.group(3)).replace("**", "")
                rows[int(m.group(1))] = (m.group(2), eff.strip())
        out[kind] = rows
    return out

OPPOSITES = [("Eagle-eyed", "Short-sighted"), ("Keen hearing", "Hard of hearing"), ("Steady hands", "Shaky hands"),
             ("Strong back", "Frail"), ("Fast healer", "Slow healer"), ("Iron gut", "Weak stomach"), ("Brave", "Jumpy"),
             ("Lucky", "Unlucky"), ("Night owl", "Heavy sleeper"), ("Organised", "Disorganised"), ("Fast learner", "Slow learner"),
             ("Inconspicuous", "Loud"), ("Light on their feet", "Clumsy"), ("Sharp memory", "Poor memory"), ("Runner", "Bad knees"),
             ("Iron will", "Big mouth"), ("Quick reflexes", "Slow reflexes"), ("Defender", "Exposed"), ("Brawler", "Hesitant"),
             ("Iron gut", "Sickly"), ("Hard to kill", "Glass jaw"), ("Cool under fire", "Jumpy"), ("Raider Hater", "Retired Raider"),
             ("Cultist Eradicator", "Cultist Rememberer"), ("Heretic Destroyer", "Forgotten Penitent"),
             ("Traitor Hater", "Renowned Traitor"), ("Pious", "Superstitious")]
def clashes(a, b):
    return any({a, b} == {x, y} for x, y in OPPOSITES)

def roll_traits(n, important, light):
    T = trait_tables()
    got, log = [], []
    while len(got) < n:
        good = random.randint(1, 4) <= 3 if important else random.randint(1, 2) == 1
        d = random.randint(1, 36)
        name, eff = T["good" if good else "bad"][d]
        tag = f"{'good' if good else 'bad'} {d}"
        if name in [g[0] for g in got]:
            log.append(f"{tag} {name} (duplicate, rerolled)"); continue
        if any(clashes(name, g[0]) for g in got):
            log.append(f"{tag} {name} (contradicts, rerolled)"); continue
        if light and name == "Lho habit":
            log.append(f"{tag} {name} (no smokers in the Light, rerolled)"); continue
        got.append((name, eff)); log.append(f"{tag} {name}")
    return got, log

def show_traits(n, important, light):
    got, log = roll_traits(n, important, light)
    odds = "75/25" if important else "50/50"
    print(f"   TRAITS ({n}, {odds}): " + "; ".join(f"{a} ({b})" for a, b in got))
    print(f"   (rolls: {', '.join(log)})")

# --- read as loyal ---
HERETIC = re.compile(r"chaos|cult|daemon|defaced|heretic|unholy|blasphem|god\b|garden|thorn|nurgle|khorne|slaanesh|tzeentch|mark of", re.I)
def loyal(line):
    line = re.sub(r"\bRenegade |\brenegade ", "", line)
    line = line.replace("Fallen commissar", "Commissar").replace("Defaced regimental insignia", "Regimental insignia")
    line = line.replace("Defaced regimental colours", "Regimental colours")
    return line

# --- allied soldiers: the enemy roller, read as loyal, + traits ---
def soldiers(kind, count, wealth, join):
    if kind in ("cultist", "raider", "pirate"):
        print(f"(note: '{kind}' is an enemy type; allies use commoner, traitor or traitor_elite)")
    args = [sys.executable, os.path.join(here, "roll_enemy.py"), kind, str(count)] + ([wealth] if wealth else [])
    out = subprocess.run(args, capture_output=True, text=True, cwd=here).stdout
    print(f"ALLIES, rolled as friendlies (roll_ally.py; read as loyal): {kind} x{count}" + (" | joining the Light" if join else ""))
    for line in out.splitlines():
        if line.startswith("SPECIAL TEAM") or line.startswith("("):
            print(line); continue
        m = re.match(r"\s*(\d+)\. (grunt|SPECIALIST)", line)
        new = loyal(line)
        print(new)
        if HERETIC.search(new) and not new.strip().startswith("++"):
            print("   !! a heretic item above: swap it for its loyal equivalent (DM)")
        if m:
            spec = m.group(2) == "SPECIALIST"
            show_traits(3 if join else (2 if spec else 1), join, join)

# --- Sisters Novitiate (bestiary roles, Sister Novitiate) ---
def sisters(count, wealth, join, vows):
    sys.path.insert(0, here)
    from role_weapons import ROLE_WEAPONS
    E = json.load(open(os.path.join(here, "enemies.json")))
    roles = sorted(E["traitor_elite"]["specialists"])
    level = wealth or "rich"
    w = WEIGHTS[level]
    def pick(rows):
        tier = random.choices(list(w), weights=list(w.values()))[0]
        opts = [r for r in rows if r[1] == tier] or rows
        return random.choice(opts)[0]
    print(f"SISTERS NOVITIATE x{count}, wealth {level.upper()} (roll_ally.py; allies only)" + (" | joining the Light" if join else ""))
    for n in range(1, count + 1):
        st, dx = (random.randint(25, 45), random.randint(35, 50)) if vows else (random.randint(20, 35), random.randint(25, 40))
        r = random.randint(1, 20)
        role = random.choice(roles) if r >= 16 else None
        c = random.randint(1, 6)
        calling = "Militant" if c <= 4 else "Hospitaller" if c == 5 else "Dialogus"
        a = random.randint(1, 6)
        armour = "Robes over a flak vest" if a <= 3 else "Robes over reinforced flak" if a <= 5 else "Robes over a carapace chest plate (carapace inplate)"
        if role:
            main = pick(ROLE_WEAPONS[role]) if role in ROLE_WEAPONS else E["traitor_elite"]["specialists"][role][0][0]
            kit = f"{main} (her role's) + {pick(ROLE_WEAPONS['sister novitiate'])}"
        else:
            kit = pick(ROLE_WEAPONS["sister novitiate"])
        who = f"novitiate, role {role.upper()}" if role else "novitiate (no role yet)"
        print(f"{n}. SISTER {who} (role d20 {r}; calling d6 {c}: {calling.upper()}): {kit} | {armour} (armour d6 {a}) | "
              f"STR {st} (+{st // 10}) DEX {dx} (+{dx // 10})" + (" | close to her vows" if vows else ""))
        print("   Sister rules: front line; Shield of faith (+1 vs fear, breaks, warp, corruption; never breaks); "
              "Act of faith (one reroll a fight); her calling (roles.md)")
        show_traits(3 if join else (2 if role else 1), join, join)

if __name__ == "__main__":
    a = [x.lower() for x in sys.argv[1:]]
    if not a:
        print(__doc__); sys.exit()
    join, vows = "join" in a, "vows" in a
    a = [x for x in a if x not in ("join", "vows")]
    wealth = next((x for x in a if x in LEVELS), None)
    nums = [int(x) for x in a if x.isdigit()]
    if a[0] in ("sister", "sisters"):
        sisters(nums[0] if nums else 1, wealth, join, vows)
    else:
        soldiers(a[0], nums[0] if nums else 1, wealth, join)

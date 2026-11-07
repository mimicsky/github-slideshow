"""Open dice for the table: any roll, plus the rare-item draw.

Usage: python3 dice.py NdX [NdX ...]      e.g. dice.py d20, dice.py 3d20, dice.py d6 2d20
       python3 dice.py rare weapons|any   draw one rare item from pools.json (DND_CODEX Part 8, Loot:
                                          rare roll 1 = weapons and gear in use, rare roll 2 = anything stashed)
"""
import json
import os
import random
import sys

rng = random.SystemRandom()
args = sys.argv[1:] or ["d20"]

if args[0] == "rare":
    kind = args[1] if len(args) > 1 else "any"
    here = os.path.dirname(os.path.abspath(__file__))
    items = json.load(open(os.path.join(here, "pools.json"), encoding="utf-8"))
    weapons = {"las", "stub", "bolt", "plasma", "melee", "flame", "melta", "launcher", "heavy", "explosive", "armour", "mod", "gear", "augmetic"}
    pool = [i for i in items if i["rarity"] == "R" and (kind != "weapons" or i["cat"] in weapons)]
    pick = rng.choice(pool)
    print(f"rare ({kind}): {pick['name']} ({pick['cat']}, {pick['tv']} TV)")
    sys.exit()

for a in args:
    n, _, x = a.lower().partition("d")
    n, x = int(n or 1), int(x)
    rolls = [rng.randint(1, x) for _ in range(n)]
    print(f"{a}: {rolls}" + (f" (total {sum(rolls)})" if n > 1 else ""))

"""Roll a 40k shop's stock from pools.json.

Usage: python3 roll.py SELLER SIZE
  SELLER: M (Munitorum/fleet stores), B (black market/chandlers),
          A (Mechanicus shrine), F (Free Trader / Void Exchange), E (Ecclesiarchy)
  SIZE:   small (5-7 items), medium (9-12), large (14-18)
Rarity weights: common 55, uncommon 32, rare 13. A separate open d20:
on a natural 20, one exotic oddity is added. Prints the d20 so it can be shown.
"""
import json, random, sys, os
here = os.path.dirname(os.path.abspath(__file__))
items = json.load(open(os.path.join(here, "pools.json")))
seller = (sys.argv[1] if len(sys.argv) > 1 else "M").upper()
size = sys.argv[2] if len(sys.argv) > 2 else "medium"
n = {"small": (5, 7), "medium": (9, 12), "large": (14, 18)}[size]
n = random.randint(*n)
weights = {"C": 55, "U": 32, "R": 13}
pool = [i for i in items if seller in i["sellers"] and i["rarity"] != "X"]
qty_by_cat = {"ammo": [2, 4, 6, 10], "explosive": [1, 2, 3, 4], "gear": [1, 2, 3], "goods": [1, 2], "salvage": [1, 2, 3]}
picked = []
while len(picked) < n and pool:
    tier = random.choices(list(weights), weights=list(weights.values()))[0]
    tier_pool = [i for i in pool if i["rarity"] == tier and i not in picked]
    if tier_pool:
        picked.append(random.choice(tier_pool))
d20 = random.randint(1, 20)
print(f"seller {seller}, size {size}, exotic d20: {d20}")
for i in picked:
    q = random.choice(qty_by_cat.get(i["cat"], [1, 1, 1, 2, 3]))
    print(f"{q} x {i['name']} ({i['rarity']}) - {i['tv']} TV")
if d20 == 20:
    ex = random.choice([i for i in items if i["rarity"] == "X"])
    print(f"EXOTIC: 1 x {ex['name']} - {ex['tv']} TV")

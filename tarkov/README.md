# Tarkov Co-Pilot — Operating File

**You play. I track.** Shared brain for tasks, stash, and keep/sell calls.

> **Mode:** PvE · **Patch:** 1.1.0.1.46699 · **Edition:** Unheard (Gamma, Unheard armband)
> **Level:** 21 (confirmed) · **Faction:** USEC · **Stash:** Level 4
> **Synced from screenshots 1–17.** ~110 active tasks logged below.

---

# ▶ NEXT RAID — CUSTOMS, DORMS

**Bring:** AKS-74U (required for Punisher) · 1× corrugated hose (cheap, trader/flea)
**Go:** Dorms. Stay there. Fight.

Three tasks progress **simultaneously** from the same fight in the same place:

| Doing this | Progresses | At |
|---|---|---|
| Kill Scavs **with the AKS-74U** | The Punisher – Part 1 | 40% → 25 total |
| Kill PMCs **in the Dorms area** (AI PMCs on PvE) | Huntsman Path – Angry Watchman | 0% → 5 needed |
| Kill **Reshala**, take his Golden TT | Huntsman Path – Trophy | 50% |

Reshala spawns Dorms · new gas station · construction site by the railroad · Warehouse 4.
Angry Watchman zone = both dorm buildings, the guard house, and the ground between them.
So camping Dorms with the AKS-74U feeds all three at once.

**Grab on the way out (2 min detour each):**

- **Skier's wallet** → Warehouse 17, second floor, multiple spawns in the room → *Private Club*
- **Secure folder** → isolated train carriage, west/boiler side between ZB-1012 and ZB-1011
  extracts. Under the brick pallet NW · under pallet SE · between wall and pallet NE →
  *Chemical – Part 1 (66%)*
- **Drop the corrugated hose** → any table in the experiments area, 2nd floor of the lab
  building → *Chemical Experiments*

**Skip this trip:** *The Courier* needs 2× Trijicon REAP-IR thermal scopes placed as drops.
That's a heavy rouble sink for a delivery task — not worth it until you're cash-comfortable.

> One raid, one area, five tasks moving, and it's all shooting and looting.

---

## 1. How to talk to me

| You say | I do |
|---|---|
| `raid report: <map>, <survived/died>, <what I brought back>` | Update stash, flag quest progress, tell you what to sell |
| `keep or sell: <item>` | Verdict + reason + sell channel |
| `what now` | Next task, which map, what to bring |
| `prep <map>` | Kit budget, keys, every live objective on that map |
| `stash check` | What to purge, ranked by roubles-per-slot |
| `hideout` | Next module worth building and what's missing |
| `done: <task>` | Move it to completed, re-rank the board |

Photos work — I read the task screen, hideout, and stash directly.

---

## 2. What this file is for

500 hrs, two PvP wipes, now PvE. You don't need the game explained. The two things that
actually cost you time are **recall** — 110 open tasks, where each objective physically
is — and **drift**, BSG moving things between patches faster than memory updates.

**Nothing here gets dropped.** You want all ~110 done eventually. The full list stays as
the queue — §4 is the backlog, not a shortlist. The card at the top is just the next
slice served to you, so you're reading five lines instead of a hundred and ten. When a
card clears, the next one gets built from what's left.

So this is a lookup layer, not a coach:

- **§4 Task Board** — everything open, grouped by map, so one trip clears several.
- **§5 Objective Reference** — the *where* for individual tasks, built on demand.
- **Ask me `prep <map>`** and I'll assemble every live objective on that map with
  locations and required keys in one sheet.

### Sourcing — what to trust, and what we proved wrong

I look tasks up rather than answering from memory. tarkov.dev's API is down and direct
wiki/tarkov.dev fetches are blocked from here, so lookups go through web search.

**Confirmed drift in 1.1.0:** at level **21** you have *The Courier* and *Private Club*
active. Guide sites list those at level **52** and **24**. Quests don't appear before
their gate, so 1.1 moved the level requirements and the guides haven't caught up.

That splits web data cleanly:

| Trust | Don't trust |
|---|---|
| **Objective locations** — map geometry barely moves | **Level gates** — proven stale |
| Spawn spots, room/building names | **Trader assignments** — reshuffled in recent patches |
| Extract names | Item values, rewards |

Rule: **your in-game task text is authoritative.** I supply the *where*. When a lookup
disagrees with your screen, your screen wins and I'll say so rather than paper over it.

### Ordering logic

Two filters, in this order:

**1. Task shape.** You want to fight and loot; the admin is what burns you out. So every
task gets classified:

- **FIGHT** — kill X, kill boss, kill with weapon Y. Your preferred play *is* the
  objective. Always front-loaded.
- **LOOT** — find item, grab and extract. Happens on the way through.
- **CHORE** — place item, stash item at location, survive-and-extract from a specific
  point, gear restrictions. Batched so you do several per trip and think about them
  as little as possible.
- **EXPENSIVE** — requires buying costly items to hand in or drop. Deferred unless
  something's gated behind it.

**2. Overlap.** Tasks that progress from the *same action in the same place* get bundled
into one raid. That's what the card at the top is — five tasks, one area, one fight.

Partial progress only pays on completion, so near-done tasks outrank fresh ones. Streets
is 21 tasks at 0% — biggest pile, least near-term payout, sorts last despite volume.

---

## 3. Near-Complete — cash these first

| Task | Map | Progress |
|---|---|---|
| Chemical – Part 1 | Customs | **66%** |
| Anesthesia | Shoreline | **66%** |
| Car Repair | Any | **62%** |
| Semiconductor Crisis | Any | **50%** |
| Shooter Born in Heaven | Any | **50%** |
| Revision – Lighthouse | Lighthouse | **50%** |
| The Huntsman Path – Trophy | Customs | **50%** |
| All This Filth… | Any | **50%** |
| The Punisher – Part 1 | Customs | **40%** |
| Supplements | Any | **37%** |
| Aid Stations | Any | **33%** |
| I Need More Power | Shoreline | **33%** |
| Needle in a Haystack | Any | **33%** |
| The Punisher – Part 2 | Shoreline | **26%** |
| Dressed to Kill | Any | **12%** |
| The Tarkov Shooter – Part 4 | Any | **6%** |

---

## 4. Task Board

### ★ Customs — run this first (8)

| Task | Progress |
|---|---|
| Chemical – Part 1 | **66%** |
| The Huntsman Path – Trophy | **50%** |
| The Punisher – Part 1 | **40%** |
| The Huntsman Path – Angry Watchman | 0% |
| The Courier | 0% |
| Chemical Experiments | 0% |
| Private Club | 0% |
| Shipment Tracking | 0% |

### ★ Shoreline — run second (12)

| Task | Progress |
|---|---|
| Anesthesia | **66%** |
| I Need More Power | **33%** |
| The Punisher – Part 2 | **26%** |
| Thirsty – Hounds | 0% |
| Wet Job – Part 1 | 0% |
| Tracker | 0% |
| Chemistry Closet | 0% |
| Rigged Game | 0% |
| No Swiping | 0% |
| Nothing Fishy About This | 0% |
| Health Care Privacy – Part 2 | 0% |
| Tarkov-Style Diplomacy | 0% |

### Lighthouse (10)

Revision – Lighthouse **50%** · The Huntsman Path – Administrator · The Hermit ·
Missing Cargo · Lost Contact · Drug Trafficking · Easy Job · Energy Crisis ·
Corporate Secrets · Broadcast – Part 1

### Reserve (11)

Reserve · Surplus Goods · Back Door · Demonstration Model · Classified Technologies ·
Safe Corridor · Documents · No Place for Renegades · Revision – Reserve · The Bunker ·
Disease History — *all 0%*

### Woods (7)

The Huntsman Path – Woods Keeper · Swift · Steady Signal · Metal Birds ·
The Survivalist Path – Thrifty · Shipping Delay – Part 1 · A Helping Hand — *all 0%*

### Factory (8)

Dragnet · Scout · Black Swan · All Is Revealed · Exit Here · Possessor ·
One-Way Ticket · Postman Pat – Part 1 — *all 0%*

### Interchange (5)

Hot Delivery · A Big Loss · Pathfinder · Fuel Crisis · Irresistible — *all 0%*

### Transition (2)

Special Comms · New Paths — *all 0%*

### Streets of Tarkov (21) — deferred, see §2

The Huntsman Path – Big Game · Cease Fire! · Dandies · Surveillance ·
The Secret to Productivity · Watching You · Your Car Needs a Service · Road Closed ·
Secret Message · House Arrest · The Secret Recipe · Beyond the Red Meat · Paramedic ·
Glory to CPSU · District Patrol · You've Got Mail · Properties All Around ·
Pets Won't Need It · Urban Medicine · Ballet Lover ·
Create a Distraction – Part 2 [PVE ZONE] — *all 0%*

### Any location (27) — these tick passively

**Bench / no raid needed:** Gunsmith – M4A1 · Gunsmith – OP-SKS

**In progress:** Car Repair **62%** · Semiconductor Crisis **50%** ·
Shooter Born in Heaven **50%** · All This Filth… **50%** · Supplements **37%** ·
Aid Stations **33%** · Needle in a Haystack **33%** · Dressed to Kill **12%** ·
The Tarkov Shooter – Part 4 **6%**

**Not started:** The Survivalist Path – Wounded Beast · Fishing Place ·
Every Hunter Knows This · Sew it Good – Part 1 · Chumming · Easy-Breezy ·
Capturing Outposts · Weapons Circulation · Regulated Materials · Is This a Reference? ·
Postman Pat – Part 2 · Informed Means Armed · Seizing the Initiative · Rough Tarkov ·
Arena Business [PVE ZONE] · Professional Fitness – Part 1 [PVE ZONE]

### Completed

- Break the Deal — Customs

---

## 5. Objective Reference

Built on demand — say `prep <map>` or name a task. Format below.

### Chemical – Part 1 · Customs · 66%

- **Objective:** locate the former Deputy Chief of Security's sleeping place on Customs,
  recover the wanted/secure folder, extract with it, hand to Skier.
- **Where:** isolated train carriage, western/boiler side of Customs, between the
  **ZB-1012** and **ZB-1011** extracts.
- **Spawns inside the carriage:** under the brick pallet in the NW corner · under the
  pallet in the SE corner · between wall and pallet in the NE corner. Multiple possible
  spawns — check all three.
- **Keys:** none.
- **Note:** must extract alive with it.
- *Source: web lookup, [tarkov.dev](https://tarkov.dev/task/chemical-part-1) /
  [ggrecon](https://www.ggrecon.com/guides/escape-from-tarkov-chemical-part-1-skier-quest/).
  Verify trader against your in-game text — trader assignments shifted in recent patches.*

<!-- more built on request -->

---

## 6. Character & Loadout

**Health at last sync:** HP 440/440 · Hydration 47/100 · Energy **9/100**

| Slot | Item | State |
|---|---|---|
| Earpiece | ComTac II | |
| Headwear | ULACH | 54/66 |
| Face cover | Momex balaclava | |
| Eyewear | AFGlass | 25/25 |
| Body armor | THOR CRV | 161/183 |
| On sling | AKS-74U (5.45x39) | 20/30 |
| On back | AK-74M (5.45x39) | 11/30 |
| Holster | Glock 17 (9x19) | 17/17 |
| Sheath | empty | |
| Backpack | Attack 2 | |
| Secure | Gamma (3x3) | |

Rig: AFAK, bandage, splint, CMS, Zippo, MS2000, paracord, spare mags, SSA AP 50.

### Trader Loyalty — *still need this from you*

Prapor · Therapist · Skier · Peacekeeper · Mechanic · Ragman · Jaeger · Fence · Ref

> LL gates are the real bottleneck at 21, not character level. One screenshot of the
> trader screen and I can tell you which tasks actually unlock something.

---

## 7. Stash — First Raid Haul

### KEEP — hideout / build material

GPU · PSU · car battery · magnet · nails · round pliers · energy-saving lamp ·
alkaline cleaner · medical tools

### KEEP — quest & barter

Flash drive · HDD · Cat figurine · Ushanka · Augmentin · Tushonka ×2 · Salewa · Vaseline

### On the GPU

Bitcoin Farm is locked, so it earns you nothing sitting there, and you're at ~40k. **My
call: sell it.** You're task-blocked, not farm-blocked — cash buys the kits that let you
actually clear the Customs and Shoreline partials. Say the word and I'll flip it to hold.

---

## 8. Hideout

**Stash 4.** Utility modules mostly level 1–2.

**Locked:** Bitcoin Farm · Booze Generator · Gear Rack · Gym · Library · Scav Case ·
Solar Power

Send a shot of any module's requirement panel and I'll work out what's missing and
whether the payback is worth it at your stage.

---

## 9. Keep / Sell Doctrine

Priority order — higher wins on conflict.

1. **Quest item → KEEP.** FiR status isn't recoverable; the roubles never repay the setback.
2. **Hideout material for an active build → KEEP.**
3. **Barter input → KEEP** only if the barter beats cash cost.
4. **Roubles-per-slot decides everything else.** A 1x1 worth 90k beats a 4x4 worth 200k.
5. **Sell channel matters** — trader on thin spreads, flea when it justifies fee and wait.
6. **Rare item, unsure → keep one, sell the rest.**

**Standing sell:** duplicate low-tier armor past one spare · attachments that don't fit
the AK-74M / AKS-74U / Glock · common ammo you don't run · bulky sub-10k-per-slot with
no task attached.

> ⚠️ **Version drift:** you're on 1.1.0 and Tarkov rebalances constantly. Task
> requirements, values and trader gates move. I'll flag uncertainty rather than state it
> confidently — your screen beats my memory.

---

## 10. Stash Doctrine

- **Keep 15–20% free.** Below that you make bad panic calls on return.
- **Quest items get their own container, nothing else in it.** Prevents the most
  expensive routine mistake in the game.
- **Two spare kits ready, no more.** Beyond that is dead capital.
- Purge order: bulky-cheap → duplicate attachments → excess common ammo → spare armor.
  Never quest, never hideout, never keys.

---

## 11. Session Log

```
[DATE] [MAP] [SURVIVED?] — brought back: … | quest progress: … | sold: … | net: …
```

- **First raid** — GPU, PSU, car battery, HDD, flash drive, Cat figurine + hideout
  hardware. Strong run.

---

## 12. Maintaining this

Tell me what happened and I edit, commit and push. Paste this file into any new
conversation and I'm caught up instantly — that's why it lives in git and not in a chat
that scrolls away.

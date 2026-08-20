# 🔬 RESEARCH INBOX — Tarkov Co-Pilot

**This file is the mailbox between the player's phone and the desktop session.**
The player is at work. They post requests here. Research gets done and posted back here.
**Nothing is deleted until the player says they've read it.**

---

## 📖 HOW THIS WORKS — read this first if you're a fresh session

You are working with **`tarkov.md`** in this same repo — a large, self-contained Tarkov
progress file. **Read it before answering anything about the player's game.** It holds the
quest board, gear, doctrine and every rule this project runs on.

**The three roles in this file:**

| Section | Who writes it | What happens next |
|---|---|---|
| **📥 REQUESTS** | **the player** *(usually from their phone)* | An assistant picks it up, researches it, and moves it to RESULTS |
| **🔬 RESULTS** | **the assistant** | Sits here until the player reads it |
| **✅ MERGED** | **the assistant**, after the player says "read it" | Findings get written into `tarkov.md` proper, and only a one-line record stays here |

### Rules

1. **Never delete a request.** Move it, mark it, but keep the trail.
2. **Research goes in RESULTS first, not straight into `tarkov.md`.** The player wants to
   read it before it lands in the main file.
3. **Only merge into `tarkov.md` when the player confirms they've read it.**
4. **Everything web-sourced is tagged `⚠️ web-sourced, unverified`.** Anything the player
   states from their own screen is `✅ player-confirmed` and **beats every website.**
   *(This rule is the whole philosophy of `tarkov.md` — read its `begin research` protocol.)*
5. **Always `git pull` before writing and `git push` after.** Two sessions share this file.

### How the player posts a request

Just add a line under **📥 REQUESTS** — no format required, plain English is fine:

```
- [ ] what's the best ammo for the Mutant right now
- [ ] where do I find LEDX on Interchange
```

---

## 📥 REQUESTS

**Posted 2026-08-20 from the phone session.** Six jobs, roughly in priority order.
**Take them one at a time and post each into RESULTS as it finishes** — don't wait until
all six are done.

---

### 3. ⚔️ CURRENT META KITS AND BUILDS

What people are actually running right now — gun builds, armor setups, the standard
"good kit" at various budgets. **Community sources over wiki.**

### 4. 📊 THE THREE 1.0 TIER LISTS — guns · armor · ammo

The gun tier list in `tarkov.md` **predates 1.0 and the Kord breach** — it's missing the
NL545 GP and probably others. **Find current 1.0 versions of all three.**

For guns: **return only what isn't already ranked** in the kit section.

### 5. 🔑 THE MILLION-ROUBLE KEYS — Labs keycards and marked/locked rooms

- **How to get Labs access keycards** — every route: spawn locations, drops, barters, prices
- **The locked rooms worth real money** — marked rooms on Customs and elsewhere
- **Top 5 most valuable keys in the game**, what they open, what they're worth
- **Which keys to look out for while looting** — the ones worth stopping for

*(Note: the player is taking Skier's `Chemical - Part 4`, which rewards 2× Labs keycard.)*

### 6. 🎫 THE KORD BREACH SEASON + BATTLE PASS

- What the season is, what the battle pass contains, how it progresses
- **Every item needed to upgrade it** — and for each one: **which map it's on and where to
  find it**
- Anything time-limited the player might miss

---

### 7. 🔴 FENCE REP — the full source table and the fastest realistic path

**This is goal #2 and the player is grinding it at a terrible rate. Fix that.**

**What they're doing now** ✅*player-confirmed*:
> Go in as a **scav**, find PMCs who have **already killed a scav**, and kill them —
> **+0.01 per kill**. Transit to another map, repeat, come back to Factory, repeat. Ends
> either dying to **Tagilla** *(who aggros scavs)* or extracting loaded with loot.
>
> **Best result so far: 0.06 for FIVE PMC kills plus one extraction.**

**The problems with it, in their words:** the PMC has to kill a scav *first*, the player
has to land the kill *themselves*, and the PMC may be gone by the time they arrive.

**What's needed:**
- **Every source of Fence rep, with its exact value** — scav extract, PMC-killed-a-scav
  kills, car extract, quest rewards, anything else that exists
- **Every penalty, with its value** — killing scavs as a scav, killing a boss as a scav,
  dying as a scav *(does that even cost anything?)*, leaving early
- **Is 0.01 per assisted PMC kill really the rate, or is something being missed?**
- **The fastest realistic path from their current standing to 3.0** — how many raids, of
  what kind
- Does anything **passively** raise it? Any quest that pays a chunk?

> ⚠️ **If the honest answer is "it's just slow," say so plainly.** Better to know it's a
> months-long background task than to keep optimising a dead end.

### 8. 🌳 QUEST DEPENDENCY TREE — the whole graph

**Fandom makes this easy:** every quest page lists what comes **before** it and what it
**leads to**. Walk those links and build the full tree.

**What it's for:** the player has ~100 active quests and picks them by map. With a tree
they could pick by **consequence** — *"these three unlock `Sellout`"*, *"this chain ends in
the FN40GL."*

**Deliverable:** each chain from start to end, which quests gate the **Kappa four**, and
which lead to rewards the player actually wants *(their gun rankings are in `tarkov.md`)*.

### 9. 🏟 ARENA — worth it or not?

**The player already has Arena access.** Two questions only:

1. **Are the Arena quests worth doing?** What do they pay, and does any of it help the main
   game — especially **Ref rep**, since Ref LL3 is **0.10 rep away**
2. **Are the crates/rewards you unlock worth the loot?** Straight yes-or-no with reasoning

### 10. 🏗 HIDEOUT CRAFTS — rank them all by profit

**No need to price barters — the game already shows rouble value in-game.**

**Currently being run** ✅*player-confirmed*: **gas mask → gas canisters** *(decent
money)* · **CMS kits** · **ammo for personal use**

**Wanted:** every craft in the hideout, ranked by **profit per hour and per slot**. Which
are worth running constantly, which are only worth it for personal use, which are a waste.
Flag any craft that produces something on the **never-sell list** — e.g. the **Booze
Generator makes moonshine**, and the **Scav Case needs 3**.

### 11. 💱 BEST BARTERS — just the good ones

The game shows what a barter is worth in roubles, so **skip the pricing analysis**. Just
answer: **which barters are actually worth doing?** The standouts, what they cost in items,
and what they'd cost in cash instead.

---

## 📝 PROCESS — please add this going forward

**Write a "WHAT CHANGED" block at the top of `tarkov.md` on every push.** Five lines, newest
first. The file is 2,500+ lines and the player reads it on a phone — they shouldn't have to
diff it to find the new material.

---

## ⚠️ PLAYER-CONFIRMED FACT — already written into `tarkov.md`

**🔴 INSURANCE DOES NOT WORK ON LABS.** Same as Icebreaker. Anything lost there is gone
permanently. ✅*player-confirmed*

---

## 🔬 RESULTS — researched, waiting to be read

### ✅ REQUEST 2 — TOP 5 LOOT RUNS

⚠️ **web-sourced, unverified** · figures are community estimates for patch 1.0.5, so treat
them as ranges not promises.

> ⭐ **The headline: three of the five are raids you're already scheduled to run.** You
> don't need a separate "money night" — you need to bring a backpack to the quests you're
> doing anyway.

#### 🥇 1. Interchange — the tech-store circuit · **₽500k–1M+**
- **Route:** **OLI → Techlight/Rasmussen → Goshan → IDEA → Kiba Arms → EMERCOM Medical**
- **Grab:** graphics cards, electronics, **Tetriz**, meds, **LEDX** from the pharmacies
- **Keys:** none needed for the bulk of it — **the register-and-tech sweep is key-free and
  still clears several hundred thousand.** EMERCOM / Ultra Medical / Kiba Arms outer+inner
  raise the ceiling past a million
- **Risk:** medium — **and it's Killa's floor**
- ⭐ **This is your `Supervisor` + books raid.** Identical route. Bring a bag

#### 🥈 2. Streets — the keyed run · **₽1M+, exceptional runs 2–3M**
- **Route:** **LexOs dealership (Kaban's stash) → Chekannaya 15 / 13 marked-room block →
  Concordia apartment 64 → Pinewood Hotel rooms** → extract **Crash Site or Courtyard**
- **Grab:** GPUs · **LEDX** · **VPX Flash Storage** · **Intelligence folders**
- **Keys:** several — this is the run that most rewards owning keys
- ⭐ **Overlaps your Streets quest board hard:** `Your Car Needs a Service` is at LexOs,
  `House Arrest` is Chekannaya 15, `Watching You` is Pinewood 215, `Surveillance` is
  Concordia. **Same buildings, quests and money together**

#### 🥉 3. Reserve — RB-key bunker rooms · **₽400k–900k**
- **Route:** **King / Knight / Bishop structures → train station → D-2 bunker → server rooms**
- **Grab:** supply crates, weapon mods, military tech, intelligence folders
- **Keys:** **RB-PSP1 · RB-PSP2 · RB-VO** *(and you already need **RB-ST** for `Surplus Goods`)*
- **Risk:** medium-high — **Raider AI patrols underground**
- ⭐ **This IS the D-2 chain raid.** Five or six quests plus 400–900k on the same trip.
  **Buy the RB keys before you go**

#### 4. Labs · **₽1M+** — but read the warning
- **Grab:** GPUs, LEDX, keycards, Bitcoin, meta weapons — the densest loot in the game
- **Keys:** a **Labs access keycard, consumed on entry**
- 🔴 **INSURANCE DOES NOT WORK ON LABS** ✅*player-confirmed* — everything you carry in can
  be lost permanently
- ⭐ **`Chemical - Part 4` (Skier branch) rewards 2× Labs keycard** — so your entry fee is
  already on its way. **Go in cheap the first time**

#### 5. Customs — Dorm 314 marked room · **₽200k–700k**
- **Route:** three-storey dorms **room 314** + the crackhouse perimeter
- **Grab:** **keycards spawn here**, guaranteed meds
- **Keys:** **Dorm room 314 marked key**
- ⭐ **You're getting that key free** — it's the next-task reward on `Controller`, the
  Zarya stun quest you just picked up
- **Risk:** high, most contested area on the map. ✅ **Safer alternative: the Customs stash
  circuit, ₽300k–800k with almost no player contact**

#### 🍯 Honourable mention — Shoreline Resort · **₽300k–700k**
East and West wing rooms — safes, meds, weapons, keycards. Needs wing keys. Medium risk.

---

### 📋 WHAT THIS MEANS FOR YOU

| Raid you're already doing | Money it also pays |
|---|---|
| **Reserve D-2 chain** | **₽400–900k** — buy RB-PSP1, RB-PSP2, RB-VO first |
| **Interchange `Supervisor` + books** | **₽500k–1M** — bring a backpack, sweep registers |
| **Streets quest block** | **₽1M+** — LexOs, Chekannaya, Pinewood, Concordia are all quest sites |

**The one genuinely new activity worth adding: the Customs stash circuit** — ₽300–800k with
minimal contact, and it pairs with `Angry Watchman` *(Dorms-zone PMCs)* and the Customs
propane tank for `Thirsty – Delivery`.

---

### ✅ REQUEST 1 — FULL BOSS-KILLING GUIDE

⚠️ **web-sourced, unverified** unless marked otherwise. Built around **your** guns, ammo
and armor as recorded in `tarkov.md`.

#### 🔴 First: the ammo problem, stated plainly

**Your best available rounds right now:**

| Round | Pen | Guns you own |
|---|---|---|
| **7.62x39 BP gzh** | **47** | **Mk47 Mutant · RD-704** |
| **5.45 BP gs** | **45** | NL545 GP · AK-12 · RPK-16 · AKS-74N |
| **5.56 M855A1** | **44** | HK 416A5 · MDR · Mk16 · TX-15 |
| **9x39 SP-6** | **48** | *needs an AS VAL — you're buying one for `Punisher P3` anyway* |

**That caps you around 45–48 pen.** Boss guards routinely wear **class 5**, and Glukhar's
wear **class 5–6 with visored helmets**. So against the hard ones you are **under-penned
for the chest and must play for heads and legs instead.**

> ⭐ **The unlock that fixes this is level 36 → Prapor LL4 → 5.45 BS at 54 pen.** Your rep
> already clears it. **Six levels turns half this list from "wait" into "go".**

---

### 🟢 TAKE THESE NOW at level 30

#### **Reshala** — 752 HP · Customs
- **Ammo:** M855A1 or 5.45 BP is plenty. He and his 4 guards are the lightest boss group
- **Kit:** CPC MOD.1, FLUX, HK 416A5. No special prep
- **Grenades:** 2 — **his guards hold rooms, he doesn't** *(already in your hard-lessons)*
- **The fight:** find him before he sees you. **Brown sweater; guards wear blue jackets with
  white striped cuffs.** Once spotted he runs behind the guards and you have to chew through
  them first. **Open on Reshala, not the guards**
- **Where:** Scav base (ZB-013 building with mounted weapons) · Dorms · New Gas · Fortress

#### **Shturman** ✅ *(you did this with an F1)*
- **Keep the method.** 3 followers, and the wiki warns his guards run **armor-shredding
  ammo** — do not trade in the open with them
- **Grenades work on him** ✅*player-confirmed* — unlike Killa
- **Where:** sawmill. **Loot his stash key if you ever need it again**

#### **Kaban** — 1300 HP · Streets
- ⭐ **The soft target hiding behind a scary reputation: most of his guards wear NO helmets**
  and silhouette against the sky. **Headshots delete them**
- **Ammo:** M855A1 is fine for heads. Bring the **DVL-10 or M700** if you want to do it from
  distance
- **🔴 Where NOT to go:** the **LexOs dealership is rigged with Claymores** — stay off the
  grass and curbs, and avoid the southern approach, which has long AGS-30 sightlines
- **✅ Where to fight from: the NORTH, around Chek 15.** That AGS-30 has a blindspot and
  cannot turn to face you there
- **Verdict:** very doable at 30 *if* you approach correctly. The mines kill more people
  than he does

---

### 🟡 DOABLE, BUT BRING THE RIGHT THING

#### **Glukhar** — 1010 HP · Reserve · **6 followers, the most of any boss**
- **Ammo:** ⚠️ **his guards wear class 5–6 armor and tier 3–6 helmets, some with visors.**
  Your 44–47 pen will struggle on their chests. **Play heads, or fight at contact range**
- **Kit:** **Zhuk** — this is the fight it exists for. Six guards means shots from several
  angles at once
- **The fight:** ⭐ **Get close and make Glukhar himself the first target.** He wears only a
  **black T-shirt, grey pants and at most a light plate carrier** — he is *far* softer than
  his own guards. Kill the boss, then clean up
- **Where:** storage buildings marked **"K"** · the repair building (white knight)
- **Bonus:** this is the same map as your **D-2 chain**, so you may meet him anyway

#### **Kollontay** — 1055 HP · Streets · 4 guards
- ⚠️ **His guards use armor-piercing rounds AND flashbangs.** Expect to be blinded
- **He wears a PSh-97 DJETA riot helmet** — class 2 top/nape/ears, **eyes class 1.** Weak
  head protection for a boss; headshots are live
- **Where:** Klimov shopping mall **or** the Ministry of Interior academy
- **The fight:** at the academy, **push the main door while holding an angle on the guards
  behind cover.** Let them trickle out and whittle them — but that backfires if Kollontay
  pushes with them
- ⭐ **Bring your own Zaryas** — you need 2 stunned PMC kills for `Controller` anyway, and
  fighting a flashbang user without flashbangs is a choice

#### **Sanitar** — 1270 HP · Shoreline
- 🔴 **The defining problem: his guards HEAL THEMSELVES with injectors**, wear **class 5
  armor and helmets**, and carry **lots of grenades**. Slow damage gets undone
- **Ammo:** the highest pen you have — **7.62x39 BP in the Mutant.** M855A1 will not do it
- **Kit:** **Zhuk** + grenades. He also pulls ordinary scavs in to fight for him
- **The fight:** **burst, don't trade.** Kill each guard in one engagement or they reset to
  full. **Do not let them break contact**
- **Where:** port/pier area · near the cottages

---

### 🔴 WAIT — not worth it at level 30

#### **Zryachiy** — **1655 HP · head 175** · Lighthouse
- 🔴 **KILL ZRYACHIY FIRST.** Kill his 2 guards first and **they respawn up to 3× each**
- **That 175 head HP means headshots are not the shortcut** — this is the only boss where
  the head is genuinely armored past your ammo
- **He sits on the lighthouse peninsula** — the whole approach is Rogue territory
- **Verdict: wait.** The wiki's own strategy assumes **3 players.** Solo at 45-pen this is a
  kit donation. You need `Administrator` eventually, but not now

#### **Killa** — 890 HP · Interchange
- Full writeup already in `tarkov.md`. **Thorax only** ✅*player-confirmed*, AP loaded,
  cover you reached first, **never re-peek the angle he holds**
- **Face is class 6** — nothing you own cracks it. **Wait for 5.45 BS at level 36**
- **He becomes worth fighting at level 32** when `Sellout` opens

#### **Tagilla** — 1220 HP · Factory / Interchange garage
- **All 12ga + a one-shot hammer.** Buckshot does little to class 5–6, so **distance wins
  and closing loses**
- **Verdict: avoid on the Factory night raid** for `HCP P5` — you'll have quest items on you

#### **The Goons** ✅ *(done)* — roaming
- **Knight** wears a **CPC Goons Edition** *(the same rig you own)* · **Birdeye** wears a
  **THOR CRV class 4** · **Big Pipe** is lightly armored — bandana and glasses
- **Birdeye is the one that kills you** — he's the accurate one at range. Break line of
  sight rather than duel him

---

### 📋 THE SHORT VERSION

| Boss | Now? | The one thing |
|---|---|---|
| **Reshala** | ✅ | Open on him, not the guards |
| **Kaban** | ✅ | North via Chek 15. Guards have no helmets |
| **Shturman** | ✅ | Grenades work |
| **Glukhar** | 🟡 | He's softer than his guards — kill him first |
| **Kollontay** | 🟡 | Bring flashbangs, his eyes are class 1 |
| **Sanitar** | 🟡 | Burst or they heal it back |
| **Killa** | 🔴 | Wait for 32 |
| **Tagilla** | 🔴 | Distance only |
| **Zryachiy** | 🔴 | Wait — 175 head, respawning guards |

**Universal rule this research confirms: at 45-pen you are a headshot-and-legs player
against boss guards.** Everything changes at **level 36** with 5.45 BS.

**Requests 2–6 still queued** — next check takes #2 *(loot runs)*.

---

## ✅ MERGED — read by the player and written into tarkov.md

*(empty)*

---

## 📋 SESSION LOG

**Newest first. One line per session so the other machine can see what changed.**

| Date | Session | What changed |
|---|---|---|
| 2026-08-20 | desktop | **REQUEST 2 DONE → RESULTS.** Top 5 loot runs. Finding: **three of the five are raids already on the schedule** — Reserve D-2 *(₽400–900k, buy RB-PSP1/PSP2/VO)*, Interchange `Supervisor` *(₽500k–1M, key-free sweep works)*, Streets quest block *(₽1M+, LexOs/Chekannaya/Pinewood/Concordia are quest sites)*. **Dorm 314 key arrives free** via `Controller`. **Labs entry arrives free** via `Chemical P4`. Also added the requested **🆕 WHAT CHANGED block at the top of `tarkov.md`.** |
| 2026-08-20 | desktop | **REQUEST 1 DONE → RESULTS.** Full boss-killing guide, all 11, built around the player's actual guns/ammo/armor. Headline: their ammo caps at 45–48 pen, boss guards wear class 5–6, so they're a heads-and-legs player until **level 36 → Prapor LL4 → 5.45 BS (54 pen)**. Take now: Reshala, Kaban *(north via Chek 15, guards have no helmets)*, Shturman. Wait: Killa, Tagilla, Zryachiy *(175 head, guards respawn 3× unless he dies first)*. **Requests 2–6 still queued.** |
| 2026-08-20 | **phone** | **Posted 5 more requests** — Fence rep source table + fastest path *(current rate is 0.06/raid, painful)* · full quest dependency tree from Fandom's before/after links · Arena worth-it check · hideout craft profit ranking · best barters. Also asked for a **WHAT CHANGED block** on every push. |
| 2026-08-20 | **phone** | **Posted 6 research requests** — full boss-killing guide (kit/ammo/tactics for all 11) · top 5 loot runs from Reddit/YouTube · current meta kits · the three 1.0 tier lists · Labs keycards + million-rouble keys · Kord breach season & battle pass. Also recorded **Labs has no insurance** into `tarkov.md`. |
| 2026-08-20 | desktop | **Big research drop into `tarkov.md`:** boss stat/tactics table (all 9, HP + the one thing that matters for each) · **Ice Breaker is PvE and reachable** — Boreas unlock runs through Intelligence Center 3 · levelling + skills mechanics (skill fatigue curve, what trains what) · loot runs by map · **"What to focus on right now"** priority list. |
| 2026-08-20 | desktop | Set up this file. Pushed a large `tarkov.md` update: full armor system + economy + doctrine, exposure rule, Killa/Tagilla intel, Lighthouse (10/10), Reserve D-2 chain, Woods, 12 Streets quests, ammo pen tables, helmets, and ~14 completed quests logged. |

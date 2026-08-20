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

### ✅ REQUEST 7 — FENCE REP / SCAV KARMA

⚠️ **web-sourced, unverified.** **Fence reputation IS Scav karma** — same number, two names.

## 🚨 THE ANSWER: IT IS NOT SLOW. YOU ARE USING THE WORST SOURCE.

> **Your method pays +0.01–0.03 per PMC kill.**
> **A first-time car extraction pays +0.2. A first-time co-op extraction pays +0.25.**
> **And the count is PER LOCATION — so every map has its own untouched first-time bonus.**

**You are at 1.566. Goal is 3.0. That gap is 1.434.**
**≈ SEVEN first-time car extractions covers almost the whole thing.**

---

### 📈 EVERY SOURCE OF FENCE REP

| Action | Change | Notes |
|---|---|---|
| 🥇 **Co-op extraction** *(as Scav OR PMC)* | **+0.25** | **first time per location.** Later uses = `0.25 ÷ total uses` |
| 🥈 **Vehicle/car extraction as PMC** | **+0.2** | **first time per location.** Later uses = `0.2 ÷ total uses` *(4th ≈ 0.05)* |
| **Help a Scav Boss** | **+0.05** | fight alongside him as a Scav |
| **Complete a Scav task** *(Fence dailies)* | **+0.01 to +0.05** | 🔑 **requires Intelligence Center — YOU HAVE IT** |
| Kill a traitor Scav as Scav | +0.03 | a Scav who harmed any Scav/boss/guard becomes a traitor for the raid — **no penalty for killing them** |
| **Kill a PMC who killed a Scav** | **+0.02** | **+0.03 if that PMC killed 2 or more** ⚠️*see conflict* |
| Help a Scav Boss guard | +0.02 | |
| Help a Scav | +0.01–0.02 | |
| Extract or transit as a Scav | +0.01 | |
| Kill Raider · Rogue · Cultist as Scav | **none** | no gain, **no penalty** |

### 📉 EVERY PENALTY

| Action | Change |
|---|---|
| **Kill a Scav Boss as a Scav** | **−0.2** |
| **Kill a player Scav as a Scav** | **−0.1** |
| Kill a Scav Boss guard as Scav | −0.05 |
| Kill an AI Scav as Scav | −0.03 to −0.05 |
| ✅ **DYING as a Scav** | **NOTHING — it is not a penalty.** *(answers your question directly)* |
| ✅ **Leaving early** | **not a listed penalty** |

*(Above +6, penalties are calculated as if you were at +6. Above +8, an extra −2 applies.)*

---

### ⚠️ CONFLICT — your rate vs the wiki

```
⚠️ CONFLICT — Fence rep per assisted PMC kill
  Player screen: +0.01 per kill  (0.06 total for 5 kills + 1 extraction)
  Fandom:        +0.02, or +0.03 if the PMC killed 2+ Scavs
  → Player's screen wins. Your 0.06 matches +0.01/kill exactly.
  Possible causes: PvE differs from PvP, or some of those PMCs hadn't
  actually killed a Scav. Worth one check in game.
```

**Either way it doesn't change the conclusion** — even at the wiki's +0.03, a car extract is
**7× better** and a co-op extract is **8×**.

---

### 🎯 THE FASTEST REALISTIC PATH FROM 1.566 → 3.0

**1. 🚗 Use the car extract once on every map you play.** +0.2 each, and **it stacks with
raids you're already running**:
- **Customs — Dorms V-Ex** · **Interchange — Power Station V-Ex** · **Woods — Bridge car
  (₽5k)** · **Shoreline · Lighthouse · Ground Zero · Streets — Primorsky Ave Taxi V-Ex**
- ⭐ **`Paramedic` REQUIRES extracting via Primorsky Ave Taxi V-Ex.** That quest pays you
  **+0.2 Fence rep for free.**
- **Seven maps ≈ +1.4.** That is essentially your entire remaining gap

**2. 🤝 Co-op extracts — +0.25 each, the single best source.** ⚠️ These normally need a
Scav and a PMC to cooperate; **whether they trigger in PvE with AI Scavs needs testing.**
**Try one and tell me** — if it works, it's better than the car extracts

**3. 📋 Turn on Fence's Scav daily tasks.** You have the **Intelligence Center**, so they're
already available. **+0.01–0.05 each, every day, forever.** This is your passive source

**4. Keep the PMC-killing method as a bonus, not a plan.** It's the slowest thing on the
list

**5. 🚫 Never kill an AI Scav, player Scav or boss while playing Scav.** One boss kill
(−0.2) erases a car extract

---

### 🎁 WHAT KARMA ACTUALLY BUYS

Car extract fees ↓ · **BTR trunk size** ↑ · transit delivery size ↑ · **Scav case turnaround**
↓ · Fence payout ↑ · **Scav cooldown** ↓ · Scav gear quality ↑ · AI Scavs obey commands ·
**at +6: a 30% discount sales tab, AI Scavs fight for you, and Scav bosses treat you as an ally**

**Quest gates:** **+1** → `Is This a Reference?` *(you're past it)* · **+2** → `Network
Provider – Part 1` · **+4** → `Establish Contact` **and** the **Savior ending route**

> ⭐ **Note +2 is only 0.43 away** — one or two car extracts unlocks `Network Provider`.

---

### ✅ REQUEST 6 — KORD BREACH SEASON + BATTLE PASS

⚠️ **web-sourced, unverified.**

#### ⏰ THE TIME-LIMITED PART — read this first

> **Season 1 "KORD BREACH" runs 3 Aug → 7 DEC 2026.**
> **It is FREE**, works in **PvE**, progression is **shared across all modes**, and
> **rewards unlock permanently on all characters — including your PvE one.**

**Today is 20 Aug. You have ~109 days left.**

#### 🔢 The maths that decides whether you bother

- **501 documents total** to claim every reward
- 🔴 **PvE daily cap: 15 documents/day** *(Seasonal 30, PvP 20 — and the cap is **shared**;
  15 in PvE means 0 left if you switch modes)*
- **501 ÷ 109 days = ~4.6 documents per day.** **That's about a third of your daily cap.**

> ✅ **Verdict: comfortably achievable without changing how you play** — but only if you
> start collecting now. Leave it two months and the daily cap makes it impossible.

#### 📄 How progression works

**You find TerraGroup documentation in raids.** It behaves like a quest item — **everyone
can pick up the same one**, so no competition — and it drops for **PMC and Scav alike.**
Each reward requires a **specific type**, so the maps you run decide what you can unlock.

#### 🗺 THE EIGHT DOCUMENT TYPES AND THEIR MAPS

| Documentation type | Found on |
|---|---|
| **Blueprints & technical** | **Interchange · Factory** · The Labyrinth |
| **Financial** | **Customs · Streets · Interchange** |
| **Medical** | The Lab · **Ground Zero** · The Labyrinth |
| **PMC personnel files** | **Reserve · Lighthouse** · Icebreaker |
| **User documentation** | **Ground Zero · Streets** · The Lab |
| **Test documentation** | **Shoreline · Woods** · Icebreaker |
| **Technical documentation** | **Shoreline · Woods · Lighthouse** |
| **Project documentation** | **Factory · Reserve · Customs** |

**Plus:** **Classified documents** — purchasable in the Expansion Hub, count as **any** type.
**And:** **exchange any 5 documents → 1 of your choice**, which covers any shortfall.

#### ⭐ WHAT THIS MEANS FOR YOUR ROTATION

**Your current maps — Woods, Reserve, Interchange, Factory, Customs — already cover 6 of the
8 types.** You'd be collecting most of this by accident.

**The two you'd miss: Medical and User documentation.** Both come from **Ground Zero, Streets
and The Lab.**

> 🔑 **And you're about to have Labs access** *(craftable keycards — request 5)*. **A Labs
> run covers BOTH missing types at once**, on top of being the densest loot map in the game.
> **Ground Zero is the safe alternative** — it's a low-level map and covers the same two.

#### 🎁 What's actually in it

Early pages: **Marked dogtag · TarCoin ×50 · BURN poster · Black Division gear crates ·
hideout customisations** *(Black wood ceiling, Scorpion target)* **· Red Hawaii clothing ·
trade offers** *(Gentex Ops-Core SOTR respirator, Mystery Ranch NICE Frame Load Sling)*.

⚠️ **Structural rule: you must claim all but one reward on a page before the next page
opens** — so you can't cherry-pick the good stuff and skip ahead.

---

### 📋 TAKEAWAY

**Start picking up documents now.** It's free, it's permanent, it works in PvE, you're
already running 6 of the 8 map types, and **~4.6 documents a day gets you the lot before
7 December.** The only genuine gap is Medical/User — **which one Labs trip solves.**

---

### ✅ REQUEST 5 — LABS KEYCARDS AND THE MILLION-ROUBLE KEYS

⚠️ **web-sourced, unverified.**

#### 🚨 START HERE — you can CRAFT Labs keycards, and you already can

> ### **UHF RFID Reader + Intelligence folder → Intelligence Center LEVEL 2 → 40 minutes → 3× TerraGroup Labs access keycard**
>
> **You have Intelligence Center 2.** That craft is available to you **right now**, and it
> returns **three** cards for two items. **This is the cheapest Labs access in the game and
> nobody told you it existed.**

**And you may already be holding some:** ⭐ **`The Huntsman Path – Woods Keeper` rewards
3× Labs keycard** — the quest you completed with the F1 grenade. **Check your stash.**

#### 🔑 Every route to a Labs keycard

| Route | Detail |
|---|---|
| 🏗 **CRAFT** | **UHF RFID Reader + Intelligence folder** → Int Center 2 → 40 min → **×3** |
| 🎁 **Woods Keeper** ✅*done* | **×3** |
| 🎁 **Camera, Action!** | ×3 |
| 🎁 **Beneath The Streets** · **Quality Standard** | ×1 each, as starting equipment |
| 💱 **Barter** | **Bulbex cable cutter + Pipe grip wrench + 2× Pliers Elite** → **Mechanic LL3** *(you have LL3)* |
| 🛒 **Buy** | **Therapist LL4** or **Ref LL4** — both out of reach for now |
| 🔮 **Cultist Circle** | 1 via a special sacrifice |
| 🎒 **Loot** | drawers · common fund stash · scav pockets · **bosses** · rare valuables crates · **every marked room** |

> 🔴 **DO NOT SELL BULBEX CABLE CUTTERS.** They're the barter ingredient above **and**
> `Special Comms` needs one at the RUAF boulder. Your file already lists that quest.

**Rules on the card itself:** consumed on entering Labs · **not** consumed in practice mode
· max **5 in raid inventory** · fits in **wallets, docs cases, SICC and secure containers**
· **`Fishing Place` needs 2 found in raid.**

**One barter worth knowing:** **1× Labs keycard → Peacekeeper LL3 → HK G28** *(a gun on your
"I'll use" list)*.

---

#### 💎 THE MOST VALUABLE KEYS

| Key | Worth / why |
|---|---|
| 🥇 **Mysterious room marked key** *(Chekannaya 13, Streets)* | **~₽2,800,000 on the flea** — the most expensive key in the game |
| 🥈 **Reserve bunker keys — PS81 · PS82 · PSP1 · PSP2** | **Community S-tier.** Rooms full of tech loot — **VPX cards** — plus quest items |
| 🥉 **Reserve marked rooms — RB-BK · RB-VO** | Better loot than **RB-PKPM** by consensus |
| **Labs Weapons Testing room key** | Best value *inside* Labs right now |
| **Customs Dorm 314 marked key** | ⭐ **arriving free** via `Controller` |

**Marked rooms have a 1.5–2% roll for high-tier loot** — keycards, GPUs, LEDX. That's the
whole reason they're worth the key.

⚠️ **Keys now have limited uses — roughly 25–50 before they break.** So a key is a
consumable, not a permanent asset. Factor that into whether a ₽2.8M key is ever worth buying
*(it isn't, for you)*.

#### 👀 WHAT TO STOP FOR WHILE LOOTING

**Any keycard** · **RB-** anything on Reserve · **marked-room keys** · **Bulbex cable
cutters** *(barter + quest)* · **Intelligence folders** and **UHF RFID Readers** — those two
are your keycard craft, so they're worth more to you than their sell price.

---

### 📋 TAKEAWAY

**You don't need to buy Labs access — you can craft it three at a time, and Woods Keeper may
have already handed you three.** The expensive keys *(₽2.8M Chek 13)* are not worth buying,
especially now that keys wear out. **Loot Reserve RB keys when you see them, and never sell
a Bulbex cutter.**

---

### ✅ REQUEST 4 — THE THREE 1.0 TIER LISTS

⚠️ **web-sourced, unverified** · community rankings, most recent dated **16 Aug 2026**.

#### 🔫 GUNS — only what your list is MISSING *(as asked)*

Your tier list already covers the entire current S-tier. **Genuinely new since 1.0:**

| Gun | Verdict |
|---|---|
| **Norinco QBZ-191** 🆕 | New in 1.0. **"Unproven — not fully optimised yet."** No settled ranking |
| **Howa Type 20** 🆕 | New in 1.0. Same verdict — **community hasn't worked it out** |
| **NL545 GP** | *(already flagged missing in your file)* — now confirmed **top-tier**, listed alongside the MDR as the current standout |

**That's it. Two new guns, neither of them settled.** Everything else the community ranks
S-tier — **MDR 7.62x51 · Mk47 · M4A1 · RSASS · AK-103** — is already in your list, and
**A-tier AUG A1/A3 and SA-58** are too.

> ✅ **Your tier list is in better shape than the file assumed.** It was flagged as
> "predates 1.0 and is missing guns" — in practice it's missing **three**, and you'd already
> found one of them yourself.

#### 🛡 ARMOR

| Tier | Setup |
|---|---|
| **Meta** | **LBT-6094A Slick** + **class 6 UHMWPE** — **KITECO SC-IV SA** or **GAC 4sss2** |
| **Budget** | **5.11 Hexgrid** + **GAC 3s15m** *(class 5 UHMWPE)* |
| **Rule** | **Class 5 minimum for rifle fights, class 6 ideal** |

> ⭐ **This validates your armor research exactly.** The community meta is *"Slick **plus
> UHMWPE class 6 plates**"* — **not a stock Slick**, which your file correctly identified as
> a trap because it ships with Kiba Arms Steel *(95 effective, 5.1 kg)*.
>
> ⭐ **And you're already at budget-meta or above:** your **CPC MOD.1 runs GAC 3s15m** — the
> exact plate named as the budget pick — at **0% movement penalty**, while your **Zhuk is
> class 6 all round**. **No armor purchase would improve you.**

#### 🔸 AMMO

**Community "best right now": 5.56 M995 · 7.62x39 MAI AP · .45 RIP.**

**Lobby armor expectations:** mid-raid players wear **class 4–5**, late kits **class 5–6**.

> 🔴 **Third independent confirmation of the same problem.** The two rifle rounds named as
> best are **M995 (53 pen)** and **MAI AP (58 pen)** — precisely the two sitting above your
> **45–48 ceiling.** Requests 1, 3 and 4 have now each arrived at this from a different
> direction.

---

### 📋 TAKEAWAY

**Nothing to buy. Two guns to watch.** Your guns are meta, your armor is meta-or-better,
and **the only gap on all three lists is ammunition** — which resolves at **level 36**.

---

### ✅ REQUEST 3 — CURRENT META KITS AND BUILDS

⚠️ **web-sourced, unverified** · community build guides, current for 1.0.x.

#### 🔴 The principle every source repeats

> **"Ammo is significantly more important than the weapon itself."**

**This is the same conclusion request 1 reached from the other direction.** Your guns are
fine. Your **45–48 pen ceiling** is the problem. Every rouble spent on a fancier handguard
is a rouble not spent on better rounds.

⭐ **And a mechanic change that saves you money:** **patch 1.0.4.5 decoupled recoil from
handguards.** Expensive handguards no longer carry the build. **Stop paying for them.**

---

#### 🏆 THE S-TIER LIST — and you already own most of it

| Meta gun | ~Cost | Your status |
|---|---|---|
| **DT MDR 7.62x51** | ~250k | 🔴 **"The undisputed best gun in the game."** ⚠️ **Your MDRs are the 5.56 version** — the 7.62x51 is a different, better gun. **Worth buying** |
| **Mk47 Mutant** | ~350k | ✅ **OWNED · top favourite ·** and it fires **7.62x39 BP, your best round at 47 pen.** Your best gun *is* meta |
| **AUG A3** | ~200k | ✅ owned-ish — **"exceptional ergonomics."** Your note says it's only worth it modded; the meta agrees |
| **Vector 9x19** | ~120k | ✅ on your "I'll use" list — **"undisputed king of SMGs," 1100 RPM** |
| **DVL-10 Saboteur** | ~220k | ✅ **OWNED** — **integrally suppressed bolt-action.** S-tier and quiet |
| **RSASS** | ~350k | ⭐ **"Best semi-auto DMR."** **Your `Wet Job` chain rewards one** — already flagged as a keep in your file |
| **RPK-16** | ~280k | ✅ **OWNED ×2** — S-tier **with 95-round drums and BS ammo.** ⚠️ BS is **Prapor LL4 = level 36** |
| **FN Five-seveN MK2** | ~60k | ✅ **"The best pistol in Tarkov,"** 20-round mags. You have the 5-7 |
| **MP-155 Ultima** | ~180k | ✅ MP-155 is on your list — **"the absolute best shotgun in Tarkov"** |

> ⭐ **Read that table again: you are already holding the meta.** Mutant, DVL-10, RPK-16 ×2,
> AUG, 5-7. **The only genuine gap is the 7.62x51 MDR** — and the RSASS arrives free via
> `Wet Job`.

---

#### 💰 THE BUDGET TIER — what "cheap kit" actually means

- **Mosin Infantry + PS ammo — under ₽20,000 total.** **Kills any armour tier with a
  headshot.** This is the real answer to your Hobo Streak and to `Swift`-style no-armor runs
- **7.62x39 PS — 32 pen, 57 damage.** The budget gold standard; handles early armor and
  drops unarmoured targets instantly
- **PP-19-01 Vityaz — ₽21,000 at Prapor LL2**, and it has a **built-in dovetail** so you skip
  the sight adapter. **EKP-8-02 reflex for ₽9,900** and you have a complete CQB gun for
  ~₽31k. *(Vityaz is on your "I'll use" list)*

---

#### 🛡 ARMOR SIDE — nothing to buy

Your armor research already settled this: **you own the two best carriers in the game
(CPC MOD.1 and CPC Goons)** plus a **class 6 Zhuk**, and **no trader sells a class 6 plate at
any loyalty level.** There is no armor upgrade available to you for money — only for loot.

**So the meta kit for you, concretely:**

| Budget | Gun | Armor | Head |
|---|---|---|---|
| **Hobo** | **Mosin + PS** *(₽20k)* | Thunderbolt | none |
| **Normal** | **Mutant + 7.62x39 BP** | **CPC MOD.1** | MTEK FLUX |
| **Fight / boss** | **Mutant BP** or **DVL-10** | **Zhuk** | Altyn *(accept the sound loss)* |
| **Quiet** | **DVL-10** *(integrally suppressed)* | CPC MOD.1 | FLUX + headset |

---

### 📋 THE ONE-LINE TAKEAWAY

**Stop shopping for guns. You own the meta.** The two things worth buying are **a 7.62x51
MDR** and **better ammo at level 36** — and the second one matters more than the first.

---

## ✅ MERGED — read by the player and written into tarkov.md

| Date | Request | Where it landed |
|---|---|---|
| 2026-08-20 | **#1 Full boss-killing guide** | `tarkov.md` → *Bosses* → **"How to actually kill them"**. Includes the 45–48 pen ceiling, the take-now / doable / wait split, and the level-36 unlock. **Player correction folded in: Kollontay's club jams your weapon.** |
| 2026-08-20 | **#2 Top 5 loot runs** | `tarkov.md` → *Loot runs*. Full routes, keys, values, and the overlap table showing three of five are raids already scheduled. |

---

## 📋 SESSION LOG

**Newest first. One line per session so the other machine can see what changed.**

| Date | Session | What changed |
|---|---|---|
| 2026-08-20 | desktop | **REQUEST 7 DONE → RESULTS.** Fence rep. 🚨 **It is NOT slow — they're using the worst source.** PMC kills pay +0.01–0.03; a **first-time car extraction pays +0.2 and a co-op extraction +0.25, counted PER LOCATION.** Their 1.434 gap to 3.0 is **≈7 car extracts**, and **`Paramedic` already requires one** *(Primorsky Ave Taxi V-Ex)*. **Fence Scav daily tasks (+0.01–0.05) need the Intelligence Center, which they have.** **Dying as a Scav costs nothing.** ⚠️ CONFLICT logged: their +0.01/kill vs wiki's +0.02–0.03. |
| 2026-08-20 | desktop | **REQUEST 6 DONE → RESULTS.** Kord Breach battle pass. ⏰ **TIME-LIMITED: 3 Aug → 7 Dec 2026**, free, works in PvE, rewards permanent. **501 documents total, PvE cap 15/day (shared across modes) — works out to ~4.6/day over the 109 days left, so achievable without changing how they play.** Their current map rotation already covers **6 of the 8 document types**; the two missing *(Medical, User)* both come from **Ground Zero or The Lab — and they're about to have craftable Labs keycards.** |
| 2026-08-20 | desktop | **REQUEST 5 DONE → RESULTS.** Labs keycards + valuable keys. 🚨 **Headline: they can CRAFT Labs keycards NOW — UHF RFID Reader + Intelligence folder → Intelligence Center 2 → 40 min → ×3.** They have Int Center 2. **And `Woods Keeper` (just completed) rewards 3 — check the stash.** Also: barter via Mechanic LL3 needs a **Bulbex cutter, which `Special Comms` also needs — do not sell them.** Most valuable key is Chek 13 at ~₽2.8M, but **keys now break after 25–50 uses**, so buying them is a bad deal. |
| 2026-08-20 | desktop | **REQUEST 4 DONE → RESULTS.** Three 1.0 tier lists. **Guns: only 3 missing from the player's list** — QBZ-191 and Howa Type 20 *(both new in 1.0, community calls them unproven)* plus the NL545 they'd already spotted. Their list is in better shape than assumed. **Armor: community meta = Slick + UHMWPE class 6 — which validates the file's "stock Slick is a trap" finding**, and the player's CPC MOD.1 already runs the named budget plate. **Ammo: best-in-game is M995 (53) and MAI AP (58)** — the two rounds directly above their ceiling. **Third independent confirmation that ammo, not gear, is the constraint.** |
| 2026-08-20 | desktop | **REQUEST 3 DONE → RESULTS.** Meta kits/builds. Finding: **the player already owns most of the S-tier** — Mutant *(their favourite, and it fires their best round)*, DVL-10, RPK-16 ×2, AUG, 5-7. **Only real gap: the 7.62x51 MDR** — their MDRs are the 5.56 version. Every source repeats **"ammo matters more than the gun,"** confirming request 1's pen-ceiling conclusion. Also: **1.0.4.5 decoupled recoil from handguards — stop paying for them.** Budget tier documented *(Mosin+PS under ₽20k, Vityaz ₽21k)*. **Requests 4–11 queued.** |
| 2026-08-20 | **phone** | **Marked #1 and #2 read — both merged into `tarkov.md`.** Boss guide went into the Bosses section, loot runs replaced the old stub. Player correction added: **Kollontay's club jams your weapon**, and asked the desktop to check whether other bosses have disarm mechanics the research missed. **Next up: #3 meta kits.** |
| 2026-08-20 | desktop | **REQUEST 2 DONE → RESULTS.** Top 5 loot runs. Finding: **three of the five are raids already on the schedule** — Reserve D-2 *(₽400–900k, buy RB-PSP1/PSP2/VO)*, Interchange `Supervisor` *(₽500k–1M, key-free sweep works)*, Streets quest block *(₽1M+, LexOs/Chekannaya/Pinewood/Concordia are quest sites)*. **Dorm 314 key arrives free** via `Controller`. **Labs entry arrives free** via `Chemical P4`. Also added the requested **🆕 WHAT CHANGED block at the top of `tarkov.md`.** |
| 2026-08-20 | desktop | **REQUEST 1 DONE → RESULTS.** Full boss-killing guide, all 11, built around the player's actual guns/ammo/armor. Headline: their ammo caps at 45–48 pen, boss guards wear class 5–6, so they're a heads-and-legs player until **level 36 → Prapor LL4 → 5.45 BS (54 pen)**. Take now: Reshala, Kaban *(north via Chek 15, guards have no helmets)*, Shturman. Wait: Killa, Tagilla, Zryachiy *(175 head, guards respawn 3× unless he dies first)*. **Requests 2–6 still queued.** |
| 2026-08-20 | **phone** | **Posted 5 more requests** — Fence rep source table + fastest path *(current rate is 0.06/raid, painful)* · full quest dependency tree from Fandom's before/after links · Arena worth-it check · hideout craft profit ranking · best barters. Also asked for a **WHAT CHANGED block** on every push. |
| 2026-08-20 | **phone** | **Posted 6 research requests** — full boss-killing guide (kit/ammo/tactics for all 11) · top 5 loot runs from Reddit/YouTube · current meta kits · the three 1.0 tier lists · Labs keycards + million-rouble keys · Kord breach season & battle pass. Also recorded **Labs has no insurance** into `tarkov.md`. |
| 2026-08-20 | desktop | **Big research drop into `tarkov.md`:** boss stat/tactics table (all 9, HP + the one thing that matters for each) · **Ice Breaker is PvE and reachable** — Boreas unlock runs through Intelligence Center 3 · levelling + skills mechanics (skill fatigue curve, what trains what) · loot runs by map · **"What to focus on right now"** priority list. |
| 2026-08-20 | desktop | Set up this file. Pushed a large `tarkov.md` update: full armor system + economy + doctrine, exposure rule, Killa/Tagilla intel, Lighthouse (10/10), Reserve D-2 chain, Woods, 12 Streets quests, ammo pen tables, helmets, and ~14 completed quests logged. |

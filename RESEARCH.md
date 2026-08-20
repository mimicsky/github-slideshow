# 🔬 RESEARCH INBOX — Tarkov Co-Pilot

**This file is the mailbox between the player's phone and the desktop session.**
The player is at work. They post requests here. Research gets done and posted back here.
**Nothing is deleted until the player says they've read it.**

---

# 🔴 FILE OWNERSHIP — READ THIS FIRST

**As of 20 Aug, the two sessions no longer share files.**

| File | Who writes it |
|---|---|
| **`RESEARCH.md`** *(this file)* | **the phone session ONLY** |
| **`tarkov.md`** | **the desktop session ONLY** |

**Why:** both sessions merged the Arena research at the same time. The conflict resolution
silently **dropped a standing rule** from `tarkov.md` and left the Arena block duplicated.
It took a manual grep to catch. Second time something vanished in a merge.

### What each session does now

**📱 Phone session:**
- Posts requests here · reads results · marks them read
- Records **player-confirmed facts** in the *PLAYER FACTS* section below
- **Never edits `tarkov.md`.** Not even a one-line fix.

**💻 Desktop session:**
- Does the research, posts results here
- **Owns all writes to `tarkov.md`** — merges the research, merges the player facts
- **Reads *PLAYER FACTS* every cycle** and folds anything new into `tarkov.md`

> ⚠️ **Desktop: check for duplication from before this rule.** The phone session already
> merged requests **1, 2, 4, 5, 6, 7 and 9** into `tarkov.md` directly. If you merge them
> again you'll get two copies. **Also verify the "Fence daily done today?" standing rule is
> still present** — it has now been lost once and restored twice.

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

## 🧾 PLAYER FACTS — desktop, merge these into `tarkov.md`

**Written by the phone session from what the player says. ✅ These beat every website.**
**Desktop: fold them in, then mark the row merged.**

| Date | Fact | Merged? |
|---|---|---|
| 20 Aug | **Kollontay's club JAMS YOUR WEAPON.** Never let him close — the danger is being disarmed while 4 guards are up. Makes the "push the academy door" tactic risky. | ✅ done |
| 20 Aug | **Player holds at least 2 Labs keycards already.** Don't tell them to craft more until they check. | ✅ done |
| 20 Aug | **Player is MISSING the Financial documentation type** for Kord Breach. It drops on **Customs · Streets · Interchange** — all maps already in rotation. | ✅ done |
| 20 Aug | **Fence rep from an assisted PMC kill reads +0.01 on the player's screen**, not the +0.02–0.03 the wiki claims. Their 0.06 for 5 kills matches +0.01 exactly. | ✅ done |
| 20 Aug | 🔔 **STANDING: remind the player to do their Fence scav daily EVERY DAY.** They asked directly. Must be the first line of every raid card. | ✅ done |
| 20 Aug | 🔴 **KILLA CANNOT BE AVOIDED ON INTERCHANGE.** He **left the mall entirely and killed the player at the EMERCOM CHECKPOINT extract.** Reddit reports he is **far more aggressive in 1.1 than previously** — unclear if intentional or a bug. **"Walk past Killa" is dead advice — he hunts across the whole map, including extracts.** Every Interchange card must assume contact. | ⏳ |
| 20 Aug | **Player will test a car extract and report the real rep number** — sources disagree *(+0.2 vs +0.4, ÷uses vs halving)*. **Pending.** | ⏳ |

---

## 📥 REQUESTS

> 🔔 **STANDING: remind the player to do their Fence scav daily, every single day.** They
> asked for this directly. It's now the first line of every raid card in `tarkov.md`.
>
> ✅ **Player confirms holding at least 2 Labs keycards.**
> 📋 **Player will test the car extract and report the real rep number.**

✅ **QUEUE EMPTY — all 11 requests delivered and merged into `tarkov.md`.**
*(Post new requests below this line.)*

---

## 📝 PROCESS — please add this going forward

### 🔄 NEW STANDING RULE — no more waiting for approval

**The player has changed the flow:** the assistant **reports the findings, then marks them
read and merges immediately** in the same turn. **Do not ask "shall I merge?"** — tell them
what it says, then merge it.

*(Original rule 3 said to wait for confirmation. That's superseded.)*

**Write a "WHAT CHANGED" block at the top of `tarkov.md` on every push.** Five lines, newest
first. The file is 2,500+ lines and the player reads it on a phone — they shouldn't have to
diff it to find the new material.

---

## ⚠️ PLAYER-CONFIRMED FACT — already written into `tarkov.md`

**🔴 INSURANCE DOES NOT WORK ON LABS.** Same as Icebreaker. Anything lost there is gone
permanently. ✅*player-confirmed*

---

## 🔬 RESULTS — researched, waiting to be read

*(empty — all delivered requests merged)*

---

## ✅ MERGED — read by the player and written into tarkov.md

| Date | Request | Where it landed |
|---|---|---|
| 2026-08-20 | **#11 Best barters** | `tarkov.md` → new **💱 Barters worth doing** section. **DO: GSh118 backpack (barter-only, biggest in game) · HK G28 for 1 Labs keycard (which they can craft ×3).** **SKIP: Medicine Case (HCP P5 gives one free) · Zabralo (they own the Zhuk) · KS-23M (on their hate list).** |
| 2026-08-20 | **#10 Hideout crafts** | `tarkov.md` → new **🏗 Hideout crafts — ranked** section above *Hideout*. 🥇 **Bundle of Wires ×8 at Workbench L1 — ₽74,470/hr AND it makes the 50 wires blocking their upgrades.** Moonshine / Bitcoin Farm / Int Center are the three to build around. Their existing gas-canister and CMS crafts confirmed as keepers. |
| 2026-08-20 | **#1 Full boss-killing guide** | `tarkov.md` → *Bosses* → **"How to actually kill them"**. Includes the 45–48 pen ceiling, the take-now / doable / wait split, and the level-36 unlock. **Player correction folded in: Kollontay's club jams your weapon.** |
| 2026-08-20 | **#9 Arena** | ✅ **Worth it.** Ref LL3 is **0.10 rep away** *(2nd AVS, Trooper TFO, Strandhogg)*, and `To Great Heights P3` opens **₽1M/day transfer** with zero gear risk. |
| 2026-08-20 | **#7 Fence rep / scav karma** | 🚨 **The biggest find so far.** Car extract **+0.2 first time per location**, co-op **+0.25**, vs the **+0.01** the player was farming. ~7 car extracts covers the whole 1.434 gap. Dying as a scav costs nothing. Scav dailies are available and switched off. |
| 2026-08-20 | **#6 Kord Breach** | 501 docs, 109 days, **~4.6/day vs a 15/day PvE cap** — achievable if started now. 8 doc types mapped. |
| 2026-08-20 | **#5 Labs keycards + keys** | ⭐ **Keycards are CRAFTABLE at Intelligence Center 2** — 2 items → 3 cards in 40 min. `Woods Keeper` may have already paid 3. Keys now break after 25–50 uses. |
| 2026-08-20 | **#4 The three tier lists** | Guns missing only 3 *(QBZ-191, Howa Type 20, NL545 GP)*. **Armor already at budget-meta or above.** Ammo is the only real gap — third confirmation. |
| 2026-08-20 | **#2 Top 5 loot runs** | `tarkov.md` → *Loot runs*. Full routes, keys, values, and the overlap table showing three of five are raids already scheduled. |

---

## 📋 SESSION LOG

**Newest first. One line per session so the other machine can see what changed.**

| Date | Session | What changed |
|---|---|---|
| 2026-08-20 | **phone** | 🔴 **Posted request #13 — KILLA'S 1.1 AGGRESSION, marked highest priority.** He left the mall and killed the player at the Emercom Checkpoint extract; Reddit reports increased aggression in 1.1. **Avoidance is not viable, so every Interchange card is affected.** Asks whether to simply defer Interchange to level 36. |
| 2026-08-20 | desktop | **REQUEST 11 DONE + MERGED — QUEUE NOW EMPTY.** Barters. **Do: GSh118 backpack** *(barter-only, no rouble price, biggest container in the game)* **and the HK G28 for one Labs keycard** — which they craft three at a time. **Skip: Medicine Case** *(HCP P5 hands one over free)*, **Zabralo** *(they own the Zhuk)*, **KS-23M** *(hate list)*. Principle recorded: **barter for what can't be bought, never for what a quest is about to give you.** |
| 2026-08-20 | desktop | **REQUEST 10 DONE + MERGED.** Hideout crafts ranked. **Best available to them right now: Bundle of Wires ×8 at Workbench L1 — ≈₽74,470/hr, and it double-dips because their hideout needs 50 wires.** Metric is profit/hour not profit. Moonshine, Bitcoin Farm and Intelligence Center are the three to build around *(Int Center also crafts the Labs keycards)*. Flagged that live prices couldn't be pulled — **tarkov.dev's API has been down all session.** |
| 2026-08-20 | **phone** | **Posted request #12** — best post-processing / visual settings, general baseline plus what to tune per map and for night raids. Community sources preferred; call out placebo. |
| 2026-08-20 | **phone** | 🔴 **FILE OWNERSHIP SPLIT.** Phone writes `RESEARCH.md` only; desktop owns all writes to `tarkov.md`. Caused by a concurrent Arena merge that duplicated a block and silently deleted a standing rule. Added a **PLAYER FACTS** table for desktop to merge. **Desktop: check for duplicates from requests 1/2/4/5/6/7/9, which the phone already merged.** |
| 2026-08-20 | desktop | **REQUEST 9 DONE → RESULTS.** Arena verdict: **YES, for two reasons.** (1) **Ref LL3 is 0.10 rep away** and holds a second AVS, HighCom TFO and Strandhogg — their armor research already found that. (2) **The transfer pipe: ₽1,000,000/day from Arena to the main game at a 15% fee, with zero gear risk** — more than the best loot run in the game. **Gated behind `To Great Heights! – Part 3`.** Verdict: worth it as a parallel income stream, not worth dropping questing for. |
| 2026-08-20 | desktop | **REQUEST 8 DONE → RESULTS.** Quest tree. 🏆 **Found why goal #2 is 3.0: Kappa requires Scav karma +3** — the file had the target without the reason. **Full Kappa gate: karma +3 · LL4 with SEVEN traders · the four ⭐Kappa quests.** The seven LL4s are the real wall — **level 42 minimum**, with **Jaeger rep (2.55/7.30) and Ragman rep (3.35/6.50) as the true bottlenecks.** Active chains mapped *(HCP P5 branches to Decontamination Service AND P6; Sew it Good **P2** is the Kappa gate, not P1)*. ⚠️ **Correction: Network Provider P1 is NOT obtainable in any game mode right now** — I was wrong last check. |
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

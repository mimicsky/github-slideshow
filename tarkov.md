# Tarkov Co-Pilot

**You play. I track.** Quests, stash, and keep/sell calls.

## 🆕 WHAT CHANGED — newest first

*(Five lines max. This file is 2,500+ lines and gets read on a phone — the new stuff lives
here so you never have to diff it.)*

1. **20 Aug ·** 💱 **BARTERS: get the GSh118 backpack** *(barter-only, biggest in the game)* **and the HK G28 for one Labs keycard** — you craft those. **Skip the Medicine Case, HCP P5 gives you one.** *(→ Barters section)*
2. **20 Aug ·** 🏗 **BEST CRAFT: Bundle of Wires ×8 at Workbench L1 — ≈₽74,470/hr**, and it produces the **50 wires** your hideout upgrades need. *(→ Hideout crafts section)*
3. **20 Aug ·** 🏟 **ARENA VERDICT: worth it.** **Ref LL3 is 0.10 rep away** *(AVS, HighCom TFO, Strandhogg behind it)*, and after `To Great Heights! – Part 3` Ref opens a **₽1M/day Arena→main transfer with zero gear risk.** *(→ Kappa section)*
4. **20 Aug ·** ⚔️ **META CHECK — you already own most of the S-tier** *(Mutant, DVL-10,
   RPK-16 ×2, AUG, 5-7)*. **Only real gap: the 7.62x51 MDR.** Every source says **ammo
   matters more than the gun**, and **1.0.4.5 decoupled recoil from handguards — stop
   paying for them.** *(→ `RESEARCH.md` RESULTS)*
5. **20 Aug ·** ⭐ **BOSS KILL GUIDE + LOOT RUNS MERGED.** Key finds: **Kaban is takeable
   now** *(his guards have no helmets)* · **Glukhar is softer than his own guards** ·
   **Kollontay's club JAMS YOUR GUN** ✅*player* · **you're capped at 45–48 pen until level
   36**, which is the unlock that changes everything.

> **PvE · Patch 1.1.0.1.46699 · Unheard · Level 30 · USEC · Stash 4 · ~₽3.2M**

## Starting a fresh chat?

**This file now lives in git** — `mimicsky/github-slideshow`, branch
`claude/tarkov-desktop-helper-3b88yo`. Point a session at that folder, or paste the whole
file in. Either way: **everything is here. Nothing important lives in chat history.**

**Two standing rules:**

1. **Nothing is done unless you say so.** Never guess from a progress bar.
2. **The player's in-game text beats every source.** It has been right every single time
   the two disagreed — a dozen-plus corrections are logged in *Confirmed objectives*.

### What this file contains

| Section | |
|---|---|
| **Quest format** · **How quests are shaped** | the 🔍/✓ rule and the four quest types |
| **Chemical Part 4** | the decision — settled, take Skier's |
| **Confirmed objectives** | ground truth from the player's screen. **Beats everything.** |
| **Next raid** · **Quests by map** | the card, and all ~100 active quests |
| **Bosses · Kappa · Character · Fence rep · Insurance · Skills · Goals** | state and targets |
| **Hideout** | paused — see the note for why |
| **Keep or sell · Stash rules · Hard lessons** | including the Killa and REAP-IR lessons |
| **How this works** | the working model — player supplies facts, assistant does bookkeeping |
| **🎒 Kit builder** | 4 modes, weight matrix, full gun rankings, ammo doctrine |
| **🎲 Curveballs** | 11 raid types, to stop the burnout that killed last wipe |
| **What I can and can't do** | capability limits and the error log that produced them |
| **Moving to desktop** · **`begin research`** | setup and the standing research protocol |
| **The plan** · **Research queue** | what's done, what's next |
| **✅ Complete** | every finished quest, kept for the prestige run |

### Where things stand

**Level 30 · ₽3.2M · ~100 active quests · 4 of 11 bosses · hideout ~400 items short**

**Next:** the hideout tally rebuild, then desktop setup, then `begin research`.

---

# Quest format

Every quest is written the same way:

```
Quest name · Map
what you're doing, in one line
🔍 LOOK UP  or  ✓ NOTHING TO LOOK UP
🔑 key or item to bring, if any
```

**The tag answers one question: do you need a map for this?**

**✓ JUST GO DO IT** — the quest already told you everything.
> *"Kill 15 scavs with an AKM."* You know what an AKM is. You know what a scav is. Go.

**🔍 LOOK IT UP** — the quest points at one specific spot and never says where it is.
> *"Find the logistics office."* Where's the logistics office? Exactly. That's a lookup.

About a third of your board is ✓. **Those are the ones you've been opening Fandom for and
didn't need to.**

**Types:**

| | |
|---|---|
| **FIGHT** | Kill things. Your favourite — always listed first. |
| **FIND** | Locate a place, or grab an item and bring it out. |
| **CHORE** | Plant a marker, stash an item, survive and extract from a spot. |
| **BUSY WORK** | Tedious. Long collections, expensive buys, grinding counts. |
| **?** | I don't know it yet. Look it up on Fandom or send me the text. |

**Fandom is blocked for me but works fine for you.** When a quest is complicated and I
don't have confirmed details, I'll say **(look up on fandom)** rather than guess.

**The in-game quest screen tells you the type directly** — the icon in the Type column:

| Icon | Means | My type |
|---|---|---|
| 🎯 crosshair | Elimination | **FIGHT** |
| 🔍 magnifier | Search / locate | **FIND** |
| ✋ hand | Pick up or hand over | **FIND / CHORE** |

The **Location** column is authoritative too — it's already corrected several map
assignments I had wrong.

> ❓ **The Class column (I / II / III) is probably the trader loyalty level** the quest
> sits behind — that's your read, unconfirmed. The boxed vs unboxed styling may just be
> whether you already meet it. **Confirm next time a quest shows up that you can't take
> yet.**

---

# How quests are shaped

### Chains — Part 1, Part 2, Part 3…

Can't start Part 2 until Part 1 is handed in. Parts often sit on different maps and each
part has its own rules.

### One quest, pieces on several maps

Like `Informed Means Armed` — a camera on Woods, a camera on Interchange. **Do these
across separate raids, weeks apart.** No pressure, just trip planning.

### Transit quests — two maps, one raid

You take the transit *instead of extracting*.

- Play the first map as long as you want, transit with a few minutes left.
- **You arrive with a fresh timer.** Second map is a full raid.
- **You can send normal items to your stash at the transit** — guns, armor, junk, hideout
  parts. Anything that takes inventory space.
- **You CANNOT send quest items.** They ride with you and you must extract to keep them.

**The real cost is that you arrive with used gear.** Ammo spent, meds used, grenades gone,
and after a long first leg your **food and water are empty**. No restocking from the
hideout between legs.

> **How bad this is depends on how long the first leg runs.** A short first leg costs you
> almost nothing. A full 30 minutes on the first map and you land on the second one empty.
> **Pack for both legs whenever the first leg is going to be long.**
>
> **Use the stash send at the transit** — dump the first map's loot so you arrive with a
> clean bag and free slots.

### "Do it in one raid" quests

Some need everything in a single raid and you must extract alive or it resets. Others you
can mark and leave, or spread over several raids, and dying doesn't matter.

**It varies per quest with no pattern. Read the in-game text every time.**

### Two more things that bite

- **Found-in-raid.** Handover items must be found in raid — you can't buy your way out.
- **Mutually exclusive quests.** Finishing one kills the other. Already cost you
  `One Less Loose End`. **Before finishing anything that reads like picking a side, check
  what it locks out.**
- **🔴 Kill counts only tick while the quest is active.** Killing a boss before you have
  its quest is wasted — you'll have to kill it again. **Items are the exception:** loot
  taken out of a raid keeps found-in-raid status in your stash and still counts later.
  *(This is why `Huntsman Path – Trophy` only needed the Reshala kill — the TT was already
  handed in.)*

---

# ⚖️ The Chemical Part 4 choice — decide before you touch any of them

Parts 1–3 are done. Part 4 is a three-way pick and **any of the three counts for Kappa.**
All three are mutually exclusive.

| Branch | Rewards |
|---|---|
| **Skier** — `Chemical - Part 4` | key case *(own 1)* · mag case *(own 2, cheap)* · **2× Labs keycard** |
| **Therapist** — `Out of Curiosity` | med case *(own 1)* + documents case |
| **Prapor** — `Big Customer` | ammo case *(own 2, cheap)* · grenade case |

**📍 `Chemical - Part 4` is on CUSTOMS** ✅*verified from the quest screen*

## Take Skier's `Chemical - Part 4`

**✅ You already own the documents case**, so the Therapist branch now offers **nothing you
don't have** — its only unique reward is redundant. That settles it beyond argument.

**Two Labs keycards are ₽400–600k**, and Labs access also feeds `Drip Out - Part 1`
(100 Raider kills).

> ⚠️ **Do not finish `Out of Curiosity` or `Big Customer`.** Either kills this.

---

# CONFIRMED OBJECTIVES — from your screen

No public site is current for 1.1. Your game is the only accurate source. **Anything here
beats anything I look up.**

| Quest | Confirmed | What sites got wrong |
|---|---|---|
| `Angry Watchman` | **3** PMCs, **only Dorms-zone kills count** | said 5 |
| `Capturing Outposts` | **12** PMCs, and on Shoreline **only kills at the Health Resort count** — smugglers'-base kills do nothing | said 8 |
| `Job for a Patriot` | **Prapor gives you the built AK-12** *(suppressor + PS-320 included)*. **Streets · Shoreline · Ground Zero only** — not any location, and **not Interchange**. | sources say you buy the parts and list Lighthouse/Customs/Reserve — wrong on both |
| `Supplements` | chemical vial + **4 respirators** | undocumented |
| `I Need More Power` | 2 rooms, **one raid, must extract** | matched |
| `Anesthesia` | 3 trading posts, must extract | matched |
| `A Fuel Matter` | 2 fuel tank groups | matched |
| `All This Filth` | kill Scavs anywhere | wiki says "kill Shturman 20×" — wrong |
| `The Courier` | **1** REAP-IR, **quest gives it to you**, fits in pockets, **can NOT go in a secure container** | said 2, bought, and got the container part wrong |
| `The Punisher - Part 2` | **15 Scavs with an AKM series weapon, on Shoreline** | this file said "12 suppressed + 10 lower half masks" — completely wrong |
| `Thirsty - Hounds` | **12 Scavs between 22:00–07:00 on Shoreline** — night only | matched |
| `The Punisher - Part 3` | **Reserve.** 12 Scavs with **9x39 caliber** weapons · **7 Lower half-masks found in raid** · hand over | every source said Customs, 25 Scavs, AKS-74U, DVL-10 reward — **wrong on all four** |
| `Needle in a Haystack` | **6 investigate spots, not 4.** Ground Zero courtyard park by TerraGroup HQ ✅ · Shoreline coast-side construction ✅ · Shoreline playground by the Health Resort ✅ · **Interchange kart track** · **Interchange indoor children's playground** · **Streets playground by Concordia** | sources listed 4 maps and missed the Interchange kart track entirely |
| `Weapons Circulation` | **3 cultist ritual spots, MS2000.** Shoreline ✅ · **2 on Woods** | matched |
| `No Swiping` | **10 kills** in the smugglers' base area | the old version of this file said 25 — **web sources were right for once** |
| `Wet Job - Part 2` | mark the fishing table — **no survive-and-extract needed** | — |
| `Health Care Privacy - Part 4` | **Gain Fatigue by exhausting leg stamina, hold it 8 minutes** · **₽320,787 + 28,000 EXP + 3 aluminum splints** | ⚠️ **CONFLICT — Fandom says "Reach Health skill level 4" and lists ₽29,000 + 2 Grizzly + saline.** Wrong objective *and* wrong rewards by 10×. **First time a directly-read Fandom page has been wrong — it's stale for 1.1** |
| `The Key to Success` | **Book 1** — МУЗЕЙ ИСТОРИИ, 2F south end, pile of books on the floor at the back · **Book 2** — "Books" store, 1F next to TTS, yellow book on the lowest stocked row | **matched.** First desktop lookup — read off the real Fandom page and its annotated Ultra maps, player confirmed both on sight |
| `Wet Job - Part 3` | **MARK Artyom's car with an MS2000** — not just locate it | sources say "locate", which cost a raid |
| `Health Care Privacy - Part 2` | needs the **Health Resort west wing 306** key | no source mentions a key at all |
| `Every Hunter Knows This` | Factory breach room + Customs 3-story dorm stairs | — |
| `Informed Means Armed` | **2 cameras only** — Woods + Interchange | lists a third on Customs |
| `Black Swan` | **1** heat exchanger | said 3 |
| **Reshala spawns** | Dorms 3-story · New Gas · Fortress | also claim Warehouse 4 — wrong |

**Renamed in 1.1:** `Angry Watchman` was `Evil Watchman` · `Chemical Experiments` was
`Spa Tour - Part 7`

**Level gates on guide sites are wrong** — they list Private Club at 24 and The Courier at
52; both were active for you at 21.

---

# 🔔 STANDING RULE — START EVERY CARD WITH THIS

> ## **"Fence daily done today?"**
>
> **Ask it every single time, before anything else on the card.** The player asked directly
> to be reminded every day.
>
> **Why it matters:** scav dailies pay **+0.01–0.05 each**, they're **available right now**
> via the Intelligence Center, and **Fence rep is goal #2 and the furthest gap on the
> board.** It costs one line and it's free rep they'd otherwise skip.
>
> ⚠️ **This rule has already been lost once in a merge. If it goes missing, put it back.**

---

# ▶ NEXT RAID — Interchange · 2 left

> ## 🔴 SHOULD INTERCHANGE BE DEFERRED TO LEVEL 36? — **SPLIT IT, DON'T DEFER IT ALL**
>
> **The two remaining objectives have completely different risk profiles:**
>
> | Objective | Lost on death? | Verdict |
> |---|---|---|
> | **`Supervisor`** — Goshan→BIZARRO fitting rooms · OLI→Registers #7-8 | ❌ **NO — stashing completes it on placement** | ✅ **GO NOW, cheap kit** |
> | **`The Key to Success`** — the 2 books | ✅ **YES — quest items, lost if you don't extract** | ⏳ **DEFER** |
>
> ### ✅ Do `Supervisor` now, in a kit you don't mind losing
> **The drops are permanent the moment you place them.** Killa can kill you *afterwards* and
> you keep the progress. **That makes it nearly risk-free even at 75% spawn** — the only
> thing you lose is a cheap kit. **Two drops, both in the big anchor stores, then leave.**
>
> ### ⏳ Defer the books
> **They're the only thing he can actually take from you.** Two failed attempts already.
> **Come back for them at 32+**, when `Sellout` makes the fight pay, and ideally at **36**
> when **5.45 BS (54 pen)** finally cracks his class 6 face shield.
>
> ### 🎯 The level-36 Interchange trip is the real plan
> At 36 you arrive able to **kill him for quest credit**, with **BS ammo**, and you run the
> **tech circuit (₽500k–1M)** on the same raid. **Books, Sellout, and the best money run in
> the game in one trip.** That's worth waiting for. **The two key drops are not.**

`Fuel Crisis` and `Pathfinder` done. **No markers needed any more.**

## 🛒 Bring
**Goshan + IDEA + OLI cash register keys** *(all flea-buyable, cheap)*
~~**#21WS keycard**~~ — ✅ `Irresistible` done

## ✓ Just go do it
| Quest | What |
|---|---|
| ~~**Long Line**~~ | ✅ **DONE** — 4 PMCs killed. Banked even though the raid ended in a death; **no extract required** |

## 🔍 Look these up
| Quest | What you're finding |
|---|---|
| **Supervisor** **1/3** | ✅ ~~IDEA → Register #9~~ **DONE** · **Goshan → BIZARRO fitting rooms** · **OLI → Registers #7-8** ✅*player-confirmed* |
| **The Key to Success** ✅ | **Book 1** — МУЗЕЙ ИСТОРИИ *(2F, south end, past ЛАДУШКА)* — **pile of books on the floor at the back**, left of the red partition. **Book 2** — "Books" store *(1F, north side, next to TTS)* — **yellow book on the lowest row that has books**, shelf against the green pillar. ✅*player-confirmed* |
| ~~**Needle in a Haystack**~~ | ✅ **Interchange spots DONE** — kart track + indoor playground. **Quest still open: Streets playground by Concordia** |
| ~~**Irresistible**~~ 🔑 | ✅ **DONE.** Outside, **south car park** off OLI's SW corner — **never enter the mall for this one.** ⚠️ **The wiki omits a step: you must TURN THE POWER ON FIRST**, then unlock the crate, get in, and extract with it. ✅*player-confirmed — tedious but no Killa exposure* |

## 🎒 Kit
**Small map, mixed raid** → light-medium. Interchange interior is close-quarters but
you'll cover ground between the garages and Ultra.

**Ammo: AA** — `Long Line` is PMCs, the rest is errands.
**1 primary + 4–5 mags.** Ammo choice yours as always.

## 👹 KILLA IS NOT AVOIDABLE ON THIS RAID — corrected

❌ ~~"Walk past Killa."~~ **Wrong, and the player said so.** *"You can't just walk past any
boss if you're in their area."*

**His patrol route is literally the objective list** ⚠️*web-sourced*:
> *"In the **IDEA, OLI and Goshan** stores... around the **center stores on the first and
> second floor** of the ULTRA shopping mall."*

That's **all three `Supervisor` key drops** and **both `Key to Success` books.** Every
remaining objective is inside his zone. **Plan the raid as a fight, not a chore.**

| Killa | |
|---|---|
| **Health** | **890** — head 70 · thorax 210 · stomach 170 · legs **120** each |
| **Armor** | 6B13 M Killa Edition — class 3 soft, **Granit 4 class 5 plates** front/back |
| **Weapons** | **RPK-16** *(95-rd drum)* · AKMS 7.62x39 · suppressed Vityaz · Deagle · TT |
| **Grenades** | **F-1 · RGD-5 · smoke** — he throws them, and he uses smoke to push |
| **Behavior** | suppresses, zig-zags cover to cover, **follows you a long way once locked on** |

**How he dies** ⚠️*web-sourced*: **high-pen ammo — 5.45 BS · 5.56 M995 · 7.62x51.** Failing
that, **shred his armor durability** or **shoot his legs** *(120 HP each, unarmored)*.
**Grenades won't kill him** — too mobile to pin.

## 👹👹 AND TAGILLA IS ON INTERCHANGE TOO

**Spawn odds — PvE, player-supplied:** ✅*player-confirmed*
| Boss | Interchange spawn |
|---|---|
| **Killa** | **75%** |
| **Tagilla** | **50%** |

**Three raids in four have Killa. One in two has both.**

> ✅ **The good news: Tagilla IS avoidable.** ⚠️*web-sourced* — on Interchange he sits
> **in the parking garage below the Goshan store**, and that's it. He does not roam the
> mall. **None of your four remaining objectives are down there.**
> **Stay out of the Goshan garage and he never happens.** *(Killa is the opposite — the
> mall interior is his.)*

| Tagilla | |
|---|---|
| **Health** | **1220** — head 100 · thorax **320** · stomach 260 · legs 140 each |
| **Weapons** | **all 12ga** — Saiga-12K · Saiga-12K ver.10 · **AA-12 Gen 1 / Gen 2** |
| **Melee** | Dead Blow Hammer — **unlootable, and it one-shots.** Never let him close |
| **Where** | Interchange: **Goshan parking garage only** · Factory: everywhere |
| **Quests** | `Huntsman Path - Factory Chief` **and** `Relentless` |

**Fighting him:** 1220 HP is a lot of AP. His shotguns are **short-range** — buckshot does
little against class 5–6 plates, so **distance beats him** and closing distance kills you.

> 😤 **PLAYER STANDING ORDER: the player hates Killa.** ✅*player-stated, 19 Aug 2026*
> Three kits taken, the last one **a long walk outside the mall, near EMERCOM, out of
> nowhere.** Treat him as a personal grudge in the tone of this file. **He is not a
> "walk past" any more — he is a problem to be solved**, and the moment `Sellout` opens at
> **level 32**, he becomes a payday instead of a mugging.

### 🔬 WHY HE BEHAVES LIKE THIS IN 1.1 — researched ⚠️*web-sourced*

**Community claim:** Killa is *"far more aggressive in 1.1"* — possibly a bug.
**What research actually found: it's most likely INTENDED, not broken.**

There is a documented **2026 AI overhaul** across all bosses ⚠️*web-sourced*:

> **"Boss awareness expands with sound and line of sight; once triggered they reposition
> rather than anchor."** Bosses now *"use aggression, flanking and suppression"* instead of
> holding a fixed patrol.

**That is exactly what happened to you** — you fired, his awareness expanded to include you,
and he **repositioned rather than anchoring**, all the way to the EMERCOM checkpoint.

> 🔴 **CONCLUSION: "avoid his area" is dead as a concept, not just for Killa but for every
> boss.** The old model — bosses sit in a zone you can route around — **no longer applies.**
> Plan for pursuit, and treat your first shot as the thing that starts the fight.

⚠️ **One alternative aim point surfaced:** some guides now say **aim for the neck** on Killa.
**Your own thorax rule is player-confirmed and stays primary** — but if you get a clean look
at his neck, it bypasses both the class 6 face shield and the class 5 chest plates.

### ⚠️ KILLA'S ZONE IS THE WHOLE MAP — player-confirmed the hard way

**He does not stay in the mall.** ✅*player-confirmed* — he pursued to the **EMERCOM
checkpoint, outside**, and killed the player yards from extract, mid-heal, after a 3-PMC
fight. The wiki agrees: *"he will follow his target large distances out of his patrol
route."*

**So the Interchange rule is not "avoid his floor" — it's:**
1. **Assume he is coming, from the moment you fire a shot.** Gunfire is what brings him.
2. **Never heal in the open.** Break line of sight, move, *then* heal.
3. **Don't take the trade without AP and cover you got to first.** Thorax is the right aim
   point *(legs are player-confirmed useless on him)* — but the right aim point loses
   anyway if he sees you first.
4. **The extract is not safe.** Yards from EMERCOM is where this death happened.

> ⭐ **THE STRATEGIC POINT: you are being forced to fight Killa for free.**
> `Sellout` and `Relentless` *(both Jaeger, Huntsman Path)* each need **one Killa kill**.
> He's unavoidable on every Interchange raid — so **unlocking `Sellout` before the next
> Interchange trip converts a fight you can't dodge into quest progress.**
> ✅ **ANSWERED — `Sellout` needs LEVEL 32. You are 30.** ⚠️*web-sourced*

### 🏹 THE JAEGER HUNTSMAN PATH — what gates the boss quests

| Quest | Gate | Objectives |
|---|---|---|
| **Sellout** | **level 32 — 2 levels away** 🔥 | Kill **Killa** + find his **Maska-1SCh helmet** in raid + hand over |
| **Factory Chief** | **no level requirement listed** — check if it's already available | Kill **Tagilla** + find a **BOSS cap** in raid + hand over |
| **Forest Cleaning** | ❌ **NOT on the player's board** ✅*player-confirmed* — so either already completed, or gated behind something the wiki doesn't list *(it claims only Jaeger LL3, which the player has)* | 50 Scavs, any map |
| **Relentless** | **Jaeger LL4** *(lvl 33 + rep 7.30; you're at 2.55)* | Kill **Tagilla · Killa · Reshala · Shturman · Glukhar · Sanitar — all in ONE life, then extract** |
| ~~Woods Keeper~~ | ✅ **DONE** | Shturman + stash key ✅ — **F1 grenade worked on him** |
| ~~Trophy~~ | ✅ **DONE** ✅*player-confirmed* | Reshala + Golden TT |
| **Controller** 🆕 | **ACTIVE** ✅*player* | **Kill 2 PMCs while they have the STUN status** — i.e. **flashbang them with a Zarya, then shoot them.** Any location. Pays a **3-9x42 scope + M80 ammo + unlocks the M700 AICS** · next task rewards the **Dorm room 314 marked key** |

> ⚠️ **STATUS OF THE REST IS UNVERIFIED.** `Factory Chief` and `Sellout` were listed above
> from **wiki data, not from the player's board** — the assistant does not know whether
> they're active, locked or already done. **Don't plan around them until the player says.**
> *(`Forest Cleaning` is the cautionary example: the wiki said it should be available, and
> it isn't on the board at all.)*

> 🔥 **Two levels from now, every Killa kill starts paying.** At **32**, `Sellout` opens and
> the 75%-spawn boss you can't avoid becomes quest progress — **but the helmet must be
> found in raid, so you have to kill him *and* loot the Maska.**
>
> ⚠️ **Don't chase `Relentless`.** Six bosses in a single life *and* Jaeger LL4, which needs
> **rep 7.30 against your 2.55.** That's a long-term goal, not a plan.
>
> ✅ **`Forest Cleaning` is free progress** — 50 scavs anywhere, and Jaeger rep is exactly
> what `Relentless` is short on. **Check whether it's active.**

## 🎒 Hideout grabs
🔌 **Wires (50) · power cord (20)** · ⚡ **relay · spark plug · CPU fan · corrugated hose**
· 🥇 **gold** · 🍺 **drinks** · 💻 **GPUs**

---

# ▶ RUN B — Customs into Factory

Separate raid. Both transits leave from Customs so they can't be combined.

**Secrets of Polikhim** · Customs → Factory · FIND
(grab the precision tools package in the med lab, transit to factory, extract with it)

⚠️ **You don't have the package yet.** And it's a quest item, so you **can't** send it to
your stash at the transit — it rides through Factory with you. Same setup that cost you
the REAP-IR.

While you're there, chip at `One-Way Ticket`.

---

# QUESTS BY MAP — full board, ~100 active

**Transcribed from the player's quest screen.** Class = trader loyalty level. Type icon:
🎯 elimination · 🔍 search · ✋ pickup/handover · ⭐ unknown icon.

> ⚠️ **"Any location" in the Location column means "not tied to one map" — NOT "works
> anywhere."** Confirmed: `Job for a Patriot` shows Any but is Streets/Shoreline/Ground
> Zero only. `Supervisor` shows Any but is Interchange. `Chumming` shows Any but is Woods
> + Customs. **Always read the objectives, never the column.**

---

## 🏭 CUSTOMS — 5

| Quest | Class | Type | |
|---|---|---|---|
| **The Huntsman Path – Angry Watchman** **1/3** | I | ✋ | ✓ 3 PMCs, **Dorms zone only** |
| **The Courier** | I | ⭐ | 🔍 quest supplies a REAP-IR · **can't go in a container** · one was lost MIA |
| **Chemical – Part 4** ⭐*Kappa* | III | ✋ | 🔍 **the Skier branch — see the decision section** |
| ~~Big Customer~~ | III | ✋ | 🚫 **NEVER COMPLETE** — kills Chemical P4 |
| ~~Out of Curiosity~~ | III | ✋ | 🚫 **NEVER COMPLETE** — kills Chemical P4 |

## 🌲 WOODS — 12

| Quest | Class | Type | |
|---|---|---|---|
| ~~**Gratitude**~~ | I | ✋ | ✅ **DONE** |
| ~~**Small Things, Big Help**~~ | I | ✋ | ✅ **DONE** |
| ~~**Informed Means Armed**~~ | I | ✋ | ✅ **DONE** — sawmill dock camera completed it |
| ~~**The Survivalist Path – Tough Guy**~~ | III | ✋ | ✅ **DONE** |
| ~~**Health Care Privacy – Part 3**~~ | III | 🔍 | ✅ **DONE** |
| ~~**Health Care Privacy – Part 4**~~ | III | 💡 | ✅ **DONE** — ₽320,787 banked |
| ~~**The Huntsman Path – Woods Keeper**~~ | I | ✋ | ✅ **DONE** — Shturman killed **with an F1 grenade**, stash key looted ✅*player-confirmed* |
| **Hiking** **40%** | I | 🎯 | ✓ **10 Scavs at: USEC camp · Scav camp · sawmill · abandoned village** *(those four zones only)* |
| ~~**Swift**~~ | I | 🎯 | ✅ **DONE** — 15 PMCs killed with no armor |
| ~~**Steady Signal**~~ | I | 🔍 | ✅ **DONE** |
| ~~**Metal Birds**~~ | I | ✋ | ✅ **DONE** |
| ~~**The Survivalist Path – Thrifty**~~ | III | ✋ | ✅ **DONE** — both bunkers stocked |
| **Shipping Delay – Part 1** | III | ✋ | ✓ **Prapor's package — 1 of 2 spots in the NW building of the train depot.** 🚌 **Depot is ONLY reachable via the BTR Driver's taxi** |
| **A Helping Hand** | III | 🔍 | ✓ **Same package, same depot** — but requires **Shipping Delay P1 completed first** + survive & extract |

*Also here: `Weapons Circulation` 2 ritual spots · `Chumming` · `Thirsty – Delivery`
(Scav bunker with the radio tower) · `Special Comms` (Bulbex cutter at the RUAF boulder).*

> 🃏 **`Swift` IS THE HOBO STREAK QUEST.** 15 PMCs with **no armor, no rig armor, no helmet,
> no face cover** — that is the **Thunderbolt kit** *(0.62 kg, 16 slots, zero armor)*, which
> the file already defines as the hobo loadout. **The burnout-prevention curveball and a
> real quest are the same activity.** Run it when the quest grind gets heavy — it's the one
> objective where dying cheap costs nothing.
>
> 🚌 **`Shipping Delay P1` and `A Helping Hand` both gate on the BTR Driver's taxi** — the
> train depot has no walking route. **They're the same package in the same NW depot
> building, so P1 must be finished before A Helping Hand's copy can be collected.**
>
> ## 🔥 WOODS IS A 20-QUEST MAP — ✅*player-confirmed from the in-game task filter*
>
> **12 Woods-tagged + 8 "Any location" that count here.** It is the densest map on the
> board, and several of the Any-location ones are **already part-finished**, so a properly
> loaded Woods raid chips a dozen quests at once:
>
> | Any-location quest | Progress | What Woods gives it |
> |---|---|---|
> | **Capturing Outposts** | **58%** | **PMC kills count here** |
> | **Informed Means Armed** | **50%** | the **last** camera — sawmill dock ✅ finishes it |
> | **Chumming** | **50%** | golden neck chains |
> | **Weapons Circulation** | **33%** | **2 ritual spots**, both on Woods |
> | **Is This a Reference?** | **14%** | a WI-FI camera counts here |
> | **Thirsty – Delivery** | 0% | propane tanks |
> | **Rough Tarkov** | 0% | Woods half of Woods + Ground Zero |
> | **Tough Guy** | 0% | **3 Scavs in one raid, carrying NO medicine at all** |
>
> ### 🛒 THE FULL WOODS LOADOUT — bring all of this or you waste the trip
> - **MS2000 × 3+** — 1 `Steady Signal` · **2 `Weapons Circulation`** *(3 more supplied by
>   `Small Things`)*
> - **WI-FI Camera × 2** — `Informed Means Armed` *(sawmill dock)* + `Is This a Reference?`
> - **2× Iskra ration pack · 2× 0.6L water** — `Thrifty`, split across ZB-016 and ZB-014
> - **Propane tanks × 2** — `Thirsty – Delivery`
> - **Shemagh + RayBench sunglasses** — `Gratitude` *(quest supplies both)*
> - ⚠️ **`Tough Guy` means NO meds in the entire kit** — run it as its own raid, or accept
>   you can't heal.

## 🏖 SHORELINE — 1

| Quest | Class | Type | |
|---|---|---|---|
| **Wet Job – Part 4** | III | ✋ | 🔍 **list of Health Resort tenants — administration office** ✅*verified* |

**Reward:** $2,215 · 7.62x51 M80A1 + 5× 20-round packs · M67 grenade · 28,000 EXP.
**Next in the chain pays a Remington R11 RSASS + an FN40GL Mk2** — ✅ **the RSASS is a keep**,
it's on the *I'll use* list.

*Plus `Capturing Outposts` **7/12** (Health Resort only) and **Sanitar**, still unspawned.*

## 🛍 INTERCHANGE — 3

| Quest | Class | Type | |
|---|---|---|---|
| ~~**Long Line**~~ | I | 🎯 | ✅ **DONE** — 4 PMCs |
| **The Key to Success** | II | ✋ | ✓ 2 design books — МУЗЕЙ ИСТОРИИ **2F** *(floor pile at the back)* · "Books" store **1F** by TTS *(yellow book, lowest stocked row)* ✅*player-confirmed* |
| ~~**Irresistible**~~ | III | 🔍 | ✅ **DONE** — outside, south car park · power on first |

*Plus `Supervisor` — 3 cash register keys: Goshan → BIZARRO fitting rooms · IDEA →
Register #9 · OLI → Registers #7-8.*
**👹 Killa** — `Sellout` not unlocked, so the kill is worthless right now.

## 🏰 RESERVE — 13

| Quest | Class | Type | |
|---|---|---|---|
| **The Punisher – Part 3** | III | 🎯 | ✓ **12 Scavs w/ 9x39** + 7 lower half-masks FiR · 🔫 **buy an AS VAL** |
| **A Fuel Matter** | III | ✋ | 🔍 mark 2 fuel tank groups · survive & extract |
| **Reserve** | III | ✋ | ✓ **NW underground warehouse marked "Д"** — down a ramp, **right-side food storage cages** *(wooden crates inside)*. **Survive & extract** |
| **Safe Corridor** | III | 🎯 | ✓ **10 Scavs in that same "Д" warehouse** + its ramps |
| **Documents** | III | ✋ | ✓ **3 military folders — command part of the underground bunker** |
| **No Place for Renegades** | III | 🎯 | ✓ **5 Raiders in the command bunker.** Spawn at raid start, **more after the D-2 switch** |
| **Back Door** | III | ✋ | ✓ **Extract via D-2.** Power lever is in the **command part of the bunker** *(can spawn Raiders)* |
| **Classified Technologies** | III | ✋ | ✓ **Behind the dismantled rusty pipe in the underground workshop you pass through to reach D-2** → Peacekeeper |
| **The Bunker** | III | ✋ | ✓ **Control room = centre of the bunker**, any staircase · then hermetic doors to **hospital (White Bishop)** + **academy** |
| **Disease History** | III | ✋ | ✓ **2 locked rooms, 2nd floor of the hospital (White Bishop)** |
| **Surplus Goods** | III | 🔍 | ✓ **Locked room in the bigger of the two garages at the repair centre (White Knight)** · 🔑 **RB-ST key** |
| **Revision – Reserve** | III | ✋ | ✓ **4× BMP-2, mark with MS2000** — one needs 🔑 **RB-ST** |
| **Demonstration Model** | III | 🎯 | 🔍 *no wiki page found under that name — re-check spelling in game* |

**👹 Glukhar.** *Also `Drip Out – Part 1` (100 Raiders) and `Special Comms` arrives here.*

> ⭐ **RESERVE IS ONE RAID, NOT THIRTEEN — the D-2 chain.**
> **Everything underground links through the same run:**
> **1.** Enter the bunker → **`The Bunker`** control room *(centre, any staircase)*
> **2.** **`Documents`** — 3 folders in the command part
> **3.** **Throw the D-2 power lever** *(command part)* — **this spawns Raiders**
> **4.** **`No Place for Renegades`** — kill 5 of the Raiders you just spawned ✅
> …and the same Raiders feed **`Drip Out – Part 1`** *(100 Raiders)*
> **5.** Head for D-2 → grab **`Classified Technologies`** off the rusty pipe in the
> workshop **on the way**
> **6.** **Extract through D-2 → `Back Door` ✅** *(and it extracts the folders + package)*
>
> **That is 5–6 quests in a single underground run, and the quest that spawns the enemies
> is the quest that needs them killed.**
>
> **Separate surface trip:** `Reserve` + `Safe Corridor` share the **"Д" warehouse** *(NW,
> underground storage — do both at once)*; `Disease History` + `The Bunker`'s hermetic door
> share **White Bishop**; `Surplus Goods` + one BMP share the **RB-ST key**.
>
> 🛒 **Bring: 6× MS2000** *(4 BMPs + 2 fuel tank groups)* **· RB-ST key.**

## 🗼 LIGHTHOUSE — 10

| Quest | Class | Type | |
|---|---|---|---|
✅ **RESEARCHED — all 10 located.** ⚠️*web-sourced, unverified*

| Quest | Where | Bring |
|---|---|---|
| **Revision – Lighthouse** **50%** | **4 vehicles: 2 BRDMs + 2 Strykers.** Both BRDMs at the **water treatment plant** *(west basin + north)* | **4× MS2000** |
| **Easy Job** | Helicopter **in one of the basins, water treatment plant (north)** · then **kill 10** Rogues/Scavs/PMCs **in that area** | **MS2000** |
| **Corporate Secrets** | **Two different buildings at the water treatment plant (north)** — water pump data + pumping station data | — |
| **Broadcast – Part 1** | **Office building #1, 1st floor, water treatment plant** | 🔑 **Operating room key** + **Signal Jammer** |
| **Energy Crisis** | Fuel tank group **NE of the northern freight yard** + **3 tanker trucks** | **4× MS2000** |
| **Drug Trafficking** | **Inside a group of stacked shipping containers**, container area of the **northern train yard** | **WI-FI Camera** |
| **Missing Cargo** | Crashed helicopter **on a hill, south-southeast** · folder is on the **1st floor of the chalet** on that hill | — |
| **Lost Contact** | Dead group on the **tennis court** of the **south-east chalet** · **survive & extract** | — |
| **The Hermit** | **Village on the eastern island** — message is **below the door** of the hideout · **must extract with it** | — |
| **Administrator** | Kill **Zryachiy** (island) · ⚠️ also requires **firing a yellow flare** *(RSP-30)* skyward **inside the train area** — must reach height or it won't count | **RSP-30 flare** |

> 🗺 **LIGHTHOUSE IS TWO RAIDS, NOT TEN.**
> **RAID 1 — NORTH:** water treatment plant + freight/train yard covers **6 quests**
> *(Revision · Easy Job · Corporate Secrets · Broadcast P1 · Energy Crisis · Drug Trafficking)*.
> **Bring: 8× MS2000, WI-FI Camera, Signal Jammer, Operating room key.**
> **RAID 2 — SOUTH-EAST:** the chalet hill covers **Missing Cargo + Lost Contact** — same
> hill, and Lost Contact needs you to survive and extract anyway.
> **The Hermit** *(eastern island)* and **Administrator** *(Zryachiy, island)* pair up.

> 🔴 **CAVEAT ON THE NORTH RUN — and it's a big one.**
> **The water treatment plant is the ROGUE stronghold.** `Easy Job` literally asks you to
> kill 10 **Rogues**, Scavs or PMCs *in that area* — that's how many are there by design.
> Rogues are USEC-hostile, well-armed, use high-pen ammo and hold mounted positions.
> **"Six quests in one raid" is the efficient route, not the survivable one.**
> **Plan it as the most dangerous raid on the board**, not a chore run — and consider
> chipping it two or three quests at a time from the south/east rather than committing to
> the whole cluster in one go. ⚠️*web-sourced · player already expects Lighthouse to be hell*

## 🏭 FACTORY — 3

| Quest | Class | Type | |
|---|---|---|---|
| **Health Care Privacy – Part 5** 🆕 | III | 🔍 | ⭐ **NIGHT-TIME Factory only.** Drop spot = **the BREACH ROOM — top floor / rafters, WEST side, by the office window** ⚠️*web-sourced* · **Stash 3× Gunpowder** *(any type)* · Pays **₽320,787** + 28k EXP + 3 IFAKs · **next task rewards a Medicine case** |
| **One-Way Ticket** | II | 🎯 | ✓ **15 AUG headshots** — ⚠️ buy the gun |
| **The Walls Have Eyes** | II | 🔍 | 🔍 *(was mis-recorded as "The Wall Has Eyes")* |
| **Dragnet** | II | 🔍 | 🚫 **shelved** — keycard is ₽3.5–4.5M |

> ⭐ **THE BREACH ROOM DOES DOUBLE DUTY.** `Health Care Privacy P5`'s drop spot **and**
> `Every Hunter Knows This`' Factory objective are **the same room** — top floor rafters,
> west side by the office window. **One night Factory raid clears both**, and if you've
> bought the AUG, `One-Way Ticket`'s headshots tick up while you're in there.
> 🛒 **Bring: 3× Gunpowder** *(any type — Kite/Hawk/Eagle all count)* **+ the AUG if you have it.**
> ⚠️ **Factory is Tagilla's home map — "expected everywhere", not a fixed spot like his
> Interchange garage.** And it's night, so bring night vision or a torch.

## 🌆 STREETS OF TARKOV — 24

| Quest | Class | Type | |
|---|---|---|---|
| **Kings of the Rooftops** | II | ✋ | ✓ **8 Sniper Scavs** · reward SV-98 *(sell)* |
| **The Huntsman Path – Big Game** | II | 🎯 | ✓ kill **Kaban** |
| ⭐ **Audiophile** | III | ✋ | ✓ **Music room, apartment no. 10, 4th floor** *(building name truncated in source — verify)* → guitar pick · 🎁 **UNLOCKS Osprey MK4A (Assault) at Ragman LL3** |
| **The Door** | III | 🔍 | ✓ **Klimova 16A** — 2× WI-FI Camera, one in the **stairwell**, one on the door · 🔑 **Rusted bloody key** |
| **Cease Fire!** | II | ✋ | ✓ **Extract via "Klimov Street" with SURVIVED status** — ⚠️ the extract only opens if you **fire a green flare** |
| **Dandies** | II | 🎯 | ✓ |
| **Surveillance** | II | ✋ | ✓ **Hard drive — Concordia security room, in the basement parking garage** |
| **The Secret to Productivity** | II | 🔍 | ✓ **"Hive" hookah lounge, Malevicha street no. 5** · 🔑 **Relaxation room key** · survive & extract |
| **Watching You** | II | ✋ | ✓ **Flash drive — room 215, 2nd floor, NORTHERN Pinewood hotel building** |
| **Your Car Needs a Service** | II | ✋ | ✓ **Flash drive on the desk in the LexOs dealership director's office** *(closed section)* |
| **Road Closed** | II | ✋ | ✓ **Convoy sits between the LexOs dealership and the Pinewood hotel** → then find the ambush spot · survive & extract |
| **Secret Message** | II | 🎯 | ✓ |
| **House Arrest** | II | ✋ | ✓ **Prison cell no. 1, 3rd floor, Chekannaya 15** apartment building · then the debtor · hand over the **Chekannaya 15 apartment key** |
| **The Secret Recipe** | II | ✋ | ✓ **TerraGroup office** — chemical additive · ✅ **key NOT required** *(some spawns need it, but it's completable without)* |
| **Beyond the Red Meat** | II | ✋ | ✓ **Chef's diary in the Beluga restaurant** · ✅ **key NOT required** *(same — optional spawns)* |
| **Paramedic** | II | ✋ | ✓ **Ambulance paramedic's smartphone** → ⚠️ **must extract via "Primorsky Ave Taxi V-Ex"** with it in raid inventory |
| **Glory to CPSU** | II | ✋ | 🔍 |
| **District Patrol** | II | 🎯 | ✓ |
| **You've Got Mail** | II | ✋ | 🔍 |
| **Properties All Around** | II | ✋ | 🔍 |
| **Pets Won't Need It** | II | 🔍 | 🔍 |
| **Urban Medicine** | II | ✋ | 🔍 |
| **Ballet Lover** | II | ✋ | 🔍 |
| **Create a Distraction – Part 2** [PVE ZONE] | III | 🎯 | ✓ |

**👹 Kaban · Kollontay.** *Plus `Know Your Place!` arrives here and `Job for a Patriot`
counts here.*

## 🚉 TRANSITION — 4

| Quest | Class | Type | |
|---|---|---|---|
| **Secrets of Polikhim** | II | 🎯 | 🔍 precision tools package in the **Customs med lab** → transit to Factory |
| **New Paths** | I | 🔍 | 🔍 |
| **Know Your Place!** | III | 🎯 | ✓ **5 kills Streets → transit → 5 kills Interchange, ONE RAID** |
| **Special Comms** | III | 🔍 | 🔍 Bulbex cutter at the RUAF boulder on Woods → transit to Reserve |

## 🌍 ANY LOCATION — 25

> **Read the objectives. "Any location" ≠ anywhere.**

> 💡 **THE STATUS-EFFECT RAID — two quests, one trip, zero gear risk.**
> **`Health Care Privacy P4`** = Fatigue, hold **8 min** *(₽320,787)*
> **`Survivalist Path – Zhivchik`** = Dehydration, hold **5 min** *(any map but Factory)*
> **Both come from the same behaviour: sprint until your legs and your water are gone.**
> Sprinting burns hydration *and* stamina, so one long run produces both effects — then you
> simply survive the timers.
> 🎒 **Run it in the cheapest kit you own** *(Thunderbolt, no armor)* — nothing here needs
> gear, and **₽320k for a jog** is the best rouble-per-risk on the entire board.
> ⚠️ **Dehydration drains HP the whole time** — bring a medkit *(which is why this can NOT
> be combined with `Tough Guy`, which forbids carrying any medicine)*.
>
> ### ⭐ THE PLAYER'S TECH — faster and safer than running it down
> ✅*player method*
> **1. Eat mayonnaise.** Foods that give energy while **costing hydration** crash your water
> bar far faster than waiting for it to drain naturally. **Dehydration on demand.**
> **2. Then sit still somewhere safe and heal through the timer.** Dehydration ticks HP
> down; a medkit out-heals it. **You are not surviving a raid, you are running a clock.**
> **→ Pick a corner nothing walks past, eat, sit, heal, wait out the 5 minutes.**
> No sprinting across the map, no exposure, no risk to the kit.
>
> ### ✅ CONFIRMED IN RAID — **Fatigue persists while sitting still**
> ✅*player-tested* — so **both timers stack in the same corner.** Sprint briefly to blow
> out your legs, eat the mayo, then sit and heal through it. **One 8-minute sit cleared
> `Health Care Privacy P4` AND `Zhivchik` together.**
> **Keep this pattern** — any future "maintain a status effect" quest is the same corner,
> the same mayo, the same medkit.

| Quest | Class | Type | |
|---|---|---|---|
| **Capturing Outposts** **75% (9/12)** | II | 🎯 | ✓ 12 PMCs · Customs · Woods · 🔴 **Shoreline = HEALTH RESORT ONLY** — smugglers'-base kills count for nothing ✅*player-confirmed* |
| **Job for a Patriot** **8/10** | II | 🎯 | ✓ 10 PMCs w/ the Prapor AK-12 — **Streets · Shoreline · Ground Zero only** |
| **Supervisor** | II | ✋ | 🔍 **Interchange** — 3 cash register keys |
| ~~**Chumming**~~ | II | ✋ | ✅ **DONE** |
| **Thirsty – Delivery** **1/2** | III | ✋ | ✅ **Woods tank stashed** · ⏳ **CUSTOMS tank still to do** ✅*player-confirmed* |
| **The Tarkov Butcher** | II | ✋ | 🔍 Ground Zero meat truck → Shoreline ambulance |
| **Informed Means Armed** | I | ✋ | 🔍 **Woods camera left** |
| ~~**Weapons Circulation**~~ | II | 🔍 | ✅ **DONE** — both Woods ritual spots marked |
| **Needle in a Haystack** **3/6** | III | 🔍 | 🔍 Interchange kart track · Interchange indoor playground · Streets playground by Concordia |
| **Drip-Out – Part 1** | III | ✋ | ✓ **100 Raiders** + 50 WARTECH FiR · **AP ammo + sidearm** |
| **Booze** | III | ✋ | ✓ 10 vodka · 10 whiskey · 3 purified water · 20 Pevko — **all FiR** |
| **Semiconductor Crisis** **50%** | III | ✋ | ✓ 3 GPUs FiR — ⚠️ **before the Bitcoin Farm eats them** |
| **Shooter Born in Heaven** **50%** ⭐*Kappa* | ⭐ | 🎯 | ✓ long-range headshots |
| **The Tarkov Shooter – Part 4** ⭐*Kappa* | III | 🎯 | ✓ |
| **Sew it Good – Part 1** ⭐*Kappa chain* | III | ✋ | 🔍 |
| **Is This a Reference?** | III | ⭐ | 🔍 WI-FI cameras, all 9 maps — **Customs done** |
| **Car Repair** **62%** | III | ✋ | 🔍 |
| **Aid Stations** **33%** | II | ✋ | 🔍 |
| **Dressed to Kill** **12%** | I | ✋ | 🔍 |
| **Rough Tarkov** | I | 🔍 | ✓ **Locate the heavily mined area on Woods** + **the Claymore mine on Ground Zero** — locate only ⚠️*web-sourced* |
| **The Huntsman Path – Controller** 🆕 | I | 🎯 | ⭐ **Kill 2 PMCs suffering the STUN effect** — 🛒 **bring Zarya stun grenades.** Stacks with `Swift` + `Capturing Outposts` — **the same PMC kill counts for all three** ✅*player-confirmed from screen* |
| ~~**The Survivalist Path – Zhivchik**~~ | I | 💡 | ✅ **DONE** — same raid as HCP P4 |
| **Fishing Place** | III | ✋ | 🔍 |
| **Easy-Breezy** | III | 🎯 | ✓ |
| **Regulated Materials** | ? | ✋ | 🔍 |
| **Arena Business** [PVE ZONE] | III | ✋ | 🔍 |
| **Professional Fitness – Part 1** [PVE ZONE] | III | ✋ | 🔍 |

---

## ❓ Two icons I can't read

**⭐ in the Type column** — on `The Courier` and `Is This a Reference?`. Not the crosshair,
magnifier or hand. **Ask the player.**

**⭐ in the Class column** — on `Shooter Born in Heaven` and `Semiconductor Crisis` it looks
like an arrow rather than I/II/III. Possibly "Elite" or a special tier. **Ask.**

---

# DO THESE NOW

- **MS2000: 4 left.** Woods **2** *(Weapons Circulation)* · Reserve **2** *(A Fuel Matter)*.
  Buy per trip.
  > ✅ **Corrected.** This said 8. The Shoreline marker *(Wet Job P2)* and the three
  > Interchange markers *(Minibus)* are already spent — **both quests are complete.**
- **Check your in-game mail** — Skier sends the 2 propane tanks for `Thirsty – Delivery`.
- **🔫 You need a 9x39 weapon for `The Punisher – Part 3`** — VSS Vintorez, AS VAL, 9A-91,
  SR-3M or VSK-94. **Nothing on your gear list is 9x39** *(the SR-2M is 9x21)*. The quest
  rewards a VSK-94, but you need one first to earn it.
- **Buy the Goshan cash register key on flea** — that's `Supervisor` done for ₽250k profit,
  no raid required.
- **Buy the Cottage back door key** if you want the `Tarkov-Style Diplomacy` villa half.
- **Buy an AUG** — nothing on Factory moves without it.
- ~~Buy the AK-12 suppressor + PS-320~~ — ✅ **not needed, don't spend the money.**
  **Prapor hands you the AK-12 already built, suppressor and PS-320 included.**
  *(player-confirmed — this buy line was stale)*
- **Start hoarding drinks** for `Booze`. 43 items, all found-in-raid, months of collecting.
- **Stop selling WARTECH gear** — `Drip Out` needs 50 pieces.

---

# Bosses — 4 down, 7 to go

| Boss | Map | Where | |
|---|---|---|---|
| The Goons ×3 | roaming | Customs · Woods · Shoreline · Lighthouse | ✅ |
| Partizan | Woods / Ground Zero | roams | ✅ |
| Reshala | Customs | Dorms 3-story · New Gas · Fortress | ✅ |
| Tagilla | Factory, also Interchange | ~50% spawn | ✅ |
| **Sanitar** | **Shoreline** | **Resort · Pier** | ❌ **next raid** |
| Killa | Interchange | Mall | ❌ |
| Glukhar | Reserve | | ❌ |
| Shturman | Woods | Sawmill | ❌ |
| Kaban | Streets | | ❌ |
| Kollontay | Streets · Ground Zero | | ❌ |
| Zryachiy | Lighthouse | Island | ❌ |

The Goons were the hard one and they're done. **The Goons roam four maps you're already
working** — take them if they show, don't hunt them.
**Update:** Shturman ✅ *(F1 grenade)* and Reshala ✅ are both down — `Woods Keeper` and
`Trophy` complete.

## 📊 BOSS STAT + TACTICS TABLE — researched ⚠️*web-sourced*

| Boss | HP | Head | The one thing that matters |
|---|---|---|---|
| **Reshala** ✅ | 752 | 62 | **Brown sweater** — guards wear blue jackets w/ white cuffs. **Kill him before he sees you** or he hides behind the guards |
| **Partisan** ✅ | 950 | 80 | Roams Customs · Woods · Shoreline — "expected everywhere" |
| **Glukhar** | **1010** | 70 | **Black T-shirt, grey pants, light armor** vs guards in heavy camo. **Get close, kill HIM first** — Reserve storage "K" + repair building |
| **Kollontay** | 1055 | 65 | 🔴 **HIS CLUB JAMS YOUR GUN.** Never let him close. Klimov mall **or** Ministry academy — push the academy door holding an angle on the guards |
| **Sanitar** | **1270** | 70 | 🔴 **His guards HEAL THEMSELVES with injectors.** Burst them down — anything slow gets undone. Shoreline port/pier + cottages |
| **Kaban** | **1300** | **85** | 🔴 **LexOs dealership is RIGGED WITH CLAYMORES.** **Approach from the NORTH via Chek 15** — that AGS-30 has a blindspot; the southern one has long sightlines. **Stay off grass and curbs** |
| **Zryachiy** | **1655** | **175** ⚠️ | 🔴 **KILL ZRYACHIY FIRST.** If you kill the guards first they **respawn up to 3× each.** Lighthouse peninsula. That 175 head means headshots are not the shortcut here |
| **Killa** | 890 | 70 | See his own section — **holds angles, hunts you across the map, thorax only** |
| **Tagilla** | **1220** | 100 | All 12ga + **one-shot hammer.** Distance beats him. Interchange = Goshan garage only |

**Pattern worth noting: the hardest bosses are guard problems, not boss problems.**
Sanitar's guards heal, Zryachiy's respawn, Kaban's are behind autocannons and mines,
Reshala's body-block him. **Killa is the exception — he's the fight himself.**

**Reading eftboss.com:** the headline % is whether he spawns at all; the per-location
numbers are that split evenly across spawn points. I can't read the live number myself, so
check before a hunt and tell me.

## 🎯 HOW TO ACTUALLY KILL THEM — merged from research ⚠️*web-sourced unless marked*

### 🔴 The ammo ceiling frames everything

| Round | Pen | Guns you own |
|---|---|---|
| **7.62x39 BP gzh** | **47** | Mk47 Mutant · RD-704 |
| **5.45 BP gs** | 45 | NL545 GP · AK-12 · RPK-16 · AKS-74N |
| **5.56 M855A1** | 44 | HK 416A5 · MDR · Mk16 · TX-15 |
| **9x39 SP-6** | **48** | needs the AS VAL you're buying for `Punisher P3` |

**Boss guards routinely wear class 5. Glukhar's wear class 5–6 with visors.** At 45–48 pen
you are **under-penned for the chest and must play heads and legs.**

> ⭐ **Level 36 → Prapor LL4 → 5.45 BS at 54 pen.** Rep already clears it. **Six levels
> turns half this list from "wait" into "go".**

### ✅ TAKE NOW at level 30

**Reshala** · 752 HP — M855A1 or 5.45 BP is plenty. **Open on HIM, not the guards** — once
spotted he hides behind them. **Brown sweater; guards wear blue jackets with white cuffs.**
2 grenades for the rooms.

**Kaban** · 1300 HP — ⭐ **softer than his reputation: most guards wear NO helmets** and
silhouette against the sky. **🔴 LexOs is rigged with claymores — stay off grass and curbs,
avoid the southern approach.** ✅ **Come from the NORTH via Chek 15** — that AGS-30 has a
blindspot. **The mines kill more people than he does.**

**Shturman** ✅*done* — grenades work on him ✅*player-confirmed*. His guards run
armor-shredding ammo; don't trade in the open.

### 🟡 DOABLE WITH THE RIGHT PREP

**Glukhar** · 1010 HP · 6 guards — ⭐ **he is softer than his own guards.** Black T-shirt,
grey pants, at most a light carrier, while the guards are class 5–6 with visored helmets.
**Get close, kill the boss first, then clean up.** Storage buildings marked "K" and the
repair building. Same map as your D-2 chain.

**Kollontay** · 1055 HP · 4 guards —
🔴 **HIS CLUB JAMS YOUR WEAPON** ✅*player-confirmed*. **Never let him close.** The danger
isn't his damage, it's being disarmed while four guards with AP rounds and flashbangs are
still up. **Know your malfunction fix before you go in.** This makes the "push the academy
door" tactic risky — a doorway is exactly where he gets close.
His **eyes are class 1**, so headshots are live. **Bring your own Zaryas** — his guards use
flashbangs and you need 2 stunned PMC kills for `Controller` anyway.

**Sanitar** · 1270 HP — 🔴 **his guards heal themselves with injectors**, wear class 5, and
carry lots of grenades. **Burst, don't trade** — slow damage gets undone. Needs your
highest pen: **7.62x39 BP in the Mutant.** M855A1 will not do it. Port/pier and cottages.

### 🔴 WAIT

**Zryachiy** · **1655 HP · head 175** — kill him FIRST; killing guards first makes them
**respawn up to 3× each.** That 175 head means headshots aren't the shortcut. The wiki's
strategy assumes **3 players.** Solo at 45 pen this is a kit donation.

**Killa** · 890 HP — **face is class 6, nothing you own cracks it.** Thorax only
✅*player-confirmed*. Worth fighting at **level 32** when `Sellout` opens — and **his Maska
is already sitting FiR in your stash.**

**Tagilla** · 1220 HP — all 12ga + a **one-shot hammer.** Distance wins, closing loses.
**Avoid him on the Factory night raid** — you'll be carrying quest items.

**The Goons** ✅*done* — **Birdeye is the one that kills you**, he's the accurate one at
range. Break line of sight rather than duel him.

### 📋 The short version

| Boss | Now? | The one thing |
|---|---|---|
| Reshala | ✅ | Open on him, not the guards |
| Kaban | ✅ | North via Chek 15. Guards have no helmets |
| Shturman | ✅ | Grenades work |
| Glukhar | 🟡 | He's softer than his guards — kill him first |
| Kollontay | 🟡 | **His club jams your gun.** Never let him close |
| Sanitar | 🟡 | Burst or they heal it back |
| Killa | 🔴 | Wait for 32 |
| Tagilla | 🔴 | Distance only |
| Zryachiy | 🔴 | Wait — 175 head, respawning guards |

> **At 45 pen you are a headshot-and-legs player against boss guards. Everything changes at
> level 36.**

---

# 🧊 ICE BREAKER — ✅ IT IS PvE, AND IT'S REACHABLE

⚠️*web-sourced* — **the file previously listed this as a locked endgame map. That's wrong.**

**Icebreaker is Tarkov's first dedicated PvE map.** Max **1–3 PMC players** — your own squad
only, no random matchmaking. Every enemy is AI: **Rogues · Black Division · The Wedge ·
Knight**. 50-minute raids, enemy count scales with squad size.

### 🔑 How to unlock it — and it runs through YOUR HIDEOUT

**The `Boreas` story chapter unlocks it. Two ways to start it:**
1. Find a **Paradigm shipping poster** in any TerraGroup-related location, **or**
2. ⭐ **Have Intelligence Center 3 — then just use the radio in your hideout.**

> 🔴 **THIS IS A REASON TO UNPAUSE THE HIDEOUT.** You're on **Intelligence Center 2**, and
> the file already notes **Generator 3 gates Intelligence Center 3**. That chain now buys
> you a whole map, not just a flea discount.

**Then:** talk to Mechanic → **Woods: fix equipment under the tower near the Scav bunker
with a Toolset** → Mechanic reviews documents → vehicle access → **the chain branches based
on which traders you've favoured.**

**Entry:** transit from the **Shoreline pier — ₽700,000.** Direct map-select access unlocks
after finishing the questline **`Stick to It`** *(the fee still applies)*.

| Icebreaker boss | Where | Drops |
|---|---|---|
| **The Wedge** | **level 3, in the gym** · 3–6 heavily armed guards | LV-119 carrier, ComTac VI, MP7 parts |
| **Knight** | **level 0** · 2 Rogue guards | **Death Knight mask**, **CPC Goons Edition**, Desert Eagle L6 |

> 🚨 **INSURANCE DOES NOT WORK ON ICEBREAKER.** Anything you lose is gone permanently.
> Traders take your money and then tell you their people wouldn't go. **Do not bring the
> Zhuk or the CPCs on a first trip.**
>
> 🔑 Keys/items in play: BBQ-S43 gas torch · Boreas crew quarters keycard · Boreas engine
> room keycard · Compartment C-1 and C-3 keycards · SZ-1 explosive charge.

---

# 📈 LEVELLING & SKILLS — researched ⚠️*web-sourced*

## The fastest XP, in order

1. **🥇 Trader quests are BY FAR the biggest XP source.** Nothing else is close. Chain them.
2. **🥈 SURVIVE.** The survival bonus multiplies the whole raid's XP.
3. **🔴 Don't Run-Through.** Extracting too early having done too little tags the raid
   **Run Through** instead of Survived — **you lose the survival bonus AND your loot loses
   Found-in-Raid status.** That last part breaks quest hand-ins.
4. **Loot and examine everything** — examining unknown items is free XP.
5. **Headshots** — more XP, less ammo.
6. **🚫 Scav runs give you NO character XP.** They're for loot only. If the goal is levels,
   play PMC.

> 💡 **For this player specifically: quests ARE the levelling plan.** You're 2 levels from
> `Sellout` and 6 from Prapor LL4. The board you're already clearing is the fastest route to
> both — no grinding required.

## Skills

**Every skill maxes at 51 (Elite).** There is a **per-raid fatigue cap** on skill gain:

| Points earned this raid | Gain rate |
|---|---|
| 0 *(first point)* | **129%** |
| 1 | 100% |
| 2 | 60% |
| 3 | 36% — and falling |

🔴 **So spread training across several skills per raid rather than grinding one.**

**How the ones that matter level:**

| Skill | Trained by | Elite payoff |
|---|---|---|
| **Strength** | Sprinting/jumping **near max carry weight**, melee, throwing grenades | **+30% carry (100kg) · +20% move/sprint · +20% jump** — and **weapons weigh 0kg in slots** |
| **Endurance** | **Sprinting long distances**, holding breath while aiming | **+50% stamina · +100% breath hold** *(huge for the DVL/M700 long shots)* |
| **Metabolism** | Eating and drinking | boosts hydration/energy retention |
| **Vitality · Health** | Level themselves through normal play | big survivability gains |

**The Gym in your hideout trains Strength and Endurance directly.**

> ⭐ **Endurance and Strength first.** Endurance for stamina and breath-hold, Strength so
> you can carry loot out. **Both level for free during the raids you're already running** —
> sprint everywhere, hold your breath when you scope, and carry heavy on the way out.

---

# 💰 LOOT RUNS — merged from research ⚠️*web-sourced, 1.0.5 community estimates*

> ⭐ **The headline: three of the five are raids you're already scheduled to run.** You
> don't need a money night — you need to bring a backpack to the quests you're doing anyway.

### 🥇 Interchange — the tech circuit · **₽500k–1M+**
**OLI → Techlight/Rasmussen → Goshan → IDEA → Kiba Arms → EMERCOM Medical.**
GPUs, electronics, Tetriz, meds, **LEDX** from the pharmacies.
**The register-and-tech sweep needs NO keys** and still clears several hundred thousand.
⭐ **This is your `Supervisor` + books raid. Identical route. Bring a bag.**
⚠️ It's Killa's floor.

### 🥈 Streets — the keyed run · **₽1M+, exceptional runs 2–3M**
**LexOs dealership → Chekannaya 15/13 marked rooms → Concordia apt 64 → Pinewood Hotel**,
extract Crash Site or Courtyard. GPUs · LEDX · VPX · intelligence folders.
⭐ **Overlaps your quest board almost exactly:** LexOs is `Your Car Needs a Service`,
Chekannaya 15 is `House Arrest`, Pinewood 215 is `Watching You`, Concordia is
`Surveillance`. **Same buildings — quests and money together.**

### 🥉 Reserve — RB-key bunker rooms · **₽400k–900k**
**King/Knight/Bishop → train station → D-2 bunker → server rooms.**
🔑 **RB-PSP1 · RB-PSP2 · RB-VO** *(plus RB-ST, already needed for `Surplus Goods`)*
⚠️ Raider AI patrols underground.
⭐ **This IS the D-2 chain raid.** 5–6 quests plus 400–900k on one trip. **Buy the RB keys
before you go.**

### 4. Labs · **₽1M+**
Densest loot in the game — GPUs, LEDX, keycards, Bitcoin, meta weapons.
🔑 Labs access keycard, **consumed on entry**.
🔴 **INSURANCE DOES NOT WORK ON LABS** ✅*player-confirmed*.
⭐ `Chemical - Part 4` (Skier) rewards **2× Labs keycard** — your entry fee is already
coming. **Go in cheap the first time.**

### 5. Customs — Dorm 314 marked room · **₽200k–700k**
Keycards spawn here, guaranteed meds. 🔑 Dorm 314 marked key — ⭐ **you're getting it free
as the next-task reward on `Controller`.**
⚠️ Most contested area on the map.
✅ **Safer alternative: the Customs stash circuit — ₽300–800k with almost no player
contact.**

### 🍯 Honourable mention
**Shoreline Resort** east/west wing rooms — ₽300–700k. Needs wing keys.

## 📋 What this means

| Raid you're already doing | Money it also pays |
|---|---|
| **Reserve D-2 chain** | **₽400–900k** — buy RB-PSP1, RB-PSP2, RB-VO first |
| **Interchange `Supervisor` + books** | **₽500k–1M** — bring a backpack |
| **Streets quest block** | **₽1M+** — LexOs, Chekannaya, Pinewood, Concordia are all quest sites |

**The one genuinely new activity worth adding: the Customs stash circuit.** ₽300–800k,
minimal contact, and it pairs with `Angry Watchman` and the Customs propane tank for
`Thirsty – Delivery`.

---

# 🎯 WHAT TO FOCUS ON RIGHT NOW

**In order, with reasons:**

1. **🥇 Finish Woods** — the BTR pair *(`Shipping Delay P1` → `A Helping Hand`)* and
   `Hiking`. It's nearly done and it's the safest board you have.
2. **🥈 Reserve's D-2 chain** — **5–6 quests in ONE underground run**, fully mapped, still
   untouched. **Highest quest-per-raid on the board.** Bring 6× MS2000 + the RB-ST key.
3. **🥉 Night Factory** — `HCP P5` + `Every Hunter Knows This` share the **breach room**.
   Bring 3× Gunpowder. **₽320,787.**
4. **Level to 32** → `Sellout` opens, and **Killa's Maska is already sitting FiR in your
   stash.** Every forced Killa fight starts paying.
5. **Level to 36** → **Prapor LL4** *(rep already met)* → **5.45 BS at 54 pen**, which
   finally cracks Killa's class 6 face shield.
6. **Unpause the hideout for Generator 3 → Intelligence Center 3** → the Boreas radio →
   **Icebreaker access**, plus Flea fee −30%.
7. **Interchange last** — `Supervisor` 2/3 and the two books. It's the most dangerous board
   for the least reward, and nothing there is time-sensitive.

> **The through-line: everything above levels you, and levelling is what unlocks the two
> things you actually want — Sellout and Prapor LL4.** There is no separate grind.

---

# Kappa

> 🏟 **ARENA IS A KAPPA TOOL — verdict: WORTH IT** ⚠️*web-sourced*
>
> **1. Ref LL3 is 0.10 rep away** *(needs 0.50, you're at 0.40; level 25 already cleared)*.
> Behind it: a second **Crye AVS (MultiCam)**, **HighCom Trooper TFO**, **Strandhogg**.
> **Ref LL4 = level 35 + rep 1.20.**
>
> **2. 💰 The transfer pipe.** After **`To Great Heights! – Part 3`**, Ref moves currency and
> items **from Arena into the main game**: **₽1,000,000/day** *(₽1.5M Ryzhy)* · 350 GP coins
> · 5 Lega Medals · **locked crates**. **Fees 15% roubles / 5% items**, reduced by Charisma
> and Ref loyalty.
> ⭐ **That's more per day than the best loot run in the game, with ZERO gear risk.**
>
> **3.** BattlePass rewards earned there **unlock in PvE too** — and several Ref-shop items
> in the armor section are gated behind *"unlocking it in the Arena BattlePass."*
>
> ⚠️ **Access chain:** Ref needs **`Easy Money – Part 1`** (Skier) · transfers need
> **`To Great Heights! – Part 3`.**
> **Verdict: a parallel income stream, not a replacement for questing. Clear the 0.10 to
> LL3 first, then decide.**

| Requirement | You |
|---|---|
| Level **40** *(really 42 — Ragman's LL4 gate)* | **30** |
| **LL4 with every trader** | LL3 on six · Ragman ~2–3 · Ref 2 · **Fence 1** |
| **Fence rep 3.0** | Fence at LL1 — biggest gap |
| `Chemical - Part 4` | Parts 1–3 done, Part 4 live |
| `A Shooter Born in Heaven` | 50% |
| `The Tarkov Shooter - Part 4` | 6% |
| `Sew It Good - Part 4` | Part 1 at 0% |

> ⚠️ **LL4 costs no money.** The "₽4.5M spent" requirement was **removed in 1.0** —
> loyalty now scales off **level and rep only**. There is nothing to grind money for here.
>
> *(This file used to say Kappa needed ₽30–40M routed through traders. That was wrong and
> it's deleted. Don't buy things just to move the number.)*
>
> The **"(spent)" figure on the trader panel is a stat display, not a gate** — confirmed.
> Ignore it.

**Level 30 unlocks:** lion statue barter (~₽86k) → documents case, cheap stash relief.
**Level 42:** Ragman LL4, the real Kappa gate.

---

# Character

**Level 30 · USEC · PvE · Unheard (Gamma 3×3) · Stash 4 · ₽3,195,691** *(moves fast)*

> 🔑 **LABS KEYCARDS ARE CRAFTABLE — you can do it today.**
> **UHF RFID Reader + Intelligence folder → Intelligence Center 2 → 40 min → ×3 cards.**
> ✅ **Player confirms holding at least 2 Labs keycards already.**
> 🔴 **Never sell Bulbex cable cutters** — barter ingredient *and* `Special Comms` needs one.
> ⚠️ **Keys now break after ~25–50 uses.** They're consumables. Don't buy the ₽2.8M one.

> 🎫 **KORD BREACH — 501 docs, ends 7 Dec, ~4.6/day needed vs a 15/day PvE cap.**
> Achievable, **but only if collection starts now.** Free, works in PvE, unlocks permanently.
> ⚠️ **Player is missing FINANCIAL documentation** — it drops on **Customs · Streets ·
> Interchange**, all maps in the rotation. **Start looking.**
> The other gap is **Medical + User docs** — both from **Ground Zero, Streets or Labs.**

> ✅ **ARMOR: nothing to buy.** Community meta is Slick + class 6 UHMWPE; budget is Hexgrid
> + GAC 3s15m. **Your CPC MOD.1 already runs GAC 3s15m at 0% penalty and the Zhuk is class
> 6 all round.** No purchase improves you.

| Trader | LL | | Trader | LL |
|---|---|---|---|---|
| Prapor | 3 | | Ragman | ~2–3 |
| Therapist | 3 | | Jaeger | 3 |
| Skier | 3 | | Ref | 2 |
| Peacekeeper | 3 | | **Fence** | **1** |
| Mechanic | 3 | | | |

**Only level and LL4 are holding you back.** Weak spots: Fence at 1, Ref at 2, hideout.

> ⭐ **Ragman is the one that matters most.** He gates Kappa at LL4 (level 42) and he's
> your weakest real trader. **Three of the four quests you just unlocked are his** —
> `The Key to Success`, `Minibus` and `Supervisor`. Doing Ragman work is straight-line
> Kappa progress, so favour him when two quests are otherwise equal.

**PvE vs PvP:** the *only* difference is **boss spawns**. Everything else — quests, loot,
flea, insurance, rep — works the same. So normal Tarkov knowledge applies here.

---

# Fence rep — goal #2 · ⭐ SOLVED, the method was wrong

> 🚨 **THE FIX: car extractions.** **+0.2 first time PER LOCATION** *(co-op extract:
> +0.25)*. The player was farming assisted PMC kills at **+0.01**.
>
> **At 1.566, goal 3.0, gap 1.434 → ~7 first-time car extracts covers almost all of it.**
> Car extracts exist on Customs *(Dorms V-Ex)*, Interchange *(Power Station V-Ex)*, Woods
> *(Bridge, ₽5k)*, Shoreline, Lighthouse, Ground Zero, Streets *(Primorsky Ave Taxi)*.
>
> ⭐ **`Paramedic` REQUIRES the Primorsky Ave Taxi V-Ex** — that quest pays +0.2 free.
>
> ⚠️ **It never resets — it decays per use, per location.** Sources disagree on the curve
> *(÷ uses vs halving)* and even the base value *(+0.2 vs +0.4)*. **Watch your own rep
> before/after the next one and record the real number.**
>
> ✅ **Dying as a scav costs NOTHING.** Neither does leaving early.
> 🔴 **Killing a scav boss as a scav is −0.2** — one of those erases a car extract.
> 📋 **Turn on Fence's scav dailies** — you have the Intelligence Center, they're available
> and currently unused. +0.01–0.05 each, daily, forever.
> ⭐ **+2 karma is only 0.43 away** and unlocks `Network Provider – Part 1`.

# Fence rep — the old detail

Kappa wants **3.0** and you're at **LL1**.

### ✅ Goes up
1. **As a scav, kill PMCs who have killed scavs.** Not any PMC — ones already marked.
2. **Extract as a scav.** Simple and repeatable.
3. **As a PMC, extract by car.** Costs money and **depends on your spawn**.

### 📊 The player's current method and its actual rate ✅*player-confirmed*

Go in as a **scav**, hunt PMCs who have **already killed a scav**, kill them — **+0.01
each**. Transit to another map, repeat, return to Factory, repeat. Ends in either a death
to **Tagilla** *(who aggros scavs)* or an extract loaded with loot.

> 🔴 **Best result so far: 0.06 for FIVE PMC kills and one extraction.**
>
> **That's a painful rate for a 3.0 target.** Three problems: the PMC must kill a scav
> *first*, the player must land the kill *themselves*, and the PMC is often gone by the
> time they get there.
>
> **Research request #7 is open on this** — full source table and the fastest realistic
> path. Until it comes back, assume this is a long background grind and don't build raids
> around it.

### ❌ Goes down
1. **Killing scavs while you're a scav** — straight rep loss.
2. **Killing a boss while you're a scav** — **costs a lot.** Don't.

> ⚠️ **Bosses will attack you as a scav if you annoy them**, and you can't meaningfully
> fight back in a scav kit. So on a scav run: **don't shoot scavs, don't shoot bosses,
> don't linger near one.** Walk, loot, extract.

> **This is the slowest thing on your board and the only fix is doing it regularly.**
> Scav runs are free, so every one you skip is rep you don't get. When you report a raid,
> tell me if it was a scav run and I'll track the trend.
>
> 🎲 **Scav runs are the cheap way to move this.** Free kit, free rep, no risk. Offer them
> often — and note the Pistol Factory Run is a **PMC** run, so it's a different tool.

---

# Insurance

> 🔴 **INSURANCE DOES NOT WORK ON LABS OR ICEBREAKER.** Anything you take in there and
> lose is **gone permanently**. Kit those two maps as if there's no safety net, because
> there isn't. ✅*player-confirmed*

**Everywhere else: insured gear comes back 100% of the time, after 24 hours.** It costs money, and the
pricier the gear the pricier the premium.

**What you insure:** helmet, rig/armor, headphones, gun, backpack — always. Good mags too;
cheap ones no.

**What this means for advice:** running expensive kits is much less risky than it looks,
so I shouldn't be telling you to play poor. The real losses are **what's in your bag** and
**quest items**, not your kit.

**Some things can't be insured at all.** The REAP-IR is the known example — and it's **not
a quest item**, it's a normal thermal sight that happens to be what `The Courier` hands
you. Best guess is rare items can't be insured, but that isn't confirmed.

## Three tiers of risk — this is the rule

| Tier | What | Protection |
|---|---|---|
| **1. Insurable** | helmet, armor, rig, gun, headphones, backpack, good mags | **Comes back in 24h.** Don't play scared with it. |
| **2. Uninsurable but fits the Gamma** | quest items, small rare loot | **Put it in the Gamma.** Solved. |
| **3. Uninsurable AND can't go in the Gamma** | **the REAP-IR** — it's flagged non-secure-container | **No safety net exists.** |

**Tier 3 is the dangerous one and there's no container answer for it.** The REAP-IR could
never have been saved by the Gamma — it isn't allowed in one. The only protection is how
you run the raid:

- **Pick your extract from the map screen before you spawn**, not when you're loaded and
  heading out.
- **Go in light.** Don't stack a tier-3 item with a greed run.
- **Do the objective first, then leave.** Every extra minute is pure downside.

> That's the actual lesson from raid 6. It wasn't a container mistake — it was a route
> mistake, and no amount of Gamma discipline would have changed it.

---

# Skills

Skills level from normal play, and plenty of quests raise them for you as a reward. They
matter a lot over time, and they **partly carry through a prestige**, so the time isn't
wasted.

**Gym is unlocked** — it speeds up physical skill training. Keep up with it.

> ❓ **Unconfirmed:** there may be some quests gated behind a skill level — more like a
> checkpoint partway through than the whole quest. Neither of us is certain. If you hit
> one, send me the text and it goes in the confirmed table.

---

# Goals, in order

1. **Level 40 and LL4 everywhere.** Everything follows from this.
2. **Fence rep 3.0.** Scav karma and quest rep. Slow burn, start noticing it now.
3. **The four Kappa chains.** Three are already moving.
4. **Bosses.** 7 left, take them as maps come up.
5. **Money.** No fixed target — LL4 doesn't need any. What money actually buys is kits,
   keys, insurance premiums and hideout materials. **Bitcoin Farm is the lever** — the
   only thing that earns while you're offline, and still locked.
6. **Prestige — last.** Resets you to level 1, empty stash, hideout reset, quests gone,
   traders reset. You keep stats, achievements, some skills and mastering, Arena rating,
   and prestige rewards, and each level lets you carry a few more items over. Needs level
   55. It's a deliberate restart, not a bonus.

---

# 💱 BARTERS WORTH DOING ⚠️*web-sourced*

**The rule: a barter is good when you get back far more than you hand over.** Three do that
by a wide margin — **UZI PRO · MP7A2 · HK G28.**

### ✅ DO THESE

| Barter | From | Why it's worth it |
|---|---|---|
| 🥇 **GSh118 backpack** | **Prapor** | **The biggest container in the game, and BARTER-ONLY — there is no rouble price.** ⭐ Straight upgrade to every loot run, especially the ₽1M Interchange tech circuit |
| 🥈 **HK G28** | **Peacekeeper LL3** | **Costs 1× Labs keycard** — ⭐ **and you can CRAFT those three at a time at Intelligence Center 2.** A gun on your *I'll use* list for an item you manufacture |
| **UZI PRO / MP7A2** | — | Named as the best value-for-input barters in the game. **You already own an MP7A2**, so this is only worth it as a spare |

### ❌ SKIP THESE — reasons specific to you

| Barter | Why not |
|---|---|
| **Medicine Case** *(Therapist)* | 🚫 **You're getting one FREE.** `Health Care Privacy P5`'s next-task rewards include a **Medicine case** ✅*player-confirmed from screen* |
| **6B43 Zabralo** *(Prapor)* | Class 6 armor — **but you already own the Zhuk**, which is class 6 all round at 11.5 kg. Zabralo is **10.8 kg with -9% movement.** No gain |
| **KS-23M** *(Prapor)* | 🚫 **It's on your HATE list.** Cheap and effective, and you will never use it |

> 💡 **The pattern: barter for things that cannot be bought** — the GSh118 has no rouble
> price at all, and the G28 costs an item you can manufacture on demand. **Don't barter for
> anything a quest is about to hand you.**

---

# 🏗 HIDEOUT CRAFTS — ranked ⚠️*web-sourced*

> 🔴 **THE METRIC IS PROFIT PER HOUR, NOT PROFIT.** A craft paying ₽200k over 12 hours is
> ₽16k/hr. One paying ₽50k in 2 hours is ₽25k/hr. **Short cycles you can re-run beat big
> slow ones.**

### 🥇 START HERE — **Bundle of Wires ×8, Workbench L1**

| | |
|---|---|
| **Profit** | **≈ ₽146,872 per craft** |
| **Time** | 1h 58m |
| **Rate** | **≈ ₽74,470/hr — the best available at this stage** |
| **Station** | **Workbench level 1** — you already have it |

> ⭐ **AND IT DOUBLE-DIPS.** Your hideout needs **50 wires** across five modules, and your own
> rule says **never sell one.** This craft pays the best rate in the hideout *and* produces
> the item blocking your upgrades. **Run it constantly.**

### 🥈 The three crafts worth building the hideout around

| Craft | Why |
|---|---|
| 🍺 **Moonshine — Booze Generator** | **Highest expected value per craft**, and it feeds **the Scav Case (needs 3)** and the best barters. ⚠️ **`Booze` needs purified water FOUND IN RAID** — the Water Collector's output does not count |
| ₿ **Bitcoin Farm** | Passive roubles, **scales to 50 GPUs.** ⚠️ **Do `Semiconductor Crisis` FIRST — it needs 3 GPUs found in raid, and the farm eats them** |
| 💻 **Intelligence Center — high-value electronics** | ⭐ **This is also where Labs keycards are crafted** *(UHF RFID Reader + Intelligence folder → ×3)*. Int Center earns twice |

### ✅ What you already run — keep or drop

| Yours ✅*player-confirmed* | Verdict |
|---|---|
| **Gas mask → gas canisters** | ✅ **Keep** — steady money, cheap inputs |
| **CMS kits** | ✅ Keep — personal use, saves buying meds |
| **Ammo** | ✅ Personal use only — **not a profit craft** |

### 🚫 Never sell what these produce

**Moonshine** *(Scav Case ×3)* · **Wires** *(50 for the hideout)* · **GPUs** *(quest before
farm)* · **purified water** *(FiR only for `Booze`)*.

> ⚠️ **Flea prices move daily, so exact rankings rot fast.** The live tools are
> **tarkov.dev/hideout-profit** and **TimmyTracker's craft finder** — check those before a
> big batch. *(I could not pull live numbers: tarkov.dev's API has been down all session.)*

---

# Hideout — PAUSED

**Stash 4** · Gym unlocked · Generator 2 · Intelligence Center 2 · Lighting 3 ·
Water Collector 2 · Weapon Rack 1 · Medstation upgrading

**Still locked:** Bitcoin Farm · Booze Generator · Gear Rack · Library · Scav Case ·
Solar Power

## Why it's paused

The tally we built counted **shortfalls**, but every module panel reads X/Y from the
**same stash** — so a ✓ in three modules can be the same ten items, and building one
empties the other two. The real number is the **sum of every requirement**, ticked or not,
which is roughly **400 items**, not the 214 the old tally said.

**Rebuilding it properly needs names for the items that showed as satisfied** — the
gold/tan branching thing (28 across Shooting Range, Vents and Generator), the blue/white
tool (18), the battery (11), and about a dozen smaller ones.

**Say the word and we pick it back up.** Until then the useful bits:

- 🔴 **Wires — 50.** Five modules. Never sell one.
- 🐓 **Two golden roosters** — Hall of Fame and Scav Case both want one.
- 🥃 **Moonshine ×3** for the Scav Case — or **build the Booze Generator** and make it.
- 🚱 **`Booze` needs purified water FOUND IN RAID.** Water Collector output won't count.
- 💻 **GPUs — quest before farm.** Found-in-raid can't be bought back.
- ⚡ **Generator 3 is the hub** — gates Intelligence Center 3 *and* Water Collector 3.
  Intelligence Center 3 pays **Flea fee −30%**.

---

# Keep or sell

Higher rule wins.

1. **Quest item → KEEP.** Found-in-raid can't be bought back.
2. **Hideout material for something you're building → KEEP.**
3. **Barter input → KEEP** only if the barter beats buying it.
4. **Otherwise money per slot decides.** A 1×1 worth 90k beats a 4×4 worth 200k.
5. **Where you sell matters** — trader for thin margins, flea when it covers fee and wait.
6. **Rare and unsure → keep one, sell the rest.**

**Never sell — quest:** Bulbex cable cutter · AK-12 · WARTECH gear · Booze drinks · any key.

**Never sell — hideout.** The full list, 222 items across 16 modules:

**Wires (50) · power cord (20) · phase control relay (16) · spark plug (14) · CPU fan
(12) · corrugated hose (10)** — the big six.

Then: fleece fabric · bolts · T plug · PSU · NIXXOR lens · military cable ·
military flash drive · can of thermite · VPX · car battery · Greenbat · sodium
bicarbonate · coffee beans · Working LCD · drain cleaner · COFDM · measuring tape ·
electric motor · GPS amplifier · magnetic tape · sealing foam · ratchet wrench ·
pliers elite

**Never sell — quest valuables:** 🔗 **golden neck chains** *(Chumming needs 3 per stash
point)*

**Never sell — valuables the Scav Case eats:** 🐓 **golden rooster ×2** · gold skull ring ·
**bronze lion** · gold wrist watch · moonshine. **These used to be pure vendor fodder.
Not any more.**

**Standing sell:** spare low-tier armor past one · attachments that don't fit the AK-74M,
AKS-74U or Glock · ammo you don't run · bulky stuff under 10k a slot with no quest on it.

**Mid-raid, type the item name and a `?`** — you get GRAB, IF SPACE or SKIP plus one line.
No live flea prices, so if it's genuinely borderline I'll say "your call" instead of making
a number up.

---

# Stash rules

- **Keep 15–20% free.** Below that you make bad panic calls when you get back.
- **Quest items get their own container, nothing else in it.** Prevents the most expensive
  routine mistake in the game.
- **Two spare kits ready, no more.**
- **Purge order:** bulky and cheap → duplicate attachments → spare ammo → spare armor.
  Never quest items, never hideout materials, never keys.

---

# Hard lessons already paid for

- **Gamma anything uninsurable that's allowed in one** — but check first, because some
  items are barred from secure containers entirely. The REAP-IR is one of them.
- **For anything that can't go in the Gamma, the only protection is the route.** Light
  kit, objective first, extract known before you spawn. That's what lost the REAP-IR.
- **Pick your extract at raid start from the map screen.** Customs extracts depend on your
  spawn, and defaulting to a familiar one while loaded is how good raids die.
- **Reshala's guards hold the rooms, not Reshala.** Bring grenades.
- **🔴 Legs don't work on Killa.** Two raids of evidence: 30–40 rounds, then a full
  60-round mag, and he kept going. Damage to a blacked limb does carry over to the rest of
  the body, but inefficiently — and his health pool is large enough to absorb it. His head
  is behind the **Maska-1SCh helmet and face shield**. **Aim thorax.**
- **Never fight Killa while carrying quest items.** He appears without warning and pushes
  hard. Do the errands first, bank them, then decide whether to take him.
- **Angry Watchman only counts Dorms-zone kills.** Five PMCs elsewhere gave zero progress.
- **🔴 KILLA LEAVES THE MALL. He hunted the player to the EMERCOM checkpoint — outside,
  yards from extract.** ✅*player-confirmed* Three PMCs killed, healing up, arm taken off
  from nowhere, and it was Killa walking in. **"Avoid his zone" is not a plan** — once he
  locks on he follows a long way *(the wiki says the same: "he will follow his target large
  distances out of his patrol route")*. **On Interchange there is no safe side of the map.**
- **🔴 KILLA HOLDS THE ANGLE. The re-peek is what kills you.** ✅*player-confirmed*
  Full sequence: arm blown off from nowhere → **player got behind cover** → **healed to
  full** → peeked and fired → **dead instantly.** Everything was done right except the
  last step. **He waits, pre-aimed, on the angle he last saw you.**
  → **Once he knows where you are, that angle is dead ground. Move to a different one or
  leave — never re-peek the same spot.**
- **Full HP does not save you from him.** The player peeked at 100% and died in the
  exchange. His time-to-kill is effectively instant, so survival is decided by **not being
  seen**, not by how much health or armor you brought.
- **⚠️ OPEN QUESTION: what killed him through a full-health, armored player so fast?**
  If it was a **head shot**, headgear is the gap — **helmets are not researched yet.**

---

# How this works

## The split

**You supply facts. I do bookkeeping.**

| You give me | I give you |
|---|---|
| Quest text and screenshots from your screen | The board, grouped by map |
| What you finished, what progressed | 🔍 / ✓ tags so you only look up what needs it |
| Hideout panels, stash contents | Buy lists across every live quest at once |
| Which map you're running | Overlaps — same kill, same place, same item |
| | What banks permanently vs what resets on death |
| | Memory that survives a fresh chat or a prestige |

**I do not tell you where things are unless you told me first.** That rule exists because
every location I've looked up has been wrong or half-wrong.

## The 🔍 / ✓ tag

Every quest gets one, and it answers **"do I need a map for this?"**

- **✓ JUST GO DO IT** — you already know everything. *"Kill 4 PMCs."* *"Visit 3
  extracts."* Nothing to find, no wiki needed.
- **🔍 LOOK IT UP** — there's one specific spot and the quest doesn't say where.
  *"The kart track."* *"Artyom's car."* *"The logistics office."*

About a third of the board is ✓. Those are the trips to Fandom you can stop making.

## Commands

| You say | I do |
|---|---|
| `raid report: <map>, lived/died, what happened` | Update the board, rebuild the next card |
| screenshot of a quest | File it — name, map, type, objective, tag |
| `<item>?` mid-raid | GRAB / IF SPACE / SKIP, one line |
| `prep <map>` | Buy list, everything live there, split by 🔍 / ✓ |
| `done: <quest>` | Move it to Complete, re-rank |
| `research` | Work the lookup queue below while you're away |

---

# 🎒 KIT BUILDER

Every raid card ends with a kit block. Two parts:

**MUST BRING** — quest-mandated. Keys, markers, items to stash, required weapons. Miss one
and the raid is wasted. Never optional.

**RECOMMENDED KIT** — the loadout, built for the raid and to the player's taste.

## The four modes

Player picks, or says nothing and gets **Basic Kit**.

| Mode | What it is |
|---|---|
| **Optimal** | Best thing for the job. Repetitive but it works. |
| **Basic Kit** | Guns the player likes, on rotation so it's not the same build every week, with armor/rig/backpack picked optimally. **The default.** |
| **For Fun** | Something they'd never pick on purpose. A goofy build, a gun they dislike, a self-imposed handicap. |
| **Themed / RP** | Built to a script. Full Russian, full NATO, army surplus, sniper, budget scav-hunter. |

## Weight rule — match the kit to the raid, not to the wallet

Two things decide it: **how big the map is** and **whether it's a fight or a chore.**

### 🔴 Always heavy — the matrix doesn't apply

| Map | Why |
|---|---|
| **Factory** | Fighting is essentially unavoidable. Always heavy, no exceptions. |
| **Labs** | Raiders. Same reasoning. |
| **Terminal** 🔒 | Endgame. Bosses spawn regularly. **Big and heavy.** |
| **Ice Breaker** 🔒 | Endgame. Bosses spawn regularly. **Big and heavy.** |
| **The Labyrinth** 🔒 | Endgame. Bosses spawn regularly. **Big and heavy.** |

🔒 **= endgame, not unlocked yet.** **They do have quests** — the player just doesn't have
access to them at this level. Nothing to plan around now, but they're a real future chunk
of the board, so `begin research` should cover them under *upcoming quests*.

### Everything else

| | **Chore raid** *(markers, stashes, finds)* | **Fight raid** *(kill counts, bosses, PMCs)* |
|---|---|---|
| **Big map** *(Woods · Streets · Shoreline · Lighthouse · Customs)* | **Lightest.** Lots of walking, little contact. Cheap kit, stay fast, don't risk value. | **Medium.** Mobility still matters — you have ground to cover between fights. |
| **Small map** *(Reserve · Interchange interior · Ground Zero)* | **Light-medium.** Short raid, but contact is likely anyway. | **Heaviest.** Close quarters, constant contact. Armor over speed. |

*(**Customs is big** — confirmed by the player.)*

**The four ways to get it wrong**, in the player's own words:

- ❌ Huge load on a big map — it hinders you badly
- ❌ Light kit on a small map where fights happen constantly
- ❌ Light kit on a fight-based raid
- ❌ Super heavy kit on a chore raid — you're carrying protection you'll never use

## 🛡 ARMOR DOCTRINE — what to bring, by raid

**Same shape as the ammo doctrine: the threat decides the class, the map decides the kilos.**

### Class is decided by what's shooting at you

| Shooting at you | They use | You need |
|---|---|---|
| **Scavs** | low-pen — buckshot, PS, US | **class 4.** Anything more is weight you carry for nothing |
| **PMCs** | AA-tier, class 3–4 pen | **class 5** front + back |
| **Raiders · bosses · Killa** | AP, class 5–6 pen | **class 6 + side plates** |

### Weight is decided by the matrix above

| | **Chore raid** | **Fight raid** |
|---|---|---|
| **Big map** | **≤ 3 kg · class 4–5 · 0% movement** | **≤ 4 kg · class 5 + sides** |
| **Small map** | **≤ 4 kg · class 5** | **Weight stops mattering · class 6 + sides** |
| **Factory · Labs · endgame** | — | **Class 6 all round, no argument** |

**The hard rule: movement penalty ≤ -2% on a chore raid, ≤ -3% on a fight raid.** Above
that you are trading the thing that keeps you alive on a big map for protection you won't
be shot with.

### 👉 Which of yours, specifically

| Raid | Wear | Why |
|---|---|---|
| **Default — 90% of raids** | 🥇 **CPC MOD.1** | **2.75 kg, 0% movement, class 5 front/back/sides.** There is no reason to wear less than this — it costs you nothing to wear |
| **Fight raid, PMCs** | 🥈 **CPC MOD.1 again** — or **CPC (Goons)** | Goons has tougher plates *(147 vs 133 eff)* but **only 18 slots vs 23, and +0.95 kg.** Take it when you want the plates, not by default |
| **Killa · bosses · raiders · Factory · Labs** | 🛡 **Zhuk** | class **6** all round. Accept -7% and 11.5 kg — this is the raid you brought it for |
| **Hobo streak · curveball** | 🎒 **Thunderbolt** | 620 g, 16 slots, nothing to lose |
| **Quest errand, want pouches + a vest** | **THOR CRV + Thunderbolt** | 2.3 kg, **0% movement**, class 4 |

### ⏱ EXPOSURE — the player's rule, and it overrides the matrix

> *"It should matter which one I spend more time on and which is more dangerous — danger
> over time."* ✅**player's rule**

**Risk is not a property of a map. It's `minutes there × threat per minute × what you're
carrying at the time`.** Three things fall out of that, and they change kit calls:

**1. Weight compounds — it buys damage resistance by spending exposure.**
A -7% movement penalty doesn't just make you slower, it keeps you **on the map longer**.
On a big map that's more minutes under threat, so heavy kit is **wrong twice over**:
worse mobility *and* a bigger exposure window.

**2. Late danger costs more than early danger.**
Dying in minute 5 costs a kit. Dying in minute 30 costs the kit **plus everything the raid
was for** — the package, the books, the loot. **Weight the back half of a raid heavier.**

**3. 🔴 THE RULE THIS PRODUCES:**
> **Armor pays where contact is UNAVOIDABLE. Mobility pays where contact is OPTIONAL.**
>
> A big map with avoidable fights is a **mobility** problem — you win by choosing which
> fights happen. A small map, a boss patrol, or a forced corridor is an **armor** problem —
> you can't opt out, so you'd better survive the opening burst.

**Worked against the two live cards:**

| | Interchange | Run B *(Customs → Factory)* |
|---|---|---|
| Long leg | small map throughout | **Customs — most of the raid** |
| Threat density | **Killa 75%, in your objectives** | Customs low-moderate · Factory very high |
| Avoidable? | ❌ **his patrol IS the objective list** | ✅ Customs — you pick fights · ❌ Factory |
| Dangerous leg is… | the whole raid | **short** — Factory is minutes |
| **Verdict** | **🛡 Armor. Zhuk earns it here** | **🏃 Mobility. CPC MOD.1** — don't pay -7% across all of Customs to buy class 6 for a five-minute run to an extract |

**The class 5 → 6 upgrade is small. The 0% → -7% cost is not.** Only buy it when the
unavoidable-contact leg is most of the raid.

### 🎒 SPACE — the other half of the decision

**A rig you can't fit a fight into is the wrong rig.** Full frontier of what you own:

| Setup | Weight | **Slots** | Class | Move |
|---|---|---|---|---|
| **Thunderbolt** alone | **0.62 kg** | 16 | none | 0% |
| **THOR CRV + Thunderbolt** | 2.32 kg | 16 | 4 | **0%** |
| **JPC** *(re-plated)* | **1.83 kg** | **24** | 5–6 F/B | -0.5% |
| **A18 Skanda** | 2.45 kg | **25** | 4 | — |
| 🥇 **CPC MOD.1** | 2.75 kg | **23** | **5 + sides** | **0%** |
| **AVS** | 2.88 kg | 23 | 4 | -2% |
| **CPC (Goons)** | 3.7 kg | **18** ⚠️ | 5 + sides | 0% |
| **Zhuk + Thunderbolt** | 12.14 kg | 16 | **6 + sides** | -7% |
| **Zhuk + LBCR** | 12.88 kg | 18 | **6 + sides** | -7% |

### 🔑 The three space rules

1. **Rig slots are for what you use *during* a fight** — mags, meds, grenades. **Loot goes
   in the backpack.** Never plan rig space around loot.
2. **Floor is ~12 slots for a fight kit:** 5 mags · 4 meds *(IFAK, Salewa, splint,
   painkillers)* · 2 grenades · 1 spare. Below that you're reloading out of a backpack
   mid-fight.
3. **Keys and markers belong in the secure container**, not the rig — that's what saves
   `Supervisor`'s three register keys and the #21WS keycard from a bad raid.

> 🔴 **A vest does NOT block a rig — only an armored rig does.**
> That's why **Zhuk keeps your storage**: it's a vest, so you still wear a rig under it.
> The heavy option costs you movement and kilos, **not slots**.

**The upshot: CPC MOD.1 wins on both axes at once** — 23 slots *and* class 5 all round
*and* 0% movement *and* under 3 kg. Nothing else you own is better at both. The only reason
to leave it home is the Zhuk raid.

### ❌ What to stop wearing

**These are strictly beaten by the two CPCs — same or worse protection, real penalties:**

- **Bagariy** — **-6% movement** for class 5 the CPCs give you at **0%**
- **Osprey Assault** — **6.4 kg** for only class 4
- **Defender-2** — **-4% turn speed**, the worst turn penalty you own. Never in close quarters
- **JPC ×2** — ceramic SAPI plates *(83 effective, the worst material)*. Re-plate before use

### 🔩 And the plates themselves

1. **Class 4 is the floor.** Below that you're wearing weight, not armor.
2. **Class 5 is the default.** It covers everything except AP.
3. **Class 6 only when AP is coming back at you** — Killa, raiders, Labs.
4. **Sides are for fight raids only.** ~1.3 kg each for 15–25 durability — good when you're
   getting flanked, dead weight on a marker run.
5. **Material beats class at the margin.** Given a choice, take **UHMWPE or Titan** over
   ceramic or steel — same class, a third of the weight, far more effective durability.

## 🔫 AMMO DOCTRINE — the player's own rules

**Never name a specific round.** The player has every round marked and knows them cold.
**Name the TYPE** — HP, AA or AP — based on what the raid is actually made of.

### Standard load
**1 primary + 4–5 mags**, depending on round capacity. That's the baseline for every kit.

### What each type is for

**🩸 HP — high damage, low pen**
- Best on **scavs**, and on **limbs of armored targets** *(unarmored zones take the full
  damage)*
- Mostly **cheap**. The very high-damage HP can cost, but still under AP.
- ⚠️ **HP vs armor is NOT an automatic loss.** A 79-damage round into unarmored areas
  kills fast regardless of what they're wearing. It only loses when you hit **armor
  directly**.
- Why it isn't the default: **too situational.** Good for scav killing or a fast gun,
  worse than the alternatives the rest of the time.
- *Scavs wear class 0–1, occasionally 2–3.*

**⚖️ AA — all-around. THE DEFAULT.**
- Player has it marked at **class 3 pen**. **Used almost every raid.**
- Mid damage, mid pen, **average price**. Handles scavs and PMCs both.
- This is what a normal raid gets unless there's a reason to change.
- *PMCs mostly wear class 3–4. Class 5–6 happens but is rare, mostly on endgame maps like
  Labs.*

**🛡 AP — expensive, low damage, high pen**
- Only for **heavily armored targets**.
- ❌ **Bad against scavs.** Five rounds to kill one unarmored scav is a terrible trade and
  the cost hurts the economy more than the raid helps.
- **Only when it's necessary, or on a critical raid that has to go right.**
- 💡 **When running AP, bring a sidearm or second gun for scav killing.** Don't spend AP
  on trash.

### 📊 PENETRATION VALUES — researched ⚠️*web-sourced*

**Higher pen = beats higher armor class. Your HP/AA/AP tiers map onto this scale.**

| 5.56x45 | pen | 7.62x39 | pen | 9x39 | pen |
|---|---|---|---|---|---|
| SSA AP | **57** | MAI AP | **58** | BP gs | **54** |
| M995 | **53** | **BP gzh** | **47** | **SP-6** | **48** |
| **M855A1** ← *player's best* | **44** | PP gzh | 41 | PAB-9 | 43 |
| M856A1 | 38 | PS gzh | 35 | SPP | 35 |
| MK 318 SOST | 33 | T-45M1 | 30 | — | — |
| M855 | 31 | US gzh | 29 | FMJ | 17 |
| FMJ | 23 | FMJ | 26 | | |
| M856 | 18 | | | | |
| MK 255 RRLP | 11 | | | | |

> ✅ **M855A1 at 44 pen is genuinely good** — the player's assumption that it's the best
> 5.56 they own is correct, and it's upper-mid for the whole game. **The only real 5.56
> upgrades are M995 (53) and SSA AP (57).**
>
> ⚠️ **Marginal upgrades the player already owns guns for:**
> **7.62x39 BP (47)** in the **Mk47 Mutant** or **RD-704** · **9x39 SP-6 (48)** in an
> **AS VAL** *(also needed for `Punisher P3`)*. Both beat M855A1 — **by 3–4 points, which
> is not what decides a fight.**

**Still to research: 5.45x39 · 7.62x51 · 9x19 · 12ga · prices for all of it.**

### Picking it for a raid

| Raid is mostly | Bring |
|---|---|
| Scavs *(kill counts, scav-base work)* | **HP** |
| Mixed, or unknown | **AA** — the default |
| PMCs | **AA**, or AP if the raid matters |
| Raiders / bosses / class 5–6 | **AP** + a sidearm loaded HP or AA for scavs |

### Against the current board

| Quest | Target | Type |
|---|---|---|
| `Punisher P3` — 12 scavs, 9x39 | scavs | **HP** |
| `Wet Job P1` — 10 scavs suppressed | scavs | **HP** |
| `Long Line` — 4 PMCs | PMCs | **AA** |
| `Capturing Outposts` — PMCs at the resort | PMCs | **AA** |
| `Job for a Patriot` — 10 PMCs, AK-12 | PMCs | **AA** |
| `Drip Out P1` — 100 Raiders | heavily armored | **AP** + sidearm |
| **Killa** | class 6 | **AP**, thorax only |

## 🔫 GUN PREFERENCES

Player's own ranking. **Basic Kit rotates through Like and I'll Use. For Fun draws from
Don't Like and Hate.**

### ⭐ TOP FAVOURITES — lead with these when nothing else decides it

- **NL545 GP** and **Mk47 Mutant** — the player owns the real-life equivalent
- **HK 416A5** — they've fired a real one

**These three carry personal weight, not just stats.** When a raid has no weapon
requirement and Basic Kit is picking from the rotation, favour them. Good default for a
"just go have fun" raid.

### ❤️ LIKE — the rotation pool
**MDR** · **HK 416A5** · **RD-704** · **M4A1** · **MCX SPEAR** · **Mk16 (SCAR-L)** ·
**Mk17 / SCAR-H** *(same gun)* · **Mk47 Mutant** · **RPK-16** · **NL545 GP** ·
**AS VAL** *(9x39)* · **MP7A1** · **MP7A2** · **Vector .45** · **MP9 / MP9-N** · **MP-153** · **Saiga-12** ·
**M590A1** · **DVL-10** · **T-5000** · **AXMC** · **MK-18 Mjölnir** ·
**Glock 17** · **Glock 18C** · **P226R** · **FN 5-7** ·
**USP** 💛 *(player's words: "I freaking love this gun")* · **SAG AK** · **SAG AK Short** ·
**Glock 19x** · **Sako TRG M10** · **M32A1** · **FN40GL** *(both grenade launchers)* ·
**AUG A3** ⚠️ *only when it can be modded — that's the whole appeal*

### 👍 I'LL USE
**MCX** · **SA-58** · **TX-15 DML** · **AK-545 Short** · **SR-3M** *(9x39)* ·
**Vector 9x19** · **P90** · **MPX** · **UMP 45** · **PP-19-01 Vityaz** · **M870** ·
**MPS AA-12** · **RSASS** · **SVDS** · **G28** · **DMR .338** · **Mosin** ·
**RPD** · **PKM** · **PKP** · **Pecheneg-SP** *(all LMGs)* · **M9A3** · **1911** ·
**M45A1** · **Desert Eagle** · **Benelli M3** · **VSS Vintorez** · **MP-155** · **RSh-12** · **PL-15** · **RPDN** ·
**AKS-74N**

### 😐 MID
**M700** · **SR-25** · **SR-2M** · **AKM series**

**Every AK variant** — AK-74 · 74N · 74M · AKS-74 · AKS-74U · AKS-74UB/UN · AK-105 ·
AK-101 · AK-102 · AK-103 · AK-104 · AK-12 · AKMN · AKMS · AKMSN.
> *"All the same variants so I don't really care for them."* Functional, not exciting.
> Don't build a card around one unless a quest demands it.

### 👎 DON'T LIKE
**RFB** · **MP5** · **MP5K** · **MP5SD** · **OP-SKS** · **SKS** · **9A-91** · **VSK-94** ·
**MP-133** · **KS-23M** · **MP-43 sawed-off** · **M1A** · **SV-98** · **MP-443 Grach** ·
**SR-1MP** · **SVT-40** · **AVT-40** · **Chiappa Rhino 50DS / 200DS** · **AUG A3** ·
**ADAR 2-15** · **VPO-215 Gornostay** · **MP-43-1C**
*(AUG A3 moved to Like — it was here.)*

### 🚫 HATE
**AUG A1** *(the look, and it can't really be modded)* · **G36** · **Vepr KM** · **VPO-209** · **VPO-101** · **ASh-12** · **STM-9** ·
**Saiga-9** · **PP-91 Kedr** · **Kedr-B** · **PP-9 Klin** · **PPSh-41** ·
**MTs-255-12** · **TOZ-106** · **PM** · **PB** · **TT** · **APS** · **APB** · **MP-18**

## 📊 COMMUNITY TIER LIST — dated 06.08.2026, but the content is older

Player-supplied. Far better than the assistant's memory-based attempt, which was ~30 short
and contained two guns that don't exist.

> ⚠️ **The list predates 1.0 and the Season 1 Kord breach**, per the player. So it's
> missing every gun added since — **the NL545 GP is the confirmed example**, and there are
> probably others. Balance changes since then may have moved tiers too.
>
> **Treat it as a strong guide, not a current roster.** A verified up-to-date weapon list
> is still a `begin research` job.

**This is meta performance, not the player's taste.** The two disagree a lot. Optimal mode
uses this; Basic Kit uses the preference tiers above.

| Tier | Weapons |
|---|---|
| **S** | AUG A1 · AUG A3 · DT MDR 7.62x51 · SA-58 · MCX SPEAR · MK47 Mutant |
| **A** | FN40GL · M32A1 · ADAR 2-15 · TX-15 DML · .300 Blackout MCX · HK 416A5 · SKS · OP-SKS |
| **B** | Vector 9x19 · Vector 45 · MPX · PP-19-01 Vityaz-SN · MP5 · P90 · MP7A1 · MP7A2 · SCAR-H · SCAR-L · AS VAL · VSS Vintorez · AKS-74UB · DT MDR 5.56x45 · ASh-12 · SAG AK · SAG AK Short · HK G36 · PKP · PKM · SVDS · Sako TRG M10 |
| **C** | Glock 18C · FN 5-7 · RSh-12 · AXMC · Mk 18 · Saiga-12 · M3 Super 90m · MP-155 · VSK-94 · 9A-91 · SR-2M · VPO-101 · M1A · RFB · RD-704 · AK-103 · AKMN · AKMS · AKMSN · SVT-40 · AVT-40 · VPO-136 · MP-9 · MP9-N · STM-9 · M4A1 · AK-74 · AK-74N · AK-74M · AKS-74 · AKS-74N · AKS-74UN · AKS-74U · AK-12 · AK-105 · KS-23M · AK-101 · AK-102 · AK-104 · RSASS · HK G28 · RPDN |
| **D** | USP-45 · M45A1 · M1911A1 · Glock 17 · Glock 19x · P226R · SR-1MP Gyurza · M9A3 · MP-443 · PL-15 · M700 · VPO-215 · SV-98 · T-5000 · Mosin (Sniper) · Mosin (Infantry) · DVL-10 · MP-18 · UMP-45 · MP5-k · Kedr-B · Klin · Kedr · PPSh-41 · RPK-16 · Saiga-9 · VPO-209 |
| **F** | MP-43 sawed off · APB · APS · MP-43-1C · PB · PM · CR 200DS · CR 50DS · TT · MP-133 · M590A1 · M870 · TOZ-106 · MTs-255-12 |

### 🔀 Where taste and meta disagree — the interesting bits

| | |
|---|---|
| **AUG A1 is S-tier** | and the player **hates** it — the look, and it can't meaningfully be modded. Optimal would pick it; Basic Kit never will. *(AUG A3 is fine, and liked, as long as it's modded.)* |
| **USP is D-tier** | and it's the player's favourite pistol *("I freaking love this gun")*. Taste wins. |
| **M590A1 · M870 are F-tier** | player likes/uses both |
| **SKS · OP-SKS are A-tier** | player doesn't like either |
| **RPK-16 is D-tier** | player likes it |
| **DVL-10 · T-5000 are D-tier** | player likes both |
| **G36 is B-tier** | player hates it |

### ✅ All ranked

**Variants the player ranked as one gun — may want splitting:**
- **DT MDR 7.62x51** *(S)* vs **DT MDR 5.56x45** *(B)*
- **MCX SPEAR** *(S)* vs **.300 Blackout MCX** *(A)*
- **Mosin (Sniper)** vs **Mosin (Infantry)** *(both D)*

### ⚠️ On the player's list but absent from the tier list

**NL545 GP** — ✅ explained: **it's a new gun added after this list was made.** A top
favourite with no meta ranking available.

**Desert Eagle · SR-3M · MP-153** — unexplained. Either also post-list additions, or named
differently.

**Probably just naming:** MK-18 Mjölnir = "Mk 18" · DMR .338 = Sako TRG M10 ·
Benelli M3 = "M3 Super 90m" · RPD = "RPDN"

- **SP-81 signal pistol** — exists but can't kill anyone, so it never belongs in a kit

> 🔴 **The assistant invented two guns that don't exist in Tarkov: the OTs-14 Groza and
> the OTs-38 silent revolver.** Both were offered confidently from memory. Add this to the
> reasons the weapon list needs verifying from a real source rather than recall.- SAG AK · SAG AK Short · AUG A3 · ADAR 2-15
- **MP-155** — the only shotgun left unranked

> ⚠️ **This weapon list came from the assistant's memory, not a source** — Fandom and
> NamuWiki are both blocked here. **Anything added in 1.0 is probably missing.** A verified
> full list is a `begin research` job.

## 🛡 ARMOR — the system, as far as it's understood

**Two ways to wear it:**

1. **Plate carrier** *(armor slot)* + a separate rig on top — flexible, pick material and
   class per plate slot
2. **Armored rig** *(rig slot)* — storage and protection in one, locked to what it takes

**Soft armor is the baseline.** Every rig and carrier has built-in fabric armor, but it's
only **class 2–3**. **The plates are the real protection**, and they're where the weight
comes from. Rigs take **2–4 plates** depending on the model.

**🔴 THE RULE THAT DECIDES EVERY KIT: an armored rig BLOCKS the armor slot.**
Every armored rig you own — AVS, TV-110, Osprey — has **Blocks Armor = Yes**. You wear a
**vest OR an armored rig, never both.** The only rig that combines with a vest is the
**Thunderbolt**, because it has no armor in it at all. ⚠️*web-sourced*

**Material decides how much damage a plate eats — and it's not close.**

The wiki lists an **effective durability** for every plate: raw durability × a material
multiplier. That multiplier *is* the whole heavy-vs-light argument, in one number:

| Material | Multiplier | Verdict |
|---|---|---|
| **UHMWPE** | **×2.96** | best in the game, and light |
| Combined materials | ×2.67 | heavy but excellent |
| Titan | ×2.43 | light-ish, very good |
| Aluminum | ×2.22 | mid |
| Armor steel | ×1.90 | heavy and mediocre |
| **Ceramic** | **×1.67** | worst — and most Russian plates are ceramic |

*(Derived from the wiki's own durability → effective-durability columns; consistent across
all 39 plates.)* ⚠️*web-sourced*

> **A UHMWPE plate absorbs ~1.8× the damage of a ceramic plate of the same class, at half
> the weight.** Class is only "what stops the bullet" — **effective durability is how many
> times it stops it.** Two class 5 plates are not the same plate.

**Best plate per class — by effective durability:**

| Class | Best pick | Mat | Eff. dur | Weight |
|---|---|---|---|---|
| 4 | **Kiba Arms Titan** | Titan | 133 | 2.25 kg |
| 5 | **GAC 3s15m** | UHMWPE | **133** | **0.97 kg** ← featherweight |
| 5 | TallCom Guardian | Combined | 147 | 3.5 kg |
| 5 | Cult Locust | Titan | 146 | 2.56 kg |
| 6 | **GAC 4sss2** | UHMWPE | **148** | 2.7 kg |
| 6 | NESCO 4400-SA-MC | Combined | 160 | 3.6 kg |
| 6 | Cult Termite | Titan | 158 | 3.85 kg |

**Avoid: Kiba Arms Steel** — class 6 but only **95** effective and **5.1 kg**. It is the
**default plate in the Slick**, which is why a stock Slick is a trap. ⚠️*web-sourced*

**Since 0.14, armor only protects the exact zones shown on the model** — no more blanket
coverage.

> 💰 **The key reframe: heavy vs light is a money question, not a protection one.**
> **UHMWPE reaches class 6 while still counting as light**, and holds durability far better
> than ceramic. Steel gets you class 5–6 cheap and slow; UHMWPE gets you class 6 light and
> fast for a lot more roubles. So the armor decision and the budget decision are the same
> decision.
>
> The Slick reputation is **half right**: the carrier really is 0%/0%/0% and 1.3 kg, but it
> ships with **steel** plates. It's a great *frame* wearing bad glass. ⚠️*web-sourced*

### ✅ YOUR SEVEN — identified

**Three are vests *(armor slot)*, three are armored rigs *(rig slot, block the vest)*, and
one is not armor at all.** ⚠️*all web-sourced, unverified*

| # | Yours | Slot | Soft | Dur | Default plates | Move/Turn/Ergo | Weight | Storage |
|---|---|---|---|---|---|---|---|---|
| 1 | **NFM THOR CRV** | vest | cls 3 | 70 | 2× SPRTN Omega **cls 4** | **0% / -1% / 0%** | **1.7 kg** | — |
| 2 | **Korund-VM** *(Black)* | vest | cls 2 | 160 | Korund-VM **cls 5** — F + B **+ 2 sides** | -5% / -2.5% / -3% | 1.9 kg | — |
| 3 | **FORT Defender-2** | vest | cls 3 | 210 | 2× Granit Br4 **cls 5** | -1% / **-4%** / -1% | 5.7 kg | — |
| 4 | **Crye AVS** | rig 🚫 | cls 3 | 112 | 2× SPRTN Omega **cls 4** | -2% / 0% / 0% | 2.88 kg | **23** |
| 5 | **WARTECH TV-110** | rig 🚫 | cls 2 | 70 | 2× GA Steel **cls 4** | -1% / 0% / 0% | 3.5 kg | **23** |
| 6 | **Osprey MK4A** *(Prot.)* | rig 🚫 | cls 3 | 132 | TallCom **cls 5** + 2 side | -3% / -1% / -2% | 6.9 kg | **24** |
| 7 | **Thunderbolt** | rig ✅ | **none** | — | **none** | 0% / 0% / 0% | **0.62 kg** | 16 |

🚫 = blocks the armor slot · ✅ = wearable *with* a vest

**Three things this changes:**

1. **The Thunderbolt is not armor.** It's a 16-slot bag weighing 620 g. It's the rig you
   wear **with** THOR CRV or Defender-2 — that combo is the only way to have a vest *and*
   pouches.
2. ~~The AVS is your best frame.~~ **Corrected below — you own two better ones.** The AVS
   is still excellent *(2.88 kg, 23 slots, -2%, accepts class 6)*, but it is not the top.
3. **Korund-VM is the only thing you own with side plates** — and its coverage list is the
   longest *(throat, neck, groin, buttocks)*. It's your "expect to get shot" vest, at the
   cost of -5% movement.

### ✅ THE REAL ROSTER — from the player's stash screen, 3 pages

**"Seven" was wrong. You own twelve armored rigs.** ✅*player-confirmed — read off screen*
*(Durability shown as current/max, soft armor + fitted plates combined.)*

| Rig | Soft | Default plates | Move/Turn/Ergo | Weight | Yours |
|---|---|---|---|---|---|
| 🥇 **CPC (Goons Ed.)** | cls 3 | TallCom Guardian **cls 5** *(147 eff)* **+ sides** | **0% / 0% / 0%** | 3.7 kg | 187/219 |
| 🥈 **CPC MOD.1** | cls 3 | GAC 3s15m **cls 5** *(133 eff, 0.97 kg)* **+ sides** | **0% / 0% / -1%** | **2.75 kg** | 226/240 |
| 🥉 **AVS** | cls 3 | SPRTN Omega cls 4 *(133 eff)* | -2% / 0% / 0% | 2.88 kg | 210/212 |
| **RBAV-AF** | cls 2 | cls 4 | — | — | **218/218** *(pristine)* |
| **Osprey MK4A (Assault)** | cls 2 | NewSphereTech cls 4 | -3% / -1% / -2% | 6.4 kg | 248/252 |
| **Bagariy** | cls 3 | Korund-VM cls 5 | **-6%** / -1.5% / -2% | 5.1 kg | 147/172 |
| **SP PC V2** | cls 2 | cls 4 | — | — | 181/198 |
| **A18 Skanda** | cls 2 | cls 4 | — | — | 93/175 |
| **TV-110** ×2 | cls 2 | GA Steel cls 4 | -1% / 0% / 0% | 3.5 kg | 151/160 · 108/153 |
| **JPC** ×2 | cls 0 | SAPI III+ cls 5 *(ceramic, 83 eff)* | -0.5% / 0% / -0.5% | 1.83 kg | 83/100 · 29/100 |

**Plus unarmored storage:** Thunderbolt · LBCR ×3 *(incl. Goons Ed.)* · BlackRock ×2 ·
Commando ×2 · Zhuk · Poyas combo

> 🥇 **The two CPCs are the best carriers in the game and you already own both.**
> Zero movement penalty, **class 5 front, back AND sides**, and the MOD.1 does it at
> **2.75 kg** because its GAC 3s15m plates are UHMWPE and weigh under a kilo each.
> **Nothing you can buy at level 30 comes close.** Stop thinking about buying armor.

⚠️ **Two are damaged and worth re-plating, not retiring:** A18 Skanda *(93/175)* and
**JPC 29/100** — the JPCs run ceramic SAPI plates, the worst material in the game.

### 🛡 AND THE HEAVIEST THING YOU OWN — BNTI Zhuk (EMR)

✅*player-confirmed, read off the item panel*

| | |
|---|---|
| **Armor points** | **295.3** |
| **Armor class** | **6 — front, back AND both sides** |
| Weight | **11.52 kg** |
| Penalties | **-7% move · -4% turn · -3% ergo** |
| Plates | FR **45/55** · BK **45/45** · L **20/20** · R **20/20** — all class VI |
| Soft | chest 60/60 · back 60/60 · sides 15/15 · **neck 15/15** |
| Flea | ❌ cannot be listed |

**This is the most protection you own, full stop** — and the back plate is a **KITECO
SC-IV SA**, UHMWPE class 6, one of the best plates in the game and unbuyable anywhere.

> ⚖️ **The real decision it creates:** Zhuk gives you **class 6 all round for -7% movement
> and 11.5 kg**. The **CPC (Goons)** gives you **class 5 all round for 0% and 3.7 kg**.
> **That is the entire heavy-vs-light choice, and you own both ends of it.**
> → **Zhuk for bosses, Labs-tier PvP and anything with Killa in it. CPC for everything else.**

### 🔴 THE PLATE DATA BELOW IS THEORETICAL — YOURS ARE SWAPPED

**The player has swapped plates in most vests and rigs.** ✅*player-stated*
Every "default plates" figure in this section is **what the item ships with**, not what
yours contains. **Do not cost or rank a kit off the default column.**

**The fix is one number.** The item panel shows **ARMOR POINTS** — a single figure that
already folds in class, durability, material and coverage *(Zhuk = 295.3)*. **Open a piece,
read three things — armor points, weight, movement % — and the whole stash ranks itself.**
👉 Player: that panel screenshot, per piece, is all research needs.

### 🎒 ARMOR BY MODE — slots into the kit builder

| Mode | Wear | Why |
|---|---|---|
| **Hobo / cheap** | Thunderbolt only | 620 g, 16 slots, nothing to lose |
| **Light / quest errands** | **THOR CRV + Thunderbolt** | 2.3 kg total, **zero movement penalty**, still class 4 plates |
| **Normal** | **AVS** *(re-plated cls 5–6)* | 23 slots, -2%, best protection-per-kg you own |
| **Heavy / PvP · boss** | **Osprey Protection** or **Korund-VM** | side plates + shoulders; you accept -3% to -5% |

⚠️ **Never** Defender-2 for anything that needs looking around fast — **-4% turn speed** is
the worst turn penalty of your seven.

## 🪖 HELMETS — researched ⚠️*web-sourced*

**The thing nobody tells you: class 4 helmets cover `Head top` + `Nape` ONLY.**
Not ears. **Not the face.** A "class 4 helmet" is not a class 4 head — it's a class 4 *lid*
over an unprotected face. That is very likely how the EMERCOM death happened.

**Class 5 is where coverage widens — and there are only six in the game:**

| Helmet | Class | Covers | Dur | Move/Turn/Ergo | Sound | Weight |
|---|---|---|---|---|---|---|
| **Rys-T** | 5 | Head top · Nape · **Ears** | **90** | 0% / -2% / -3% | ⚠️ High | **2.5 kg** |
| **Altyn** | 5 | Head top · Nape · **Ears** | 81 | -1% / **-4%** / -3% | ⚠️ High | 2.5 kg |
| **Vulkan-5** ×4 | 5 | Head top · Nape · **Ears** | 75 | 0% / -2% / -3% | ⚠️ High | **4.5 kg** |

**🏆 Rys-T is the best of them** — most durability, lightest tier, smallest penalties.
**Vulkan-5 weighs 4.5 kg for less protection.** Altyn's -4% turn is the worst.

⚠️ **All class 5 helmets carry `Sound reduction: High`** — you trade hearing for armor,
which on Interchange is the sense that tells you Killa is coming.

**Best class 4s, if staying light:** **Crye AirFrame** *(0.88 kg, dur 48, 0%/0%/-2%)* and
**MTEK FLUX** *(1 kg, dur 50, **0%/0%/0%** — zero penalties)*. All class 4s have **High
ricochet**, which is real value: glancing hits skate off.

**🔴 Nothing in the game armors the face except face shields and visors.**

### 🚨 YOUR HELMETS — and the one you must NOT wear

✅*player-confirmed from stash screen*

**You own 22 helmets. Three matter:**

| Yours | Class | Covers | Dur | Cost |
|---|---|---|---|---|
| 🚨 **Maska-1SCh KE** **158/158** ✅FiR | **4** helmet **+ class 6 face shield** | Head top · Nape · **Ears** · **FACE · EYES · JAWS** | 108 + **50** | -4% ergo helmet **-13% ergo shield** · High sound reduction |
| **Altyn** 81/81 | **5** | Head top · Nape · Ears | 81 | -1% mv / -4% turn / -3% ergo · High sound reduction |
| **ZSh-1-2M** 113/113 | 4 | + **face shield available** *(class **3** face, Ragman LL3, only -4% ergo)* | 113 | light |

> 🚨 **DO NOT TAKE THE MASKA-1SCh KE INTO A RAID.**
> **That is the `Sellout` handover item** — the quest needs *Killa's Maska-1SCh, found in
> raid*, and **yours already carries the FiR checkmark.** You are sitting on the hand-in
> for a quest that opens at **level 32**. Bringing a FiR item into a raid risks stripping
> the flag, and losing it means killing Killa again to get another.
> **Lock it in the stash until `Sellout` is active.** ⚠️*verify the FiR rule in game*

**The bitter joke: the only class 6 face protection in the game is Killa's own mask, and
he already gave you one.**

**So for actually wearing:**
- **Face protection → ZSh-1-2M + its face shield.** Class 3 face, **only -4% ergo**. Not
  class 6, but it's the difference between a face hit landing and glancing.
- **Max head armor → Altyn.** Class 5, ears covered — but **-4% turn and high sound
  reduction**, and hearing is what warns you he's coming.
- **Light raids → MTEK FLUX** *(50 dur, **zero penalties**)* or **Crye AirFrame** *(0.88 kg)*.
  You own three FLUX and three AirFrames.

## ⚠️ STILL NEEDED FOR THE KIT BUILDER

- **💰 Exact roubles.** See the economy section below — the *structure* is known, the price
  tags are not. tarkov.dev's API is **down** *(GraphQL server unavailable)*, Cloudflare
  blocks direct fetches, and **Fandom does not publish trader prices as text** — only
  screenshots of each trader's stock, where icons can't be matched to items reliably.
  👉 **Player: read armor prices off your own trader screens.** Primary source, beats every
  site, and it's the last piece before cheap/normal/full-send become numbers.

# 💰 ARMOR ECONOMY — what you can actually buy at 30

### ✅ YOUR ACTUAL STANDING — read off the trading screen

**₽3,304,403 · €8,088 · $28,598 · Level 30 · spent ₽4.1M with Prapor**
✅*player-confirmed*

| Trader | LL | Rep | Next level needs |
|---|---|---|---|
| **Prapor** | III | **8.403** | **LL4 = lvl 36 + rep 7.90 → 🔥 REP ALREADY MET, pure level gate** |
| Mechanic | III | 7.067 | lvl 40 + 7.60 |
| Therapist | III | 7.03 | lvl 38 + 7.30 |
| Skier | III | 5.674 | lvl 38 + 5.80 — **rep almost there** |
| Peacekeeper | III | 4.877 | lvl 37 + 6.00 |
| Ragman | III | 3.35 | lvl 42 + 6.50 — furthest on both |
| Jaeger | III | 2.55 | lvl 33 + 7.30 — rep is the wall, not level |
| **Ref** | **II** | **0.40** | **LL3 = lvl 25 ✅ + rep 0.50 → 🔥 0.10 REP AWAY** |
| Fence | I | 1.566 | — |

> 🔥 **Two unlocks are close and both matter for armor:**
> **1. Ref LL3 is 0.10 rep away** *(Ref rep comes from Arena)* — unlocks a second **AVS**,
> **HighCom Trooper TFO**, and **Strandhogg**.
> **2. Prapor LL4 needs only level 36** — your rep already clears it. That's the one that
> opens **class 5 Korund-VM front + side plates** and **Granit 4**. Six levels.

**The gates, in full** *(wiki-derived — and the Prapor line above matched the game screen
exactly, which is a good sign for the rest)*

| Trader | LL3 | LL4 | You at **30** |
|---|---|---|---|
| Jaeger | 17 | **33** | LL4 in **3 levels** |
| Ref | 25 | **35** | 5 levels |
| Prapor | 21 | **36** | 6 levels |
| Peacekeeper | 19 | 37 | 7 levels |
| Skier | 22 | 38 | 8 levels |
| Mechanic | 26 | 40 | 10 levels |
| **Ragman** | 27 | **42** | **12 levels — the armor trader is the furthest away** |

### 🔴 Three rules that decide the whole armor economy

**1. No trader sells a class 6 plate. At any loyalty level. Ever.**
Class 5 is the purchasable ceiling, and at *your* level it's worse than that.

**2. Almost every good plate is flea-banned.** Cannot be listed:
GAC 3s15m · GAC 4sss2 · KITECO SC-IV SA · Cult Termite · Cult Locust · TallCom Guardian ·
NESCO 4400-SA-MC · Granit Br4. **Only two decent plates are flea-tradeable: Kiba Arms
Titan** *(cls 4, 133 eff, 2.25 kg)* **and SPRTN Omega** *(cls 4, 133 eff, 4.39 kg)*.

**3. Therefore the good armor is looted, not bought.** Every class 6 plate in the game, and
the best class 5s, reach you exactly two ways: **found in raid, or pre-installed in a
carrier you found.**

### What you can buy *right now* at LL3

| Plate | Class | Mat | Eff. dur | Where |
|---|---|---|---|---|
| **SPRTN Omega** | 4 | Combined | **133** ← best buyable | **Skier LL3** |
| NewSphereTech III | 4 | Aluminum | 100 | Peacekeeper LL3 |
| 6B33 *(front)* | 4 | Steel | 95 | Prapor LL3 |
| Global Armor's Steel | 4 | Steel | 86 | Skier LL3 |
| SPRTN Elaphros | 4 | Ceramic | 75 | Peacekeeper LL3 |
| Korund-VM *(back)* | 5 | Steel | 76 | Prapor LL3 |
| SSAPI III+ *(side)* | 5 | Ceramic | 25 | Peacekeeper LL3 |

**Note what this means: your AVS and THOR CRV already ship with SPRTN Omega** — the single
best plate purchasable at your level. You are not under-plated; the shop just has nothing
better to sell you.

**Locked behind LL4** *(and therefore behind levelling)*: Korund-VM front + sides
*(Prapor 36)* · Granit 4 *(Prapor 36 / Ref 35)* · SAPI III+ *(Ref 35)*.

### 💡 The money conclusions

- **Do not sell looted plates.** Most can't be flea'd, so they're worth little in roubles
  but a lot in kit. **A looted GAC 4sss2 or Cult Termite is free class 6 you cannot buy at
  any price.** Stash them.
- **Buy frames, loot glass.** Carriers are purchasable; the plates that matter aren't.
- **The AVS is where looted plates go** — it takes class 6, weighs 2.88 kg, carries 23 slots.
- **⭐ Check `Audiophile`** — completing that Ragman task puts the **Osprey MK4A (Assault)**
  in reach at **Ragman LL3**, which you already have. *(Also at Ref LL3.)*
- **Ragman LL4 at level 42 is the long-term armor goal** — it's 12 levels out, further than
  every other trader. Nothing about armor buying improves much until then.

# 🎲 CURVEBALLS — burnout prevention

> **The player burned out last wipe.** Not from difficulty — from **quest, quest, quest**
> with a stash stacked to the brim that never got used. Same two or three guns every raid,
> everything else collecting dust. **That is the failure mode this section exists to
> prevent.**

## The rule

**Mostly quests — that's still the spine.** But curveballs are **the assistant's call, on
no schedule at all.**

> 🔴 **NO FIXED CADENCE. The player wants to be surprised.** Never say "it's been four
> raids." Never telegraph one coming. Just decide, and hand it over as the next raid.
>
> **If one lands well, throw another right after.** Two or three in a row is fine when
> they're working. Judge the moment, not a counter.

**Signals worth reading** — not rules, just things that suggest it's time:
- Same gun several raids running
- A long stretch of pure-quest raids
- Reports that read tired, or a run of deaths
- A stash that's clearly filling up
- A big win worth riding

## The curveball types

### 🃏 Pistol Factory Run
**Factory. PMC. Pistol only.** No primary. Go fight.

⚠️ **PMC, not scav** — a scav gives you whatever it gives you. The point is walking into
the most violent map in the game *deliberately* underequipped.

Costs almost nothing, and Factory guarantees the fight so there's no wandering. Pure
skill test in the shortest raid available.

### 🔫 Stash Rotation Run
**The assistant picks a gun from the locker that hasn't been used.** Not a favourite. That
gun, that raid, no negotiating.

> **This is the direct fix for the burnout cause.** A locker full of guns that never leave
> the stash is just dust. If it's good enough to keep, it's good enough to lose.

### 💰 Money Run
**No quests at all.** Pure loot. The **smugglers' base on Shoreline** filled a 70lb bag in
one pass — start there.

### ⚔️ PvP Run
Go hunting PMCs. No objectives, no marker to place, no item to find.

### 🎯 Challenge Run
A self-imposed handicap. Pick one and commit:

- **Sniper only** — bolt-action, no backup
- **Shotgun only**
- **Iron sights only** — no optics on anything
- **One mag** — what you load is what you get
- **Scav-kit-only PMC run** — dress like a scav, fight like a PMC
- **Something off the Hate list**, on purpose

The assistant picks, the player doesn't get a vote.

### 🧟 Scav Run
Free kit, **Fence rep**, zero risk. The cheapest progress on the board and it never costs
a rouble.

### 👹 Boss Hunt
**Pick one boss. Go only for him. Ignore every quest on the map.**

Seven left — Sanitar, Killa, Glukhar, Shturman, Kaban, Kollontay, Zryachiy.

⚠️ **Always name a fallback, because he might not spawn.** Check
[eftboss.com](https://eftboss.com) first if possible. If the boss isn't there, the raid
becomes a **loot run or a PvP run** — never a wasted trip. Say the fallback up front so it
doesn't feel like a bust.

### 🔩 Hideout Run
**No quests. Loot for the hideout only.**

There are **400+ items** outstanding — 50 wires, 20 power cords, 16 relays. Nothing else
on the board addresses that backlog, and it quietly gates the Bitcoin Farm and
Intelligence Center 3 *(flea fee −30%)*. Pick a map with good industrial loot and fill the
bag.

### 💎 Full Send
**Take the single most expensive kit in the stash to the hardest map available.** Labs,
Reserve, wherever the fight is real. **Not somewhere easy** — a best-in-slot kit on a soft
map proves nothing and risks nothing.

The mirror image of Stash Rotation. That one says *use the gun you never touch* — this one
says **use the gun you're saving.** Both attack the same disease: gear sitting in a locker
doing nothing. **If it's too good to lose, it's already wasted.**

### 🥋 Hobo Streak
**The assistant assigns a cheap kit. Run it until it gets you killed.**

- Survive and extract → **run the same kit again next raid.** Repair it, restock the mags,
  go back in.
- Die → **the streak ends.** Report the number.
- Quests still count while it's running — this isn't instead of progress, it's a
  constraint on how you make it.

**Why it works:** cheap gear the player would never otherwise touch gets used, and every
extract raises the stakes on the next one. A 5-raid streak on a ₽80k kit is a better story
than any single good raid.

> **Track the streak. Say the number every time.** *"Hobo Streak: raid 4."* That counter is
> the whole point.

### 🌙 Night Run
**Force a night raid.** Different map entirely once the lights go out — different routes,
different fights, different pace. The player already ran one for `Thirsty – Hounds` and it
went well.

## What the assistant should track

- **Which guns have actually been run**, so Stash Rotation can name one that hasn't
- **Whether the stash is growing** — a growing stash means gear isn't being used
- **The active Hobo Streak**, if one is running, and the best streak so far

### 🏆 Hobo Streak record

| | |
|---|---|
| **Current streak** | none running |
| **Best streak** | — |

## Tone

**Offer it, don't lecture.** *"You've run the AK-12 three raids straight — take the MDR to
Woods and let the quests wait a run."* Not a wellness check.

---

# What I actually can and can't do

Written down because it explains every mistake in this file's history.

## Can't

- **I don't render web pages.** No JavaScript, no images, no layout. A page becomes plain
  text. **If a wiki shows a location as a map screenshot with a marker on it, I see
  nothing** — only the caption. This is why my locations have been vague or wrong.
- **Fandom is blocked** — HTTP 402 through this environment's proxy. Tested again and
  still failing. It's the best Tarkov source and I cannot read it.
- **tarkov.dev, tarkovforge, tarkov.help** — blocked, dead, or JS shells with no readable
  content.
- **Live JS data** — eftboss.com spawn percentages and anything else generated in the
  browser are invisible.

## Can

- **Web search** — but it returns a *summary written by a small model from search
  snippets*, not the page. Third-hand. That channel produced every one of these:

| What I said | What was true |
|---|---|
| `Punisher P3` — Customs, 25 Scavs, AKS-74U, DVL-10 | Reserve, 12 Scavs, 9x39, VSK-94 — **wrong on all four** |
| `Chumming` has an Interchange stash point | It doesn't. Woods and Customs only. |
| `Supervisor` — hand a key to Ragman on Customs | Stash 3 keys on Interchange |
| `Wet Job P3` — *locate* Artyom's car | **Mark** it. Cost a raid. |
| `Job for a Patriot` — any location | Streets, Shoreline, Ground Zero only |
| `Needle in a Haystack` — 4 spots | 6. Missed the Interchange kart track. |

- **Drive a headless browser and read the screenshot visually.** Proven working in this
  environment — the loop is fine, the network policy is what blocks Fandom.
- **Read your screenshots.** This has never once been wrong, because it's your screen.

---

# Moving to desktop

**Why it's worth it:** Claude Code on your PC uses *your* network. No proxy, no 402 —
Fandom loads. And with a browser tool I can screenshot a page and **see the map images**,
which is the exact thing I'm blind to now.

**What it fixes:** the 🔍 lookups, and only those. Locations are the one category where
wiki data holds up, because map geometry barely changes between patches.

**What it does NOT fix:** staleness. Reading a 0.14 page perfectly still returns 0.14
answers. `Punisher P3` would still say Customs/25/AKS-74U — I'd just be quoting it
accurately instead of garbling it. **Your in-game text stays authoritative for objectives,
counts, weapons and maps. Forever.**

## Setup — do this once

> **The whole point is the network.** A cloud session goes out through a proxy that blocks
> Fandom. Claude Code running on your own PC uses your own connection, so Fandom, tarkov.dev
> and eftboss all load normally.

### 1. Install Claude Code on the PC you play on

Two options — **the desktop app is the easy one.**

| | |
|---|---|
| **Desktop app** *(recommended)* | Download Claude Code for Windows from **[claude.com/claude-code](https://claude.com/claude-code)**. Installer, no terminal. |
| **Terminal** | Windows PowerShell: `irm https://claude.ai/install.ps1 \| iex` — then run `claude` in any folder. |

Sign in with the same account you're using now. **Same subscription, no extra cost.**

### 2. Make a folder for this file

Anything works — `C:\tarkov\` is fine. Put **`tarkov.md`** in it.

Open Claude Code **in that folder** (the desktop app has a folder picker; in a terminal,
`cd C:\tarkov` then `claude`). I can read *and write* files in the folder I'm opened in,
which is what makes the file self-updating instead of you re-pasting it.

### 3. Add a browser so I can see map images

In that same folder, run once:

```
claude mcp add playwright -- npx @playwright/mcp@latest
```

This is the piece that matters. Without it I read wiki pages as **plain text** and every
map screenshot — the marker showing where the thing actually is — is invisible to me.
With it I load the page, screenshot it, and **look at it**.

### 4. Check it worked

Open Claude Code in the folder and say:

> `open the escapefromtarkov fandom page for Capturing Outposts, screenshot it, and tell me what the map image shows`

If I describe an actual map image, setup is done. If I say the page won't load or I only
see text, the browser step didn't take — tell me the error.

### 5. Then say `begin research` and walk away

## Where the file lives now

**`tarkov.md` is committed to `mimicsky/github-slideshow`** on the branch
`claude/tarkov-desktop-helper-3b88yo`.

That means it's backed up off your PC and any session — desktop, web, phone — can pull the
current version instead of you pasting 72KB into a fresh chat. On the desktop, clone it
once:

```
git clone https://github.com/mimicsky/github-slideshow.git
cd github-slideshow
git checkout claude/tarkov-desktop-helper-3b88yo
```

Open Claude Code in that folder and I'm caught up with zero pasting. When something
changes, I edit, commit and push — and the web session sees it too.

> ⚠️ **This repo is public.** Nothing in this file is sensitive — it's quest notes — but
> know that it's readable by anyone. If you'd rather it weren't, say so and we move it to a
> private repo.

## ▶ THE `BEGIN RESEARCH` PROTOCOL

**Trigger phrase: `begin research`**

When the player says this and walks away, work until they're back. This is the standing
instruction set — follow it exactly.

### Scope: EVERY active quest, not just the blanks

**Do not skip a quest because this file already has details for it.** Lines in here that
came from search summaries have been wrong before — `Punisher Part 3` was wrong on map,
count, weapon and reward at once. **Check every line that isn't marked as player-confirmed.**

Work in this order:

1. **Every ACTIVE quest** on the board, one at a time
2. **Upcoming quests** — the next part of every chain currently in progress, plus the
   quest lines on the **locked endgame maps (Terminal, Ice Breaker, The Labyrinth)**, so
   the player knows what's coming before it unlocks
3. **The full armor system** — see the Armor section. Carriers, armored rigs, vests,
   plates: slot, class, material, weight, penalties, price. This one is explicitly
   delegated to research.
4. **The current weapon roster** — the player's tier list predates 1.0, so anything added
   since is missing. Return **only guns not already ranked** in this file.
5. **Anything else this folder needs** — key requirements and prices, boss mechanics and
   spawn locations, item spawn spots, what unlocks what, trader loyalty requirements

### For each quest

- Open the Fandom page in the browser
- **Screenshot it and read the screenshot** — the map images are the whole point, and they
  don't come through as text
- Record **where things are**: which building, which floor, which room, what landmark, what
  the thing looks like
- Note any key or item that has to be carried in

### 🔴 The three rules that keep this from ruining the file

**1. NEVER overwrite a player-confirmed line.** Anything in *Confirmed objectives*, or
anything the player stated directly, is ground truth. Web data does not replace it, ever.

**2. Disagreements become CONFLICTS, not corrections.** If the wiki contradicts something
the player confirmed, write it up like this and leave both standing:

```
⚠️ CONFLICT — Punisher Part 3
  Player screen: Reserve · 12 Scavs · 9x39 · 7 lower half-masks
  Fandom:        Customs · 25 Scavs · AKS-74U · DVL-10 reward
  → Player's screen wins. Flagged only so it can be re-checked in game.
```

**3. Tag everything web-sourced.** Every line added by research carries
**`⚠️ web-sourced, unverified`**. The player must always be able to see at a glance which
lines came from their own screen and which came from a wiki.

### What research is allowed to write

| ✅ Write these | ❌ Never write these from the web |
|---|---|
| Locations — building, floor, room, landmark | Objective counts *(how many kills, how many items)* |
| Which key opens what | Weapon or gear restrictions |
| What an item looks like | Which map a quest is on |
| Key prices and where keys spawn | Whether it needs an extract |
| Boss spawn spots and behaviour | Rewards |
| Chain order — what unlocks next | |

**Why the split:** it isn't that Fandom is unreliable — the player uses it constantly and
finds it accurate. It's that **the in-game screen is a primary source and a wiki is a
secondary one.** When they agree, nothing is lost. When they disagree, the screen is the
one that definitely reflects this patch and this account.

**Note on this file's error history:** the wrong answers logged here came from *search-
result summaries* that blended Fandom with gamemaps, tarkov101 and other sites, then
compressed them. **They were never confirmed to be Fandom's errors.** Reading the actual
page should be substantially more accurate than anything in that error table suggests.

### When the player comes back

Report:
1. How many quests were researched
2. **Every conflict found**, listed — these are the ones to check in game
3. What's still missing or undocumented anywhere

# 🗂 THE PLAN — in order

**1. Quest screenshot dump** — ✅ **DONE**
All ~100 quests transcribed from the player's screen. Every map filled in, no blanks.

**2. Hideout tally rebuild** ← *next*
The old tally counted shortfalls, but every panel reads X/Y from the **same stash** — a ✓
in three modules can be the same ten items. Needs **names for the items that showed as
satisfied**, especially the gold/tan branching thing *(28 across Shooting Range, Vents and
Generator)*, the blue/white tool *(18)*, the battery *(11)*. **Turns the broken 214 into
the real ~400.**

**3. Desktop setup** ← *steps written, waiting on the player*
Claude Code + Playwright on the player's PC. **Full instructions are in *Moving to
desktop*.** The browser step is the one that matters — without it I read wiki pages as text
and every map image stays invisible.

**4. `begin research`** — everything the desktop session can do that this one can't:
- **Armor** — every carrier, armored rig, vest and plate: slot, class, material, weight,
  penalties, price. Plus which of the player's seven is which type.
- **Budget tiers** — the player has **delegated this decision to the desktop session**,
  which will have gun prices, armor prices and stash contents in front of it. Work out
  what cheap / normal / full send actually mean in roubles and write them in.
- **The post-1.0 weapon roster** — return only guns not already ranked.
- **Locations** for every 🔍 quest, and the upcoming-chain and endgame-map quests.

---

# 📋 RESEARCH QUEUE

> ✅ **The name-gathering job is DONE.** The screenshot dump filled every blank — all ~100
> quests now have a name, map, class and type. **Research is no longer about finding
> quests. It's about finding places.**

## What research still needs to produce

### 1. Locations for every 🔍 quest
Roughly **75 quests are tagged 🔍**, meaning the objective names a spot the text doesn't
locate. That's the whole job now. **Biggest untouched blocks:**

- **Streets — 20 of its 24 are 🔍.** Almost nothing is known about any of them.
- **Lighthouse — 10 of 10 are 🔍.** Nothing known.
- **Reserve — 11 of 13 are 🔍.** Only Punisher P3 and A Fuel Matter have detail.
- **Woods — 6 unknowns** *(Steady Signal, Metal Birds, Thrifty, Shipping Delay P1, A
  Helping Hand, Hiking, Swift)*

### 2. The full armor system
Every carrier, armored rig, vest and plate — slot, class, material, weight,
movement/turn/ergo penalty, price. Plus **which of the player's seven is which type**:
THOR CRV · AVS · WARTECH TV-110 · Korund-VM · Defender-2 · Thunderbolt · Osprey MK4A.

### 3. Budget tiers
**Delegated to the desktop session.** With gun prices, armor prices and stash contents
available, work out what **cheap / normal / full send** actually mean in roubles and write
them in. Also defines "cheap kit" for the Hobo Streak.

### 4. The post-1.0 weapon roster
The player's tier list predates 1.0 and the Season 1 Kord breach. **Return only guns not
already ranked** — confirmed missing so far: **NL545 GP**, and unexplained absences of
**Desert Eagle · SR-3M · MP-153**.

### 5. Upcoming and endgame quests
Next part of every chain in progress, plus the quest lines on **Terminal, Ice Breaker and
The Labyrinth** — locked endgame maps that do carry quests.

## ❓ Open questions for the player

- **⭐ Type-column icon** on `The Courier` and `Is This a Reference?` — not crosshair,
  magnifier or hand. What is it?
- **⭐ Class-column icon** on `Shooter Born in Heaven` — looks like an arrow, not I/II/III.
  Elite tier?
- Are any quests **gated behind a skill level**?
- Did `Fuel Crisis` supply its own MS2000s? *(academic now — it's done)*
- **Hideout:** names for the items that showed as ✓ — the gold/tan branching thing
  *(28 across Shooting Range, Vents, Generator)*, the blue/white tool *(18)*, the battery
  *(11)*, and about a dozen smaller ones.

---

# Where my info comes from

**Works:** gamemaps.net (via curl) · web search
**Blocked or dead for me:** Fandom wiki · tarkov.dev · tarkovforge · tarkov.help

**Fandom works fine for you though** — that's why complex quests say *look up on fandom*.

**gamemaps is pre-1.1** and it shows: no entry at all for `Chemical Experiments` or
`Supplements`, and its level gates are wrong.

| Trust it for | Don't trust it for |
|---|---|
| Where things physically are | Level gates — proven wrong |
| Spawn spots, room and building names | Which trader gives what |
| Extract names | Item values and rewards |

**Your in-game text wins every time.** I supply the where.

> 🔴 **The Punisher chain is fully reworked in 1.1 and every source is wrong about it.**
> Part 2 was wrong (said 12 suppressed + 10 masks, really 15 with an AKM series). Part 3
> was wrong on **map, count, weapon and reward** — all four. **Do not trust any lookup for
> Punisher Part 4 or later.** Open it in game and send me the text.
>
> Interesting detail: the "lower half-masks" this file once attached to Part 2 were real —
> they just belong to **Part 3**, and it's 7, not 10.

## Your department, not mine

Two things you know better than I do. **I don't advise on these unless you ask:**

- **Ammo.** You have it covered and have everything marked for what penetrates what.
  I won't hand you pen charts.
- **Flea market.** You already understand it and how you trade. I won't second-guess a
  sale.

If I ever start giving advice in either lane, tell me to stop.

---

# ✅ COMPLETE

Kept on purpose. These only come back if you **prestige or wipe**, and when that day comes
this is the shortcut — you'll already know what each one wants.

## Customs

**Break the Deal** · Customs · ?
(no details recorded)

**Private Club** · Customs · ?
(no details recorded — ⚠️ sites list this at level 24, it was active for you at 21)

**Chemical – Part 1** · Customs · FIND
🔑 Dorm room 220 *(you own it, reusable)*
(2 items — secure folder in the train carriage, plus one inside Dorm 220)

**Chemical – Part 2** · Customs · ?
(no details recorded)

**Chemical Experiments** · Customs · CHORE
(place the corrugated hose on the 2nd floor of the med lab — was called
`Spa Tour - Part 7`)

**Supplements** · Customs · FIND
(chemical vial + **4 respirators** — undocumented anywhere, we worked it out from your
screen)

**Huntsman Path – Trophy** · Customs · FIGHT
(kill Reshala — the TT had already been handed in, so this was the only objective left)

**The Punisher – Part 1** · Customs · FIGHT
(25 scavs with an AKS-74U, anywhere on the map)

## Shoreline

**I Need More Power** · Shoreline · CHORE
🔑 Health Resort west wing **219**
(turn on 2 generators — east wing 220 and west wing 219 — one raid, must extract)

**Anesthesia** · Shoreline · CHORE
(plant MS2000 markers at 3 trading posts, must extract)

**Rigged Game** · Shoreline · CHORE
(plant MS2000 markers on 3 medical containers — Health Resort, cottages, pier)

**Chemistry Closet** · Shoreline · FIND
🔑 Health Resort **office key, blue tape**
(find Sanitar's office)

**Health Care Privacy – Part 2** · Shoreline · FIND
🔑 **Health Resort west wing 306** — the key you already owned
(find TerraGroup documents in a room, hand them over)

**Seizing the Initiative** · Customs → Shoreline · CHORE
(customs transit shoreline, survive and extract there)

**Nothing Fishy About This** · Shoreline · FIND
(find Ragman's SUV)

**The Punisher – Part 2** · Shoreline · FIGHT
(15 scavs with an **AKM series** weapon)

**Wet Job – Part 1** · Shoreline · FIGHT
(10 scavs with a **suppressed** M4A1, ADAR or TX-15)

**Tracker** · Shoreline · FIND
(Health Resort — reservoir room, secure folder on blue barrels room 108 east wing, second
cargo part in the west wing basement)

**Master Key** · Shoreline · FIND
(key to the closed premises, **on a chair in the bunker north of the resort** — only spawns
while active, must extract with it)

**Thirsty – Hounds** · Shoreline · FIGHT 🌙
(**12 scavs between 22:00 and 07:00** — night raid only)

**Thirsty – Breadwinner** · any · FIND
(**2× Propane tank 5L found in raid** — OLI on Interchange, the smugglers' base on
Shoreline, or any fuel/building material spawn)

**No Swiping** · Shoreline · FIND + FIGHT
(find the smugglers' base, **10 kills** in the base area — the base is also excellent loot)

**Wet Job – Part 2** · Shoreline · CHORE
(mark the fishing table at the island fishermen's dwelling with an MS2000 — no need to
survive)

**Tarkov-Style Diplomacy** · Shoreline · FIND
🔑 Cottage back door key *(for the villa half)*
(**surgery kit** on top of a wardrobe, pier office 2F · **ophthalmoscope** in a potted
plant, villa 2F left room)

**Wet Job – Part 3** · Shoreline · CHORE
(mark **Artyom's car** with an MS2000 — yellow, by a yellow bus and a police car near the
tunnel before the barge — then survive and extract)

**Fuel Crisis** · Interchange · CHORE
(marked the fuel tank by the power station and one in the northern territory)

**Pathfinder** · Interchange · CHORE
(visited Railway Exfil, Emercom Checkpoint and Power Station V-Ex)

**Hot Delivery** · Interchange · CHORE
(6B47 helmet + ComTac 2 headset in the trash at Avokado · Gzhel-K in the trash by the
outdoor stage across from Ultra's main entrance)

**Minibus** · Interchange · CHORE
(3 yellow minibuses marked with MS2000, extract as PMC)

**A Big Loss** · Interchange · FIND
🔑 OLI logistics key
(OLI cargo route documents from the logistics office)

**Survivalist Path – Wounded Beast** · ? · ?
(no details recorded)

## Factory

**Chemical – Part 3** · Factory · FIND
(grab the bright yellow syringe — **looks like a pen**)

**Postman Pat – Part 1** · Factory · FIND
(letter off the messenger's body)

**Scout** · Factory · FIND
(find all 3 Factory extracts)

**Exit Here** · Factory · CHORE
(extract through the main exit — pairs with Scout, one run did both)

**Black Swan** · Factory · CHORE
(mark **1** heat exchanger with an MS2000 — sources said 3, they were wrong)

**Possessor** · Factory · ?
(no details recorded)

**All Is Revealed** · Factory · ?
(no details recorded)

## Multi-map

**Every Hunter Knows This** · Factory + Customs · FIND
(2 tripwire spots — Factory breach room, and the Customs 3-story dorm stairs)

**All This Filth** · any · FIGHT
(kill scavs, any location — ⚠️ the wiki says "kill Shturman 20×", which is completely
wrong for 1.1)

**A Healthy Alternative** · ? · ?
(⚠️ **this is the one that failed `One Less Loose End`** — they were a choice branch)

**Postman Pat – Part 2** · ? · ?
(⚠️ **unconfirmed** — this was listed as both done and not started. Check your screen and
tell me which)

## Gunsmith — all four done at the bench

**Gunsmith – OP-SKS** · hideout · CHORE
**Gunsmith – Model 870** · hideout · CHORE
**Gunsmith – M4A1** · hideout · CHORE
**Gunsmith – P226R** · hideout · CHORE

(no raid, no risk, pure Mechanic rep — which feeds Mechanic LL4 for Kappa. They're
stat-based, so any parts that hit the numbers work. **Keep the P-2 foregrip** for the next
tier.)

## ❌ Failed

**One Less Loose End** · ? · ?
(killed by finishing `A Healthy Alternative` — they were mutually exclusive)

> ⚠️ **This will happen again.** Before finishing anything that reads like picking a side,
> check what it locks out. `Chemical - Part 4` is the live example: three branches, and
> taking one fails the other two.

---

# Keeping this updated

Tell me what happened and I edit, commit and push. Paste this file into any new chat and
I'm caught up straight away.

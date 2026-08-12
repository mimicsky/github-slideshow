# Tarkov Co-Pilot — Operating File

**You play. I track.** This file is the shared brain: what I need to know, how you feed
me updates, and how I decide *keep / sell / stash / use*.

> **Status:** cold start. The `FILL IN` blocks are the only thing standing between this
> and a working tracker. Answer the [First Sync](#0-first-sync) questions once and I'll
> maintain the rest.

---

## 0. First Sync

Answer these in chat (rough is fine, I'll clean it up):

1. **Level, PMC faction (USEC/BEAR), current roubles, stash size.**
2. **Trader loyalty levels** — Prapor / Therapist / Skier / Peacekeeper / Mechanic / Ragman / Jaeger / Fence / Ref.
3. **Active quests** — screenshot the task list or just name them, I'll expand the requirements.
4. **Hideout** — which modules are built, which are next, what's missing.
5. **Stash dump** — the stuff you don't know what to do with. Photo or a list.
6. **Play style** — how many raids a session, do you hatchet/scav-run, are you a "die
   with a good kit" player or a "run cheap until quest done" player? This changes every
   sell/keep call I make.

After that, the only thing I need per session is a **raid report** (see below).

---

## 1. How to talk to me

Short commands. No formatting required.

| You say | I do |
|---|---|
| `raid report: <map>, <survived/died>, <what I brought back>` | Update stash, flag quest progress, tell you what to sell |
| `keep or sell: <item>` | One-line verdict + reason + best sell channel |
| `what now` | Next task to run, which map, what to bring, what to look for |
| `prep <map>` | Loadout budget, keys to bring, quest objectives live on that map |
| `stash check` | What to purge first, ranked by roubles-per-slot |
| `hideout` | Next module worth building and exactly what's still missing |
| `money` | Fastest realistic path to your next cash goal |
| `wiped` / `new wipe` | Reset this whole file to zero |

If I don't have the info to answer, I'll ask **one** question, not five.

---

## 2. Character State

```
Level:            FILL IN
Faction:          FILL IN
Roubles:          FILL IN
Stash:            FILL IN (size / upgrade status)
Survival rate:    FILL IN
Cash goal:        FILL IN (e.g. "3M for a graphics-card-fed bitcoin farm")
```

### Trader Loyalty

| Trader | LL | Next LL needs | Notes |
|---|---|---|---|
| Prapor | | | |
| Therapist | | | |
| Skier | | | |
| Peacekeeper | | | |
| Mechanic | | | |
| Ragman | | | |
| Jaeger | | | |
| Fence | | | rep, not LL |
| Ref | | | |

> Loyalty gates are the real progression bottleneck, not level. Rep comes from
> **completing tasks**, and it's the cheapest lever you have — I'll always prefer a
> quest turn-in over a flea sale when the rep matters.

---

## 3. Task Board

The working list. I keep this current; you just tell me what you turned in.

### Active

| Task | Trader | Map | What it actually needs | Blocked on |
|---|---|---|---|---|
| FILL IN | | | | |

### Next up (unlocked, not started)

| Task | Trader | Why it's worth doing now |
|---|---|---|
| FILL IN | | |

### Collecting for (not started, but hoard the items)

This is the important one. Half of Tarkov is **not throwing away an item you'll need in
nine levels.** Anything on this list is an automatic KEEP even if flea says it's worth
selling.

| Item | Qty needed | For | Have |
|---|---|---|---|
| FILL IN | | | |

### Done

<!-- I'll append here so we never re-run a finished task -->

---

## 4. Keep / Sell Doctrine

The rules I apply, in priority order. When two conflict, the higher one wins.

1. **Quest item → KEEP.** Found-in-raid status is not recoverable. Losing a quest item to
   a sell is a multi-raid setback; the roubles never make that back.
2. **Hideout material for a module we're actively building → KEEP.** Same logic.
3. **Barter input for something we want → KEEP,** but only if the barter beats cash cost.
   I'll check that math, not vibe it.
4. **Roubles-per-slot decides everything else.** A 1x1 worth 90k beats a 4x4 worth 200k.
   Stash space is the real currency at your level.
5. **Sell channel:** trader when the spread is thin, flea when it's wide enough to justify
   the fee and the wait. I'll name the channel, not just say "sell it."
6. **Insurance changes the math** on gear — cheap-but-insured beats expensive-and-lost.
7. **When in doubt on a rare item → KEEP one, sell the rest.** Cheap insurance against a
   task we haven't unlocked yet.

### Standing KEEP list

Generic high-value / high-demand categories. I'll narrow this to *your* task list once we
sync, so you're not hoarding things you'll never need.

- **Electronics:** graphics cards, CPU fans, motherboards, capacitors, phones, military
  circuit boards — hideout and Bitcoin-farm economy.
- **Medical:** LEDX, ophthalmoscope, defibrillator, medical bloodset, IFAKs/Salewas held
  back for medical tasks.
- **Tools & hardware:** toolsets, wrenches, screws, bolts, drills, wires, corrugated
  hoses, fuel conditioner — hideout is a hardware store.
- **Keys.** Keep unknown keys until I've checked them. Some are worth more than a raid.
- **Quest-flagged food/trinkets** (figurines, cases, specific canned goods) — these are
  worthless-looking and constantly needed.

### Standing SELL list

- Duplicate low-tier armor and helmets past your first spare.
- Weapon attachments you can't mount on anything you run.
- Common ammo below what you actually use.
- Anything bulky under ~10k roubles-per-slot with no task attached.

> ⚠️ **Version drift:** Tarkov re-balances every wipe — item values, task requirements,
> trader levels, and flea rules all move. I'll flag anything I'm not certain is current
> for this patch rather than state it confidently. Correct me freely; your in-game screen
> beats my memory every time.

---

## 5. Stash Doctrine

- **Target: 15–20% free space at all times.** Below that you start making bad panic
  decisions mid-raid-return.
- **One container per category** — meds, ammo, barter, quest, keys. Junkbox/items case
  when affordable; the space they pay back is worth more than the rouble cost.
- **Quest items live in one dedicated container.** Nothing else goes in it. This single
  habit prevents the most common expensive mistake in the game.
- **Gear rack:** exactly two spare kits ready to go. More than that is dead capital.
- Purge order when full: bulky-cheap → duplicate attachments → excess common ammo →
  spare armor. Never quest, never hideout, never keys.

---

## 6. Hideout

| Module | Level | Status | Missing |
|---|---|---|---|
| FILL IN | | | |

**Priority logic I use:** modules that pay rent first (anything generating currency or
consumables), then quality-of-life that saves you roubles per raid, then vanity. I'll
tell you when a module's payback period is longer than the wipe has left.

---

## 7. Loadout Budget

Set a ceiling and stick to it. Losing kits you can't replace is how runs end.

```
Standard raid ceiling:   FILL IN roubles
Quest-run ceiling:       FILL IN (go cheaper — objective matters, not kills)
"Send it" ceiling:       FILL IN (rare, only with a stocked stash)
```

Rule: **never field a kit you can't afford to lose twice in a row.**

---

## 8. Session Log

Append-only. Gives me continuity across chats — if a conversation ends, paste the last
few entries and I'm caught up instantly.

```
[DATE] [MAP] [SURVIVED?] — brought back: … | quest progress: … | sold: … | net: …
```

<!-- entries below -->

---

## 9. Maintaining this file

This is a git repo, so the file is the source of truth and the history is the audit log.

```bash
git add tarkov/README.md
git commit -m "tarkov: update after <map> run"
git push -u origin claude/tarkov-inventory-tracker-1hbkzr
```

If you'd rather never touch git: just tell me what happened in chat and I'll edit,
commit, and push it for you. Paste the file back to me at the start of any new
conversation and I pick up exactly where we left off.

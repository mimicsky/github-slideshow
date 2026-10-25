# Ash on Ostrava

Warhammer 40,000 on the 5e chassis. Season 1: *Seed of Nurgle* (done). Season 2: aboard *The Bright Light*.
Branch: **`claude/ash-ostrava-campaign-closeout-ma000x`**. Rules: [`../../DND_CODEX.md`](../../DND_CODEX.md).

---

## Start checklist (every new chat, and after every context compaction)

Read these in order. Then open the first reply with one line ticking them off, e.g.
`Checklist: README ✓ sheet ✓ DM notes ✓ codex 6-8 ✓ last chapter ✓ indexes ✓`.
Don't say what's in the DM notes.

1. **This README**, all of it.
2. **The campaign sheet** ([`ash-on-ostrava-campaign-sheet.md`](ash-on-ostrava-campaign-sheet.md)): "Where we stopped", "Current state", "What the Light knows about Thask", "Full kit", Tamsin ("The character"), the Light (roster, roles, specialties), "Owed", "Season Two: how it plays".
3. **The DM notes**, read silently, never told to the player: hidden threads, nemeses, pre-rolls. *(During the cleanup they are still the sheet's last section, "DM threads"; they move to `dm-notes.md` in cleanup step 3.)*
4. **The codex** ([`../../DND_CODEX.md`](../../DND_CODEX.md)), Parts 6, 7 and 8: the player's play preferences, the house rules, cover, the roll checklist, how the game is run, the book rule, and the 40k rules (renown, power rating, nemeses, crew posts, gear).
5. **The last chapter** written in [`book-season-2.md`](book-season-2.md), plus the sheet's day log for anything after it.
6. **Tables of contents only**: [`../../wh40k_gear/catalogue/README.md`](../../wh40k_gear/catalogue/README.md) and [`../../wh40k_gear/bestiary/README.md`](../../wh40k_gear/bestiary/README.md). Open an entry only when it comes up. Read [`../../wh40k_gear/bestiary/roles.md`](../../wh40k_gear/bestiary/roles.md) at the start of any fight.

Then pick up exactly where we stopped.

## Every reply (the things that keep slipping)

- **Never roll Tamsin's dice.** Ask "Roll me a d20" and wait. NPC dice and undecided facts are rolled openly with a real RNG. The DM rolls will checks for the player.
- **Show the math** on every roll: (die + stat + other bonuses = total). DCs stay hidden; contests show both totals.
- **Name + role on every mention**, dialogue lines included: `Kell (Light-bringer sergeant, assault): line`.
- **Second person** for Tamsin. **Don't act, think or feel for him.** Stop at the first new decision point.
- **No game terms in the fiction.** NPCs never mention rolls, dice or numbers.
- **Save before the scene**: the note is just "(saved)", and the scene is the last thing in the reply. Commit and push after anything important.
- **Full kit:** when gear is used, swapped, found or handed out, update the sheet's Full kit table and the crate count in the same save.
- **Don't read pools, hidden notes or nemeses out to the player.**

## End of every in-game day

1. Show the **tally sheet** (Tamsin's stats before and after, then the Light's).
2. **Write that day as book chapters** in `book-season-2.md` (codex Part 7, The book).
3. Delete that day's scene notes from the day log, and update "Where we stopped".
4. Commit and push.

On a long day, add a one-line note to the day log after each big scene, so nothing is lost if the context is cut.

## Start of a mission

- Roll the faction's wealth: `python3 wh40k_gear/roll_enemy.py wealth TYPE` (once per mission or world).
- Roll each active nemesis (codex Part 8, 17+ they turn up). Keep the results in the DM notes.
- Enemies: `python3 wh40k_gear/roll_enemy.py TYPE COUNT WEALTH [GOD]`. The types are cultist, raider, pirate, traitor and traitor_elite.
- Shops: `python3 wh40k_gear/roll.py SELLER SIZE` (restock every 2 days).

---

## Files

| File | What it is |
| --- | --- |
| [`ash-on-ostrava-campaign-sheet.md`](ash-on-ostrava-campaign-sheet.md) | Current state: where we stopped, orders, health, coin, Tamsin, the Full kit, the Light, owed |
| [`book-season-2.md`](book-season-2.md) | Season Two as a novel (the only story file) |
| [`book.md`](book.md) | Season One as a novel |
| [`maps/`](maps) | Pictures of *The Bright Light* |

**Cleanup in progress (session 10).** The sheet is being split. Steps: 2 checklist ✓ · 3 DM notes → `dm-notes.md` · 4 write days 17-33 into the book · 5 history → `archive.md` · 6 rebuild the sheet · 7 NPCs and missions → `world.md`, gear → `inventory.md` · 8 remove duplicates, rules into the codex · 9 cold test. Update this table as each file appears; delete this note when done.

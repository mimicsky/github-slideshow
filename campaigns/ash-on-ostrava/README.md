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
3. **The DM notes** ([`dm-notes.md`](dm-notes.md)), **down to the STOP line only**, read silently, never told to the player: how the campaign runs, the live mission's secrets, nemeses, pre-rolls. Below STOP, open an entry only when its trigger comes up.
4. **The codex** ([`../../DND_CODEX.md`](../../DND_CODEX.md)): **only the sections marked "Always" in the map at its top** (about 450 lines: the play preferences, house rules 1-6, cover, the roll checklist, shots and hits, breaking and Down, describing the world, armour and weapons). Open the rest when the map's trigger comes up.
5. **The sheet's day log** (newest first): what happened since the last written chapter. Read the end of the last chapter in [`book-season-2.md`](book-season-2.md) (search for the last `## Chapter`) only if the day log doesn't cover where we are.
6. **Tables of contents only**: [`../../wh40k_gear/catalogue/README.md`](../../wh40k_gear/catalogue/README.md) and [`../../wh40k_gear/bestiary/README.md`](../../wh40k_gear/bestiary/README.md). Open an entry only when it comes up. Read [`../../wh40k_gear/bestiary/roles.md`](../../wh40k_gear/bestiary/roles.md) at the start of any fight.

Then pick up exactly where we stopped.

## Where things are (open only when it comes up)

Like the gear catalogue: don't read these up front. When the trigger happens, open just that part.

| When this comes up | Open |
| --- | --- |
| A fight starts | [`roles.md`](../../wh40k_gear/bestiary/roles.md): its index, then only the roles in the fight; the enemy team's bestiary entry if it's a special team; codex Part 6: house rules 5 (the exchange) and 6 (shot chains), Cover, the Roll checklist, Shots and hits, Stacking |
| Someone is hit, goes Down or gets healed | Codex Part 6: Shots and hits, Breaking and Down; Part 8: Armour, the refractor field (Gear rules); `roles.md`: Medic (the patch roll); the catalogue's `drugs.md` (stimm, SCIHU) |
| A fight ends | Codex Part 6, Breaking and Down (who surrenders, runs, lives); Part 8, Loot (the two rare rolls, coin on a body); house rule 7 (reps: a Down counts as a kill); log witnesses in `dm-notes.md`; update the Full kit (ammo, grenades, Dirty guns) |
| Rolling enemies | `roll_enemy.py` (commands below); codex Part 8 for enemy stats |
| A gear item's own rules | The catalogue index, then just that entry |
| Heat, hot-shot, drop-prone guns, jams, going Down | Codex Part 8, Gear rules |
| Shopping or selling | `roll.py`; codex Part 8 (shop size, the quartermaster, the Void Exchange); the sheet's coin |
| Training and the tally | Codex house rule 7; the sheet's Light table |
| Interrogation or recruiting | Codex house rule 8 (Will) |
| Food, a cook | Codex house rules, Food |
| Crafting, blessings, purity seals | Codex Part 8 (crafting, blessings, seals); the sheet's open threads |
| Psykers or the warp | Codex Part 8, Perils and Psyker powers |
| Walking into a new place | Codex Part 8, Renown; Tamsin's renown on the sheet |
| A hidden trigger (a sniper, Kesh, Ustrennos, a nemesis) | The index in [`dm-notes.md`](dm-notes.md), then that entry |
| An NPC or a place | The sheet's NPC tables |
| The next mission or Kesh's targets | The sheet's target list and mission briefs |
| The ship's layout | The sheet's "Season Two: how it plays"; [`maps/`](maps) |
| A picture of an item, a battle map, a ship map | The lore-art skill |
| Something from long ago | Search the books; [`archive.md`](archive.md) |

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

## End of a session

Award XP (the sheet's XP table), check the book is up to date with every day played, update "Where we stopped", commit and push.

## Start of a mission

- Roll the faction's wealth: `python3 wh40k_gear/roll_enemy.py wealth TYPE` (once per mission or world).
- Check the DM notes' witnesses and nemeses: bring one back if the story fits (codex Part 8, Nemeses; the DM's call, no automatic rolls).
- Enemies: `python3 wh40k_gear/roll_enemy.py TYPE COUNT WEALTH [GOD]`. The types are cultist, raider, pirate, traitor and traitor_elite.
- Shops: `python3 wh40k_gear/roll.py SELLER SIZE` (restock every 2 days). Sellers: **M** Munitorum or fleet stores, **B** black market or chandlers, **A** Mechanicus shrine, **F** Free Trader or Void Exchange, **E** Ecclesiarchy. Sizes: small (5-7), medium (9-12), large (14-18), huge (20-25).

---

## Files

| File | What it is |
| --- | --- |
| [`ash-on-ostrava-campaign-sheet.md`](ash-on-ostrava-campaign-sheet.md) | Current state: where we stopped, orders, health, coin, Tamsin, the Full kit, the Light, owed |
| [`dm-notes.md`](dm-notes.md) | Hidden: how the campaign runs, live secrets, nemeses, pre-rolls (top part every resume; entries on demand) |
| [`archive.md`](archive.md) | Closed history; never read on resume |
| [`book-season-2.md`](book-season-2.md) | Season Two as a novel (the only story file) |
| [`book.md`](book.md) | Season One as a novel |
| [`maps/`](maps) | Pictures of *The Bright Light* |

**Cleanup in progress (session 10).** The sheet is being split. Steps: 2 checklist ✓ · 3 DM notes → `dm-notes.md` ✓ · cold-test fixes ✓ · codex map ✓ · 4 write days 17-33 into the book · 5 history → `archive.md` · 6 rebuild the sheet · 7 NPCs and missions → `world.md`, gear → `inventory.md` · 8 remove duplicates, rules into the codex · 9 cold test. Update this table as each file appears; delete this note when done.

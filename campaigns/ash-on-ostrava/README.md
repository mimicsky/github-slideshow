# Ash on Ostrava

Warhammer 40,000 on the 5e chassis. Season 1: *Seed of Nurgle* (done). Season 2: aboard *The Bright Light*.
Branch: **`claude/ash-ostrava-campaign-closeout-ma000x`**. Rules: [`../../DND_CODEX.md`](../../DND_CODEX.md).

---

## Start checklist (every new chat, and after every context compaction)

Read these in order. Then open the first reply with one line ticking them off, e.g.
`Checklist: README ✓ sheet ✓ DM notes ✓ codex Always ✓ last scene ✓`.
Don't say what's in the DM notes.

1. **This README**, all of it.
2. **The campaign sheet** ([`ash-on-ostrava-campaign-sheet.md`](ash-on-ostrava-campaign-sheet.md)): "Where we stopped", "Current state", "What the Light knows about Thask", "Full kit", Tamsin ("The character"), the Light (roster, roles, specialties, stats). It's about 260 lines, all current state.
3. **The DM notes** ([`dm-notes.md`](dm-notes.md)), **down to the STOP line only**, read silently, never told to the player: how the campaign runs, the live mission's secrets, nemeses, pre-rolls. Below STOP, open an entry only when its trigger comes up.
4. **The codex** ([`../../DND_CODEX.md`](../../DND_CODEX.md)): **only the sections marked "Always" in the map at its top** (about 450 lines: the play preferences, house rules 1-6, cover, the roll checklist, shots and hits, breaking and Down, describing the world, armour and weapons). Open the rest when the map's trigger comes up.
5. **The end of the last chapter** in [`book-season-2.md`](book-season-2.md) (search for the last `## Chapter`; read its final scene), plus the sheet's day log for anything played since.
6. **Nothing else up front.** The gear catalogue's index, the bestiary's index and its roles file are opened when an item or a fight comes up ("Where things are" below).

Then pick up exactly where we stopped.

## Where things are (open only when it comes up)

Like the gear catalogue: don't read these up front. When the trigger happens, open just that part.

| When this comes up | Open |
| --- | --- |
| A fight starts | [`roles.md`](../../wh40k_gear/bestiary/roles.md): its index, then only the roles in the fight; the enemy team's bestiary entry if it's a special team; codex Part 6: house rules 5 (the exchange) and 6 (shot chains), Cover, the Roll checklist, Shots and hits, Stacking |
| Someone is hit, goes Down or gets healed | Codex Part 6: Shots and hits, Breaking and Down; Part 8: Armour, the refractor field (Gear rules); `roles.md`: Medic (the patch roll); the catalogue's `drugs.md` (stimm, SCIHU) |
| A fight ends | Codex Part 6, Breaking and Down (who surrenders, runs, lives); Part 8, Loot (the two rare rolls, coin on a body); house rule 7 (reps: a Down counts as a kill); log witnesses in `dm-notes.md`; update the Full kit (ammo, grenades, Dirty guns) |
| Rolling enemies | `roll_enemy.py` (commands below); [the bestiary index](../../wh40k_gear/bestiary/README.md) for special teams; codex Part 8, Loot, for enemy stats |
| A gear item's own rules | [The catalogue index](../../wh40k_gear/catalogue/README.md), then just that entry |
| Heat, hot-shot, drop-prone guns, jams, going Down | Codex Part 8, Gear rules |
| Shopping or selling | `roll.py`; codex Part 8 (shop size, the quartermaster, the Void Exchange); the sheet's coin |
| Training and the tally | Codex house rule 7; the sheet's Light table |
| Interrogation or recruiting | Codex house rule 8 (Will) |
| Food, a cook | Codex house rules, Food |
| Crafting, blessings, purity seals | Codex Part 8 (crafting, blessings, seals); `inventory.md` (blessings on offer, upgrade paths, builds) |
| Psykers or the warp | Codex Part 8, Perils and Psyker powers |
| Walking into a new place | Codex Part 8, Renown; Tamsin's renown on the sheet |
| A hidden trigger (a sniper, Kesh, Ustrennos, a nemesis) | The index in [`dm-notes.md`](dm-notes.md), then that entry |
| An NPC or a place, or a Light-bringer's backstory | [`world.md`](world.md): its contents list, or search the file for the name |
| The live mission | The sheet's Current state (orders, plan, what the Mart knows) and the top of `dm-notes.md` |
| Later missions or Kesh's targets | [`world.md`](world.md): Kesh's target list and the later-mission briefs |
| The ship's layout | [`world.md`](world.md): "Season Two: how it plays"; [`maps/`](maps) |
| An item's history, blessing or spirit; the container's stock; builds; books; the wishlist | [`inventory.md`](inventory.md): its contents list, then that part |
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
- Any other roll (saves, break checks, loot d20s, NPCs): `python3 wh40k_gear/dice.py d20` (or `3d20`, `d6`...). A rare item: `python3 wh40k_gear/dice.py rare weapons` (rare roll 1, gear in use) or `rare any` (rare roll 2, stashed).
- Shops: `python3 wh40k_gear/roll.py SELLER SIZE` (restock every 2 days). Sellers: **M** Munitorum or fleet stores, **B** black market or chandlers, **A** Mechanicus shrine, **F** Free Trader or Void Exchange, **E** Ecclesiarchy. Sizes: small (5-7), medium (9-12), large (14-18), huge (20-25).

---

## Files

| File | What it is |
| --- | --- |
| [`ash-on-ostrava-campaign-sheet.md`](ash-on-ostrava-campaign-sheet.md) | Current state: where we stopped, orders, health, coin, Tamsin, the Full kit, the Light, owed |
| [`world.md`](world.md) | People, places, the ship, Kesh's targets, mission briefs (on demand) |
| [`inventory.md`](inventory.md) | Gear detail, the container, builds, books, blessings, wishlist (on demand) |
| [`dm-notes.md`](dm-notes.md) | Hidden: how the campaign runs, live secrets, nemeses, pre-rolls (top part every resume; entries on demand) |
| [`archive.md`](archive.md) | Closed history; never read on resume |
| [`book-season-2.md`](book-season-2.md) | Season Two as a novel (the only story file) |
| [`book.md`](book.md) | Season One as a novel |
| [`maps/`](maps) | Pictures of *The Bright Light* |

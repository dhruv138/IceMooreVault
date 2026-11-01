# Updating the Icemoor vault

After each game session you add the session notes to the vault. The scripts in this folder then do the bookkeeping:

- They tidy up the new session note: file name, date and title line.
- They record who and what each session mentions, so the Dataview tables in Obsidian stay current.
- They refresh the **Session history** box at the bottom of every person, place, faction, item and quest note.
- They rebuild the campaign dashboard, a web page you can open in any browser.

Everything happens in one step. You don't need to know any programming.

---

## Part 1: One-time setup

You only do this once per computer.

### Step 1. Install Python

Python is the free program that runs the scripts.

**On a Mac**

1. Go to **python.org/downloads** and click the yellow **Download Python** button.
2. Open the downloaded file and click through the installer, accepting the defaults.
3. When it finishes, a Finder window opens. Double-click **Install Certificates.command** in it. It's harmless and avoids problems later.

**On Windows**

1. Go to **python.org/downloads** and click the yellow **Download Python** button.
2. Open the downloaded file. **Before clicking Install, tick the box "Add python.exe to PATH"** at the bottom of the first screen. This is the step people most often miss.
3. Click **Install Now** and wait for it to finish.

Any Python version 3.8 or newer works.

### Step 2. Find your vault folder on your computer

This is the folder Obsidian opens. It contains `Sessions`, `People`, `Places` and so on, plus this `scripts` folder. In Obsidian you can find it by right-clicking any note and choosing **Reveal in Finder** (Mac) or **Show in system explorer** (Windows).

### Step 3. Install the script requirements

The scripts don't need any extra packages right now, so you can skip this step. If someone adds a package to `scripts/requirements.txt` later, this is how to install it:

1. Open a terminal *in the vault folder*:
   - **Mac:** in Finder, right-click the vault folder and choose **New Terminal at Folder**. If you don't see it, open the **Terminal** app, type `cd ` (with a space after it), drag the vault folder onto the window, and press Return.
   - **Windows:** open the vault folder in File Explorer, click in the address bar at the top, type `cmd` and press Enter.
2. Type this and press Return/Enter:
   - Mac: `python3 -m pip install -r scripts/requirements.txt`
   - Windows: `py -m pip install -r scripts\requirements.txt`

### Step 4 (Mac only). Allow the update shortcut to run

The first time you double-click **Update Vault (Mac).command**, macOS may say it "can't be opened" or comes from "an unidentified developer". If so:

1. Click **Done** or **Cancel**.
2. Right-click (or Control-click) the file and choose **Open**.
3. Click **Open** in the box that appears.

macOS remembers this, so from then on a plain double-click works.

---

## Part 2: After every session

### Step 1. Add the session note

In Obsidian, create a new note in the **Sessions** folder and paste in the session write-up. Start the note with the session number and date on the first lines, as you already do:

```
Session 39
8 October 2026
Riffle bursts into Talir's office to explain...
```

You can name the note `Session 39` or `Session_39`; the script fixes the name either way. Don't add a header or metadata yourself; the script writes them.

### Step 2. Link the names (mostly automatic)

The vault knows a person, place or quest is in a session only when its name is a link. **The update links names for you** the first time it sets up a new session, and keeps your wording: "Peter" becomes `[[Peter Owens|Peter]]`, which still reads "Peter" in Obsidian.

It deliberately skips names that are also ordinary words (Tiny, Queen, Wolf and a few others), and it can't link someone who has no note yet. For those, link by hand: type `[[`, start typing the name and pick from the list.

- **To keep the wording you wrote**, add a vertical bar after the name: `[[Theo'din Corvis|Theo]]` shows as "Theo" but links to Theo'din's note.
- **For someone new**, link the name anyway. The link shows faded because there's no note yet; click it and Obsidian creates the note. Put new notes in the right folder (People, Places, and so on).

To link names in a session that's already set up (say, after adding new notes), run this from a terminal in the vault folder. The first line only shows what it would link; the second does it:

```
python3 scripts/link_session.py "Session 39"
python3 scripts/link_session.py "Session 39" --apply
```

### Step 3. Add a short recap (optional)

Add two lines like this just below the date lines (or, once the update has run, just below the title line it creates):

```
> [!summary] TL;DR
> Riffle defends themself to Talir while Deanira and Theo find a staircase under the Owens mausoleum.
```

Obsidian shows this as a recap box, and the dashboard uses it as the session summary. Without it, the dashboard shows the session's first two sentences instead.

### Step 4. Run the update

Pick whichever is easiest:

- **Mac:** open the `scripts` folder in Finder and double-click **Update Vault (Mac).command**.
- **Windows:** open the `scripts` folder in File Explorer and double-click **Update Vault (Windows).bat**.
- **From a terminal** (opened in the vault folder, as in Part 1, Step 3): type `python3 scripts/update_all.py` on a Mac or `py scripts\update_all.py` on Windows, then press Return/Enter.

A window opens and reports its progress. It finishes in a few seconds with **All done**.

### Step 5. Read the "Things to check" list

If anything needs your attention, the window lists it before "All done". For example:

```
Things to check in Obsidian:
  • Session 39 has no TL;DR recap (the dashboard will show its opening lines instead)
  • Session 39 mentions but doesn't link: Furgus, Hana Goldfirm, Samuel Patel
```

Fix what you want to fix in Obsidian, then run the update again (Step 4). Running it more than once is always safe.

The list only covers new sessions and the latest one, so it won't nag you about old sessions. It deliberately ignores names that are also ordinary words, like Tiny, Queen or Wolf, so check those yourself.

### Step 6. Look at the dashboard

Open the `dashboard` folder in the vault and double-click **Icemoor Dashboard.html**. It opens in your web browser and shows:

- the latest session's recap
- the open threads, and when each last came up
- a grid of who appears in which session
- a searchable session log
- a directory of every note

If it was already open, refresh the browser tab.

The online copy Claude published is a separate snapshot. Ask Claude to republish it when you want that copy updated too.

### Step 7. Save to GitHub

Commit and push the changes the way you normally back up the vault. The update changes the new session, the metadata blocks and history boxes of affected notes, and the dashboard file.

---

## Part 3 (optional): Let a local AI model suggest notes

Step 1 to 7 keep the metadata and links tidy, but they don't write anything new: no recap, no notes for new people, no "what changed" lines on existing notes. A model running on your own computer through **Ollama** can suggest those. Nothing goes into the vault until you've ticked it.

### One-time setup

1. Install Ollama from ollama.com and open it.
2. In a terminal, download a model. `qwen3:8b` works on most laptops with 16 GB of memory; `gpt-oss:20b` is better if you have 24 GB or more:

   ```
   ollama pull qwen3:8b
   ```

### After each session

1. Do Part 2, Steps 1 to 4 first, so the session is set up and linked.
2. Ask the model for suggestions (a few minutes on a laptop):

   ```
   python3 scripts/ingest_session.py --model qwen3:8b "Session 39"
   ```

   It reads the session plus every note the session links to, and a one-line list of every other note, so it knows what already exists. If the model's memory is too small for all that, it says so and stops rather than guessing.
3. Open **Ingestion/Session 39 proposals.md** in Obsidian. It lists a recap, new notes, facts for existing notes, status changes and open questions, each with the line from the session it came from.
   - Tick the box on each item you agree with.
   - Change an item's wording if you like, but keep the `%%f3%%`-style marker at the start.
   - Items under **Rejected** failed the automatic checks: the quote isn't actually in the session, the name doesn't appear in the session, the note already exists or doesn't exist, or a status was given to something that isn't a quest or mystery. They can't be applied; add them by hand if one is right.
4. Write the ticked items into the vault:

   ```
   python3 scripts/apply_ingestion.py "Session 39"
   ```

   This adds the recap box, creates the new notes, adds facts under **Recent developments** on each note (marked with the session), adds questions under **Open questions**, updates statuses, links the new names in the session, and then runs the normal update. Applied items get a ✓ on the proposals page. You can tick more items later and run it again; items already applied are skipped.
5. Check the changes before you save to GitHub (Part 2, Step 7). In GitHub Desktop or `git diff` you can see exactly what was added.

Other options for `ingest_session.py`: `--think` lets reasoning models think first (slower, sometimes better); `--host` points at Ollama on another computer; `--ctx` sets the context size yourself. You can set the `OLLAMA_MODEL` environment variable instead of typing `--model` each time.

---

## What each file does

| File | What it's for |
|---|---|
| `Update Vault (Mac).command` | Double-click shortcut that runs everything on a Mac |
| `Update Vault (Windows).bat` | Double-click shortcut that runs everything on Windows |
| `update_all.py` | Runs the three scripts below, in order |
| `update_metadata.py` | Sets up new session files (links names, adds a Timeline entry), refreshes each note's metadata block, and lists the "Things to check" |
| `update_session_history.py` | Rewrites the collapsed **Session history** box at the bottom of each note |
| `link_session.py` | Links names in a session while keeping your wording; `update_metadata.py` uses it for new sessions |
| `vault_names.py` | The shared list of note names and the rules for matching them in text |
| `ingest_session.py` | Asks a local Ollama model for suggestions and writes the proposals page in `Ingestion/` |
| `apply_ingestion.py` | Writes the ticked items from a proposals page into the vault |
| `build_dashboard.py` | Rebuilds `dashboard/Icemoor Dashboard.html` |
| `dashboard_template.html` | The dashboard's design; `build_dashboard.py` fills it with the vault's data |
| `requirements.txt` | Extra Python packages to install (none at the moment) |

### What the scripts change, and what they leave alone

- **Metadata block** (between the `---` lines at the very top of a note): the scripts rewrite only their own fields. On every note those are `type`, `status`, `first_seen`, `party_member`, `location_type` and `item_type`. On sessions they also rewrite `session`, `date`, `previous_session`, `next_session` and the lists of linked people, places, factions, quests and items. Anything else you put in the block stays.
- **Session history box:** fully rewritten each time, between the `%% session-history:start %%` and `%% session-history:end %%` markers. Don't write inside those markers, because your text would be replaced. Everywhere else in a note is yours.
- **Your own writing:** never changed. The only exception is a brand-new session note, which gets its title line and metadata added the first time.
- **Nothing is ever deleted.** A new session file may be renamed (for example `Session_39.md` to `Session 39.md`). Obsidian doesn't notice renames made outside it, so if you already linked to the old name somewhere, change that link to the new name.

### Changing who's in the party

The party list sits near the top of `update_metadata.py`. Open that file in any plain text editor (TextEdit on Mac, Notepad on Windows) and find these two lines:

```
PARTY = {"WISC", "Furgus", "Deanira", "Riffle", "Philip", "Theo'din Corvis"}
PCS = {"WISC", "Furgus", "Deanira", "Riffle", "Philip"}
```

`PARTY` is everyone who travels with the group. `PCS` is the player characters only. To add someone, put their note name in double quotes, separated by a comma, exactly as the note is named. Save the file and run the update.

---

## If something goes wrong

**"python3: command not found", "'py' is not recognized", or the window closes immediately**
Python isn't installed, or on Windows the "Add python.exe to PATH" box wasn't ticked. Re-run the Python installer, choose **Modify**, and make sure that option is on. Then restart the computer.

**Mac says the .command file can't be opened**
See Part 1, Step 4.

**"Session_39.md and Session 39.md are both session 39"**
There are two notes for the same session. Combine them into one in Obsidian, delete the other, and run the update again.

**"can't tell the session number from the file name"**
The script found a file in `Sessions` whose name doesn't contain a number. Rename it to something like `Session 39`.

**A session's title has no date ("no date found in the first lines")**
Put the date on the first or second line, written like `8 October 2026`, and run the update again. If the note already has its title line, just fix the date in the title line (`# Session 39 — 8 October 2026`) and the `title:` line in the metadata block above it.

**"Something went wrong and the update stopped partway"**
Nothing was deleted. Copy the whole message from the window and send it to whoever helps with the vault (Claude can read it too).

**The dashboard didn't change**
Refresh the browser tab. If you opened the dashboard from GitHub or Claude, that's a different copy; open the file in your vault's `dashboard` folder instead.

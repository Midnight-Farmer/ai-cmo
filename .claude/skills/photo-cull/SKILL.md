---
name: photo-cull
description: Review a photo shoot day and cull a large pool of stills down to a tight, ordered "best of" set staged for the edit pass. Use whenever the user wants to go through shoot photos, pick the keepers, narrow a big folder down to the best N, decide which shots to edit, choose carousel/reveal stills, or build a reusable background library from a shoot. Trigger on phrases like "review the photos from the shoot", "which of these should we edit", "pick the best shots", "cull the shoot", "narrow this down to the top 20", "go through the [project] finals", "I need to choose carousel photos", or any time there's a folder of many images (often raws/CR3 you can't see directly) and the goal is a smaller curated subset. Also reach for this right after organize-shoot when stills need selecting, or before carousel-slides when a carousel needs its photos chosen. Works for any AI-CMO client.
metadata:
  version: 1.0.0
---

# Photo Cull

You are a photo editor culling a shoot. The input is a folder with too many images to eyeball one by one — often hundreds of raws you can't even open directly. The output is a small, ordered set of the strongest frames, staged full-res so a human can do the final edit pass, plus a clear record of why each made the cut.

This is the front end of the carousel/reveal pipeline: **shoot pool → contact sheets → curate → staged edit set.** It hands off to the human edit pass, then to `carousel-slides` (rendering) or a straight multi-photo post. It complements `organize-shoot` (which transcribes/renames/catalogs a whole shoot day) — run this when you specifically need to *choose stills*, not process footage.

The hard part isn't the file shuffling — the scripts do that. The hard part is **judgment**: which 20 of 200 frames actually earn a slot, and in what order. That's your job. Don't outsource it to filename or filesize.

---

## Why you can't skip looking

You cannot cull from a file listing. RAW files (`.CR3`, `.NEF`, `.ARW`, `.DNG`) aren't viewable as-is, and even JPEGs tell you nothing from their names. Past attempts to "pick by filename" or trust a mapping CSV produce confident, wrong selections — a blurry frame and the keeper next to it have adjacent names. **Always render contact sheets and actually read them.** The whole skill is built around making that fast.

---

## The loop

### 1. Resolve the source folder (and the edit policy)

Find the folder of candidates. Prefer a finals/`edits/` subfolder if the photographer already culled+edited — those are stronger starting frames than the full raw dump. Otherwise point at the raw shoot folder.

Then check the **client's edit policy** — this is the one per-client variable, and it lives in the client's `CLAUDE.md` (and `memory/reference_carousel_flow.md` for the clients that have it):

- **Edit-always** clients: every still gets a human edit pass before it ships. Your job ends at *staging the picks* into a `_to-edit` folder; the human edits them into `_edited/`; downstream builds read from `_edited/`.
- **Never-edit** clients: stills ship as shot. Your picks are the finals; no staging-for-edit step, just hand them off.

If the policy isn't recorded for this client, ask once and write the answer to their `CLAUDE.md` so the next run doesn't have to.

### 2. Build contact sheets

```bash
bash scripts/contact-sheets.sh --src "<photo-folder>" [--out <workdir>] [--batch 18]
```

This enumerates every image (raws rendered via `sips`), writes a labeled thumbnail per frame, batches them into readable contact sheets, and writes `manifest.tsv` mapping each on-sheet index `#N` back to the original full-res file. Defaults are tuned so each sheet stays legible when you Read it (≈18 frames, 4 across). Output paths print at the end.

**Then Read every sheet.** This is the actual review — don't shortcut it. Build a mental (or written) catalog as you go: for each `#N`, what's the subject, the angle, is it sharp, is it a wide/detail/context shot, is it background-worthy.

### 3. Curate — the judgment that matters

Pick the keepers by their `#N` labels. Hold two goals in tension:

- **Story / coverage.** A reveal walks a space: open strong, establish wide, move through the zones (for a kitchen: the feature wall → cooking → sink → storage details → materials), close on a pull-back or lifestyle frame. Cover the beats the content note or brief calls for.
- **Each frame standing alone.** Especially if the set doubles as a reusable background library (text-over-photo slides later), favor clean, composed frames with breathing room over busy tight crops.

Discipline that keeps a cull good:
- **No adjacent duplicates.** Two near-identical angles back to back waste a slot and read as filler. Pick the better one, move on.
- **Vary the shot type across the sequence.** Don't stack five wides then five details — interleave so the swipe keeps surprising.
- **Match the deliverable's count.** A carousel caps at 20 slides on Instagram. If you're opening with a split-hero (see step 6), that one photo eats *two* slides, so 20 slides = 19 photos. Do that math before you promise a number.
- **Name what you benched and why.** When you drop a frame, say so in one line — it lets the user overrule you cheaply.

Show the user your picks before staging — ideally as a contact sheet of just the chosen set, in order (re-run a montage on the staged folder, or build one from the picked thumbnails). They're about to spend real time editing these; a 30-second confirm beats re-editing the wrong 20.

### 4. Stage the picks

```bash
bash scripts/stage-picks.sh --manifest <workdir>/manifest.tsv \
  --picks "11,3,44,9,..." --dest "<project>/<date>/Photos/_to-edit"
```

`--picks` is your ordered `#N` list — order = posting/deliverable order. The script copies each full-res original into the dest as `01_<name>`, `02_<name>`, … in that order, records the mapping in `_pick-order.tsv`, and sweeps the `._*` AppleDouble sidecars that copying to exFAT/network drives leaves behind. For edit-always clients this dest is the `_to-edit` folder; for never-edit clients it's just the handoff folder.

### 5. Hand off to the edit pass (edit-always clients)

Tell the user exactly which files to edit and flag anything orientation-sensitive (verticals that may need straightening, a hero that must stay landscape for a split). They edit into a sibling `_edited/` folder. Wait for that before building anything downstream — don't build slides from unedited frames.

### 6. Rebuild the deliverable (optional, after edits land)

If the deliverable is a carousel and the user wants the "swipe to reveal one continuous image" opener, split the hero landscape frame into two seamless halves:

```bash
bash scripts/split-hero.sh --src "<edited>/01_<hero>.jpg" --dest "<post-folder>"
```

This writes `01.jpg` + `02.jpg` (each a clean 4:5 panel that lines up edge-to-edge) plus a `.seam-check.jpg` — **Read the seam check** and confirm the join is invisible and nothing important is bisected. Then place the remaining edited photos as `03.jpg…` in order, drop the caption file in, and that folder is ready to post. For the full carousel-rendering path (branded text slides, not full-bleed photos), hand off to the `carousel-slides` skill instead.

---

## The scripts (and why they're bundled)

Three small, generic, client-agnostic helpers live in `scripts/`. They exist because every manual run of this workflow otherwise re-derives the same fiddly ImageMagick incantations and re-hits the same platform gotchas:

| Script | Does | Key gotchas it handles for you |
|--------|------|-------------------------------|
| `contact-sheets.sh` | thumbnails + contact sheets + manifest | renders unviewable RAW via `sips`; macOS ImageMagick has **no default font** so annotate/montage need an explicit `-font` (baked in); filters `._*` sidecars; portable to macOS's bash 3.2 |
| `stage-picks.sh` | copies chosen full-res files in order | resolves `#N`→original via manifest; slot-numbers in pick order; sweeps `._*` after copying |
| `split-hero.sh` | seamless 4:5 split of a landscape hero | computes the exact center-crop so halves are distortion-free; writes a seam-check image; refuses non-landscape input |

Run them with `bash scripts/<name>.sh` (no chmod needed). Pass `--help`-style by reading the header comment in each — every argument is documented there. They take paths as arguments and hardcode no client values, so they're safe in the public repo and work for any client.

If you find yourself reaching for a fourth repeated operation across runs (e.g. cover-cropping a batch to 1080×1350 — `magick in -resize 1080x1350^ -gravity center -extent 1080x1350 out`), consider adding it as a script rather than re-typing it each time.

---

## When this is NOT the right tool

- **Processing a whole shoot day** (extract audio, transcribe, rename, catalog) → that's `organize-shoot`. This skill only selects stills.
- **Rendering branded text-over-photo carousel slides** → `carousel-slides`. This skill picks the photos; that one designs the slides.
- **One known photo, no choosing involved** → just edit it directly; no need to build contact sheets.
- **Video frame selection** → out of scope; these tools are for still pools.

---

## Reference

- The full carousel loop this plugs into (source → photos → per-client edit policy → slides → caption → review → publish) is documented per-client; the canonical pattern lives in a client's `memory/reference_carousel_flow.md`. This skill is the "identify + cull candidate photos" stretch of that loop, generalized and scripted.

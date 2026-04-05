# Content Notes System

Each content piece generated in a biweekly or weekly brief is saved as its own atomic markdown note. This enables Kanban board tracking, per-piece status management, and clickable navigation from briefs to individual content details.

Monthly plans do NOT create content notes — they remain strategic documents.

---

## Status Workflow

```
concept → pre-production → captured → editing → pre-approval → approved → scheduled → published
                                        ↑                          |
                                        └──── (revision needed) ───┘
```

| Status | Meaning |
|--------|---------|
| `concept` | Initial idea from brief generation. Has hook, format, platform defined. |
| `pre-production` | Shot list finalized, shoot day scheduled, talent/location confirmed. |
| `captured` | Footage/photos taken. `source_footage` field populated. |
| `editing` | Editor is assembling the piece. |
| `pre-approval` | Edit complete, awaiting client/team review. |
| `approved` | Approved with no changes needed. |
| `scheduled` | Captions finalized, post scheduled in platform or Typefully. |
| `published` | Live on platform. |

**Revision loop:** If changes are needed at `pre-approval`, set status back to `editing` and append revision notes to the `## Revision History` section.

---

## File Location & Naming

**Location:** `clients/[client]/outputs/content/` (flat folder, no subfolders)

**Naming pattern:** `YYYY-MM-DD-PREFIX-NN-slug.md`

- `YYYY-MM-DD` = scheduled post date
- `PREFIX` = client abbreviation (e.g., `AB` for Acme Builders, `PP` for client name initials)
- `NN` = sequential number within the brief (01, 02, 03...)
- `slug` = lowercase hyphenated title (max 40 chars)

**Examples:**
- `2026-04-15-AB-01-kitchen-final-reveal.md`
- `2026-04-17-AB-02-kitchen-walkthrough.md`
- `2026-03-05-PP-01-origin-story-reel.md`

**Content ID format:** `PREFIX-YYYYMMDD-NN` (matches filename without the slug)
- `AB-20260415-01`
- `PP-20260305-01`

---

## YAML Frontmatter Schema

```yaml
---
content_id: "AB-20260415-01"       # Unique ID, maps to content-log.csv
title: "Kitchen Final Reveal"      # Human-readable name
client: "acme-builders"            # Client folder name
brief: "[[brief-filename]]"       # Wiki-link to source brief (empty string for ad-hoc)
status: concept                    # Current workflow status
post_date: 2026-04-15             # Scheduled post date
platform:                          # Target platforms (list)
  - Instagram
  - Facebook
format: "Carousel 6-8"            # Content format
project: "Mitchell"                # Internal project name (if applicable)
project_social_name: "1966 Kitchen" # Public-facing project name
duration: ""                       # Target duration for video (e.g., "60-90s")
source_footage: ""                 # File path or folder for raw footage
shoot_date: 2026-04-06            # When footage was/will be shot
tags: [reveal, carousel]           # Obsidian tags for filtering
---
```

**Required fields:** content_id, title, client, status, post_date, platform, format
**Optional fields:** brief, project, project_social_name, duration, source_footage, shoot_date, tags

---

## Body Sections

### `## Concept`
Why this content exists. What story it tells. Data support from `whats-working.md`. Connection to goals.

### `## Script` (for video content)
| Section | Time | Visual | Audio |
|---------|------|--------|-------|
| HOOK | 0-3s | ... | ... |
| BODY | 3-30s | ... | ... |
| CLOSE | 30-60s | ... | ... |

### `## Carousel Structure` (for carousel content, replaces Script)
Slide-by-slide breakdown:
1. **Slide 1:** [description]
2. **Slide 2:** [description]

### `## Caption`
Full caption text with hook, body, CTA, and hashtags.

### `## Shot List`
Checklist of shots needed specifically for this piece:
- [ ] Shot description

### `## Edit Notes`
Text overlays, transitions, music direction, duration targets, any editor-facing instructions.

### `## Revision History`
Append-only log. Every status change or significant update gets a line:
- `YYYY-MM-DD: Created from [[brief-filename]]`
- `YYYY-MM-DD: Status → captured (organize-shoot). Source: ARoll-Mitchell-Reveal.MP4`
- `YYYY-MM-DD: Status → editing. Assigned to [editor]`
- `YYYY-MM-DD: Status → pre-approval. Edit v1 ready`
- `YYYY-MM-DD: Status → editing (revision). Feedback: shorten intro, add text overlay at 0:15`
- `YYYY-MM-DD: Status → approved`
- `YYYY-MM-DD: Status → scheduled. Typefully draft created`
- `YYYY-MM-DD: Status → published`

---

## How Briefs Reference Content Notes

When a biweekly or weekly brief is generated, inline content piece details are replaced with a linked table:

```markdown
## Content Pieces

| # | Title | Format | Status | Link |
|---|-------|--------|--------|------|
| 1 | 1966 Kitchen Final Reveal | Carousel 6-8 | concept | [[2026-04-15-CP-01-kirk-kitchen-final-reveal]] |
| 2 | Kitchen Final Walkthrough | Reel 60-90s | concept | [[2026-04-17-CP-02-kirk-kitchen-final-walkthrough]] |
```

The brief retains:
- Overview, performance snapshot, testing section
- Master shot list (consolidated by location for shoot-day efficiency)
- Posting schedule table
- Cross-platform notes, checklists

Each content note has the full detail: concept, script/carousel structure, caption, piece-specific shot list, edit notes.

---

## Ad-Hoc Content Notes

For one-off content ideas not tied to a brief:
- Set `brief: ""` in frontmatter
- Fill all other applicable YAML fields
- The note enters the same Kanban pipeline and can be tracked identically
- Use the same naming convention: `YYYY-MM-DD-PREFIX-NN-slug.md` (use the target post date and next available number)

---

## Integration with Other Workflows

### organize-shoot
After matching footage to content pieces, `organize-shoot` should:
1. Find matching content notes in `outputs/content/`
2. Set `status: captured`
3. Set `source_footage` to the actual file path or renamed filename
4. Append to Revision History: `YYYY-MM-DD: Status → captured (organize-shoot). Source: [filename]`
5. For pieces NOT captured: append `YYYY-MM-DD: NOT CAPTURED — needs rescheduling`

### Content logging
When logging published content (`log content`):
- `content_id` in `tracking/content-log.csv` should match the content note's `content_id`
- Update the matching content note's status to `published`

### Typefully drafts
When creating Typefully drafts from content notes:
- Update `status: scheduled` after draft creation
- Append to Revision History with draft URL

---

## Obsidian Kanban Board Setup

To track content notes on a Kanban board in Obsidian:

1. Install the **Kanban** plugin (if not already installed)
2. Create a new Kanban board in `clients/[client]/outputs/`
3. Create lanes matching the status values: concept, pre-production, captured, editing, pre-approval, approved, scheduled, published
4. Add content notes as cards — dragging between lanes updates the note's `status` frontmatter property

Alternatively, use **Dataview** to create a live status dashboard:

```dataview
TABLE status, format, post_date, platform
FROM "clients/your-client-name/outputs/content"
WHERE status != "published"
SORT post_date ASC
```

Group by status:
```dataview
TABLE WITHOUT ID file.link AS "Content", format, post_date
FROM "clients/your-client-name/outputs/content"
WHERE status = "editing"
SORT post_date ASC
```

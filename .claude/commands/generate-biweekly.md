---
description: Generate a two-week content plan with 10-14 pieces, performance data pull, and platform research
argument-hint: [client-name]
---

# Generate Bi-Weekly Plan

The user wants a bi-weekly content plan. Read `references/biweekly.md` for the full procedure, and `references/planning.md` for general planning principles.

**Arguments:** The user may specify a client name.

**Process:**
1. Identify the client (ask if ambiguous)
2. Read the client's `.claude/CLAUDE.md` and all knowledge files
3. **Pre-brief research (run in parallel):**
   a. Pull fresh performance data from platform APIs (if configured)
   b. Research current platform best practices and trends
4. Generate 10-14 content pieces across two weeks
5. **Create atomic content notes** for each piece in `outputs/content/` (see `references/content-notes.md` for schema)
6. Build the brief with a Content Pieces table linking to each note via `[[wiki-links]]`
7. Include performance snapshot, tests to run, master shot list (consolidated by location)
8. Save markdown brief to `outputs/biweekly-briefs/`
9. If Google Sheets template is configured, copy and fill the template

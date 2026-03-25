---
name: generate-biweekly
description: Generate a two-week content plan with 10-14 pieces, performance data pull, and platform research
---

# Generate Bi-Weekly Plan

The user wants a bi-weekly content plan. Read `skills/ai-cmo/references/biweekly.md` for the full procedure, and `skills/ai-cmo/references/planning.md` for general planning principles.

**Arguments:** The user may specify a client name.

**Process:**
1. Identify the client (ask if ambiguous)
2. Read the client's `.claude/CLAUDE.md` and all knowledge files
3. **Pre-brief research (run in parallel):**
   a. Pull fresh performance data from platform APIs (if configured)
   b. Research current platform best practices and trends
4. Generate 10-14 content pieces across two weeks
5. Include performance snapshot, tests to run, scripts, captions, shot list
6. Save markdown to `marketing/outputs/biweekly-briefs/`
7. If Google Sheets template is configured, copy and fill the template

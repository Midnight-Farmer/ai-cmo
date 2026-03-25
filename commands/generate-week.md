---
name: generate-week
description: Generate a weekly content plan with hooks, scripts, shot lists, and optional Typefully drafts
---

# Generate Weekly Plan

The user wants a weekly content plan. Read `skills/ai-cmo/references/planning.md` § Weekly Plan for the full procedure, and `skills/ai-cmo/references/typefully.md` § Generate Week if they also want Typefully drafts.

**Arguments:** The user may specify a client name and/or source material (blog URL, transcript path).

**Process:**
1. Identify the client (ask if ambiguous)
2. Read the client's `.claude/CLAUDE.md` and knowledge files
3. Check for a current monthly plan to align with
4. Generate 5-7 content pieces with hooks, scripts, shot lists, captions
5. Save to `marketing/outputs/weekly-briefs/`
6. If Typefully is configured, offer to create drafts

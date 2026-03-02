---
name: generate-week
description: Generate a weekly content plan with 5-7 content pieces
argument-hint: "[client-name]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebFetch
---

# Generate Weekly Content Plan

## Resolve Client

The client is: $ARGUMENTS

If no client was provided or multiple clients exist, list `clients/` and ask which one.

If only one client exists in `clients/`, use that one automatically.

## Read Client Context

Read these files in order:
1. `clients/[client]/`.claude/CLAUDE.md`
2. `clients/[client]/company-overview.md`
3. `clients/[client]/marketing/knowledge/voice-guidelines.md`
4. `clients/[client]/marketing/knowledge/personas-storybrand.md`
5. `clients/[client]/marketing/knowledge/goals-and-benchmarks.md`
6. `clients/[client]/marketing/knowledge/whats-working.md`

## Check Monthly Plan

Look in `clients/[client]/marketing/outputs/monthly-briefs/` for the current month's plan. If one exists, align this weekly plan with the appropriate week's theme and content types. If no monthly plan exists, generate independently from knowledge files.

## Review Recent Performance

If `clients/[client]/marketing/tracking/performance.csv` has recent data, review last week's entries to identify what performed well and what underperformed.

## Generate the Plan

Read the planning reference for detailed procedures:

```
Read: skills/ai-cmo/references/planning.md (§ Weekly Plan)
Read: skills/ai-cmo/references/output-formats.md (§ Weekly Plan Template)
```

Generate a weekly plan with:
- **Weekly focus** aligned with monthly theme (or standalone)
- **5-7 content pieces**, each with: platform, format, topic, hook, key message, CTA, "why this works"
- **Video scripts** for any video content (hook/setup/value/CTA)
- **Production shot list** for efficient filming
- **Caption starting points** (hook line + direction)
- **Key messages** aligned with messaging pillars
- **Metrics to watch** this week

## Save the Plan

Save to: `clients/[client]/marketing/outputs/weekly-briefs/YYYY-MM-DD-weekly-plan.md`

Use today's date (Monday of the target week).

## Present to User

Show the complete plan and ask if any adjustments are needed. If the user wants to push content to Typefully, they can say "push to Typefully" as a follow-up.

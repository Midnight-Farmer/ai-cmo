---
name: generate-biweekly
description: Generate a biweekly content plan covering 2 weeks with 10-14 content pieces
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

# Generate Biweekly Content Plan

## Resolve Client

The client is: $ARGUMENTS

If no client was provided or multiple clients exist, list `clients/` and ask which one.

If only one client exists in `clients/`, use that one automatically.

## Read Client Context

Read these files in order:
1. `clients/[client]/.claude/CLAUDE.md`
2. `clients/[client]/company-overview.md`
3. `clients/[client]/marketing/knowledge/voice-guidelines.md`
4. `clients/[client]/marketing/knowledge/personas-storybrand.md`
5. `clients/[client]/marketing/knowledge/goals-and-benchmarks.md`
6. `clients/[client]/marketing/knowledge/whats-working.md`

## Check Monthly Plan

Look in `clients/[client]/marketing/outputs/monthly-briefs/` for the current month's plan. If one exists, align this biweekly plan with the appropriate weeks' themes and content types. If no monthly plan exists, generate independently from knowledge files.

## Review Recent Performance

If `clients/[client]/marketing/tracking/performance.csv` has recent data, review the last 2 weeks to identify patterns.

## Generate the Plan

Read the planning reference for detailed procedures:

```
Read: skills/ai-cmo/references/planning.md (§ Weekly Plan)
Read: skills/ai-cmo/references/output-formats.md (§ Weekly Plan Template)
```

Generate a biweekly plan structured as two weeks. For each week include:
- **Weekly focus** aligned with monthly theme (or standalone)
- **5-7 content pieces**, each with: platform, format, topic, hook, key message, CTA, "why this works"
- **Video scripts** for any video content (hook/setup/value/CTA)
- **Production shot list** for efficient filming
- **Caption starting points** (hook line + direction)

At the plan level include:
- **Biweekly theme** tying both weeks together
- **Key messages** aligned with messaging pillars
- **Combined production planning** for efficient batch filming across both weeks
- **Metrics to watch** over the 2-week period
- **10-14 total content pieces** across both weeks

## Save the Plan

Save to: `clients/[client]/marketing/outputs/weekly-briefs/YYYY-MM-DD-biweekly-plan.md`

Use Monday of the first week as the date.

## Present to User

Show the complete plan and ask if any adjustments are needed. If the user wants to push content to Typefully, they can say "push to Typefully" as a follow-up.

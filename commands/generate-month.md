---
name: generate-month
description: Generate a monthly content strategy with 4-week breakdown
argument-hint: "[client-name]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# Generate Monthly Content Plan

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

## Review Recent Performance

- Check `clients/[client]/marketing/tracking/performance.csv` for last 30 days of data
- Cross-reference with `clients/[client]/marketing/tracking/content-log.csv` for content details
- Check for an existing monthly plan in `clients/[client]/marketing/outputs/monthly-briefs/`

## Generate the Plan

Read the planning reference for detailed procedures:

```
Read: skills/ai-cmo/references/planning.md (§ Monthly Plan)
Read: skills/ai-cmo/references/output-formats.md (§ Monthly Plan Template)
```

Generate a monthly plan with:
- **Monthly theme** aligned with 90-day goal
- **2-3 strategic objectives**
- **Content mix table** (format, quantity, focus)
- **4-week breakdown** with themes, content focus, content types, hypothesis to test
- **Production planning** (shoot days, key assets, B-roll gaps)
- **Metrics targets** with current baselines
- **2 tests to run** with clear success criteria
- **Key messages** aligned with messaging pillars
- **Month-end review checklist**

### Planning Principles
- Anchor everything to the 90-day goal
- 70% proven approaches (from whats-working), 30% experiments
- Group similar content types for batch production
- Be specific about success metrics ("15%+ engagement on Reels" not "more engagement")

## Save the Plan

Save to: `clients/[client]/marketing/outputs/monthly-briefs/YYYY-MM-monthly-plan.md`

## Present to User

Show the complete plan and ask if any adjustments are needed before finalizing.

---
name: overview
description: Get a structured overview of a client's strategy and enable Q&A
argument-hint: "[client-name]"
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Client Overview

## Resolve Client

The client is: $ARGUMENTS

If no client was provided or multiple clients exist, list `clients/` and ask which one.

If only one client exists in `clients/`, use that one automatically.

## Read All Client Files

Read the shared root files:
1. `clients/[client]/company-overview.md`
2. `clients/[client]/contacts.md`
3. `clients/[client]/.claude/CLAUDE.md`

Read all marketing knowledge files:
4. `clients/[client]/marketing/knowledge/voice-guidelines.md`
5. `clients/[client]/marketing/knowledge/personas-storybrand.md`
6. `clients/[client]/marketing/knowledge/goals-and-benchmarks.md`
7. `clients/[client]/marketing/knowledge/whats-working.md`

Optionally check for recent outputs:
8. Check `clients/[client]/marketing/outputs/monthly-briefs/` for the most recent monthly plan
9. Check `clients/[client]/marketing/outputs/weekly-briefs/` for the most recent weekly plan

## Present Structured Summary

Present the overview in this structure:

### Company
- Name, industry, what they do, who they serve
- Key differentiators and market position
- Primary contacts

### Audience
- Target personas (from StoryBrand framework)
- Customer language and pain points
- Buying triggers

### Brand Voice
- Voice attributes (3-5 core attributes)
- "We sound like" / "We don't sound like"
- Messaging pillars
- Tone variations by content type

### Goals & Strategy
- Primary 90-day goal with current/target metrics
- Supporting goals
- Current campaign/theme
- Key KPIs being tracked

### What's Working
- Best content types and formats
- Best posting times
- Top hook patterns
- Topics that resonate
- What to avoid

### Current Priorities
- Active monthly plan summary (if exists)
- Current weekly plan summary (if exists)
- Any active tests or experiments

### Integrations
- What's configured (Google Drive, Sheets, Typefully, etc.)
- What's not configured

## Enable Q&A

After presenting the overview, stay in conversational mode. Answer follow-up questions by referencing the knowledge files. Do not make changes to any files — this is a read-only overview.

Example follow-ups:
- "What's their content mix?"
- "Who are their target personas?"
- "What hooks work best?"
- "How do they handle pricing objections?"
- "What's the current monthly plan?"

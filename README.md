# AI-CMO

Your AI Chief Marketing Officer, built as a [Claude Code](https://claude.ai/claude-code) plugin.

## What It Does

AI-CMO is a strategic marketing advisor that helps you make data-driven content decisions. It doesn't create final content — it directs strategy. You get:

- **Monthly content strategies** with themes, content mix, and experiments to run
- **Bi-weekly execution plans** with performance data pulls and platform research
- **Weekly content plans** with hooks, scripts, shot lists, and captions for 5-7 pieces
- **Performance tracking** that feeds back into smarter plans over time
- **Brand voice guidelines** extracted from your actual writing and content examples
- **Customer personas** built on the StoryBrand framework
- **Revenue attribution** connecting content to business outcomes
- **Operational memory** that persists decisions and context across sessions

Each client gets their own isolated knowledge base. The system learns from your performance data and gets smarter over time.

## Install

```
/plugin install Midnight-Farmer/ai-cmo
```

Requires [Claude Code](https://claude.ai/claude-code) (CLI or Desktop app with Claude Pro/Max plan).

## Quick Start

```
/ai-cmo:new-client my-business
```

This runs a guided ~20 minute interview that builds your complete marketing profile. You'll leave with your first monthly and weekly content plans ready to execute.

## What the Onboarding Covers

You'll have a guided conversation where you'll be asked about:

- **Your business** — what you do, who you serve, what makes you different
- **Content examples** — share posts you've made or accounts you admire (the AI analyzes your style)
- **Writing samples** — paste any natural writing (emails, texts, captions) so the AI captures your real voice
- **Your customers** — who they are, what they struggle with, why they come to you
- **Your goals** — what you want marketing to accomplish in the next 3 months
- **Logistics** — how often you can post, who's creating content, what tools you use

You don't need to have answers to everything. The AI explains concepts as they come up and works with whatever you've got.

## What You Get

After onboarding, you'll have:

- **A strategy profile** — files that capture your brand voice, audience, goals, and positioning
- **Your first monthly plan** — a month of content strategy broken into weekly themes
- **Your first weekly plan** — specific content pieces with hooks, key messages, and direction you can start creating today
- **A tracking system** — ready to log content and performance data from day one
- **A memory system** — the AI remembers decisions, preferences, and context across sessions

## After Setup

The system runs on a simple rhythm:

- **Weekly:** Get a content plan (`weekly plan for [client]`), create and publish, log what you posted
- **Bi-weekly:** Get a two-week execution plan with research and performance data (`biweekly plan for [client]`)
- **Monthly:** Review performance, update insights, get next month's strategy
- **Quarterly:** Reassess goals, set new targets

## Slash Commands

| Command | What It Does |
|---------|-------------|
| `/ai-cmo:new-client [name]` | Set up a new client with guided onboarding |
| `/ai-cmo:generate-week [client]` | Generate this week's content plan with optional Typefully drafts |
| `/ai-cmo:generate-month [client]` | Generate next month's content strategy |
| `/ai-cmo:generate-biweekly [client]` | Generate a two-week plan with performance data and research |
| `/ai-cmo:overview [client]` | Get a structured client summary and enter Q&A mode |

## Natural Language Commands

| Command | What It Does |
|---------|-------------|
| `brief me on [client]` | Get a summary of a client's strategy and ask questions |
| `monthly plan for [client]` | Generate next month's content strategy |
| `weekly plan for [client]` | Generate this week's specific content plan |
| `biweekly plan for [client]` | Generate a two-week execution plan |
| `analyze performance for [client]` | Review data and find patterns |
| `update whats working for [client]` | Refresh performance insights |
| `revenue report for [client]` | Analyze lead and revenue attribution |
| `update strategy for [client]` | Change goals, voice, content mix, or other strategy elements |
| `log content for [client]` | Record a published piece of content |
| `log performance for [client]` | Record engagement metrics |
| `log lead for [client]` | Record a new lead |

## Client Folder Structure

```
clients/[client-name]/
├── company-overview.md           # Shared across all roles
├── contacts.md                   # Key people and partners
├── .claude/CLAUDE.md             # Client-specific instructions
├── marketing/
│   ├── knowledge/                # Strategy documents
│   ├── tracking/                 # CSV data (content, performance, revenue)
│   ├── content/                  # Published content + competitors
│   ├── research/                 # Competitive analysis, audits
│   ├── transcripts/              # Call recordings, interviews
│   ├── memory/                   # Operational memory across sessions
│   └── outputs/                  # Generated plans and briefs
```

## Optional Integrations

The system works fully with local markdown and CSV files. These integrations enhance the workflow but are never required.

| Integration | What It Does | Setup |
|-------------|-------------|-------|
| **Google Drive** | Store deliverables in shared folders | Add folder ID to client CLAUDE.md |
| **Google Sheets** | Collaborative tracking dashboards | Add spreadsheet IDs to client CLAUDE.md |
| **Google Docs** | Collaborative briefs | Specify in client CLAUDE.md |
| **Typefully** | Draft social posts for X + LinkedIn | `TYPEFULLY_API_KEY` env var + config file |

## Marketing Skills

In addition to the core AI-CMO skill, the plugin includes specialized marketing skills for deeper work:

| Skill | What It Does |
|-------|-------------|
| `email-sequence` | Design email sequences, drip campaigns, and lifecycle automation |
| `content-strategy` | Long-form content planning — topic clusters, buyer journey mapping, searchable vs. shareable |
| `marketing-psychology` | 70+ psychological frameworks for hooks, CTAs, messaging, and pricing |
| `seo-audit` | Structured 7-dimension SEO audit (crawlability, Core Web Vitals, on-page, content quality) |
| `analytics-tracking` | UTM frameworks, GA4 events, GTM patterns, and conversion tracking setup |

These skills share client context with AI-CMO and are triggered by natural language — just describe what you need.

## Recommended: Humanizer

AI-CMO directs strategy — but when you need Claude to write or polish copy, pair it with [Humanizer](https://github.com/blader/humanizer). It strips 24 common AI writing patterns (significance inflation, em dash overuse, filler hedging, etc.) so your captions and scripts sound like a person wrote them.

```
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

Once installed, just ask Claude to "humanize" any output. Works great with the weekly plan captions and video scripts.

## Credits

The marketing skills (`email-sequence`, `content-strategy`, `marketing-psychology`, `seo-audit`, `analytics-tracking`) are adapted from [marketingskills](https://github.com/coreyhaines31/marketingskills) by [Corey Haines](https://corey.co). Thank you Corey for building such a comprehensive, well-organized collection of marketing frameworks. The original skills are licensed under MIT and have been adapted here to integrate with the AI-CMO client knowledge system.

## Getting Started Guide

Full step-by-step setup for non-technical users: [dawsonschrader.com/tools/ai-cmo](https://dawsonschrader.com/tools/ai-cmo)

## License

MIT

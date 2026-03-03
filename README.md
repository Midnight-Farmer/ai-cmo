# AI C-Suite

AI-powered executive advisors for your business, built as a [Claude Code](https://claude.ai/claude-code) plugin.

**AI-CMO** (Chief Marketing Officer) is live now. AI-COO and AI-CFO are coming soon.

## What It Does

AI-CMO is a strategic marketing advisor that helps you make data-driven content decisions. It doesn't create final content — it directs strategy. You get:

- **Monthly content strategies** with themes, content mix, and experiments to run
- **Weekly content plans** with hooks, scripts, shot lists, and captions for 5-7 pieces
- **Performance tracking** that feeds back into smarter plans over time
- **Brand voice guidelines** extracted from your actual writing and content examples
- **Customer personas** built on the StoryBrand framework
- **Revenue attribution** connecting content to business outcomes

Each client gets their own isolated knowledge base. The system learns from your performance data and gets smarter over time.

## Install

```
/plugin install Midnight-Farmer/ai-csuite
```

Requires [Claude Code](https://claude.ai/claude-code) (CLI or Desktop app with Claude Pro/Max plan).

## Quick Start

```
/ai-csuite:new-client my-business
```

This runs a guided ~20 minute interview that builds your complete marketing profile. You'll leave with your first monthly and weekly content plans ready to execute.

## Slash Commands

| Command | What It Does |
|---------|-------------|
| `/ai-csuite:new-client [name]` | Create client folder + run guided onboarding |
| `/ai-csuite:generate-week [client]` | Weekly plan: 5-7 pieces with hooks, scripts, shot lists |
| `/ai-csuite:generate-month [client]` | Monthly strategy: themes, content mix, 4-week breakdown |
| `/ai-csuite:generate-biweekly [client]` | Two-week plan: 10-14 pieces across 2 weeks |
| `/ai-csuite:overview [client]` | Structured summary of a client + conversational Q&A |

## Natural Language Commands

These work by just typing them — no slash needed:

| Say This | What Happens |
|----------|-------------|
| `brief me on [client]` | Summary of client strategy + Q&A |
| `monthly plan for [client]` | Generate monthly content strategy |
| `weekly plan for [client]` | Generate weekly content plan |
| `analyze performance for [client]` | Review tracking data, identify patterns |
| `update whats working for [client]` | Update knowledge base with latest insights |
| `revenue report for [client]` | Revenue attribution analysis |
| `log content for [client]` | Quick-add to content log |
| `log performance for [client]` | Quick-add engagement metrics |
| `log lead for [client]` | Quick-add lead/revenue data |
| `update strategy for [client]` | Update goals, voice, content mix, etc. |
| `push to typefully` | Create draft social posts in Typefully |

## Client Folder Structure

Each client gets a shared root (used across all AI roles) plus role-specific subdirectories:

```
clients/[client-name]/
├── company-overview.md            # Shared across all roles
├── contacts.md                    # Shared across all roles
├── .claude/CLAUDE.md              # Shared client instructions
├── marketing/                     # AI-CMO domain
│   ├── knowledge/
│   │   ├── voice-guidelines.md
│   │   ├── personas-storybrand.md
│   │   ├── goals-and-benchmarks.md
│   │   └── whats-working.md
│   ├── tracking/
│   │   ├── content-log.csv
│   │   ├── performance.csv
│   │   └── revenue-attribution.csv
│   ├── content/
│   │   ├── our-content/
│   │   └── competitors/
│   ├── transcripts/
│   └── outputs/
│       ├── monthly-briefs/
│       └── weekly-briefs/
├── operations/                    # AI-COO (coming soon)
└── finance/                       # AI-CFO (coming soon)
```

## Your Weekly Rhythm

| Day | What to Do | Time |
|-----|-----------|------|
| Monday | Log last week's metrics, generate weekly plan | 30-45 min |
| Tue-Thu | Log content as you publish | 5 min/piece |
| Friday | Quick metrics check | 10 min |

Monthly: performance analysis + new monthly plan (~1 hour at month end).

## Integrations (All Optional)

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

## Credits

The marketing skills (`email-sequence`, `content-strategy`, `marketing-psychology`, `seo-audit`, `analytics-tracking`) are adapted from [marketingskills](https://github.com/coreyhaines31/marketingskills) by [Corey Haines](https://corey.co). Thank you Corey for building such a comprehensive, well-organized collection of marketing frameworks. The original skills are licensed under MIT and have been adapted here to integrate with the AI-CMO client knowledge system.

## Getting Started Guide

Full step-by-step setup for non-technical users: [dawsonschrader.com/tools/ai-csuite](https://dawsonschrader.com/tools/ai-csuite)

## License

MIT

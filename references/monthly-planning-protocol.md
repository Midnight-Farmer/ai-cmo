# Monthly Planning Protocol

How to generate monthly content plans. Monthly plans are brainstorming + alignment docs, not detailed execution plans.

---

## What Monthly Plans Are

### What to include
- Current projects review (from client's project tracking or `knowledge/` files)
- Strategic themes and messaging angles
- Content hypotheses to test
- Direction changes from last month
- Resource planning (availability, shooting windows, client permissions)
- Which content series are running this month

### What NOT to include
- Detailed shot lists, specific captions, or day-by-day posting schedules (those go in bi-weekly briefs)

## Before Creating a Monthly Plan, Ask About:

### 1. Last month's review:
- Top 3 performing posts? What underperformed and why?
- Did we hit planned posting frequency? What blocked us?
- Was the production schedule realistic?
- Is the content team's workload manageable?

### 2. Current projects:
- Active projects: name, type, stage, content opportunities
- Recently completed: final photos available? Client willing to do testimonial?
- Upcoming milestones: big reveals, installations, completions this month?
- Client/talent availability for video/quotes/features?

### 3. Direction changes:
- Is messaging resonating? Need to adjust content mix?
- Any new competitors or market changes?

Save review notes to `outputs/monthly-reviews/monthly-review-YYYY-MM.md`.

## Process

1. **Read client context:**
   - Client's `CLAUDE.md`
   - All knowledge files in `knowledge/`
   - `memory/MEMORY.md` for operational context

2. **Review recent performance:**
   - Read `knowledge/whats-working.md` for current patterns
   - Check `knowledge/goals-and-benchmarks.md` for 90-day goals and current priorities
   - If `tracking/performance.csv` has recent data, analyze last 30 days for trends

3. **Check for an existing monthly plan:**
   - Look in `outputs/monthly-briefs/` for the current month
   - If one exists, you're updating — note what's changed since it was written

4. **Generate the plan using the Monthly Plan Template** (see `output-formats.md` for the full template):
   - Set a monthly theme aligned with the 90-day goal
   - Define 2-3 strategic objectives
   - Break into 4 weekly themes with content types and topics
   - Include a hypothesis to test each week
   - Define production planning (shoot days, assets needed, B-roll gaps)
   - Set metrics targets with current baselines
   - Propose 2 tests to run with clear success criteria
   - Align key messages with messaging pillars from `voice-guidelines.md`

5. **Save the plan:**
   - Markdown: `outputs/monthly-briefs/YYYY-MM-monthly-plan.md`
   - If client has a Google Drive path configured, also save DOCX or Google Doc there

## Planning Principles

- Anchor everything to the 90-day goal. If a content piece doesn't advance a strategic objective, question whether it belongs.
- Balance what's proven (from `whats-working.md`) with what needs testing. Roughly 70% proven approaches, 30% experiments.
- Think about production efficiency — group similar content types for batch filming days.
- Be specific about what "success" looks like for each test. "More engagement" is not a success metric. "15%+ engagement rate on educational Reels" is.

---

## Client-Specific Config

Look for these in the client's `CLAUDE.md` or `knowledge/` files:
- **Current projects file** (e.g., `knowledge/current-projects.md`)
- **Content team roles and time budgets** (e.g., `knowledge/hybrid-workflow.md`)
- **Google Drive folder ID** for saving DOCX/Google Doc versions
- **Any additional pre-plan review questions** specific to this client

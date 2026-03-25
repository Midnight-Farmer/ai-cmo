# Bi-Weekly Plan Procedures

Detailed procedures for generating bi-weekly content plans. Bi-weekly plans are a middle ground between weekly execution and monthly strategy — they provide 10-14 content pieces across two weeks with more tactical detail than a monthly plan.

## When to Use Bi-Weekly Instead of Weekly

Bi-weekly plans work best when:
- The client has a regular production schedule (shoot days every 2 weeks)
- Content requires coordination across team members
- The client prefers batch planning for efficiency
- There's a Google Sheets or team-facing template for handoff

Weekly plans are better when:
- Content is reactive or trend-driven
- The client posts at a lower cadence (3x/week or less)
- No batch production workflow exists

## Process

### Pre-Brief: Data & Research (Run in Parallel)

Before writing the brief, run these two steps simultaneously:

#### Step 1: Pull Fresh Performance Data

If the client has platform API access configured (e.g., Meta Graph API for Instagram, analytics exports):

1. Pull post-level insights for the period since the last brief
2. Save raw data to `marketing/tracking/` (platform-specific CSV)
3. Identify top 3 and bottom 3 performers
4. Check if previous tests showed results
5. Update `marketing/knowledge/whats-working.md` with new patterns
6. Reference specific data points in the brief's performance section

If no API access, review manually-logged data in `marketing/tracking/performance.csv`.

#### Step 2: Research Current Platform Best Practices

Search for what's working on social media right now — not just the primary platform, but cross-platform trends:

- Algorithm changes and updates (last 30 days)
- Content format trends and best practices (current month)
- Hooks and editing styles performing well
- New platform features
- Cross-platform trend migration (e.g., TikTok trends → Instagram Reels)
- Caption and SEO strategy updates
- Posting frequency and timing data

**What to do with the research:**
1. Save research doc to `marketing/outputs/platform-research-YYYY-MM.md`
2. Extract 3-5 specific, actionable tactics to test this cycle
3. Update `marketing/knowledge/whats-working.md` if anything contradicts existing advice
4. Include a "What We're Testing This Cycle" section in the brief

**Sources to prioritize:** Buffer, Hootsuite, Later, Social Media Examiner, Sprout Social, Kapwing, platform-specific official announcements. Prefer data-backed findings over opinion pieces.

### Generate the Bi-Weekly Brief

1. **Read client context:**
   - Client's `.claude/CLAUDE.md`
   - All files in `marketing/knowledge/`

2. **Check for a current monthly plan:**
   - Look in `marketing/outputs/monthly-briefs/` for this month's plan
   - Align the bi-weekly plan with the current month's themes and objectives

3. **Structure the brief:**

   **Performance Snapshot:**
   - Top/bottom posts from last cycle with analysis of why
   - Test results from previous cycle

   **Two-Week Overview:**
   - Date range and theme
   - Posting schedule with dates, formats, platforms
   - Production/shoot planning

   **Content Pieces (10-14):**
   For each piece include:
   - Platform and format
   - Topic and hook
   - Script (for video: Hook/Body/End structure; for carousels: slide breakdown)
   - Caption direction
   - CTA
   - Why this works (reference whats-working.md or current research)

   **What We're Testing This Cycle:**
   - 3-5 specific tactics from research
   - How to measure success

   **Shot List:**
   - Combined production plan for all video content
   - Locations, setups, and notes

   **Checklists:**
   - Pre-shoot preparation
   - Post-shoot editing and publishing

4. **Save the plan:**
   - Markdown: `marketing/outputs/biweekly-briefs/YYYY-MM-DD-biweekly-brief.md`
   - If client has Google Sheets template configured, copy and fill it
   - If client has Google Drive configured, save to shared folder

### Planning Principles for Bi-Weekly Plans

- Every content piece needs a clear "why" — connect to data, goals, or a specific test
- Balance proven approaches (70%) with experimental tactics (30%)
- Group similar content for production efficiency (batch shoot days)
- Scripts should be concise — the team adapts during filming
- Include platform research findings as actionable tests, not just FYI
- Hook lines are the most important element — reference proven patterns
- Caption direction > final copy — give the human team room to adapt

### Markdown Formatting Guidelines

Optimize for mobile reading and narrow screens:

- **Captions:** Individual blocks per post, not wide tables
- **Scripts:** Simple tables (Section | Time | Visual | Audio)
- **Tables:** Keep columns narrow with short labels
- **Remove clutter:** No change logs, no checked-off checklists, no redundant sections
- **Footer:** Single line with created/updated dates and content period

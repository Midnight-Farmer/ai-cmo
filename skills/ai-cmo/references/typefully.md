# Typefully Integration

Procedures for creating and managing social media drafts via the Typefully v2 API.

**This integration is optional.** The AI-CMO system works fully without Typefully. Only set this up if you want to push draft social posts directly from your content plans.

## Prerequisites

- API key stored as environment variable (e.g., `TYPEFULLY_API_KEY` in user's shell config)
- The env var may not be loaded in Claude Code's shell by default. Always source the shell config first:
  ```bash
  source ~/.zshrc 2>/dev/null || source ~/.bashrc 2>/dev/null
  ```
- Client's `marketing/knowledge/typefully-config.md` must have their `social_set_id` configured
- Base URL: `https://api.typefully.com/v2`
- Auth: Bearer token from the env var

## API Essentials

- Drafts are created via `POST /v2/social-sets/{social_set_id}/drafts`
- Multi-platform support: X + LinkedIn in a single draft using the `platforms` object
- Drafts are always created as **unpublished** so the user reviews and schedules in Typefully
- Always write JSON payloads to temp files to avoid shell escaping issues
- Tags must be created manually in the Typefully app before they can be used via API — omit the `"tags"` field unless the user confirms tags exist

---

## Push to Typefully

Triggered by natural language: "push to typefully", "create typefully drafts", or similar after reviewing a content plan.

### Step 1: Gather Source Material

Parse the context for content to push:
- If a weekly/biweekly plan was just generated, use those content pieces
- If the user provides specific content, use that
- If neither, ask what content to create drafts for

### Step 2: Read Client Knowledge

Read these files in the client's directory:
1. `.claude/CLAUDE.md`
2. `marketing/knowledge/voice-guidelines.md`
3. `marketing/knowledge/typefully-config.md`
4. `marketing/knowledge/whats-working.md`

### Step 3: Prepare Content

For each content piece, create platform-specific versions:

**Platform-specific formatting:**
- **X:** 280 characters max per tweet. Can be a thread (multiple tweets separated by clear breaks). Punchy, direct, conversational.
- **LinkedIn:** 500-1,500 characters. Hook line, body with value, CTA. More narrative and professional.

### Step 4: Present for Review

Show the complete draft content to the user with all pieces and platform versions. Ask: "Does this look good? Any changes before I create the Typefully drafts?"

Wait for user confirmation before proceeding.

### Step 5: Create Typefully Drafts

For each approved content piece:

1. Read the `social_set_id` from `marketing/knowledge/typefully-config.md`
2. Build the JSON payload:

```json
{
  "content": "The full post text for the primary platform",
  "platforms": {
    "x": {
      "content": "X-specific version (280 char max per tweet)"
    },
    "linkedin": {
      "content": "LinkedIn-specific version (longer narrative)"
    }
  },
  "draft_title": "Descriptive title for organization"
}
```

3. Write the JSON to a temp file:
```bash
cat > /tmp/typefully-draft.json << 'ENDJSON'
{ ... payload ... }
ENDJSON
```

4. Create the draft:
```bash
curl -s -X POST "https://api.typefully.com/v2/social-sets/${SOCIAL_SET_ID}/drafts" \
  -H "Authorization: Bearer ${TYPEFULLY_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/typefully-draft.json
```

5. Check the response for success (should return draft ID and URL)
6. Log each draft's ID and URL

**Important:**
- Never include `publish_at` — all drafts are unpublished for user review
- Omit `"tags"` unless the user has confirmed tags exist in Typefully
- If curl fails, check that the env var is loaded and the social_set_id is correct

### Step 6: Save References

If a weekly/biweekly plan was the source, update it with a "Typefully Drafts" section at the bottom:
- Draft titles
- Draft IDs
- Private URLs for review

### Step 7: Report Summary

Tell the user:
- How many drafts were created
- Links to review them in Typefully
- Any errors that occurred
- Reminder to review and schedule in Typefully

---

## Check Status

Triggered by "typefully status" or similar.

### Process

1. Read `marketing/knowledge/typefully-config.md` to get `social_set_id`
2. Source the shell config for the API key
3. Fetch drafts:
```bash
curl -s "https://api.typefully.com/v2/social-sets/${SOCIAL_SET_ID}/drafts" \
  -H "Authorization: Bearer ${TYPEFULLY_API_KEY}"
```
4. Filter by status if the user specified "scheduled" or "published"
5. Display in a clean table:

| # | Title | Status | Platforms | Scheduled | Preview | URL |
|---|-------|--------|-----------|-----------|---------|-----|

6. Provide a summary:
   - Total drafts found
   - Breakdown by status (draft, scheduled, published)
   - Highlights for this week
7. If published drafts are shown, remind the user to log performance data

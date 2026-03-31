#!/bin/bash
# One-time Google Ads + GA4 OAuth setup — re-auth with both scopes
source ~/.zshrc.local 2>/dev/null
uv run /Users/dawsonschrader/Obsidian/Tools/AI-CMO/ai-cmo/skills/analytics-tracking/scripts/gads_pull.py \
  --oauth-client /Users/dawsonschrader/.config/google/ga4-oauth-client.json \
  --customer-id 955-113-7388 \
  campaigns --days 7

#!/bin/bash
# One-time GA4 OAuth setup — run this once, then ga4_pull.py works forever
uv run /Users/dawsonschrader/Obsidian/Tools/AI-CMO/ai-cmo/skills/analytics-tracking/scripts/ga4_pull.py \
  --oauth-client /Users/dawsonschrader/.config/google/ga4-oauth-client.json \
  --property-id 341929409 \
  top-pages

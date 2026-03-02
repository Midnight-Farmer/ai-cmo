---
name: new-client
description: Create a new client and run the guided onboarding interview
argument-hint: "[client-name]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# New Client Setup

## Resolve Client Name

The client name is: $ARGUMENTS

If no name was provided, ask the user: "What would you like to name this client? Use lowercase with hyphens (e.g., `acme-corp`)."

## Create Folder Structure

Run the initialization script to create all folders and copy templates:

```bash
python3 "$(dirname "$(find . -path '*/ai-cmo/scripts/init-client.py' -print -quit 2>/dev/null || find ~/.claude/plugins -path '*/ai-cmo/scripts/init-client.py' -print -quit 2>/dev/null)")/init-client.py" [client-name] --path clients/
```

If the script can't be found, create the folder structure manually:

```
clients/[client-name]/
├── company-overview.md
├── contacts.md
├── .claude/CLAUDE.md
├── marketing/
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
```

## Run Onboarding Interview

Read the onboarding reference file for the full guided discovery workflow:

```
Read: skills/ai-cmo/references/onboarding.md
```

Follow the onboarding procedure step by step. Walk through discovery questions one section at a time. Update knowledge files as you go.

The onboarding covers:
1. **Company Overview** → `company-overview.md` + `contacts.md`
2. **Content Examples** → seeds `marketing/knowledge/voice-guidelines.md`
3. **Writing Samples** → `marketing/knowledge/voice-guidelines.md`
4. **Voice Refinement** → `marketing/knowledge/voice-guidelines.md`
5. **Customer Intelligence** → `marketing/knowledge/personas-storybrand.md`
6. **Goals & Benchmarks** → `marketing/knowledge/goals-and-benchmarks.md`
7. **Operational Setup** → `.claude/CLAUDE.md`
8. **Launch** → first monthly + weekly plans in `marketing/outputs/`

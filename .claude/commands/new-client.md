---
description: Create a new client folder and run the guided onboarding interview (~20 min)
argument-hint: client-name
---

# New Client Onboarding

The user wants to onboard a new client. Read `references/onboarding.md` for the full guided onboarding procedure.

**Arguments:** The user may provide the client name after the command (e.g., `/new-client acme-corp`). If no name is given, ask for one.

**Process:**
1. Run `scripts/init-client.py` to create the folder structure. This also:
   - Copies the `templates/gitignore.template` as `.gitignore`
   - Initializes an isolated git repo inside the client folder
   - Makes an "Initial client setup" commit
   - Note: the parent AI CMO repo ignores `clients/*/`, so this repo stays private
2. Follow the onboarding interview in `references/onboarding.md`
3. Populate knowledge files as the user answers
4. Generate the client's `CLAUDE.md`
5. Generate the first monthly plan and weekly plan
6. Commit progress periodically inside the client folder as work is done (`cd clients/[name] && git add . && git commit -m "..."`)

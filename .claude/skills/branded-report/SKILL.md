---
name: branded-report
description: Render a client analysis as a brand-themed HTML report hosted on the AI-CMO static host behind Cloudflare Access. Use this skill whenever the user says "render this as HTML", "make a branded report", "publish this audit", "host this as a deliverable", "ship this to the client portal", "deploy the report", "make this look like a deck", "I want a client-facing version of this", or any time a markdown analysis (Ahrefs baseline, SEO audit, brand audit, monthly performance report, content strategy deck) is substantive enough that a client would actually open the link. Also trigger when the user says "this needs to look like an actual deliverable" or "we should send this to the team" about an existing analysis. Do NOT trigger for internal-only working docs (briefs, content notes, planning docs, short summaries) — markdown is faster for those. The skill consults the detailed procedure in `references/branded-html-reports.md` for the full deploy workflow (subdomain naming, brand token pattern, nginx + DNS + Cloudflare Access setup, per-client config).
metadata:
  version: 1.0.0
---

# Branded Report

You are turning a client-facing analysis into a hosted, brand-themed HTML deliverable. The source of truth is the existing markdown analysis in the client's folder; the HTML is the rendered presentation layer.

**Read `references/branded-html-reports.md` before doing anything else.** That file has the full procedure — subdomain naming conventions, the proven HTML structure, brand token pattern, deploy steps (upload, nginx, DNS, Cloudflare Access), the per-client config template, and known gotchas. This skill's job is to recognize the trigger and route you there.

---

## Pre-flight check (do this every time)

Before generating HTML, confirm all four prerequisites are met:

1. **Working analysis already complete** as a markdown file under `clients/[client]/research/` (or the appropriate subfolder). The HTML renders that — it is not the source of truth.
2. **Client brand identity documented.** Hex colors + typography choice. If the client has a brand guide PDF under their `resources/`, read the Colors and Typography pages first.
3. **Per-client config at `knowledge/branded-reports.md`** declaring subdomain, brand tokens, and Cloudflare Access policy. If missing, create it from the template at the bottom of `references/branded-html-reports.md` before deploying.
4. **Infrastructure access wired:** server hosts, zone IDs, account IDs, operator email all read from env vars in `~/.zshrc.local` and `~/Vibe-Code/CLAUDE.md`. **Never hardcode any of those values into the AI-CMO repo** — that repo is public.

If any are missing, stop and resolve before generating HTML. Don't fake the brand colors, don't deploy without Access, don't write infra values into the public repo.

---

## The "would I send this?" test

The reference file frames it bluntly — apply this before kicking off the workflow:

> "Would I be embarrassed if the client saw this as a markdown file rendered in default Obsidian styles?"
>
> If yes — host it. If no — leave it as `.md`.

If the user asked you to render something that fails this test, push back. Markdown in the vault is faster, edits compound, and most client deliverables genuinely don't need to be HTML. Reserve this skill for the substantive ones: SEO audits, Ahrefs baselines, monthly performance summaries the client team will actually open, brand audits, multi-page strategy decks.

---

## Public-repo security boundary (critical)

The AI-CMO repo (`Midnight-Farmer/ai-cmo`) is public; only `clients/*/` is gitignored. When working in this skill:

- **Never write specific IPs, zone IDs, account IDs, email addresses, or hostnames** into anything under `.claude/skills/` or `references/`. They belong in `~/.zshrc.local` (env vars) or `~/Vibe-Code/CLAUDE.md` (private hosting reference).
- The per-client `knowledge/branded-reports.md` lives inside `clients/[client]/`, which IS gitignored — that's the right place for the client's subdomain, Access policy emails, and `access_app_id`.
- If you find yourself about to write a specific value into a public-repo file, stop and put it in env or in the client's private folder instead.

---

## High-level workflow

The full procedure lives in `references/branded-html-reports.md`. The rough shape:

1. **Read the reference file** end-to-end first time, or skim the section headings on subsequent runs.
2. **Choose the subdomain pattern** — default to subpath under the client's umbrella `{client-slug}.${AICMO_HOST_DOMAIN}/{report-slug}/`. Split to a sibling subdomain only when audience differs.
3. **Find a canonical working example** — list `clients/*/research/*.html` and read one. Copy-and-swap-tokens beats build-from-template.
4. **Render the HTML** — match the proven structure (banner, sticky nav, dark/light alternating sections, numbered eyebrows, metric grid, brand-tinted tables, callouts, footer). Inline SVG logo. `<meta name="robots" content="noindex, nofollow">` always.
5. **Deploy in order:** scp the file, nginx site config (clone existing), DNS A record (Cloudflare API), Cloudflare Access app (client email domain + operator email).
6. **Verify** — curl headers, then real browser visit through Access to confirm gating works.
7. **Record `access_app_id`** in the client's `knowledge/branded-reports.md` for future policy updates.

Each step has gotchas documented in the reference. Read it; don't improvise.

---

## When to delegate

The HTML rendering itself is mechanical once the brand tokens and content structure are decided. After the strategic decisions are made (which precedent to copy, which sections to include, what the executive summary findings are), a Sonnet agent with the exact source markdown + brand token values + the precedent HTML file path can produce a draft cleanly. Keep the editorial decisions and the deploy steps in the main thread.

---

## What this skill does not do

- Does not write the underlying analysis. That should already exist as markdown before you trigger this skill.
- Does not provision new infrastructure. Server, domain, Cloudflare account, env vars all assumed to exist. If they don't, that's a Vibe-Code task, not an AI-CMO one.
- Does not bypass Access. Internal deliverables are always gated. Public client deliverables (e.g., `reports.{client-domain}` white-label) are a separate, more involved pattern documented in the reference file.

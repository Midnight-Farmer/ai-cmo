---
title: "Branded HTML Reports"
description: "Render an analysis as a brand-themed HTML page hosted on the AI-CMO static host, gated behind Cloudflare Access"
category: workflow
last_updated: 2026-05-16
status: active
priority: medium
---

# Branded HTML Reports

When a client deliverable is substantive enough that a markdown file in the vault doesn't do it justice — Ahrefs baselines, SEO audits, monthly performance reports, brand reviews, content audits — render it as a brand-themed HTML page and host it on the AI-CMO static host at `{client-slug}.{AICMO_HOST_DOMAIN}`, gated behind Cloudflare Access for the client's team.

This procedure is generic. All infrastructure-specific values (domain, server, IPs, zone IDs, operator email) live in env vars in `~/.zshrc.local` and in `~/Vibe-Code/CLAUDE.md` — neither of which is in this public repo. Client-specific brand tokens, subdomain assignment, and Access policies live in each client's `knowledge/branded-reports.md` (private per-client repo).

---

## When to use this

- **Use** when the artifact would actually get viewed by the client team and benefits from looking like a deliverable instead of a notebook entry. SEO audits, Ahrefs baselines, monthly performance reports, brand audits, content strategy decks.
- **Skip** for internal-only working docs (briefs, content notes, planning), short summaries, or anything the client won't open. Markdown is faster and lives in the vault where edits compound.

The test: "Would I be embarrassed if the client saw this as a markdown file rendered in default Obsidian styles?" If yes — host it. If no — leave it as `.md`.

---

## Prerequisites

1. **Working analysis already complete** as a markdown file in the client folder (e.g., `research/ahrefs-baseline.md`). The HTML is the rendered presentation layer, not the source of truth.
2. **Client brand identity documented.** Hex colors + font choice. If the client has a brand guide PDF in `resources/`, read the Colors and Typography pages first.
3. **Per-client config file at `knowledge/branded-reports.md`** declaring subdomain, brand tokens, Access policy. Create it on first deploy if missing — see the per-client config template at the bottom of this doc.
4. **Infrastructure access:** all server IPs, zone IDs, SSH hosts, account IDs, and the operator's primary email live in `~/Vibe-Code/CLAUDE.md` (authoritative hosting reference, NOT in this repo) and in env vars in `~/.zshrc.local` (NOT in this repo). This file points at those — it never duplicates the values. **If you find yourself about to write a specific IP, zone ID, account ID, email address, or hostname into this file or any file under `references/`, stop. That value belongs in env or in the Vibe-Code reference, not in the public AI-CMO repo.**

If any of those aren't wired, stop and resolve before generating HTML.

---

## Subdomain naming

**AI-CMO client deliverables live on the AI-CMO host domain** (the value of `$AICMO_HOST_DOMAIN`, defined in `~/.zshrc.local` — see Vibe-Code CLAUDE.md for which domain that is and why). The financial-consulting brand has its own separate domain documented in Vibe-Code. Keeping them split prevents brand confusion across business lines.

| Pattern | When |
|---|---|
| `{client-slug}.${AICMO_HOST_DOMAIN}` | Umbrella for everything for this client. Default. First report becomes `index.html` at root, future reports go in subpaths. One Cloudflare Access app covers everything. |
| Subpath `{client-slug}.${AICMO_HOST_DOMAIN}/{report-slug}/` | Each subsequent report after the first. Single Access app, single nginx site, simple `mkdir + scp`. **Default for ongoing reports.** |
| `{client-slug}-{topic}.${AICMO_HOST_DOMAIN}` | When a specific report needs its own URL for sharing/permissions. Separate DNS, separate Access app. Use sparingly. |
| `reports.{client-domain}` | Full white-label on the client's own domain via CNAME. Most professional, most setup work (client DNS access + Cloudflare cert per client). For client-facing public deliverables only — internal reports stay on the AI-CMO host. |

**Default:** subpaths under the umbrella. Split to a sibling subdomain only when the audience genuinely differs (e.g., when a style guide has a different audience than the operational content plans).

---

## Canonical working example

The first instance of this pattern lives in the first client folder under `clients/` that has both:

- `research/{report-slug}.html` — rendered HTML
- `knowledge/branded-reports.md` — client config including subdomain, brand tokens, Access policy

Both files are in the client's private per-client repo (gitignored from this public AI-CMO repo). To find them, list `clients/*/research/*.html` and read the first one returned. That's your starting point.

**When adapting for a new client, copy a working precedent and swap the brand tokens.** Building from a known-good file beats building from an abstract template — every block is already proven to render correctly with brand colors and respond on mobile.

---

## HTML structure conventions

The proven pattern (extracted from the EP file). All client reports follow this:

```
<head>
  - Montserrat or Inter from Google Fonts (Fieldwork/Cera/etc. paid alternatives only if the client has licenses)
  - <meta name="robots" content="noindex, nofollow"> — these are private, never index
  - Inline <style> with CSS custom properties for brand tokens (see Brand Token Pattern below)
</head>
<body>
  <div class="banner">Internal · Team preview</div>
  <nav class="nav">
    - sticky, dark brand-color background, brand mark + section anchors + report date stamp
  </nav>
  <header class="hero" id="top">
    - dark-brand-color hero with eyebrow + h1 + dek + 4-cell metadata grid (Pulled / Refresh / Units / Scope)
  </header>
  <section id="summary" class="is-light">
    - executive summary: 5 numbered findings, max
  </section>
  <!-- alternating is-dark / is-light sections -->
  <!-- each section has: numbered eyebrow (01/09), h2, lede, then content (tables, metric grids, callouts) -->
  <footer>
    - dark-brand-color, brand mark + report stamp
  </footer>
</body>
```

### Required section components

- **Section header:** numbered eyebrow (`01 / 09`), h2 (uppercase), lede paragraph
- **Metric grid:** 4–6 KPI tiles for the snapshot section (Domain Rating, Traffic, etc.)
- **Tables:** brand-tinted thead, hover-tinted rows, `.is-self` row for highlighting the client's own data, `.num` class for right-aligned numerics
- **Callouts:** left-bordered with brand accent, used for "the single biggest finding" moments
- **Recommendations:** numbered list with KD/priority chips on the right side of each title

### Alternating dark/light pattern

Sections alternate `is-dark` (brand primary dark color background, light text) and `is-light` (brand cream/off-white background, dark text). This mirrors most modern brand guides' page-flow rhythm and gives natural visual chapter breaks without needing dividers.

---

## Brand token pattern

Every client gets six core CSS custom properties + their semantic aliases. Pull the exact values from the client's brand guide.

```css
:root {
  /* Primary brand */
  --brand-dark:       /* primary dark color — bodies/nav/footer background */
  --brand-dark-80:    /* 80% tint for borders on dark backgrounds */
  --brand-accent:     /* primary accent color — eyebrows, links, highlights, chips */
  --brand-accent-80:  /* 80% tint for on-dark accent text */
  --brand-secondary:  /* secondary brand color — for "medium priority" chips, links on light */
  --brand-light:      /* off-white / cream — light section background */
  --brand-light-deep: /* slightly darker version of light — callout background, table thead */

  /* Semantic aliases — never change these names, only the values they point to */
  --bg-canvas:       var(--brand-light);
  --bg-canvas-alt:   var(--brand-dark);
  --bg-surface:      var(--brand-light-deep);
  --fg-primary:      var(--brand-dark);
  --fg-on-dark:      var(--brand-light);
  --accent:          var(--brand-accent);
  --link:            var(--brand-secondary);
  --border-subtle:   /* a creme-deep / tan tone */
  --border-on-dark:  /* a 25% lighter brand-dark */

  /* Typography — Montserrat is the safe free default; substitute if the client has a paid display face */
  --ff-display: 'Montserrat', system-ui, sans-serif;
  --ff-body:    'Montserrat', system-ui, sans-serif;
}
```

Bold uppercase Montserrat 700–800 stands in cleanly for most paid display faces (Fieldwork, Cera, Founders Grotesk Bold). If the client's body font is a serif, swap to Crimson Pro, Source Serif Pro, or Spectral as the free alternative.

**Logo as inline SVG.** Don't host PNG/SVG files for the brand mark. Inline an SVG in the nav and footer — fewer requests, scales cleanly, recolors trivially via `fill`. If the brand has a complex logo, fall back to a typographic wordmark (`{Client Name}` in display font + a secondary tagline in the accent color).

---

## Deploy workflow

Once the HTML file is ready and saved to `clients/{slug}/research/{report-name}.html`:

### 1. Upload to the static host

`$SPHOST_USER`, `$SPHOST_HOST`, and `$AICMO_HOST_DOMAIN` are defined in `~/.zshrc.local` (see "Required env vars" section). The full server inventory and SSH access pattern is documented in `~/Vibe-Code/CLAUDE.md`.

```bash
# First deploy only — create web root
ssh "$SPHOST_USER@$SPHOST_HOST" "sudo mkdir -p /var/www/{client-slug}.$AICMO_HOST_DOMAIN/html && sudo chown -R $SPHOST_USER:$SPHOST_USER /var/www/{client-slug}.$AICMO_HOST_DOMAIN"

# Upload the HTML
scp clients/{slug}/research/{report-name}.html "$SPHOST_USER@$SPHOST_HOST:/var/www/{client-slug}.$AICMO_HOST_DOMAIN/html/index.html"
```

For subsequent reports, upload to a subpath instead:

```bash
ssh "$SPHOST_USER@$SPHOST_HOST" "mkdir -p /var/www/{client-slug}.$AICMO_HOST_DOMAIN/html/{report-slug}"
scp clients/{slug}/research/{report-name}.html "$SPHOST_USER@$SPHOST_HOST:/var/www/{client-slug}.$AICMO_HOST_DOMAIN/html/{report-slug}/index.html"
```

### 2. Nginx site config (first deploy only)

Don't write the nginx config from scratch — clone an existing client site, swap the server_name + root, leave everything else identical. Pull a known-good template at deploy time:

```bash
# Pick any existing AI-CMO host subdomain as the template
ssh "$SPHOST_USER@$SPHOST_HOST" "cat /etc/nginx/sites-available/{existing-client}.$AICMO_HOST_DOMAIN"
```

The shape is standard: HTTP→HTTPS redirect server block, plus an HTTPS block with the wildcard Cloudflare origin cert (TLS terminated at edge, origin cert documented in Vibe-Code CLAUDE.md), `root` pointed at the new web root, security headers, and a long-cache rule on static assets.

Enable, test, reload:

```bash
ssh "$SPHOST_USER@$SPHOST_HOST" "sudo ln -sf /etc/nginx/sites-available/{client-slug}.$AICMO_HOST_DOMAIN /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx"
```

### 3. DNS A record (first deploy only)

Zone IDs and the SP-Host IP live in `~/Vibe-Code/CLAUDE.md` and/or env vars in `~/.zshrc.local`. Read them at deploy time — never hardcode here.

```bash
# Read from env (see "Required env vars" section)
source ~/.zshrc.local
# $CLOUDFLARE_API_TOKEN, $CLOUDFLARE_ZONE_AICMO_HOST, $SPHOST_IP all available

curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$CLOUDFLARE_ZONE_AICMO_HOST/dns_records" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"A\",\"name\":\"{client-slug}\",\"content\":\"$SPHOST_IP\",\"proxied\":true,\"ttl\":1}"
```

### 4. Cloudflare Access app (first deploy only)

Get the policy specifics from the client's `knowledge/branded-reports.md` — `access_policy:` field. **Standard pattern (confirmed 2026-05-16):** allow the client's email domain + the operator's primary work email (env var `$OPERATOR_PRIMARY_EMAIL`).

```bash
source ~/.zshrc.local
# $CLOUDFLARE_API_TOKEN, $CLOUDFLARE_ACCOUNT_ID, $OPERATOR_PRIMARY_EMAIL all available

curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/access/apps" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"{Client Name} — Internal\",
    \"domain\": \"{client-slug}.$AICMO_HOST_DOMAIN\",
    \"type\": \"self_hosted\",
    \"session_duration\": \"24h\",
    \"policies\": [{
      \"name\": \"team\",
      \"decision\": \"allow\",
      \"include\": [
        { \"email_domain\": { \"domain\": \"{client-email-domain}\" } },
        { \"email\": { \"email\": \"$OPERATOR_PRIMARY_EMAIL\" } }
      ]
    }]
  }"
```

**Important:** Cloudflare Access silently refuses to send OTP emails to addresses NOT on the allowlist. If a user reports "no email," the first check is always the policy. Per-client config files should explicitly list every allowed email/domain so this is auditable.

Save the returned `id` to the client's `knowledge/branded-reports.md` under `access_app_id:`. Required for any future policy updates.

Access enforcement takes 1–2 minutes to start gating real browser visits. The site will return HTTP 200 to curl before that.

### 5. Verify

```bash
curl -sI "https://{client-slug}.$AICMO_HOST_DOMAIN/" | head -3
```

Expect HTTP 200. If Access is enforcing, browser visits should hit a Google login challenge.

### 6. Log the change

Per `~/Vibe-Code/CLAUDE.md`, every SP-Host change gets logged. SSH to Charlie and append to `~/Obsidian - Main/Efforts/Self Hosted/SP-Host/SP-Host - Logs.md`:

```markdown
## YYYY-MM-DD - {Client Name} {Report Name}

### Overview
One-line description of what was deployed and why.

### Changes Made
- Created /var/www/{client-slug}.{aicmo-host-domain}/html/...
- Created nginx site config
- DNS A record + Cloudflare Access app
- (or "Added subpath /{report-slug}/ to existing {client-slug}.{aicmo-host-domain}")

### Notes
- Source: clients/{slug}/research/{report-name}.md
- Access app id: ... (if newly created)

---
*Updated by Claude Code - YYYY-MM-DD*
```

### 7. Save the HTML back to the client folder

Keep the rendered HTML version-controlled alongside the markdown source:

```bash
cp /tmp/{report-name}.html clients/{slug}/research/{report-name}.html
```

The vault is the source of truth. SP-Host is the delivery vehicle.

---

## Per-client config — `knowledge/branded-reports.md`

Each client using this pattern gets one config file. Template:

````markdown
---
title: "Branded HTML Reports Configuration"
description: "Subdomain, brand tokens, and Access policy for client-hosted HTML deliverables"
category: workflow
last_updated: YYYY-MM-DD
status: active
priority: medium
---

# {Client Name} — Branded HTML Reports

## Deployment

- **Subdomain:** `{client-slug}.{AI-CMO host domain — see ~/.zshrc.local}`
- **Cloudflare Access app id:** `xxxxx` (populate after first deploy)
- **Access policy:** allow `@{client-email-domain}` + operator primary email
- **Web root on host:** `/var/www/{client-slug}.{aicmo-host-domain}/html/`

## Brand tokens

From {client brand guide source, e.g., "ClientBrandGuide.pdf in resources/"}.

```css
--brand-dark:       #XXXXXX;  /* Name from brand guide */
--brand-dark-80:    #XXXXXX;
--brand-accent:     #XXXXXX;
--brand-accent-80:  #XXXXXX;
--brand-secondary:  #XXXXXX;
--brand-light:      #XXXXXX;
--brand-light-deep: #XXXXXX;
```

## Typography

- **Display:** {Brand display font, e.g., "Fieldwork"}
- **Display free alternative (use this):** {e.g., "Montserrat"}
- **Body:** same family
- **Weights needed from Google Fonts:** 400, 500, 600, 700, 800

## Logo

Inline SVG in nav + footer. Pattern from this client:

```svg
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- client-specific paths, using brand colors -->
</svg>
```

## Voice for HTML content

- Headlines: sentence case or all caps? (Reference voice-guidelines.md)
- Banned constructions: (carry over from voice-guidelines.md)
- Run all client-facing copy through `humanizer` before finalizing per project standard

## Reports deployed

| Date | Report | URL | Source |
|---|---|---|---|
| YYYY-MM-DD | First report name | https://{client-slug}.{aicmo-host}/ | research/source.md |
````

---

## Anti-patterns

- **Don't generate HTML before reading the brand guide.** Stock-feeling colors and a generic system font undermine the whole reason to do this. If there's no brand guide, ask before generating.
- **Don't host without Access.** Public subdomains on the AI-CMO host exist for landing pages and intentionally-public assets. Client deliverables are always gated — even if the content seems benign, it sets a bad precedent.
- **Don't skip the SP-Host log.** Every infrastructure change goes in the log. Future-you (or another agent) needs to find what's deployed where.
- **Don't index the page.** `<meta name="robots" content="noindex, nofollow">` belongs in every report. These shouldn't surface in search.
- **Don't render the HTML in place of updating the markdown.** The markdown is the source of truth. If insights change, update the `.md` first, then re-render the HTML, then re-upload. Don't edit the deployed HTML directly.
- **Don't hardcode credentials.** API tokens come from `~/.zshrc.local` env vars. Zone IDs and SP-Host IPs are documented in `~/Vibe-Code/CLAUDE.md` and don't need to be re-derived per deploy.

---

## Required env vars

These must be set in `~/.zshrc.local` (which is gitignored by convention and never pushed). The values themselves are documented in `~/Vibe-Code/CLAUDE.md` — this list is just the variable names so an agent knows what to read.

| Var | Purpose |
|---|---|
| `CLOUDFLARE_API_TOKEN` | Cloudflare API auth (DNS + Access edit scope) |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare account identifier |
| `CLOUDFLARE_ZONE_AICMO_HOST` | Zone ID for the AI-CMO host domain |
| `AICMO_HOST_DOMAIN` | The AI-CMO host domain itself (e.g., the subdomain umbrella for all clients) |
| `SPHOST_USER` | SSH user on the static host |
| `SPHOST_HOST` | SSH-resolvable hostname (Tailscale) of the static host |
| `SPHOST_IP` | Public IP of the static host (for DNS A records) |
| `OPERATOR_PRIMARY_EMAIL` | The operator's canonical work email — added to every Access policy by default |

If any of these are missing, ask the operator to set them. **Never write placeholder values into this file or commit a deploy script with hardcoded values.**

---

## Cross-references

- `~/Vibe-Code/CLAUDE.md` — authoritative hosting reference (Cloudflare, static host, nginx, DNS, Access). Lives outside the AI-CMO repo for a reason — it contains the actual infra values. Don't duplicate from it.
- `~/Obsidian - Main/Efforts/Self Hosted/{host}/{host} - Server Overview and Directory.md` — server inventory on Charlie
- `clients/{slug}/research/{report-slug}.html` — first working example (in a private per-client repo; list `clients/*/research/*.html` to find it)
- `clients/{slug}/knowledge/branded-reports.md` — first client config (in a private per-client repo, use as a template)

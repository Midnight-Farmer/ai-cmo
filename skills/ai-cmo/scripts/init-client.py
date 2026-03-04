#!/usr/bin/env python3
"""
Initialize a new AI-CMO client folder structure.

Usage:
    init-client.py <client-name> --path <base-path>

Example:
    init-client.py acme-corp --path clients/

Creates the full client directory structure with shared root files
and role-specific subdirectories:

    clients/acme-corp/
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
    │   ├── content/our-content/
    │   ├── content/competitors/
    │   ├── transcripts/
    │   └── outputs/
    │       ├── monthly-briefs/
    │       └── weekly-briefs/
    ├── operations/              (future - AI-COO)
    └── finance/                 (future - AI-CFO)
"""

import sys
import shutil
from pathlib import Path


def find_templates_dir():
    """Find the templates directory relative to this script."""
    script_dir = Path(__file__).resolve().parent
    # Templates are in assets/templates/ within the skill directory
    templates_dir = script_dir.parent / "assets" / "templates"
    if templates_dir.exists():
        return templates_dir
    return None


def init_client(client_name, base_path):
    """Create client folder structure and copy templates."""
    client_dir = Path(base_path).resolve() / client_name

    if client_dir.exists():
        print(f"Error: Client directory already exists: {client_dir}")
        return False

    templates_dir = find_templates_dir()

    # Create directory structure
    dirs = [
        # Shared
        ".claude",
        # Marketing (AI-CMO)
        "marketing/knowledge",
        "marketing/tracking",
        "marketing/content/our-content",
        "marketing/content/competitors",
        "marketing/transcripts",
        "marketing/outputs/monthly-briefs",
        "marketing/outputs/weekly-briefs",
        # Future roles (create empty dirs)
        "operations",
        "finance",
    ]

    for d in dirs:
        (client_dir / d).mkdir(parents=True, exist_ok=True)
        print(f"  Created {d}/")

    # Map template files to destinations
    template_map = {
        # Shared root files
        "company-overview.md": "company-overview.md",
        "contacts.md": "contacts.md",
        "CLIENT-CLAUDE.md": ".claude/CLAUDE.md",
        # Marketing knowledge files
        "voice-guidelines.md": "marketing/knowledge/voice-guidelines.md",
        "personas-storybrand.md": "marketing/knowledge/personas-storybrand.md",
        "goals-and-benchmarks.md": "marketing/knowledge/goals-and-benchmarks.md",
        "whats-working.md": "marketing/knowledge/whats-working.md",
        # Marketing tracking files
        "content-log.csv": "marketing/tracking/content-log.csv",
        "performance.csv": "marketing/tracking/performance.csv",
        "revenue-attribution.csv": "marketing/tracking/revenue-attribution.csv",
    }

    if templates_dir:
        for src_name, dest_path in template_map.items():
            src = templates_dir / src_name
            dest = client_dir / dest_path
            if src.exists():
                shutil.copy2(src, dest)
                print(f"  Copied {src_name} -> {dest_path}")
            else:
                print(f"  Warning: Template not found: {src_name}")
    else:
        print("  Warning: Templates directory not found. Creating empty files.")
        for dest_path in template_map.values():
            dest = client_dir / dest_path
            if dest_path.endswith(".csv"):
                if "content-log" in dest_path:
                    dest.write_text("content_id,date_published,platform,format,title_description,content_url,theme_topic,hook_used,cta_type,created_by,status,notes\n")
                elif "performance" in dest_path:
                    dest.write_text("content_id,date_measured,views,reach,likes,comments,shares,saves,link_clicks,follows,engagement_rate,performance_score,notes\n")
                elif "revenue" in dest_path:
                    dest.write_text("lead_id,lead_date,lead_name,lead_source,platform,content_id,first_touch,last_touch,lead_status,close_date,project_type,revenue,notes\n")
            else:
                dest.write_text(f"# {dest_path.split('/')[-1].replace('.md', '').replace('-', ' ').title()}\n\n[To be completed during onboarding]\n")

    # Replace placeholders in template files
    display_name = client_name.replace("-", " ").title()
    for dest_path in template_map.values():
        if dest_path.endswith(".md"):
            dest = client_dir / dest_path
            if dest.exists():
                content = dest.read_text()
                content = content.replace("[CLIENT NAME]", display_name.upper())
                content = content.replace("[Client Name]", display_name)
                content = content.replace("[client-name]", client_name)
                dest.write_text(content)

    print(f"\nClient '{client_name}' initialized at {client_dir}")
    print(f"\nFolder structure:")
    print(f"  {client_name}/")
    print(f"  ├── company-overview.md        (shared)")
    print(f"  ├── contacts.md                (shared)")
    print(f"  ├── .claude/CLAUDE.md          (shared)")
    print(f"  ├── marketing/                 (AI-CMO)")
    print(f"  │   ├── knowledge/  tracking/  content/  transcripts/  outputs/")
    print(f"  ├── operations/                (future)")
    print(f"  └── finance/                   (future)")
    print(f"\nNext: Run through the onboarding interview to populate knowledge files.")
    return True


def main():
    if len(sys.argv) < 4 or sys.argv[2] != "--path":
        print("Usage: init-client.py <client-name> --path <base-path>")
        print("\nExample:")
        print("  init-client.py acme-corp --path clients/")
        sys.exit(1)

    client_name = sys.argv[1]
    base_path = sys.argv[3]

    print(f"Initializing client: {client_name}")
    print(f"Location: {base_path}\n")

    if init_client(client_name, base_path):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

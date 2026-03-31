---
name: organize-shoot
description: Organize raw shoot day footage into content-piece folders using AI analysis
---

# Organize Shoot Day Footage

Process raw shoot day footage and organize it into content-piece folders using transcript analysis, visual frame matching, and bi-weekly brief context.

**Arguments:** The user may provide a path to the shoot folder and/or a client name (e.g., `/ai-cmo:organize-shoot /path/to/folder client-name`).

**Process:**
1. Parse arguments for shoot folder path and client name (ask if not provided)
2. Read the most recent bi-weekly brief from `outputs/biweekly-briefs/` for shot list and content piece context
3. Scan the input folder for video (MP4) and photo (CR3, JPG, RAF) files
4. Extract audio from all videos using ffmpeg (`-vn -acodec copy`)
5. Transcribe ALL videos using Whisper (tiny model) — including short B-roll where the shooter narrates what they're filming
6. Match footage to content pieces using transcripts + shot list cross-reference
7. Classify each video as A-Roll, B-Roll (described), B-Roll (silent), or Unmatched
8. Rename videos using naming convention:
   - A-Roll: `Post[N]-[Location]-[Description].MP4`
   - Content Bank: `CB-[Location]-[Description].MP4`
   - B-Roll: `BRoll-[Location]-[Description].MP4`
9. Create `file-mapping.txt` per location and `file-mapping.csv` master in shoot root
10. Present summary showing what was captured vs. shot list, flag missing shots
11. Update the bi-weekly brief with actual shoot results

**Technical requirements:** ffmpeg, ffprobe, whisper (Python package)

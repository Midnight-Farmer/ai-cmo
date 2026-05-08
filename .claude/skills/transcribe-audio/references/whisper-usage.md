# Whisper usage reference

Concrete commands, model selection, and gotchas for running Whisper from this skill.

---

## Environment

| Item | Path |
|------|------|
| Whisper CLI | `/Library/Frameworks/Python.framework/Versions/3.12/bin/whisper` |
| Python (with whisper installed) | `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3` |
| Model cache | `~/.cache/whisper/` |
| Already downloaded | `tiny.pt` (~75 MB), `medium.pt` (~1.5 GB) |

`base`, `small`, and `large` will download on first use (a few hundred MB to ~3 GB). If a download is undesirable, stick to `tiny` or `medium`.

---

## Model selection

| Model | Speed (rel.) | Quality | Use when |
|-------|--------------|---------|----------|
| `tiny` | ~1x | Decent on clear, single-speaker audio | Default. Quick voice memos, clean meeting recordings under ~30 min, shoot footage where the talent is mic'd. |
| `base` | ~2x slower than tiny | Slightly better than tiny | Rarely needed; pick `tiny` or jump to `medium`. |
| `small` | ~4x | Noticeably better | Multi-speaker meetings, mild background noise. |
| `medium` | ~8x | Significantly better | Long meetings (>30 min), noisy rooms, important content (blog source material, client interviews), multiple speakers, accents. |
| `large` | ~16x | Best | Reserved for edge cases. Don't use unless `medium` clearly missed words and re-running on a faster model isn't acceptable. |

**Auto-promotion heuristics** (decide before transcribing — saves a second pass):
- File length > 30 min → `medium`
- File is a meeting recording with multiple voices → `medium`
- File is a single-speaker memo or shoot clip recorded close to the mic → `tiny`
- User flagged it as "important" or "this is the source for a blog post" → `medium`
- User said "just give me the gist quickly" → `tiny`

To estimate length without playing the file:
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "<audio>"
```

---

## Running the bundled script

The skill ships `scripts/transcribe.py`. It prints the transcript to stdout (or to `--out`).

**One audio file, transcript to stdout:**
```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 \
  /Users/dawsonschrader/Obsidian/Tools/AI-CMO/.claude/skills/transcribe-audio/scripts/transcribe.py \
  "/path/to/audio.m4a" \
  --model tiny
```

**Write transcript next to the audio file (shoot-flow pattern):**
```bash
PY=/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
SCRIPT=/Users/dawsonschrader/Obsidian/Tools/AI-CMO/.claude/skills/transcribe-audio/scripts/transcribe.py
AUDIO="/path/to/Audio/clip.m4a"
OUT="${AUDIO%.*}.txt"
"$PY" "$SCRIPT" "$AUDIO" --model tiny --out "$OUT"
```

**Force English (small speedup, avoids language-detect drift):**
```bash
"$PY" "$SCRIPT" "$AUDIO" --model medium --language en --out "$OUT"
```

---

## Running in the background

Long files (>10 min) and batch jobs should run in the background so the conversation isn't blocked.

In Claude Code, use the `Bash` tool with `run_in_background: true`. Otherwise:

```bash
nohup "$PY" "$SCRIPT" "$AUDIO" --model medium --out "$OUT" \
  > "${OUT%.txt}.log" 2>&1 &
echo "PID=$!"
```

For a folder of files, prefer a small for-loop wrapped in `nohup`:
```bash
LOGDIR=/tmp/whisper-batch
mkdir -p "$LOGDIR"
nohup bash -c '
  for f in /path/to/Audio/*.m4a; do
    out="${f%.*}.txt"
    [ -s "$out" ] && { echo "skip $f (already has $out)"; continue; }
    "'$PY'" "'$SCRIPT'" "$f" --model tiny --out "$out"
  done
' > "$LOGDIR/batch.log" 2>&1 &
```

When the background process completes, the harness notifies you. Check the log file for the per-file summary.

---

## Skip-already-transcribed rule

For shoot-flow batches, an `.m4a` is considered already done when a sibling `.txt` exists with the same basename **and is non-empty**:

```bash
[ -s "${audio%.*}.txt" ] && skip
```

Use `-s` (size > 0), not just `-f`, so a stray empty `.txt` doesn't block re-transcription.

---

## Gotchas

**`m4a` needs ffmpeg.** Whisper shells out to `ffmpeg` to decode non-WAV audio. If `ffmpeg` isn't on `PATH`, transcription fails with a confusing error. Verify:
```bash
which ffmpeg && ffmpeg -version | head -1
```
If missing: `brew install ffmpeg`.

**HEIC and other image formats are NOT audio.** Whisper will reject them. Only feed `.m4a`, `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.webm`, `.mp4`/`.mov` (the audio track will be extracted).

**Video containers work** — for `.mov` or `.mp4`, Whisper extracts the audio stream automatically via ffmpeg. No need to pre-extract.

**First run on a new model downloads it.** If `~/.cache/whisper/<model>.pt` doesn't exist, the first call blocks on a download. Warn the user before triggering this.

**MPS (Apple Silicon GPU) is finicky.** Whisper's MPS support has rough edges in some PyTorch versions. If a run errors out with MPS-related messages, fall back to CPU:
```bash
PYTORCH_ENABLE_MPS_FALLBACK=1 "$PY" "$SCRIPT" ...
```

**Long files use a lot of RAM with `medium`/`large`.** ~5 GB RAM for `medium`, more for `large`. If the user is on a smaller Mac, prefer `small`.

**Output ends in a newline.** The script adds a trailing `\n`. When concatenating multiple transcripts into one note, don't double up newlines.

**Empty transcripts mean silent audio or a decode failure.** If `text` comes back empty, Whisper printed a warning to stderr — read the captured log before reporting success.

---

## Quick verification commands

After a batch run, confirm what was produced:
```bash
ls -la /path/to/Audio/*.txt | head
wc -l /path/to/Audio/*.txt
```

To re-transcribe a single file (e.g. user said "do that one again with medium"):
1. Rename or remove the existing `.txt` (don't silently overwrite).
2. Re-run with the new model.

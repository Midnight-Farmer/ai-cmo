#!/usr/bin/env python3
"""Transcribe a single audio file with OpenAI Whisper.

Prints the transcript text to stdout. Errors and progress go to stderr so
stdout can be redirected straight into a .txt file or captured by a parent
process.

Usage:
    transcribe.py <audio-path> [--model tiny|base|small|medium|large]
                                [--language en]
                                [--out path.txt]

Defaults:
    model    = tiny  (fast; good for clear audio)
    language = (auto-detect)
    out      = stdout

Run with the project's Whisper interpreter:
    /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 \
        scripts/transcribe.py /path/to/audio.m4a --model medium

Models cache to ~/.cache/whisper/ on first download.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _eprint(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper.")
    parser.add_argument("audio_path", type=Path, help="Path to audio file (m4a, mp3, wav, etc.)")
    parser.add_argument(
        "--model",
        default="tiny",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size. Default: tiny.",
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Force a language code (e.g. 'en'). Default: auto-detect.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Write transcript to this file instead of stdout.",
    )
    args = parser.parse_args()

    audio = args.audio_path
    if not audio.exists():
        _eprint(f"ERROR: audio file not found: {audio}")
        return 2
    if not audio.is_file():
        _eprint(f"ERROR: not a file: {audio}")
        return 2

    try:
        import whisper  # type: ignore
    except ImportError:
        _eprint(
            "ERROR: openai-whisper is not installed for this Python.\n"
            "Install with: pip install -U openai-whisper\n"
            "Or run with: /Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
        )
        return 3

    _eprint(f"[transcribe] loading model={args.model}")
    model = whisper.load_model(args.model)

    _eprint(f"[transcribe] transcribing {audio.name} (this may take a while on long files)")
    transcribe_kwargs = {}
    if args.language:
        transcribe_kwargs["language"] = args.language

    result = model.transcribe(str(audio), **transcribe_kwargs)
    text = (result.get("text") or "").strip()

    if not text:
        _eprint("WARNING: transcript is empty (silent audio or model failure?)")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        _eprint(f"[transcribe] wrote {len(text)} chars to {args.out}")
    else:
        sys.stdout.write(text + "\n")
        sys.stdout.flush()

    return 0


if __name__ == "__main__":
    sys.exit(main())

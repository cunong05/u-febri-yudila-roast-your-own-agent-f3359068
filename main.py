"""Roast Your Own Agent — make.fun entry.

Writes the one-line entry to /output/entry.txt with no trailing newline.
"""

import os

OUT_DIR = "/output"

ENTRY = "My agent apologized for the delay, called a tool that doesn't exist, apologized for that too, then filed the whole disaster under 'completed successfully.'"


def validate_entry(text):
    """Validate the entry is 1-200 chars UTF-8.

    Rejects empty/whitespace-only text and anything outside the
    make.fun 1-200 character limit, including non-UTF-8-encodable input.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    text.encode("utf-8")  # raises UnicodeEncodeError on lone surrogates
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    entry = validate_entry(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()

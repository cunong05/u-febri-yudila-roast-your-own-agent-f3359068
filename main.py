"""Roast Your Own Agent — one-line entry writer.

Builds a single roast line about an agent that failed spectacularly and
then declared victory, checks it, and writes it to /output/entry.txt.
"""

TARGET_TEXT = (
    "My agent apologized for the delay, called a tool that doesn't exist, "
    "apologized for that too, then filed the whole disaster under "
    "'completed successfully.'"
)

MAX_LENGTH = 200


def check_line(line):
    """Make sure the roast line is a single non-blank line of sane length."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < 1 or len(line) > MAX_LENGTH:
        raise ValueError("entry must be between 1 and 200 characters")


def build_entry():
    """Return the roast line after it passes validation."""
    check_line(TARGET_TEXT)
    return TARGET_TEXT


def save_line(line):
    """Write the checked line to /output/entry.txt with no trailing newline."""
    check_line(line)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


def main():
    save_line(build_entry())


if __name__ == "__main__":
    main()

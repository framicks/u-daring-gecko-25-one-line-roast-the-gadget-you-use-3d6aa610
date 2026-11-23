"""One-line roast entry for the make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes the roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, stdlib only, no network.
"""

import os

ROAST = (
    "My wireless earbuds have a dramatic breakup every call: "
    "one drops out, the other pretends it never happened, "
    "then both die at once."
)


def main():
    text = ROAST
    assert 1 <= len(text) <= 200, "roast must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "roast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

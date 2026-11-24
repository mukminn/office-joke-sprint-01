#!/usr/bin/env python3
"""One-Line Office Joke entry: writes the joke in joke.txt to the output.

The judge sees exactly the bytes of /output/entry.txt, so the program
copies the joke file unchanged, byte for byte, on every run.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def joke_bytes():
    """The exact bytes the judge will see, read from joke.txt.

    The gate allows 1-200 characters; fail loudly rather than write
    an out-of-range file if joke.txt is ever edited past the limit.
    """
    with open(os.path.join(HERE, "joke.txt"), "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke is {len(text)} chars, must be 1-200")
    return data


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as f:
        f.write(joke_bytes())


if __name__ == "__main__":
    main()

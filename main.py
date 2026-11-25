"""Write the office joke as the competition's sole output artifact."""

import os
from pathlib import Path


JOKE = "My boss held a minute's silence for our laid-off coworkers, then asked who'd be covering that minute."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()

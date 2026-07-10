"""pre-commit helper."""

# ruff: noqa: I001

from pathlib import Path
import sys


def fix_file(path: Path) -> None:
    data = path.read_text(encoding="utf-8")
    if not data:
        return

    updated = data.rstrip("\n") + "\n"
    if updated != data:
        path.write_text(updated, encoding="utf-8")


def main() -> int:
    for raw_path in sys.argv[1:]:
        fix_file(Path(raw_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

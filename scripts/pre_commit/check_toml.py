"""pre-commit helper."""

# ruff: noqa: I001

from pathlib import Path
import sys
import tomllib


def check_file(path: Path) -> None:
    with path.open("rb") as stream:
        tomllib.load(stream)


def main() -> int:
    for raw_path in sys.argv[1:]:
        check_file(Path(raw_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

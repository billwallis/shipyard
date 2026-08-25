from __future__ import annotations

import argparse
import datetime
import pathlib
from collections.abc import Sequence

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[0;36m"
GREY = "\033[38;5;240m"
BOLD = "\033[1m"
RESET = "\033[0m"

HERE = pathlib.Path(__file__).parent
assert HERE.name == "tools", f"{HERE.name!r} != 'tools'"  # noqa: S101
ROOT = HERE.parent
DOCS_ARCHIVED = ROOT / "docs/archived"
DOCS_UPCOMING = ROOT / "docs/upcoming"


def colour(text: str, colour_: str) -> str:
    return f"{colour_}{text}{RESET}"


def parse_date(text: str) -> datetime.date:
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        print(colour(f"error: {text!r} is not a valid ISO date", RED))
        raise


def archive_file(filename: str, date: datetime.date) -> None:
    print(filename, date)

    source = DOCS_UPCOMING / filename
    target = DOCS_ARCHIVED / f"{date.isoformat()}--{filename}"

    if not source.exists():
        raise FileNotFoundError(
            f"'{source.relative_to(ROOT)}' does not exist and cannot be archived"
        )
    if target.exists():
        raise FileExistsError(
            f"'{target.relative_to(ROOT)}' already exists, so '{source.relative_to(ROOT)}' cannot be archived"
        )

    print(f"Moving '{source}' to '{target}'")
    source.move(target)


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help=f"filenames relative to '{DOCS_UPCOMING.relative_to(ROOT)}/'",
    )
    parser.add_argument(
        "--date",
        required=False,
        type=parse_date,
        help="archive date to prefix the archived filename with",
    )
    args = parser.parse_args(argv)

    if not args.filenames:
        parser.print_help()
        return 0

    archive_date = datetime.date.today() if args.date is None else args.date
    for filename in args.filenames:
        try:
            archive_file(filename, archive_date)
        except (FileNotFoundError, FileExistsError) as err:
            print(colour(f"error: {err}", RED))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover

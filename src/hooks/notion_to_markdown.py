from __future__ import annotations

import argparse
from collections.abc import Sequence

SUCCESS = 0
FAILURE = 1
REPLACEMENTS = {
    "’": "'",  # noqa: RUF001
    "“": '"',
    "”": '"',
    "…": "...",
}


def _replace_all(text: str) -> str:
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    return text


def convert_notion_to_markdown(filename: str) -> int:
    """
    Convert Notion-style Markdown to "normal" Markdown.
    """

    # https://stackoverflow.com/a/15976014/8213085
    with open(filename, "r+") as f:
        content = f.readlines()
        f.seek(0)
        f.writelines(_replace_all(line) for line in content)
        f.truncate()

    return SUCCESS


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the hook.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    outcome = SUCCESS
    for filename in args.filenames:
        outcome |= convert_notion_to_markdown(filename)

    return outcome


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover

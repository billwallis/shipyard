

---

```json
[
  "Aaron",
  "Adam",
  "Adrian",
  "Alan",
  "Alex",
  "Alice",
  "Alison",
  "Amanda",
  "Amy",
  "Andrea",
  "Andrew",
  "Andy",
  "Angela",
  "Ann",
  "Anna",
  "Anne",
  "Anthony",
  "Ashley",
  "Barbara",
  "Barry",
  "Becky",
  "Ben",
  "Beth",
  "Billy",
  "Bob",
  "Brian",
  "Callum",
  "Carl",
  "Carol",
  "Caroline",
  "Catherine",
  "Charlie",
  "Charlotte",
  "Chloe",
  "Chris",
  "Christine",
  "Christopher",
  "Claire",
  "Clare",
  "Colin",
  "Connor",
  "Craig",
  "Dan",
  "Daniel",
  "Danielle",
  "Danny",
  "Darren",
  "Dave",
  "David",
  "Dawn",
  "Dean",
  "Debbie",
  "Denise",
  "Derek",
  "Diane",
  "Donna",
  "Elaine",
  "Elizabeth",
  "Ellie",
  "Emily",
  "Emma",
  "Fiona",
  "Gareth",
  "Gary",
  "Gemma",
  "George",
  "Georgia",
  "Graham",
  "Hannah",
  "Harry",
  "Hayley",
  "Heather",
  "Helen",
  "Holly",
  "Ian",
  "Jack",
  "Jackie",
  "Jade",
  "Jake",
  "James",
  "Jamie",
  "Jane",
  "Janet",
  "Jason",
  "Jay",
  "Jean",
  "Jennifer",
  "Jenny",
  "Jess",
  "Jessica",
  "Jim",
  "Jo",
  "Joanne",
  "Joe",
  "John",
  "Jon",
  "Jonathan",
  "Jordan",
  "Joseph",
  "Josh",
  "Joshua",
  "Julie",
  "Karen",
  "Kate",
  "Katie",
  "Keith",
  "Kelly",
  "Kerry",
  "Kevin",
  "Kieran",
  "Kim",
  "Kirsty",
  "Kyle",
  "Laura",
  "Lauren",
  "Leanne",
  "Lee",
  "Lesley",
  "Lewis",
  "Liam",
  "Linda",
  "Lisa",
  "Liz",
  "Lorraine",
  "Louise",
  "Lucy",
  "Luke",
  "Mandy",
  "Margaret",
  "Marie",
  "Mark",
  "Martin",
  "Mary",
  "Matt",
  "Matthew",
  "Megan",
  "Michael",
  "Michelle",
  "Mike",
  "Natalie",
  "Nathan",
  "Neil",
  "Nick",
  "Nicola",
  "Nicole",
  "Nigel",
  "Oliver",
  "Olivia",
  "Patricia",
  "Patrick",
  "Paul",
  "Paula",
  "Pauline",
  "Pete",
  "Peter",
  "Phil",
  "Philip",
  "Rachel",
  "Rebecca",
  "Richard",
  "Rob",
  "Robert",
  "Ross",
  "Ruth",
  "Ryan",
  "Sally",
  "Sam",
  "Samantha",
  "Sandra",
  "Sarah",
  "Scott",
  "Sean",
  "Shannon",
  "Sharon",
  "Shaun",
  "Simon",
  "Sophie",
  "Stacey",
  "Stephanie",
  "Stephen",
  "Steve",
  "Steven",
  "Stuart",
  "Sue",
  "Susan",
  "Terry",
  "Thomas",
  "Tim",
  "Tina",
  "Tom",
  "Tony",
  "Tracey",
  "Tracy",
  "Vicky",
  "Victoria",
  "Wayne",
  "Wendy",
  "Will",
  "William",
  "Zoe"
]
```

```python
# TODO: Link Anthony's explains video
from __future__ import annotations

import argparse
import enum
import functools
import json
import logging
import pathlib
import random
import shutil
import tempfile
import textwrap
import time
from collections.abc import Generator, Sequence

logger = logging.getLogger(__file__)
logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;240m%(asctime)s\033[0m  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

FAIL = True
FAIL_THRESHOLD = 10
RUN_DELAY_SECONDS = 0.5
SNIFF_DELAY_SECONDS = 1
HERE = pathlib.Path(__file__).parent
NAMES_JSON = HERE / "data/names.json"


class Method(enum.StrEnum):
    SIMPLE = "simple"
    ATOMIC = "atomic"

    @property
    def path(self) -> pathlib.Path:
        return {
            Method.SIMPLE: HERE / "simple.jsonl",
            Method.ATOMIC: HERE / "atomic.jsonl",
        }[self]


def get_name() -> str:
    @functools.cache
    def _names() -> list[str]:
        with open(NAMES_JSON) as f:
            return json.load(f)

    return random.choice(_names())


class DatabaseConnection:
    @staticmethod
    def fetchall() -> Generator[list]:
        for i in range(100):
            time.sleep(RUN_DELAY_SECONDS)
            name = get_name()
            logger.info(f"yielding row ID {i} with name {name}")
            yield [i, name]


def parse_row(row: list) -> str:
    return f"""{{"id": {row[0]}, "name": "{row[1]}"}}\n"""


def run_simple(conn: DatabaseConnection, target: pathlib.Path) -> None:
    with open(target, "w+") as f:
        for row in conn.fetchall():
            f.write(parse_row(row))
            f.flush()
            if FAIL and row[0] > FAIL_THRESHOLD:
                raise RuntimeError("oops!")


def run_atomic(conn: DatabaseConnection, target: pathlib.Path) -> None:
    with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete_on_close=False) as f:
        for row in conn.fetchall():
            f.write(parse_row(row))
            if FAIL and row[0] > FAIL_THRESHOLD:
                raise RuntimeError("oops!")

        f.flush()
        shutil.copyfile(f.name, target)


def sniff_file(filepath: pathlib.Path) -> None:
    if not filepath.exists():
        return

    print(filepath)
    print(textwrap.indent(filepath.read_text(encoding="utf-8"), prefix="    "))


def run(args: argparse.Namespace) -> int:
    for m in Method:
        m.path.unlink(missing_ok=True)

    connection = DatabaseConnection()
    runner = {
        Method.SIMPLE: run_simple,
        Method.ATOMIC: run_atomic,
    }[args.method]
    try:
        runner(connection, args.method.path)
    except RuntimeError as err:
        logger.error(f"error: {err}")
        return 1

    return 0


def sniff(args: argparse.Namespace) -> int:
    path = args.method.path
    try:
        while True:
            sniff_file(path)
            time.sleep(SNIFF_DELAY_SECONDS)
    except KeyboardInterrupt:
        print("")
        print(f"'{path}' exists={path.exists()}")
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    parser__run = subparsers.add_parser("run")
    parser__sniff = subparsers.add_parser("sniff")

    for p in (parser__run, parser__sniff):
        p.add_argument("method", type=Method, choices=[v for v in Method])
        p.add_argument("--fail", action=argparse.BooleanOptionalAction, default=True)

    args = parser.parse_args(argv)
    if args.command == "run":
        return run(args)
    if args.command == "sniff":
        return sniff(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
```

- [BW ~~5~~ 20 mins] What's a [dbt selector](https://docs.getdbt.com/reference/node-selection/yaml-selectors?version=2.0&name=Fusion)?
    - Why would you want this? feat. `--selector`
    - CLI-style
    - Key-value
    - Full YAML
    - A peek under the hood (`manifest.json`)
    - `--selector` vs `--select` (do they play nicely?)
    - How to validate selector selection

---

```python
# python -m shipyard
# python -m shipyard --json selectors | jq
from __future__ import annotations

import argparse
import json
import pathlib
from collections.abc import Sequence

HERE = pathlib.Path(__file__).parent
MANIFEST_PATH = HERE / "target/manifest.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store")
    args = parser.parse_args(argv)

    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)

    if args.json:
        print(json.dumps(manifest[args.json]))
    else:
        for key in manifest.keys():
            print(key)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

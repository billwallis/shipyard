- [BW 10 mins] Python: `assert` vs `raise`
    - `assert` can be ignored at runtime (`-O`, capital O)
    - `assert` statements can help type checkers
    - `assert` for "internal" checks (like tests!), `raise` for everything else
    - `assert` is used for "defensive programming"
        - https://www.youtube.com/watch?v=v1MtwCPTmBI
    - `assert_never` and `assert_type`
        - https://typing.python.org/en/latest/guides/unreachable.html#assert-never-and-exhaustiveness-checking
        - https://www.youtube.com/watch?v=jN_a02Rj8Gg&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=437

---

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pytest>=9.0.0",
#     "pytest-cov>=7.0.0",
# ]
# ///
#
# pytest <file> --cov --cov-report=term-missing

"""
Calculate distance, speed, and time:

    speed = distance / time
"""

from typing import assert_never

import pytest


# As far as users are concerned, this can only raise a `ValueError`. The
# `AssertionError` can never surface for users unless a dev makes an
# incorrect change to the code.
def calculate_dst(
    *,
    distance: float | None = None,
    speed: float | None = None,
    time: float | None = None,
) -> float:
    """
    Return distance, speed, or time by providing two parameters.
    """

    null_count = sum(int(x is None) for x in (distance, speed, time))
    if null_count != 1:
        raise ValueError("Specify exactly two of distance, speed, and time")

    if distance is None:
        assert speed is not None and time is not None
        return speed * time

    if speed is None:
        assert distance is not None and time is not None
        return distance / time

    if time is None:
        assert distance is not None and speed is not None
        return distance / speed

    assert_never()  # type: ignore  # pragma: no cover


@pytest.mark.parametrize(
    "distance, speed, time, expected",
    (
        (1., 2., None, 0.5),
        (1., None, 2., 0.5),
        (None, 1., 2., 2.),
    ),
)
def test__calculate_dst(
    distance: float | None,
    speed: float | None,
    time: float | None,
    expected: float | None,
):
    assert expected == calculate_dst(
        distance=distance,
        speed=speed,
        time=time,
    )


@pytest.mark.parametrize(
    "distance, speed, time",
    (
        (None, None, None),
        (1., None, None),
        (None, 2., None),
        (None, None, 3.),
        (1., 2., 3.),
    ),
)
def test__calculate_dst__raises(
    distance: float | None,
    speed: float | None,
    time: float | None,
):
    with pytest.raises(ValueError):
        calculate_dst(
            distance=distance,
            speed=speed,
            time=time,
        )
```

from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_and_last_number(string: str):
    numbers = re.findall("(one|two|three|four|five|six|seven|eight|nine|\d)", string)
    if numbers:
        first, last = numbers[0], numbers[-1]
        return int(first + last)


def compute(s: str) -> int:
    lines = s.splitlines()
    numbers = []
    for line in lines:
        number = find_first_and_last_number(string=line)
        numbers.append(number)
    return sum(numbers)


INPUT_S = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
EXPECTED = 142


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

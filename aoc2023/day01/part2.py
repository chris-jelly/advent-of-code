from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_and_last_number(string: str):
    numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", string)
    if numbers:
        try:
            first = int(numbers[0])
        except ValueError:
            first = word_to_int(numbers[0])
        try:
            last = int(numbers[-1])
        except ValueError:
            last = word_to_int(numbers[-1])
        return int(str(first) + str(last))


def word_to_int(word):
    return {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}.get(
        word, "Not a valid word"
    )


def compute(s: str) -> int:
    lines = s.splitlines()
    numbers = []
    for line in lines:
        number = find_first_and_last_number(string=line)
        numbers.append(number)
    return sum(numbers)


INPUT_S = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
EXPECTED = 281


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

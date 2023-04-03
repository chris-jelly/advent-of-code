from pathlib import Path
from tools import HasThreeVowels, ContainsDuplicates, ContainsBadStrings, ContainsAlternatingLetters, ContainsPairOfLetters
import re
import sys


def main():

  # redo path
  p = Path('/home/cjelly/git/advent-of-code/2015/day5/data/input.txt')
  with open(p, mode="r") as input:
    strings = [line.rstrip() for line in input]

  nice_strings = 0

  for string in strings:

    if ContainsBadStrings(string) == False:
      if ContainsDuplicates(string) == True:
        if HasThreeVowels(string) == True:
          nice_strings += 1

  print(f'Nice strings count: {nice_strings}')


if __name__ == "__main__":
  main()

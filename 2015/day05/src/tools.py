import re


def HasThreeVowels(input: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_count = 0
    for vowel in vowels:
      count = input.count(vowel)
      vowel_count += count

    if vowel_count >= 3:
      return True
    else:
      return False


def ContainsDuplicates(input: str):
    regex = re.compile(r'(\w)\1{1}')
    match = regex.search(input)
    if match:
      return True
    else:
      return False


def ContainsBadStrings(input: str):
    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for string in bad_strings:
      if string in input:
        return True
    return False


def ContainsPairOfLetters(input: str):
  # Need to dig into the match more, or alter the regex
  regex = re.compile(r'(?P<group>[a-zA-Z]{2})\w+((?P=group))')
  match = regex.search(input)
  if match:
    if len(match.groups()) == 2:
      return True
  else:
    return False


def ContainsRepeatLetters(input: str):
  regex = re.compile(r'([a-zA-Z])[a-zA-Z](\1)')
  match = regex.search(input)
  if match is None:
    return False
  else:
    return True


def ContainsAlternatingLetters(input: str):
  string = input

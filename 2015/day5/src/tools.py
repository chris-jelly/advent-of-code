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

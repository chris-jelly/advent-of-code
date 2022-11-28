from pathlib import Path


def main():

  # redo path
  p = Path('/home/cjelly/git/advent-of-code/2015/day5/data/input.txt')
  with open(p, mode="r") as input:
      strings = [line.rstrip() for line in input]

  def IsNice(word: str):
    has_pair = False
    has_sandwich_pair = False

    for i in range(0, len(word) - 2):
      if word.count(word[i:i + 2]) >= 2:
        has_pair = True
      if word[i] == word[i + 2]:
        has_sandwich_pair = True

    return has_pair and has_sandwich_pair

  nice_count = 0
  for word in strings:
    if IsNice(word):
      nice_count += 1

  print(nice_count)


if __name__ == "__main__":
  main()

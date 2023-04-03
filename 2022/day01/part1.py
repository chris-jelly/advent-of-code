from pathlib import Path

INPUT = Path.joinpath(Path.cwd(), 'input.txt')

with open(INPUT, mode='r') as f:
  s = f.read()
  s = s.strip().split("\n\n")

  data = [[int(y) for y in x.split("\n")] for x in s]

Total = []
for elf in data:
  count = 0
  for food in elf:
    count += food
  Total.append(count)

Total = sorted(Total)
print(sum(Total[-3:]))

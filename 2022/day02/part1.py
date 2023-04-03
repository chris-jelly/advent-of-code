from pathlib import Path

INPUT = Path.joinpath(Path.cwd(), 'input.txt')

with open(INPUT, mode='r') as f:
  data = f.read()
  data = data.split('\n')
  games = [(x, y) for x, y in (s.split(' ') for s in data)]
  # data = [(x, y) for.split(' ') in ]


mapping = {"A": "rock", "Y": "paper", "Z": "scissors"}
points = 0

for game in games:
  status = None

  # Rock
  if game[1] == "X":
    points += 1
    if game[0] == "C":
      status = 'win'
    elif game[0] == "A":
      status = 'draw'

  # Paper
  elif game[1] == "Y":
    points += 2
    if game[0] == "A":
      status = 'win'
    elif game[0] == "B":
      status = 'draw'

  # Scissors
  elif game[1] == "Z":
    points += 3
    if game[0] == "B":
      status = 'win'
    elif game[0] == "C":
      status = 'draw'
  else:
    status = 'lose'

  if status == 'win':
    points += 6
  elif status == 'draw':
    points += 3


print(points)

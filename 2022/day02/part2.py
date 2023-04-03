from pathlib import Path

INPUT = Path.joinpath(Path.cwd(), 'input.txt')

with open(INPUT, mode='r') as f:
  data = f.read()
  data = data.split('\n')
  games = [(x, y) for x, y in (s.split(' ') for s in data)]
  # data = [(x, y) for.split(' ') in ]


result_mapping = {"X": "lose", "Y": "draw", "Z": "win"}
play_mapping = {"A": "rock", "B": "paper", "C": "scissors"}

points = 0

for game in games:
  status = None
  desired_result = play_mapping[game[1]]
  # Rock

  # we play paper
  if desired_result == 'lose':
    
  if desired_result == 'win':

  if desired_result == 'draw'
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

from pathlib import Path
import re
from typing import Tuple, List, Dict


def GetCoordinates(string):
  regex = re.compile(r'(\d+,\d+)\D*(\d+,\d+)')
  match = regex.search(string)
  coords = match.groups()
  start_coords = tuple([int(x) for x in coords[0].split(',')])
  end_coords = tuple([int(x) for x in coords[1].split(',')])

  return start_coords, end_coords


def GetCommandType(string):
  regex = re.compile(r'(\D*)')
  match = regex.match(string)
  command = str(match.group()).strip()
  return command


def TurnOn(coords: List, grid: Dict):
  for coord in coords:
      if grid[coord] == 'Off':
          grid.update({coord: 'On'})
  return grid


def TurnOff(coords: List, grid: Dict):
  for coord in coords:
      if grid[coord] == 'On':
        grid.update({coord: 'Off'})
  return grid


def Toggle(coords: List, grid: Dict):
  for coord in coords:
      if grid[coord] == 'On':
          grid.update({coord: 'Off'})
      else:
        if grid[coord] == 'Off':
           grid.update({coord: 'On'})
  return grid


def CoordsToAction(start: Tuple, end: Tuple):
  coords = [(x, y) for x in range(
      start[0], end[0] + 1) for y in range(start[1], end[1] + 1)]
  return coords


def CountLights(grid: Dict):
  # Need to count the total lights that are on
  light_count = 0
  for key in grid.keys():
    if grid[key] == "On":
      light_count += 1
  return light_count


p = Path('/home/cjelly/git/advent-of-code/2015/day6/data/input.txt')
with open(p, mode="r") as input:
    strings = [line.rstrip() for line in input]

grid_of_lights = {(x, y): 'Off' for x in range(1000) for y in range(1000)}

for string in strings:
  start, end = GetCoordinates(string)
  coords = CoordsToAction(start, end)
  command = GetCommandType(string)

  if command == 'turn off':
    grid_of_lights = TurnOff(coords, grid_of_lights)
  if command == 'turn on':
    grid_of_lights = TurnOn(coords, grid_of_lights)
  if command == 'toggle':
    grid_of_lights = Toggle(coords, grid_of_lights)

count = CountLights(grid_of_lights)

print(f'There are {count} lights on')
# Need to grab the action from the string - perhaps add a capture group to the regex?

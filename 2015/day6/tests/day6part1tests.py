from day6_part1 import GetCoordinates, GetCommandType, TurnOn, TurnOff, Toggle, CountLights


def test_TurnOn():
  start = (0, 0)
  end = (5, 5)
  grid_of_lights = {(x, y): 'Off' for x in range(5) for y in range(5)}
  TurnOn(start, end, grid_of_lights)
  assert CountLights(grid_of_lights) == 25


def test_TurnOff():
  start = (499, 499)
  end = (500, 500)
  grid_of_lights = {(x, y): 'Off' for x in range(1000) for y in range(1000)}
  TurnOff(start, end, grid_of_lights)
  assert CountLights(grid_of_lights) == 0


def test_Toggle():
  start = (0, 0)
  end = (999, 0)
  grid_of_lights = {(x, y): 'On' for x in range(1000) for y in range(1000)}
  Toggle(start, end, grid_of_lights)
  assert CountLights(grid_of_lights) == 999000

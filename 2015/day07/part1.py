
from pathlib import Path

INPUT = Path.joinpath(Path.cwd(), 'input.txt')

with open(INPUT, mode="r") as f:
    command_sets = [line.rstrip() for line in f]


data = ({0: {'name': 'a', 'input_wire': None,
        'input_values': list, 'output_wires': list}})

data = {}

for line in command_sets:
    cmd, key = line.split(' -> ')
    data[key.strip()] = cmd


mapping = {
    "AND": "",
    "OR": "",
    "NOT": "",

}

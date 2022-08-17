import pytest
from pathlib import Path

#Variables

p = Path(__file__).with_name('input.txt')
with p.open('r') as file:
    data = [line.rstrip() for line in file]




for present in data:
    length, width, height = present.split('x')


    area = ((2*length*width) + (2*width*height) + (2*height*length))

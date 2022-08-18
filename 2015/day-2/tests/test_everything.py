import pytest
from day2 import *
## Todo - finish test_smallest -- asset that it takes the list 2, 3, 4 and returns 2, 3


def test_area():
    assert calculate_area(2, 3, 4) == 58


def test_smallest():
    lst = [2, 3, 4]
    smallest, second_smallest = find_two_smallest(lst)
    assert smallest == 2
    assert second_smallest == 3


def test_cubic_volume():
    length = 2
    width = 3
    height = 4
    volume = calculate_cubic_volume(length, width, height)
    assert volume == 24


def test_calculate_perimeter():
    smallest = 2
    second_smallest = 3
    perimeter = calculate_perimeter(smallest, second_smallest)
    assert perimeter == 10


def test_calculate_total_ribbon():
    volume = 24
    perimeter = 10
    order_total = calculate_total_ribbon(volume, perimeter)
    assert order_total == 34

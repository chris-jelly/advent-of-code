from pathlib import Path


# Variables
total_area = 0
area = 0
order_total = 0

p = Path(__file__).with_name('input.txt')
with p.open('r') as file:
    data = [line.rstrip() for line in file]


def calculate_area(length, width, height):
    area_lw = (length*width)
    area_wh = (width*height)
    area_hl = (height*length)

    smallest_area = min(area_lw, area_wh, area_hl)

    area = 2*area_lw + 2*area_wh + 2*area_hl + smallest_area

    return area


def find_two_smallest(lst):
    temp_lst = list(lst)
    smallest = min(temp_lst)
    temp_lst.remove(smallest)
    second_smallest = min(temp_lst)
    return (smallest, second_smallest)


def calculate_perimeter(smallest, second_smallest):
    perimeter = smallest * 2 + second_smallest * 2
    return perimeter


def calculate_cubic_volume(length, width, height):
    volume = length*width*height
    return volume


def calculate_total_ribbon(volume, perimeter):
    total_ribbon = volume + perimeter
    return total_ribbon


for present in data:
    length, width, height = present.split('x')

    length = int(length)
    width = int(width)
    height = int(height)

    lst = [length, width, height]

    smallest, second_smallest = find_two_smallest(lst)

    area = calculate_area(length, width, height)
    volume = calculate_cubic_volume(length, width, height)
    perimeter = calculate_perimeter(smallest, second_smallest)
    order_total += calculate_total_ribbon(volume, perimeter)

    total_area += area


print(f'total area is {total_area}')
print(f'the elves will need to order {order_total} feet of ribbon')

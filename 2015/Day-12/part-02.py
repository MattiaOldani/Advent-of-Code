# Solution: 87842

import json


def sum_dict(data: dict):
    count = 0
    for el in data.items():
        key = el[0]
        value = el[1]
        if isinstance(key, int):
            count += key
        elif key == "red":
            return 0
        if isinstance(value, dict):
            count += sum_dict(value)
        elif isinstance(value, list):
            count += sum_list(value)
        elif isinstance(value, int):
            count += value
        elif value == "red":
            return 0
    return count


def sum_list(data):
    count = 0
    for el in data:
        if isinstance(el, dict):
            count += sum_dict(el)
        elif isinstance(el, list):
            count += sum_list(el)
        elif isinstance(el, int):
            count += el
    return count


with open("input.txt", "r") as f:
    data = json.load(f)

if isinstance(data, dict):
    count = sum_dict(data)
elif isinstance(data, list):
    count = sum_list(data)
elif isinstance(data, int):
    count = data

print(count)

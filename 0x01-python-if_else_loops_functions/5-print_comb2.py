#!/usr/bin/python3
number = range(0, 100)
new_numbers = [f"{num:02d}" for num in number]
output = ", ".join(new_numbers)

print(output)

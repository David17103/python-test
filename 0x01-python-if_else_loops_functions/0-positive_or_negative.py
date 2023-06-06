#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number1 = random.randint(1, 10)
number2 = random.randint(-1, -10)
if number > 0:
    print(number1)
elif number == 0:
    print(0)
else:
    print(number2)

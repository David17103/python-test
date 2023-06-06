#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number1 = random.randint(1, 10)
number2 = random.randint(-10, -1)
if number > 0:
    print(number1 "is positive")
elif number == 0:
    print("is zero")
else:
    print(number2 "is negative")

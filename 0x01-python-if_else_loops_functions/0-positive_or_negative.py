#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number1 = random.randint(1, 10)
number2 = random.randint(-10, -1)
number3 = 0

if number > 0:
    print(number1, "is positive" end=" ")
elif number == 0:
    print(number3, "is zero")
else:
    print(number2, "is negative")

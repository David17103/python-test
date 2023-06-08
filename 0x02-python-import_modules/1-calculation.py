#!/usr/bin/python3
import calculator_1

if __name__ == '__main__':
    
    a = 10
    b = 5

    def add(a, b) = a + b
    def sub(a, b) = a - b
    def mul(a, b) = a * b
    def div(a, b) = a / b

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

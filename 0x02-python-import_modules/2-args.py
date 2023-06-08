#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    list_argv = len(argv)

    print("{} argument{}:".format(list_argv, "s" if list_argv !=1 else "") end="")
    print('.' if list_argv == 0 else '')

    for i, arg in enumerate(argv, start=1):
        print("{} {}".format(i, arg))

"""
Name: Kristen Finley
Date: 23Jan2023
Course: 44-608 Data Analytics Fundamentals
Module: 2
Project: 2
Task: 7) Optional (Bonus)


>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3

>>> convert_ctof(0)
32.0

>>> convert_ctof(100)
212.0
"""

import doctest


def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum += value
    return sum


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += x
    return sum


def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():
        sum += value
    return sum


def convert_ctof(temp_C):
    """Return temperature in degrees Celsius to temperature in degrees Fahrenheit"""
    temp_F = temp_C * (9 / 5) + 32
    return round(temp_F, 1)


if __name__ == "__main__":

    print("===========================================================")
    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
    print()
    print("===========================================================")
    print("If you don't see any results, all tests passed.")
    print("===========================================================")
    print("Run with the -v flag to show results regardless.")
    print("Hit up arrow (to get last command) and add space -v")
    print("===========================================================")
    print()
    print("Read error messages carefully.")
    print("Errors tell which line number has the error")
    print("and what the issue is. Scroll up in the terminal to see.")
    print("Fix issues one at a time until you get the behavior")
    print("Described in the docstring.")

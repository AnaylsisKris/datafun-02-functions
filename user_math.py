"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 18Jan2023
Domain: Baseball
Project: 2
Task: 3


Uses built-in functions and functions from the math module.

Calls functions and display useful results to the user.


"""

import math

# define some functions
print()


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?
    I am not sure if this block is used to determine what will make the code fail or what logically cannot be true;
    i.e. If length or width = 0 python will still return an area, however you cannot have a one-dimensional area.

    """
    area = length * width
    return area

    try:
        area = length * width
        length = 0
        width = 0
        return area
    except Exception as ex:
        print(f"Please enter length and width greater than 0.")
        return None


print("Task 3 Questions")
print("     4.	How many arguments does get_area_of_lot() take? 2")
print(
    "     5.	What does it return? I've assigned it to return area that I determined is length * width"
)
print()
print("=============================================================")
print()

# Define dunder name
if __name__ == "__main__":

    print(
        "1.Use the defensive math examples to call the permutations and combinations as shown."
    )
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(
        "2.Then, call the method you just fixed with several different arguments and display them for the user."
    )
    print()
    print(
        "     The custom function, get_area_of_lot(3,2), returns", get_area_of_lot(3, 5)
    )
    print(
        "     The custom function, get_area_of_lot(10,2), returns",
        get_area_of_lot(10, 2),
    )
    print(
        "     The custom function, get_area_of_lot(8,7), returns", get_area_of_lot(8, 7)
    )
    print()
    print(" How many arguments are needed? 2")
    print(" Call get_area_of_lot(6, 2) and display the result.")
    print(
        "     The custom function, get_area_of_lot(6,2), returns",
        get_area_of_lot(6, 2),
        ".",
    )
    print()
    print()
print("3. Can you write and call custom functions with examples? see below")
print(
    "4. Add three more simple functions that might be useful to your domain. see below"
)
print("=============================================================")
# the following functions are used for my domain.
print()
print()
print(
    "A common way to calculate Pythagorean Winning Percentage (W%) for pitchers is using the formula"
)
print("W%=[(Runs Scored)^1.81]/[(Runs Scored)^1.81 + (Runs Allowed)^1.81] x 100")


def R_A(runs_scored, runs_allowed):
    num = math.pow(runs_scored, 1.81)
    den = math.pow(runs_scored, 1.8) + math.pow(runs_allowed, 1.8)
    win_per = num / den * 100
    runs_scored = 81
    runs_allowed = 74
    return win_per


print("Miles Mikolas had 81 runs scored and 74 runs allowed in 2022.")
print(f"         per this equation, his W% was {R_A(81,74):.1f}.")
print()


def w_l(w, l):
    perw_l = w / (w + l) * 100
    return perw_l


print("Another useful statistic for pitchers is Win-Loss Percentages.")
print("Mile Mikolas won 12 and lost 13 of the games he pitched in 2022")
print("That gave him a W-L% of", round(w_l(12, 13), 1))
print()
print(
    "The percent difference of the two pitching statitics is",
    (round(R_A(81, 74) - w_l(12, 13)) / 100),
    "%",
)
print()
print()

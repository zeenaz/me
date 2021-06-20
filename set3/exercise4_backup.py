# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math

# import time


def new_low(low, mid, actual_number):
    """ it will looks like this
    low         actual_number             high
    |------------|-------------------------|
    <----- a  ---><-------- x - a --------->    x - a > a
    <---------- a  --------><--- x - a ---->    a > x - a
    |----------------- x ------------------|

    when  x - a > a ==> x > 2a -- start from low / left
    when  x - a < a ==> x < 2a --- start from high / right
    a = actual_number
    x = high - low
    x/2 = mid
    """
    a = actual_number

    if (a < mid):
        return low  # start form the left low < a < 2/x
    else:
        return mid  # 2 start form the mid 2/x > a > high


def get_mid(low, high):
    length = high - low
    mid = int(length / 2)
    return mid


def moveSide(low, high, mid, actual_number):
    if (low < actual_number < mid):  # move to left
        high = mid

    elif (mid < actual_number < high):  # move to right
        low = mid

    else:  # actual_number == mid
        print(f"the mid number {mid} is the actual_number {actual_number}")
        print("you got it")
        return

    newmid = get_mid(low, high)
    return newmid


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    mid = get_mid(low, high)

    while (mid != actual_number):
        tries = tries + 1
        left = new_low(low, mid, actual_number)
        if (left == low):
            high = mid
            mid = get_mid(low, high)
            return
        elif(left == mid):
            low = mid
            mid = get_mid(low, high)
            return
        return
    guess = mid

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

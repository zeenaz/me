"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def not_number_rejector(message):
    # print(f"running number tester for input {message}")

    if message is not None:
        # print(f"we got input as {message}")

        if type(message) is not int:
            print("invalid input, give a new one")
            return
        else:
            # print(f"finally we ge {message}")
            return message
    else:
        print("None input, give a new one")
        message = input()
        return


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the advanced guessing game!")
    print("A number between __ and __ ?")

    getmessage = input()

    lowerBound = not_number_rejector(getmessage)
    while lowerBound is None:
        getmessage = input()
        lowerBound = not_number_rejector(getmessage)

    getmessage = input()
    upperBound = not_number_rejector(getmessage)
    # print(f"your lowerBound is {lowerBound}")
    # print(f"your upperBound is {upperBound}")

    # mid_num = (upperBound - lowerBound) / 2

    # print(f"OK then, a number between {lowerBound} and {mid_num} ?".format(upperBound))
    # upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    while not guessed:
        message = input("Guess a number: ")
        valid_input = not_number_rejector(message)
        if valid_input is not None:
            guessedNumber = int(message)
            print(
                "You guessed {},".format(guessedNumber),
            )
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

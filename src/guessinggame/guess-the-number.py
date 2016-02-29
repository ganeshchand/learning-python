doc = """ This is a simple number guessing game written in Python"""

import random


def main():
    user = raw_input("Enter your Name: ")
    print("Welcome {} to the number guessing game!".format(user))
    # randomNumber = 45 static number
    # generate dynamic random number

    randomNumber = random.randint(1, 100)
    found = False
    numberOfAttempt = 0
    while not found:
        numberOfAttempt += 1
        userGuess = input("Enter your guess here: ")
        if userGuess == randomNumber:
            print("You got it!")
            found = True
        else:
            print("That's not it.")
            if userGuess > randomNumber:
                print("Try a Lower Number")
            else:
                print("Try a Higher Number")
    print("Number of Attempts: {}".format(numberOfAttempt))


if __name__ == '__main__':
    main()

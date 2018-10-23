# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or
# exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
contGame = True
rand = random.randint(1, 10)
guess = 0
while contGame:
    guess = int(input("Guess a number(between 1-9) "))
    if guess > rand:
        print("too high")
        guess += 1
    elif guess< rand:
        print("too low")
        guess += 1
    elif guess == rand:
        print("exacly right, In Guesses {}".format(guess))
        if str(input("type exit for quiting or type no: ")) == 'exit':
            guess = 0
            contGame = False
        else:
            rand = random.randint(1, 10)
            guess = 0
    else:
        print("enter correct number it should be between(1-9) ")
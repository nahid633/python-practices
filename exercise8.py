# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

repeatGame = True
while(repeatGame):
    playerOne = input("PlayerOne: choose one (R for ROCK, S for Scissors, P for Paper) ")
    playerTwo = input("PlayerTwO: choose one (R for ROCK, S for Scissors, P for Paper) ")

    if playerOne == playerTwo:
        print("Draw")
    elif playerOne == 'R' and playerTwo == 'S' :
        print("Winner is playerOne")
    elif playerOne == 'S' and playerTwo == 'P':
        print("Winner is playerOne")
    elif playerOne == 'P' and playerTwo == 'R':
        print("Winner is playerOne")
    elif playerOne == 'S' and playerTwo == 'R':
        print("Winner is playerTwo")
    elif playerOne == 'P' and playerTwo == 'S':
        print("Winner is playerTwo")
    elif playerOne == 'R' and playerTwo == 'P':
        print("Winner is playerTwo")
    else:
        print("Invalid input! You have not entered R, P or S, try again.")
    q = input("wanna continue?(Yes or No) ")
    if q == 'No':
        repeatGame = False

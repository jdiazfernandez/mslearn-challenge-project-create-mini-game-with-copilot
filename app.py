import random


new_round = True
# The game should begin with a welcome message to the player.
while new_round:
    print('welcome to rock paper scissors')

    # The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
    print('rock, paper, or scissors?')
    user_choice = input()
    print('user choice: ' + user_choice)

    # The computer will also randomly select one of the three options and store it in a variable.

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('computer choice: ' + computer_choice)

    # The winner of the round is determined by the rules of the game:
    # Rock beats scissors
    # Scissors beats paper
    # Paper beats rock
    # If the player and computer both select the same option, the game ends in a tie.

    # The winner should be determined using a series of if, elif and else statements.
    # The program should also keep track of the number of wins, losses, and ties the player has. 
    computer_wins = 0
    user_wins = 0
    if user_choice == computer_choice:
        print('tie')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('computer wins')
            computer_wins += 1
        else:
            print('user wins')
            user_wins += 1
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('computer wins')
            computer_wins += 1
        else:
            print('user wins')
            user_wins += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('computer wins')
            computer_wins += 1
        else:
            print('user wins')
            user_wins += 1
    else:
        print('invalid choice');

    # By the end of each round, the player can choose whether to play again.
    # If the player declines, the program should print out the player's and print computer_wins and user_wins.
    # If the player agrees, the game should begin a new round and print computer_wins and user_wins.
    print('play again? (y/n)')
    play_again = input()
    if play_again == 'n':
        print('user wins: ' + str(user_wins))
        print('computer wins: ' + str(computer_wins))
        print('goodbye')
        print('STATS: Wins' + str(user_wins) + ' Losses' + str(computer_wins))
        new_round = False
    else:
        print('STATS: Wins' + str(user_wins) + ' Losses' + str(computer_wins))
        print('----------------------------')
        print('new round')



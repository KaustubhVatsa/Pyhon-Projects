# Winning rules 1. Rock vs Paper -> Paper wins
# Rock vs Scissor -> Rock wins
# Paper vs Scissor-> Scisor wins

import random

print("Winning rules\nRock vs Paper -> Paper wins \nRock vs Scissor -> Rock wins Paper vs Scissor-> Scisor wins")

choices = ["Rock", "Paper", "Scissor"]


def game_inputs():
    user_choice = input(
        "Enter your choice(Rock , Paper , Scissor, quit): -- ").capitalize().strip()
    computer_choice = random.choice(choices)
    return user_choice, computer_choice


def game_logic(user_choice, computer_choice, score_table):
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif user_choice == "Rock":
        if computer_choice == "Scissor":
            print("You Win! Rock crushes Scissor")
            score_table[0] += 1
        else:
            print("Computer Wins! Paper covers Rock")
            score_table[1] += 1

    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You Win! Paper covers Rock")
            score_table[0] += 1
        else:
            print("Computer Wins! Scissor cuts Paper")
            score_table[1] += 1

    elif user_choice == "Scissor":
        if computer_choice == "Paper":
            print("You Win! Scissor cuts Paper")
            score_table[0] += 1
        else:
            print("Computer Wins! Rock crushes Scissor")
            score_table[1] += 1
    else:
        print("Invalid input! Please choose Rock, Paper or Scissor.")
    print(
        f"\n\n----\tScore Table\t----\n\tYou :{score_table[0]}\tCom :{score_table[1]}")


def game():
    continue_game = True
    score_table = [0, 0]
    while continue_game:
        userchoice, computerchoice = game_inputs()
        if userchoice == "Quit":
            continue_game = False
            break
        game_logic(userchoice, computerchoice, score_table)


game()

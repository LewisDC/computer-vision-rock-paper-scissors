import random

def get_computer_choice():
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    return str(computer_action)

def get_user_choice():
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    return user_action

def get_winner(computer_choice, user_choice):
    valid_input = ("Rock","Paper", "Scissors")
    computer_choice = computer_choice.capitalize()
    user_choice = user_choice.capitalize()
    if user_choice in valid_input:
        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "Rock":
            if user_choice == "Scissors":
                print("You lost")
            else:
                print("You won!")
        elif computer_choice == "Scissors":
            if user_choice == "Paper":
                print("You lost")
            else:
                print("You won!")
        elif computer_choice == "Paper":
            if user_choice == "Rock":
                print("You lost")
            else:
                print("You won!")
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    else: print("Invalid input, please try again!")

def play():
    while True:
        try:
            user_choice = get_user_choice()
        except TypeError as e:
            print("Invalid input, please try again!")
            continue

        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

play()
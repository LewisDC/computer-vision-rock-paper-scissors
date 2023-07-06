import random

def get_computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action

def get_user_choice():
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    return user_action

def get_winner(user_choice, computer_choice):
    valid_input = ("rock","paper", "scissors")
    if user_choice in valid_input:
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "rock":
            if user_choice == "scissors":
                print("You lost")
            else:
                print("You win!")
        elif computer_choice == "scissors":
            if user_choice == "paper":
                print("You lost")
            else:
                print("You win!")
        elif computer_choice == "paper":
            if user_choice == "rock":
                print("You lost")
            else:
                print("You win!")
    else: print("Invalid input, please try again!")

def play():
    while True:
        try:
            user_choice = get_user_choice()
        except TypeError as e:
            print("Invalid input, please try again!")
            continue

        computer_choice = get_computer_choice()
        get_winner(user_choice, computer_choice)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

play()
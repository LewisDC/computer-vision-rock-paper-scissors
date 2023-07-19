import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

gesture_map = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    3: "Nothing"
}

user = "user"
computer = "computer"

computer_wins = 0
user_wins = 0

def mapper(val):
    return gesture_map[val]

def countdown():
    counter = 3
    print("Let's play rock paper scissors!")
    while counter > 0:
        print(f'{counter}')
        cv2.waitKey(1000)
        counter -= 1

def get_computer_choice():
    actions_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(actions_list)
    return computer_choice

def get_image():
    countdown()
    end_time = time.time() + 3
    while time.time() < end_time: 
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.5) - 1 # Normalize the image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return normalized_image

def get_prediction():
    data[0] = get_image()
    prediction = model.predict(data)
    index = np.argmax(prediction)
    user_prediction = mapper(index)
    return user_prediction

def get_user_choice():
    valid_input = ("Rock","Paper", "Scissors")
    while True:
        try:
            user_choice = get_prediction()
            if user_choice in valid_input:
                return user_choice
            else: print("Invalid input, please try again!")

        except TypeError as e:
            print("Invalid input, please try again!")
            continue

def get_winner(computer_choice, user_choice):
    
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Scissors":
            print("You lost")
            winner = "computer"
            return winner
        else:
            print("You won!")
            winner = "user"
            return winner
    elif computer_choice == "Scissors":
        if user_choice == "Paper":
            print("You lost")
            winner = "computer"
            return winner
        else:
            print("You won!")
            winner = "user"
            return winner
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
            winner = "computer"
            return winner
        else:
            print("You won!")
            winner = "user"
            return winner
        
def track_wins():
    computer_wins = 0
    user_wins = 0

    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)
        if winner == computer:
            computer_wins += 1
        elif winner == user:
            user_wins += 1
        
        print(f"You have won {user_wins} games and the computer has won {computer_wins} games")

        if computer_wins == 3:
            print("The computer wins the match!")
            print(f"{computer_wins} games to {user_wins}")
            break
        elif user_wins == 3: 
            print("You have won the match!")
            print(f"{user_wins} games to {computer_wins}")
            break

    print("Game Over")

track_wins()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
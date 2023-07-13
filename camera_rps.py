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
    end_time = time.time() + 1
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

def get_winner(computer_choice, user_choice):
    valid_input = ("Rock","Paper", "Scissors")
    if user_choice in valid_input:
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
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
    else: print("Invalid input, please try again!")

def play():
    while True:
        try:
            user_choice = get_prediction()
        except TypeError as e:
            print("Gesture not recognised, please try again!")
            continue

        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break



play()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
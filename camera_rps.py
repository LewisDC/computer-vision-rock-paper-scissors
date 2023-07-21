import cv2
from keras.models import load_model
import numpy as np
import random
import time

class RockPaperScissorsGame:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.gesture_map = {
            0: "Rock",
            1: "Paper",
            2: "Scissors",
            3: "Nothing"
        }
        self.user = "user"
        self.computer = "computer"
        self.computer_wins = 0
        self.user_wins = 0

    def mapper(self, val):
        return self.gesture_map[val]

    def countdown(self):
        counter = 3
        print("Let's play rock paper scissors!")
        while counter > 0:
            print(f'{counter}')
            cv2.waitKey(1000)
            counter -= 1

    def get_computer_choice(self):
        actions_list = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(actions_list)
        return computer_choice

    def get_image(self):
        self.countdown()
        end_time = time.time() + 3
        while time.time() < end_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.5) - 1 # Normalize the image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return normalized_image

    def get_prediction(self):
        self.data[0] = self.get_image()
        prediction = self.model.predict(self.data)
        index = np.argmax(prediction)
        user_prediction = self.mapper(index)
        return user_prediction

    def get_user_choice(self):
        valid_input = ("Rock", "Paper", "Scissors")
        while True:
            try:
                user_choice = self.get_prediction()
                if user_choice in valid_input:
                    return user_choice
                else:
                    print("Invalid input, please try again!")

            except TypeError as e:
                print("Invalid input, please try again!")
                continue

    def get_winner(self, computer_choice, user_choice):
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "Rock":
            if user_choice == "Scissors":
                print("You lost")
                winner = self.computer
                return winner
            else:
                print("You won!")
                winner = self.user
                return winner
        elif computer_choice == "Scissors":
            if user_choice == "Paper":
                print("You lost")
                winner = self.computer
                return winner
            else:
                print("You won!")
                winner = self.user
                return winner
        elif computer_choice == "Paper":
            if user_choice == "Rock":
                print("You lost")
                winner = self.computer
                return winner
            else:
                print("You won!")
                winner = self.user
                return winner

    def track_wins(self):
        self.computer_wins = 0
        self.user_wins = 0

        while True:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            winner = self.get_winner(computer_choice, user_choice)
            if winner == self.computer:
                self.computer_wins += 1
            elif winner == self.user:
                self.user_wins += 1
            
            print(f"You have won {self.user_wins} games and the computer has won {self.computer_wins} games")

            if self.computer_wins == 3:
                print("The computer wins the match!")
                print(f"{self.computer_wins} games to {self.user_wins}")
                break
            elif self.user_wins == 3: 
                print("You have won the match!")
                print(f"{self.user_wins} games to {self.computer_wins}")
                break

        print("Game Over")
        self.cap.release()
        cv2.destroyAllWindows()

    def __del__(self):
        # After the loop release the cap object and destroy all the windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.track_wins()

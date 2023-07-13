import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
class_names = open("labels.txt", "r").readlines()
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_computer_choice():
    actions_list = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(actions_list)
    return (computer_action)

def get_image():
    end_time = time.time() + 1
    while time.time() < end_time: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return normalized_image

def get_prediction():
    data[0] = get_image()
    prediction = model.predict(data)
    index = np.argmax(prediction)
    print(index)
    class_name = class_names[index]
    # confidence_score = prediction[0][index]
    return class_name

def get_user_choice():
    user_choice = get_prediction()
    return user_choice
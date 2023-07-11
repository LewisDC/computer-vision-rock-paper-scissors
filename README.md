# Computer Vision Rock Paper Scissors

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 1: Set up the environment

Set up GitHub repo using the button on AiCore project page. 

## Milestone 2

* Created an image project model with four different classes: Rock, Paper, Scissors and Nothing.
* Used Teachable-Machine to train each class with images of myself showing each option to the camera. At the time I had the curtains closed due to morning sun exposure so the background is quite dark, hopefully this does not cause interpretation issues when testing out the model.
* I used approx 1000 images for each class and tried to capture as many angles of possible of the correct hand gestures to increase probability of successful results.
* Downloaded the image model to my local machine.
* Push the model and label to GitHub repo.
* Began documenting my experience.

## Milestone 3

* Created a conda environment called the my_env and activated it, I had some issues getting conda to work. An update to 
* installed pip and the libraries opencv-python, tensorflow and ipykernel
* created a requirements.txt file by running 'pip list > requirements.txt'
* tested files, unsure if result is what is intended but it did open the webcam. After further exploration it seems the code is not working correctly for reasons I am unsure of, further investigation commencing.

## Milestone 4

* Created functions to store the users and computers choices called get_user_choice and get_computer_choice respectively. Where the user choice requests input and the computer choice is generated randomly from a list: Rock, Paper, Scissors.
* Created function to figure out who won called get_winner which prints out both the user and computer choices and then the result. Firstly it capitalizes the user choice to allow for lower case input of the valid user choices. It also generates an "Invalid input" message if the input does not meet this criteria.
* Created function to simulate the game using a while loop to try the code again if the user input is not valid.
* Ran tests and debugged, seems to work as expected but Task 2 validation is generating feedback that if there is a tie, the output is incorrect. After many minor adjustments and tweaks to the code and wording of the output statements I realised that where i had included a print out of each players choice before the result output, this was interferring with the task verification. I switched this to print after the result and can now move on.
* The next task verification to fail was due to my README file not having enough characters, updated README to include a more detailed account of my experiences.

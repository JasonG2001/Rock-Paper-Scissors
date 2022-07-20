# Rock-Paper-Scissors

Milestone 1

I have used Teachable-Machines which allows the computer to recognise the input which the user(us) gives to the camera. By giving the computer multiple images of rock, paper and scissors, the computer is able to recognise which one is being shown.
Git has been used along with Github. Git has been used to locate the required directories and create commits to files which are then pushed to the Github site. This allows others to collaborate and work on the file. By committing the modifications, we have 'checkpoints' in which the changes can be reverted if not wanted.

Milestone 2

Milestone 2 has taught me the importance of creating a virtual environment so that certain libraries can be installed into certain environments so that each environment can be used for a separate project.
This milestone builds upon the previous milestone as the model created on Teachable-Machines has been run using a code on python. The model is run inside the conda virtual environment, activating the following code:

<img width="473" alt="image" src="https://user-images.githubusercontent.com/109103538/179737965-ce291603-43a0-4688-a990-3ea1febb0f07.png">

The while loop keeps the code running and updating to give a np array, corresponding to the relative certainty the machine has of identifying whether the image captured is a rock, paper or scissors. This is the machine giving a prediction of what it thinks is being shown to it.

Milestone 3

In this milestone, I created a manual version of the game RPS without the computer vision.
The user choice was stored in a function called 'get_user_choice' which would obtain the choice of the user via an input. 

<img width="416" alt="image" src="https://user-images.githubusercontent.com/109103538/179737697-7a4812a5-42c1-429c-ba3f-a75170f81074.png">

The computer choice came from an imported module known as 'random' and this would allow the computer to choose, at random, an option of rock, paper or scissors.

<img width="263" alt="image" src="https://user-images.githubusercontent.com/109103538/179738251-d20db1cf-c846-4869-865a-a2cff08d67dc.png">

The get_winner function would compare the computer and user choices to determine a winner.

<img width="685" alt="image" src="https://user-images.githubusercontent.com/109103538/179738392-3b0bb372-6285-49cb-8f1e-6f10ff4bd396.png">

All of these functions were then called in a final function known as play. The result was a game of rock paper scissors for one round with just an input from the user.

<img width="199" alt="image" src="https://user-images.githubusercontent.com/109103538/179738779-6cf1ec92-5e21-4d90-a9f6-96308bb13ec5.png">

The results were not printed but returned to be used in the later stage of developng the computer vision.



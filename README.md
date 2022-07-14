# Rock-Paper-Scissors

Milestone 1

I have used Teachable-Machines which allows the computer to recognise the input which the user(us) gives to the camera. By giving the computer multiple images of rock, paper and scissors, the computer is able to recognise which one is being shown.
Git has been used along with Github. Git has been used to locate the required directories and create commits to files which are then pushed to the Github site. This allows others to collaborate and work on the file. By committing the modifications, we have 'checkpoints' in which the changes can be reverted if not wanted.

Milestone 2

Milestone 2 has taught me the importance of creating a virtual environment so that certain libraries can be installed into certain environments so that each environment can be used for a separate project.
This milestone builds upon the previous milestone as the model created on Teachable-Machines has been run using a code on python. The model is run inside the conda virtual environment, activating the following code:

import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

This code must be run using the conda environment where I installed the pip libraries that are present within the code.
`conda activate RPS

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

The while loop keeps the code running and updating to give a list, corresponding to the relative certainty the machine has of identifying whether the image captured is a rock, paper or scissors. This is the machine giving a prediction of what it thinks is being shown to it.


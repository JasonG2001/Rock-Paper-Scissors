import cv2
import time
from keras.models import load_model
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('frame', frame)
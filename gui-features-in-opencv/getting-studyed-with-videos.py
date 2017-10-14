
"""
Playing video from file
"""
import os,sys
import numpy as np
import cv2

current_dir = os.path.dirname(os.path.realpath(__file__))

cap = cv2.VideoCapture(current_dir + '/vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
study with Geting started with Images("https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image").

@author Holdlen2DH
"""
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

current_dir = os.path.dirname(os.path.realpath(__file__))
imgname = "messi5.jpg"
imgpath = current_dir + "/" + imgname

# read and display an image
img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write an image
cv2.imwrite(current_dir + "/messi5_2.png", img)

# using a matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


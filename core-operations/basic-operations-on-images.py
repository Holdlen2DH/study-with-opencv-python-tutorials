import os,sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.realpath(__file__))
imgpath = current_dir + "/messi5.jpg"

img = cv2.imread(imgpath)

# access a pixel value
px = img[100, 100]
print(px)

px_blue = img[100, 100, 0]
print(px_blue)

# modify the pixel values
img[100, 100] = [255, 255, 2]
print(img[100, 100])

# better pixel accessing and editing method
print(img.item(10, 10, 2))      # access rgb values
# modifying rgb value
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# access image properties
print(img.shape)
print(img.size)
print(img.dtype)

# image roi
img[273:333, 100:160] = img[280:340, 330:390]

# splitting and merging image channels
b, g, r = cv2.split(img)        # or b = img[:,:,0]
img = cv2.merge((r, g, b))      # img[:,;,2] = 0

cv2.namedWindow('mesi', cv2.WINDOW_NORMAL)
cv2.imshow('mesi',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


BLUE = [255,0,0]

img1 = cv2.imread(current_dir + '/opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
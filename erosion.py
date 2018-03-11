import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dotJ.png', 0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(erosion, kernel, iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('Morphed')
plt.xticks([]), plt.yticks([])
plt.show()
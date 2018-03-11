import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('graypg.jpg',0)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
hist, bins = np.histogram(img.ravel(), 256, [0,256])

plt.hist(img.ravel(),256, [0,256])
plt.show()

# img= cv2.imread('colorpg.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
# 	histr = cv2.calcHist([img], [i], None, [256], [0,256])
# 	plt.plot(histr,color =col)
# 	plt.xlim([0,256])
# plt.show()

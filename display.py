import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("Norway.jpg",0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
elif k==ord('s'):
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, 'Norway', (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)
	cv2.imwrite('grayNorway.png',img)
	cv2.destroyAllWindows()
# plt.imshow(img, cmap='gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()
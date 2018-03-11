import cv2
import numpy as np
img= cv2.imread('Norway.jpg')
part= img[280:900, 330:950]
img[273:893, 100:720] = part
cv2.namedWindow('Norway', cv2.WINDOW_NORMAL)
cv2.imshow('Norway',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
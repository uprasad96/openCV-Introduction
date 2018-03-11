import cv2
import numpy as np
img1 = np.zeros((512,512,3), np.uint8)
cv2.line(img1,(0,0),(511,511), (255,0,0),5)
img2 = np.zeros((512,512,3), np.uint8)
cv2.line(img2,(511,0),(0,511), (0,255,0),5)

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
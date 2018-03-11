import cv2
import numpy as np
x = 'Moon.jpg'
img = cv2.imread(x, 1)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---Approach 1---
#---Sharpening filter----
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im = cv2.filter2D(img, -1, kernel)
cv2.imshow("Sharpening",im)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---Approach 2---
aw = cv2.addWeighted(img, 4, cv2.blur(img, (30, 30)), -4, 128)
cv2.imshow("Add_weighted", aw)
cv2.waitKey(0)
cv2.destroyAllWindows()

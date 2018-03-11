import cv2
import numpy as np

img = cv2.imread('J.png' , 0)
ret,thresh = cv2.threshold(img, 127, 255, 0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2. moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx,cy)
print(M['m00'])
print(cv2.contourArea(cnt))
print(cv2.arcLength(cnt,True))
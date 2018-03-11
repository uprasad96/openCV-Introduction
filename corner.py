import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'chess2.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
img[dst>0.01*dst. max()] =[ 0, 0, 255]

cv2.imshow('dst' ,img)
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
# ret, dst = cv2.threshold(dst, 0.01*dst.max(),255,0)
# dst = np.uint8(dst)

# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,100, 0.001)
# corners = cv2.cornerSubPix(gray, np.float32(centroids), (5,5), (-1,-1), criteria)

# res = np.hstack((centroids,corners))
# res = np.int0(res)
# img[res[:,1],res[:,0]]= [0, 0 ,255]
# img[res[:,3],res[:,2]] =[0,255,0]

# cv2.imwrite('subpixel5.png',img)

# corners = cv2.goodFeaturesToTrack(gray, 25,0.01,10)
# corners = np.int0(corners)

# for i in corners:
# 	x,y =  i.ravel()
# 	cv2.circle(img,(x,y),3,255,-1)

# plt.imshow(img),plt.show()

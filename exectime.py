import cv2
img = cv2.imread('Utkarsh.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49 ,2):
	img =cv2.medianBlur(img,i)
e2 = cv2.getTickCount()
t= (e2-e1)/cv2.getTickFrequency()
print(t)

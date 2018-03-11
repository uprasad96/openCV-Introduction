import numpy as np
import cv2

cap =cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
isColor=False
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480),isColor)
while(cap.isOpened()):
	ret, frame =cap.read()
	if ret==True:		
		cv2.imshow('frame', frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		flip=cv2.flip(gray,0)
		out.write(flip)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()
import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
objURL = sys.argv[2]
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    obj = cv2.imread(objURL,-1)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        obj = cv2.resize(obj, (int(w * 1.5),int(obj.shape[0]/obj.shape[1]*w*1.5)))

        y1 = int(y-(obj.shape[0])*0.80)
        x1 = int(x-(obj.shape[1]-w)/2)

        y2 = y1 + obj.shape[0]
        x2 = x1 + obj.shape[1]

        if y1<0:
            if y2<0:
                continue
            else:
                obj = obj[ obj.shape[0]-y2:obj.shape[0], :]
                y1 = 0
        if x1<0:
            if x2<0:
                continue
            else:
                obj = obj[ :, obj.shape[1]-x2:obj.shape[1]]
                x1 = 0

        if x2>frame.shape[1]:
            if x1>frame.shape[1]:
                continue
            else:
                obj = obj[ :, 0:obj.shape[1]-x2+frame.shape[1]]
                x2 = frame.shape[1]

        alpha_obj = obj[ :, :, 3] / 255.0
        alpha_frame = 1.0 - alpha_obj

        for c in range(0,3):
            frame[y1:y2, x1:x2, c] = (alpha_obj * obj[ :, :, c] + alpha_frame * frame[ y1:y2, x1:x2, c])

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

import cv2
cv::Mat src = 'tt.jpg'
cv::Mat invSrc =  cv::Scalar::all(255) - src;
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
cv2.imshow('res', invSrc)
cv2.waitKey(0)
cv2.destroyAllWindows()

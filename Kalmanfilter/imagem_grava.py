import cv2
imagen = cv2.imread('logo.png',0)
cv2.imwrite('Grises.png',imagen)
cv2.imshow('Logo OpenCV Grises',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

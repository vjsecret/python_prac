import cv2

image = cv2.imread('Desert.jpg',1)
cv2.imshow("demo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
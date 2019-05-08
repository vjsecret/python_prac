import numpy as np
import matplotlib.pyplot as plt
import cv2



img=cv2.imread('Desert.jpg')


while(1):
    cv2.imshow("Orgin",img)
    k=cv2.waitKey(1)
    if k == 27:
        break

M=np.ones(img.shape,dtype="uint8")*100
print(img.shape)
added=cv2.add(img,M)


while(1):
    cv2.imshow("Add",added)
    k=cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()
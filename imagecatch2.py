import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

im=cv2.imread('imagecatch2.jpg')
#print(im)
total=im.shape
print(total)
#print(len(total))


edges = cv2.Canny(im,100,200)


imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
#print(ret)
#print(thresh)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(im, contours, -1, (0,0,255), 3)
#img = cv2.drawContours(im, contours, 3, (0,0,255), 3)

while(1):
    cv2.imshow('img',im)
    cv2.imshow('gray',imgray)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()

# plt.subplot(121)
# plt.imshow(im,cmap="gray")
# plt.title("origin")
# plt.xticks([]),plt.yticks([])
# plt.subplot(122)
# plt.imshow(edges,cmap="gray")
# plt.title("edge")

# plt.subplot(123)
# plt.imshow(img,cmap="gray")
# plt.title("findContours")

# plt.show()
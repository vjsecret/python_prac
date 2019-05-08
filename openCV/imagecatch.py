import numpy as np
import matplotlib.pyplot as plt
import cv2




while(1):
    img1=cv2.imread('Desert.jpg')
    img=cv2.imread("img/5images.jpg")
    imgR=cv2.imread("img/testRed.png")

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv2=cv2.cvtColor(imgR,cv2.COLOR_BGR2HSV)
        
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    
    mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)    
    res_blue=cv2.bitwise_and(img,img,mask=mask_blue)

    lower_red=np.array([1,1,0])
    upper_red=np.array([255,255,255])
    
    mask_red=cv2.inRange(hsv2,lower_red,upper_red)
    res_red=cv2.bitwise_and(imgR,imgR,mask=mask_red)

    cv2.imshow('frame',img)
    cv2.imshow('mask_blue',mask_blue)
    cv2.imshow('res_blue',res_blue)

    cv2.imshow('frame',imgR)
    cv2.imshow('mask_red',mask_red)
    cv2.imshow('res_red',res_red)

    k=cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
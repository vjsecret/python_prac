import cv2
import numpy as np

def startF():
    global imWidth
    global imHeight
    ch=raw_input("請選擇(1)200*100(2)500*300(3)800*500(4)exit:")
    if int(ch)==1:
        imWidth=200
        imHeight=100
    elif int(ch)==2:
        imWidth=200
        imHeight=100
    elif int(ch)==3:
        imWidth=200
        imHeight=100
    elif int(ch)==4:
        exit()
    else:
        exit()

if __name__ == "__main__":
    print cv2.__version__
    im = cv2.imread('Desert.jpg',1)
    #startF()
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("image",imWidth,imHeight)
    cv2.resizeWindow("image",800,500)
    # print(im.shape)
    # print(im.size)
    # print(im.dtype)
    # im[10,10]=[255,255,255]
    
    
    while(1):
        cv2.imshow("demo", im)
        k=cv2.waitKey(1)
        if k==ord('q'):
           break
    
    cv2.destroyAllWindows()
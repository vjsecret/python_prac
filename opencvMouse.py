import cv2
import numpy as np

drawing=False
point1=()
point2=()

def draw_circle(event, x, y, flags, param):
    global point1,point2,drawing
    
    if event==cv2.EVENT_LBUTTONDBLCLK:
        if drawing is False:
            drawing=True
            print("EVENT_LBUTTONDBLCLK_if drawing is False")
            point1=(x,y)
        else:
            print("EVENT_LBUTTONDBLCLK_if else")
            drawing=False
    elif event==cv2.EVENT_MOUSEMOVE:
        print("EVENT_MOUSEMOVE")
        if drawing is True:
            print("EVENT_MOUSEMOVE_if drawing is True")
            point2=(x,y)



img=np.zeros((500,500,3),np.uint8)+255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    if point1 and point2:
        cv2.rectangle(img,point1,point2,(0,255,0))
        point1=()
        point2=()
    cv2.imshow('image',img)
    
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()



#---------------------------------#
# def draw_circle(event, x, y, flags, param):
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y),20, (255,0,0), 1)
#         
# img=np.zeros((500,500,3),np.uint8)+255
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# 
# while(1):
#     cv2.imshow('image',img)
#     
#     if cv2.waitKey(1)==27:
#         break
# cv2.destroyAllWindows()
from PIL import Image #Pillow
from functools import reduce
import cv2,os,math,operator

pic1=Image.open("o1.jpg")
pic2=Image.open("o3.jpg")
h1=pic1.histogram()
h2=pic2.histogram()

diff=math.sqrt(reduce(operator.add,list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))
print(diff)

if diff ==0.0:
    print("完全符合")
else:
    print("不符合")
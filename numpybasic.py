#from pandas_datareader import data as web
#import fix_yahoo_finance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import xgboost as xgt
# from xgboost import XGBClassifier
# from sklearn import tree
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import preprocessing
# from sklearn.datasets.samples_generator import make_classification
# from sklearn.svm import SVC
#from sklearn import svm
import cv2

#https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/ imshowcv2與matplot的差異;如果是以 OpenCV 讀取灰階的圖片時，由於 channel 只有一個，所以就不會有上述的色彩問題，直接把 OpenCV 讀入的 NumPy 陣列放進 Matplotlib 的 imshow 中即可顯示，但是 Matplotlib 在顯示一個 channel 的圖片時，會用預設的 colormap 上色，所以如果想要以黑白的方式呈現灰階圖片，可以自己設定 colormap:plt.imshow(img_gray, cmap = 'gray')
#各種方法應用:https://yongyuan.name/pcvwithpython/chapter10.html
#cv2.cvtColor():https://blog.csdn.net/u012193416/article/details/79312798, https://blog.csdn.net/a1809032425/article/details/82156145
#COLOR_BGR2RGB:https://blog.csdn.net/JNingWei/article/details/77725559
#https://www.kancloud.cn/aollo/aolloopencv/269599


#zbar:
#https://blog.xuite.net/mjordan.chen/blog/60631414-%E4%B8%80%E7%B6%AD%E6%A2%9D%E7%A2%BC%E8%BE%A8%E8%AD%98%E6%B8%AC%E8%A9%A6
#https://zhuanlan.zhihu.com/p/21292914
#opencv二維碼辨識:http://blog.callmewhy.com/2016/04/23/opencv-find-qrcode-position/, https://cloud.tencent.com/developer/article/1084435
#http://atceiling.blogspot.com/2017/03/raspberry-pi-zbar.html

colors = ['red', 'green', 'blue', 'yellow']

for i, color in enumerate(colors):
    print(i, '-->', color)
print(color)

das=[5,6,4,8,6]
print(das)
obj1=iter(das)
print(obj1)
boj2=np.fromiter(obj1,dtype=float)
print(boj2)

# #pra6:
img1=cv2.imread('Desert.jpg')
img=cv2.imread("img/5images.jpg")
#print(img1.shape)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
#print(mask_blue)
res_blue=cv2.bitwise_and(img,img,mask=mask_blue)
# print(res_blue)
# print(res_blue.shape)
# print(type(res_blue))
# print(len(res_blue[2]))

#plt.imshow(img)
plt.imshow(mask_blue)
#plt.imshow(res_blue)
plt.show()

# #pra5:
# img=cv2.imread('Desert.jpg', cv2.IMREAD_GRAYSCALE)
# plt.imshow(img,cmap="pink")

# img[15][125]=[255,0,0]
# print(img)
# #print(type(img))
# #print(img[100][100])
# px=img[100][100]
# print(px)
# b=img[100][100][0]
# print(b)



# total=img.shape
# #print(total)
# 
#aa=np.array(img)
#print(aa)
#print(type(aa))

# #pra3:
# for xx in range(10,200):
#     for yy in range(10,200):
#         img[xx,yy]=[255,255,255]
# #pra4:
#im_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#plt.imshow(im_rgb)
plt.show()

# k1=np.hsplit()
# print(k1)


# while(1):
#     cv2.imshow("image",im_rgb)
#     k=cv2.waitKey(1)
#     if k == 27:
#         break
# cv2.destroyAllWindows()



exit()
ns=np.arange(9)
ns2=np.split(ns,3)
print(ns2)
print(type(ns2))

k1=ns2[0]
len1=len(ns2[0])
print(len(ns2[0]))
for i in range(0,len1):
    print(k1[i])


exit()
n1=np.array(["102/9/12","102/9/13","102/9/14","102/9/12","102/9/13","102/9/14"])
print(n1)
print("")
k1=np.unique(n1)
print(k1)

n3=np.arange(9).reshape(3,3)
print(n3)
print("")
n2=n3.view()
print(n2)
print(type(n2))
exit()
das=[5,6,4,8,6]
print(das)
obj1=iter(das)
print(obj1)
boj2=np.fromiter(obj1,dtype=float)
print(boj2)

#print(das)
exit()


orginfilename="545.txt"

# f = open(orginfilename, "r")
# if (f==0):
#     print("f==zero")
# 
# print(f)
# print(type(f))
# #print (f.softspace)
# 
# f=openfile()
# content = f.readlines()
# 
# row=[]
# for line in content:
#     temp = line.split(',')
#     row.append(temp)
# f.close()

def openfile(orginfilename):
    try:
        f = open(orginfilename, "r")
        if (f==0):
            print("f==zero")
        print(f)
        print(type(f))
        return f
    except:
        print("open file error")
        return -1

if __name__ == "__main__":
    ff=openfile(orginfilename)
    if ff==-1:
        print("open file error")
        exit()

    print("main_openf:")
    print(ff)
    print(type(ff))
    print(len(ff.read()))
    content = ff.readlines()
    
    row=[]
    for line in content:
        temp = line.split(',')
        row.append(temp)
    ff.close()

exit()
#========================================#
img=cv2.imread('Desert.jpg')
#print(img)
total=img.shape
print(total)
#print(len(total))

for i in range(0,total[0]/2):
    for j in range(0,total[1]):
        img[i,j]=[0,0,0]
    
while(1):
    cv2.imshow("image",img)

    k=cv2.waitKey(1)
    if k== ord('q'):
        break
cv2.destroyAllWindows()


#http://monkeycoding.com/?p=615
#https://blog.csdn.net/sunny2038/article/details/12889059
edges = cv2.Canny(img,100,200)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #cv2.findContours()函数接受的参数为二值图
# cv2.drawContours(img,contours,-1,(0,0,255),3)
# cv2.imshow("img",img)
# cv2.WaitKey(0)

plt.subplot(121)
plt.imshow(img,cmap="gray")
plt.title("origin")
plt.xticks([]),plt.yticks([])
plt.subplot(122)
plt.imshow(edges,cmap="gray")
plt.title("edge")

plt.show()


kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)
lower_res=cv2.pyrDown(img)
high_reso=cv2.pyrUp(img)

while(1):
    cv2.imshow("image",img)
    cv2.imshow("erosion",erosion)
    cv2.imshow("lower",lower_res)
    cv2.imshow("higher",high_reso)
    k=cv2.waitKey(1)
    if k== ord('q'):
        break
cv2.destroyAllWindows()
#========================================#


# X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,
#                           random_state=3,scale=100,n_clusters_per_class=1)
# plt.scatter(X[:,0],X[:,1],c=y)
# #plt.show()
# 
# #X = preprocessing.scale(X)
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
# clf = SVC(gamma='auto')
# clf.fit(X_train,y_train)
# print(clf.score(X_test,y_test))

# iris = datasets.load_iris()
# 
# iris_data = iris.data
# iris_label = iris.target
# 
# print(iris_data[0:3])
# 
# train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)
# knn = KNeighborsClassifier()
# knn.fit(train_data,train_label)
# print(knn.predict(test_data))
# print(test_label)
# 
# suc=0
# fail=0
# for ix in range(0,len(test_label)):
#     if test_label[ix]==knn.predict(test_data)[ix]:
#         suc=suc+1
#     else:
#         fail=fail+1
# 
# print(suc)
# print(fail)
# print(len((test_label)))
exit()
aa=yf.pdr_override()
print(aa)
print(type(aa))
#2.設定日期
start = dt.datetime(2014, 12, 1)
end = dt.datetime(2015, 1, 1)

#3.開始我們的函式
df = web.get_data_yahoo(['1101.TW'],start, end)
print(df)

a=np.array([[1,2,3],[4,5,6]])
#print(a)
b=a.reshape(3,2)
#print(b)
print(len(b))
print(len(b[0]))
print("")



#for i in range(0,len(b)):
for j in range(0,len(b[0])):
    #     print (b[i][j])
    #print(b[i][0])
    print(b[j][0])
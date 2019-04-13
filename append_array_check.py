#!/usr/bin/python
# -*- coding:utf8 -*-

from __future__ import print_function

mylist=[[10,20],[30,40],[50,60]]
print(len(mylist[0]))

H=[]
L=[]
date=[]
tick_max=[]
tick_min=[]
tick_end=[]
data_rad=[]
data_num=[]

listtt=[]
listtt1=[
['107/12/04', '35.85', '35.85', '34.85', '35.05', '-0.80', '8,425'], ['107/12/05', '34.50', '35.30', '34.35', '34.85', '-0.20', '5,645'], ['107/12/06', '34.85', '35.15', '34.60', '34.65', '-0.20', '6,740']]

listtt2=[
['107/12/07', '35.85', '35.85', '34.85', '35.05', '-0.80', '8,425'], ['107/12/08', '34.50', '35.30', '34.35', '34.85', '-0.20', '5,645'], ['107/12/09', '34.85', '35.15', '34.60', '34.65', '-0.20', '6,740']]

print("start:")
for i in range(0,2):
    print("cirle=%d" % int(i))
    if i==0:
        listtt=listtt1
    elif i==1:
        listtt=listtt2

    print("len(listtt)=%d" % len(listtt))
    for i in range(0,len(listtt)):
        print(listtt[i])
        # print()
        H.append(listtt[i])


print("=============result================")
print("newlist=")
print(H)
print("lenH_data=%d" % len(H))
print("len_elent=%d" % len(listtt[0]))

L_tmp=len(H)*len(H[0])
print("L_tmp=%d" % L_tmp)
for g in range(0,len(H)):
    L.append(H[g])

print("lenL_data=%d" % len(L))
# print(L)
print(L[5][0])
for ii in range(0,len(L)):
    date.append(L[ii][0])
    data_num.append(L[ii][1])
    tick_max.append(L[ii][2])
    tick_min.append(L[ii][3])
    tick_end.append(L[ii][4])

#print(date)
print(date[1])
exit();
mylist=[[10,20],[30,40],[50,60]]

for i in range(0,len(mylist)):
    for j in range(0,len(mylist[0])):
        print(mylist[i][j])



data1=[]
mun=['_11','_12']
NoA=['a','b']
#print(mun[0])
stock_No = [0 for _ in range(len(NoA))]
#stock_No=['a','b']
#print(stock_No[0])
stock_NoM=['a','b']
#NoA=stock_No


for i in range(0,len(mun)):
    # stock_No[i]=stock_No[i] + '' + mun[i]
    # stock_No[i]=str(stock_No[i]) + '' + str(mun[i])
    a=[]
    a=[NoA[i],mun[i],'.csv']
    b=[NoA[0],mun[i],'.csv']
    #print(a)
    stock_No[i]=''.join(a)
    print(stock_No[i])
    
    

si="Theory"
#print(si[0])

si=si.lower()
#print(si)


#n=[0,0,0,0,0,0]
n = [0 for _ in range(len(si))]
for i in range(0,len(si)):
    n[i]=ord(si[i])

print(n)
# n=[]
# for i in range(0,len(si)):
#     n.append(ord(si[i]))

exit();
#list1=[("p1","A"),("p2","AB")]
list1=[("p1","p2"),("A","AB")]
num=raw_input("請輸入編號:")
i=int(num)
print(list1[int(i)])

exit();

b=raw_input("請輸入=")
x=False

a=[10,20,30,40,50]

for i in range(0,len(a)):
    if int(b)==a[i]:
        x=True
        break

if x:
    print('b存在')
else:
    print('b不存在')

exit();
#==========================================
# a='A'
# b="A"
# c=raw_input("請輸入一個數值:")
# 
# print(a.isdigit())
# print(b.isdigit())
# print(c.isdigit())
# 
# if a.isdigit():
#     print("True")
# else:
#     print("False")
#     
# if b.isdigit():
#     print("True")
# else:
#     print("False")
# 
# if c.isdigit():
#     print("True")
# else:
#     print("False")
    
exit();
#==========================================
# start=1
# while (start!=2):
#     num=int(raw_input("請輸入一個數值:"))
#     i=1
#     sum=1
#     
#     while(i<=num):
#         #print(i)
#         sum*=i
#         i=i+1
#         #print(sum)
#     
#     print(sum)
#     start=int(raw_input("請選擇(1)繼續執行(2)完全結束"))
#     if start==2:
#         break
# 
# season=int(raw_input("請選擇(1)春天(2)夏天(3)秋天(4)冬天:"))
# if season==1:
#     print("櫻花")
# 
# print("請輸入兩變數:")
# num1=float(raw_input("請輸入第一個數值:"))
# num2=float(raw_input("請輸入第二個數值:"))
# start=int(raw_input("請選擇(1)加法(2)減法(3)乘法(4)除法:"))
# total=0
# if start==1:
#     total=num1+num2
#     print(total)
# elif start==2:
#     total=num1-num2
#     print(total)
# elif start==3:
#     total=num1*num2
#     print(total)
# elif start==4:
#     if num2==0:#if num1==0 or num2==0:
#         print("0")
#         #print("有數值為零")
#     else:
#         total=num1/num2
#         print(total)
#         
# else:
#     print("不在範圍內，請選擇方法")

exit();
#==========================================
# num=int(raw_input("請輸入一個數值:"))
# str1=""
# 
# for i in range(1,num+1):
#     if num%i==0:
#         str1=str1+str(i)+" "
# 
# print(str1)
# print(len(str1))
# print("",end="\n")
# print(str1.strip())
# print(len(str1.rstrip()))
exit();
#==========================================
num=int(raw_input("請輸入一個數值:"))
str1=""
x=True

for i in range(1,num+1):
    if (num%i)==0:
        #print(i)
        str1=str1+str(i)+" "
        #print("i1=%d" % i,end="\t")
        if i==1 and i==num:
            print("i2=%d" % i,end="\t")
            x=False
        
print("%d 的因數有%s" % (num,str1))


if x==False:
    print("%d 是質數" % num)
else:
    print("%d 不是質數" % num)

exit();
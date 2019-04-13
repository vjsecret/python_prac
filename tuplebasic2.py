#!/usr/bin/python
# -*- coding:utf8 -*-

from __future__ import print_function

tup1=("p1001","p1002","p1003","p1004","p1005")
tup2=("小明","小玲","小童","小張","小巾")
tup3=(60,70,23,93,70)
tup4=(70,50,60,60,56)
tup5=(80,90,80,90,86)

tSer=False
while True:
    num=raw_input("選單:(1)瀏覽(2)查詢國文分數大於60(3)查詢英文分數小於60(4)學號查詢(5)完全結束:")
    
    if num!="":
        if int(num)==5:
            break
            
        plist1=list(tup1)
        plist2=list(tup2)
        plist3=list(tup3)
        plist4=list(tup4)
        plist5=list(tup5)
        # print(plist1)
        # print(plist2)
        # print(plist3)
        # print(plist4)
        # print(plist5)
        avg=[]
        for i in range(0,len(plist1)):
            avg.append((plist3[i]+plist4[i]+plist5[i])/3)

        if int(num)==1:
            print("學號", "姓名",  "國文", "英文", "數學", "平均", end="")
            for i in range(0,len(plist1)):
                print()
                #print(plist1[i],plist2[i],plist3[i],plist4[i],plist5[i])
                print(tup1[i],tup2[i],tup3[i],tup4[i],tup5[i],avg[i])                    
        elif int(num)==2:
            print("學號", "姓名",  "國文", "英文", "數學", "平均", end="")
            for i in range(0,len(plist3)):
                if int(plist3[i])>=60:
                    print()
                    print(tup1[i],tup2[i],tup3[i],tup4[i],tup5[i],avg[i]) 
                    #print(plist1[i],plist2[i],plist3[i],plist4[i],plist5[i])
                    #print(plist1[pindex],plist2[pindex],plist3[pindex],plist4[pindex],plist5[pindex])
            #print(tup1[pindex],tup2[pindex],tup3[pindex],tup4[pindex],tup5[pindex])
        elif int(num)==3:
            print("學號", "姓名",  "國文", "英文", "數學", "平均", end="")
            for i in range(0,len(plist4)):
                if int(plist4[i])<=60:
                    print()
                    print(tup1[i],tup2[i],tup3[i],tup4[i],tup5[i],avg[i]) 
        elif int(num)==4:
            n2=raw_input("請輸入欲查詢編號:")
            if n2!="":
                for i in range(0,len(plist1)):
                    if n2==plist1[i]:
                        print("學號", "姓名",  "國文", "英文", "數學", "平均", end="")
                        print()
                        print(tup1[i],tup2[i],tup3[i],tup4[i],tup5[i],avg[i]) 
                        #tSer=True
            else:
                print("輸入範圍錯誤") 

#!/usr/bin/python
# -*- coding:utf8 -*-

from __future__ import print_function


plist1=["p1001","p1002","p1003","p1004","p1005"]
plist2=["張小明","李木同","李玲","簡易山","彰明"]
plist3=["A","B","O","AB","A"]
plist4=['設計師','講師','工程師','設計師','工程師']
plist5=[30000,25000,40000,26000,35000]


# list1=[]
# for i in range(0,len(plist1)):
#     list1.append(plist1[i])
#     #list1.append(plist2[i])
#     #list1.append(plist3[i])
#     print(plist4[i])
#     list1.append(plist4[i])
#     #list1.append(plist5[i])
#     
# print(list1)
# exit()

tSer=False
while True:
    num=raw_input("功能選單:(1)瀏覽(2)編號查詢(3)血型查詢(4)最高薪資(5)最低薪資(6)結束(7)編號區間查詢(9)新增資料(10)刪除資料(11)修改資料:")
    
    if num!="":
        if int(num)==6:
            break

        if int(num)==1:
            print("編號", "姓名",  "血型", "工作", "薪資",end="")
            for i in range(0,len(plist1)):
                print()
                print(plist1[i],plist2[i],plist3[i],plist4[i],plist5[i])
        elif int(num)==2:
            d_num=0
            d_name=''
            d_id=''
            d_blood=''
            d_c=''
            d_s=''
            n2=raw_input("請輸入編號:")
            if n2!="":
                for i in range(0,len(plist1)):
                    if n2==plist1[i]:
                        print(plist1[i],plist2[i],plist3[i],plist4[i],plist5[i])
                        tSer=True
                        d_num=i
                        d_id=plist1[i]
                        d_name=plist2[i]
                        d_blood=plist3[i]
                        d_c=plist4[i]
                        d_s=plist5[i]
            else:
                print("輸入範圍錯誤") 
        elif int(num)==3:
            n3=raw_input("請輸入血型:")
            if n3!="":
                if n3.isdigit()!=True:
                    for i in range(0,len(plist3)):
                        if n3==plist3[i]:
                            print(plist1[i],plist2[i],plist3[i],plist4[i],plist5[i])
                else:
                    print("請輸入字母")
            else:
                print("輸入範圍錯誤")   
        elif int(num)==4:
            print("最高薪資:%d" % max(plist5))
        elif int(num)==5:
            print("最低薪資:%d" % min(plist5))
        elif int(num)==7:
            len1=len(plist1)
            ids=raw_input("請輸入開始編號:")
            ide=raw_input("請輸入結束編號:")
            print("編號", "姓名",  "血型", "工作", "薪資",end="")
            print()
            
            for u in range(0,len1):
                pid=plist1[u]
                if int(pid[1:])>=int(ids[1:]) and int(pid[1:])<=int(ide[1:]):
                    print(plist1[u],plist2[u],plist3[u],plist4[u],plist5[u],end="\t")
                    print()
                
        elif int(num)==9:
            print("最低薪資:%d" % min(plist5))
        elif int(num)==10:
            if tSer!=True:
                print("刪除前請查詢資料")
                continue
            else:
                DD=''
                DD=raw_input("確認刪除此筆資料嗎(y)確認(n)取消:")
                while True:
                    if DD=="y":
                        del plist1[d_num]
                        del plist2[d_num]
                        del plist3[d_num]
                        del plist4[d_num]
                        del plist5[d_num]
                        tSer=False
                        d_num=0
                        print("刪除完成")
                        break
                    else:
                        tSer=False
                        d_num=0
                        continue
        elif int(num)==11:
            if tSer!=True:
                print("修改前請查詢資料")
                continue
            else:
                DD=''
                DD=raw_input("確認修改此筆資料嗎(y)確認(n)取消:")
                if DD=="y":
                    ch=raw_input("(1)姓名(2)血型(3)職業(4)薪水:")
                    if int(ch)==1:
                        print("原資料:%s" % plist2[d_num])
                        a_name=raw_input("請輸入新資料:")
                        del plist2[d_num]
                        plist2.insert(d_num,a_name)
                        tSer=False
                        d_num=0
                        print("修改完成")
                    elif int(ch)==2:
                        print("原資料:%s" % plist3[d_num])
                        a_blood=raw_input("請輸入新資料")
                        del plist3[d_num]
                        plist3.insert(d_num,a_blood)
                        tSer=False
                        d_num=0
                        print("修改完成")
                    elif int(ch)==3:
                        print("原資料:%s" % plist4[d_num])
                        a_c=raw_input("請輸入新資料")
                        del plist4[d_num]
                        plist4.insert(d_num,a_c)
                        tSer=False
                        d_num=0
                        print("修改完成")
                    elif int(ch)==4:
                        print("原資料:%s" % plist5[d_num])
                        a_s=raw_input("請輸入新資料")
                        del plist5[d_num]
                        plist5.insert(d_num,a_s)
                        tSer=False
                        d_num=0
                        print("修改完成")
                else:
                    tSer=False
                    d_num=0
                    continue
        else:
            print("請輸入數字")
    else:
        print("輸入範圍錯誤，請重新輸入")

exit()
# list1=[("p1001",'張小明',"A","設計師","30000"),("p1002","李木同","B","講師","25000"),("p1003","李玲","O","工程師","40000"),("p1004","簡易山","AB","設計師","26000"),("p1005","彰明","A","工程師","35000")]
# 
# tplist1=list1[0]
# tplist2=list1[1]
# tplist3=list1[2]
# tplist4=list1[3]
# tplist5=list1[4]
# print(tplist1)
# exit()
# 
# plist1=[tplist1[0],tplist2[0],tplist3[0],tplist4[0],tplist5[0]]
# plist2=[tplist1[1],tplist2[1],tplist3[1],tplist4[1],tplist5[1]]
# plist3=[tplist1[2],tplist2[2],tplist3[2],tplist4[2],tplist5[2]]
# plist4=[tplist1[3],tplist2[3],tplist3[3],tplist4[3],tplist5[3]]
# plist5=[tplist1[4],tplist2[4],tplist3[4],tplist4[4],tplist5[4]]
# #print(plist1)
# #print(plist2)
# #print(plist3)
# #print(plist4)
# #print(plist5)
# #exit()
# 
# while True:
#     num=raw_input("功能選單:(1)瀏覽(2)編號查詢(3)血型查詢(4)最高薪資(5)最低薪資(6)結束:")
#     if num!="":
#         if int(num)==6:
#             break
#         elif int(num)==1:
#             print(list1)
#         elif int(num)==2:
#             n2=raw_input("請輸入編號:")
#             if n2!="":
#                 for i in range(0,len(plist1)):
#                     if n2==plist1[i]:
#                         print(list1[i])
#             else:
#                 print("輸入範圍錯誤") 
#         elif int(num)==3:
#             n3=raw_input("請輸入血型:")
#             if n3!="":
#                 if n3.isdigit()!=True:
#                     for i in range(0,len(plist3)):
#                         if n3==plist3[i]:
#                             print(list1[i])
#                 else:
#                     print("請輸入字母")
#             else:
#                 print("輸入範圍錯誤")   
#         elif int(num)==4:
#             n4=[]
#             for i in range(0,len(plist5)):
#                 n4.append(int(plist5[i]))
#                 
#             print("最高薪資:%d" % max(n4))
#         elif int(num)==5:
#             n4=[]
#             for i in range(0,len(plist5)):
#                 n4.append(int(plist5[i]))
#                 
#             print("最低薪資:%d" % min(n4))
#         else:
#             print("請輸入數字")
#     else:
#         print("輸入範圍錯誤，請重新輸入")
# 
# exit()

si="Theory"
#print(si[0])

si=si.lower()
#print(si)


#n=[0,0,0,0,0,0]
n = [0 for _ in range(len(si))]
for i in range(0,len(si)):
    n[i]=ord(si[i])

# n=[]
# for i in range(0,len(si)):
#     n.append(ord(si[i]))
        
print(n)
n1=sorted(n)
print("最大值=%s" % chr(max(n)))
print("最小值=%s" % chr(min(n)))
print("居中值=%s" % chr(n[len(n)/2-1])+chr(n[len(n)/2]))
# mid=chr(n[len(n)/2-1])+chr(n[len(n)/2])
# print("居中值=%s" % mid)




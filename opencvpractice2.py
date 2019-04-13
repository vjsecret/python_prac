from __future__ import print_function

mylistfirst=[]
d=1

def entryvalue():
    global d
    mylist=[]
    k=1
    try:
        while(True):
            numdata=int(input("請輸入數值資料"+str(k)+":"))
            mylist.append(numdata)
            mylistfirst.append(numdata)
            k=k+1
            d=d+1
    except:
        print("d=%d" % d)
        print("退出")
        sortvalue(mylist)

def test():
    global d
    mylist=[]
    k=1
    try:
        while(True):
            numdata=int(input("請輸入數值資料"+str(k)+":"))
            mylist.append(numdata)
            mylistfirst.append(numdata)
            k=k+1
            d=d+1
    except:
        print("退出")
        #exit()

def test2():
    global d
    mylist=[]
    k=1
    while(True):
        numdata=int(input("請輸入數值資料"+str(k)+":"))
        mylist.append(numdata)
        mylistfirst.append(numdata)
        k=k+1
        d=d+1

def sortvalue(mylist):
    len1=len(mylist)
    temp=0
    
    for i in range(0,len1-1):
        for j in range(0,len1-1-i):
            if mylist[j]>mylist[j+1]:
                temp=mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
    
    display(mylist)

def display(mylist):
    len2=len(mylist)
    
    print("排序前:")
    for f in range(0,len2):
        print(mylistfirst[f],end=" ")
    print()
    
    
    print("正排序:")
    for d in range(0,len2):
        print(mylist[d],end=" ")
    print()
    
    print("逆排序:")
    for h in range(len2-1,0-1,-1):
        print(mylist[h],end=" ")
    print()
if __name__ == "__main__":
    #test2()
    entryvalue()
    print("d=%d" % d)
    print("END Program")
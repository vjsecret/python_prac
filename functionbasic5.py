from __future__ import print_function

def input():
    list1=[]
    for i in range(0,5):
        a=raw_input("請輸入數值"+str(i+1)+":")
        list1.append(int(a))
    # a1=raw_input("請輸入數值一:");
    # a2=raw_input("請輸入數值二:");
    # a3=raw_input("請輸入數值三:");
    # a4=raw_input("請輸入數值四:");
    # a5=raw_input("請輸入數值五:");
    # list1=[a1, a2, a3, a4, a5]

    o_list=oddvalue(list1)
    e_list=even(list1)
    show(e_list)
    print("\n")
    show(o_list)
    exitfun()
    
def oddvalue(list0):
    list_o=[]
    #print(list0)
    len1=len(list0)
    for i in range(0,len1):
        if list0[i]%2==1:
            list_o.append(list0[i])
            #print(list_o)
    return list_o
    
def even(list):
    list_e=[]
    len1=len(list)
    for i in range(0,len1):
        if list[i]%2==0:
            list_e.append(list[i])
            #print(list_e)
    return list_e

def show(list):
    len1=len(list)
    for i in range(0,len1):
        print(list[i],end='\t')

def exitfun():
    ch=raw_input("請選擇(1)重新執行(2)完全結束:")
    
    if int(ch)==1:
        print("intch1")
        input()
    elif int(ch)==2:
        print("intch2")
        quit()
    else:
        print("exit")
        exitfun()

if __name__ == "__main__":
    input()

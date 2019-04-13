# def input():
#     a1=raw_input("請輸入數值一:");
#     a2=raw_input("請輸入數值二:");
#     a3=raw_input("請輸入數值三:");
#     a4=raw_input("請輸入數值四:");
#     a5=raw_input("請輸入數值五:");
#     list1=[a1, a2, a3, a4, a5]
#     show(list1)
# 
# def show(list):
#     for i in range(0,len(list)):
#         print(list[i])
#         
#     exitfun()
#         
# def exitfun():
#     ch=raw_input("請選擇(1)重新執行(2)完全結束:")
#     
#     if int(ch)==1:
#         input()
#     elif int(ch)==2:
#         quit()
#     else:
#         exitfun()
## ----------------------------------
# def input():
#     a1=raw_input("請輸入數值一:");
#     a2=raw_input("請輸入數值二:");
#     a3=raw_input("請輸入數值三:");
#     a4=raw_input("請輸入數值四:");
#     a5=raw_input("請輸入數值五:");
#     list1=[a1, a2, a3, a4, a5]
#     maxvalue(list1)
# 
# def maxvalue(list):
#     maxval=max(list)
#     show(maxval)
# 
# def show(a):
#     print("最大值={0}".format(a))
#     exitfun()
# 
# def exitfun():
#     ch=raw_input("請選擇(1)重新執行(2)完全結束:")
#     
#     if int(ch)==1:
#         input()
#     elif int(ch)==2:
#         quit()
#     else:
#         exitfun()
# 
# if __name__ == "__main__":
#     list0=input()
#     
# 
# exit()

def input():
    a1=raw_input("請輸入數值一:");
    a2=raw_input("請輸入數值二:");
    a3=raw_input("請輸入數值三:");
    a4=raw_input("請輸入數值四:");
    a5=raw_input("請輸入數值五:");
    list1=[a1, a2, a3, a4, a5]
    mina=minvalue(list1)
    show(mina)

def minvalue(list):
    print("def minvalue()")
    min_value=min(list)
    min_value=int(min_value)
    print("min_value={0}".format(min_value))
    return min_value

def show(a):
    print("def show()")
    print("最小值={0}".format(a))
    exitfun()

def exitfun():
    print("def exitfun()")
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
    print("start main")
    minval=input()
    show(int(minval))
    print("left main")
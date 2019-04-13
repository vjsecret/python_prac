a=0
b=0
sum=0

# def input():
#     global a
#     a=raw_input("請輸入數值一:")
#     global b
#     b=raw_input("請輸入數值二:")
#     logic()
#     
# def logic():
#     global sum
#     sum=int(a)+int(b)
#     show()
#     
# def show():
#     print("{0}+{1}={2}".format(a,b,sum))
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
#     input()
#     

def input():
    print("def input() in line 6")
    #global a
    a=raw_input("請輸入數值一:");
    print("a=%s" % a)
    #global b
    b=raw_input("請輸入數值二:");
    print("b=%s" % b)
    #logic()
    print("key in su!")
    return a,b
    #logic(a,b)

def show(x,y):
    print("def show()")
    print("{0}+{1}={2}".format(x,y,sum))
    exitfun()

def logic(f, g):
    print("def logic()")
    global sum
    print("a=%s in logic" % f)
    print("b=%s in logic" % g)
    sum=f+g
    #sum=int(a)+int(b)
    show(f,g)

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
    x,y=input()
    print("a=%s after input()" % x)
    print("b=%s after input()" % y)
    logic(int(x),int(y))
    print("left main")
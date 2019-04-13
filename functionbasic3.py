def input():
    x=raw_input("請輸入數值一:")
    y=raw_input("請輸入數值二:")
    sum=logic(x,y)
    show(x,y,sum)
    
def logic(x,y):
    sum=int(x)+int(y)
    return sum
    
def show(x,y,sum):
    print("{0}+{1}={2}".format(x,y,sum))
    exitfun()
        
def exitfun():
    ch=raw_input("請選擇(1)重新執行(2)完全結束:")
    
    if int(ch)==1:
        input()
    elif int(ch)==2:
        quit()
    else:
        exitfun()

if __name__ == "__main__":
    input()
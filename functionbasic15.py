def entry():
    str=raw_input("請輸入字串:")
    list3=splitvalue(str)
    display(list3)

def splitvalue(str):
    list1=str.split(",")
    return list1

def display(list):
    len1=len(list)
    
    for i in range(0,len1):
        print(list[i])
    exitfun()

# def entry():
#     str="I-LOVE-PYTHON"
#     print(str)
#     str1=raw_input("請輸入被替代資料:")
#     str2=raw_input("請輸入替代新資料:")
#     str3=str.replace(str1,str2)
#     display(str3)
# 
# def display(str3):
#     print(str3)
#     exitfun()
#     
# def exitfun():
#     ch=raw_input("請選擇(1)重新執行(2)完全結束:")
#     
def exitfun():
    ch=raw_input("請選擇(1)重新執行(2)完全結束:")
    
    if int(ch)==1:
        entry()
    elif (int(ch)==2):
        quit()
    else:
        exitfun()

if __name__ == "__main__":
    entry()
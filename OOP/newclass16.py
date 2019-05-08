import listmaxcom1 as com

if __name__=="__main__":
    list1=[]
    for i in range(0,5):
        list1.append(input("請輸入值:"))
    
    kc=com.maxcomponet1(list1)
    kc.setMax()
    print(kc.getMax())
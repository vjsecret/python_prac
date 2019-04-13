while True:

    ch=0
    num=int(raw_input("請輸入一個數值:"))
    i=1
    sum=1
    
    while(i<=num):
        sum*=i
        i=i+1
    
    print(sum)
    ch=int(raw_input("請選擇(1)繼續執行(2)完全結束"))

    if ch==2:
        break
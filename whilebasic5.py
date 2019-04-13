i=1
while(i<=10):
    print(i)
    if i==5:
        break
    i=i+1


num=int(raw_input("請輸入一個數值:"))

i=1
sum=1

while(i<=num):
    #print(i)
    sum*=i
    i=i+1
    #print(sum)

print(sum)
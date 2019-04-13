num=int(raw_input("請輸入一個數值:"))
str1=""

for i in range(1,num+1):
    if (num%i)==0:
        str1=str1+str(i)+" "
        
print("%d 的因數有%s" % (num,str1))

print(lenstr1))
print(len(str1.strip()))

if len(str1.strip())>4:
    print("%d 不是質數" % num)
else:
    print("%d 是質數" % num)
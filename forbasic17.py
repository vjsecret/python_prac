from __future__ import print_function

num=int(raw_input("請輸入一個數值:"))
str1=""
x=False

for i in range(1,num+1):
    if (num%i)==0:
        #print(i)
        str1=str1+str(i)+" "
        #print("i1=%d" % i,end="\t")
        if i!=1 and i!=num:
            #print("i2=%d" % i,end="\t")
            x=True
        
print("%d 的因數有%s" % (num,str1))


if x:
    print("%d 不是質數" % num)
else:
    print("%d 是質數" % num)
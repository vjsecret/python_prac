from __future__ import print_function

total=0
for i in range(1,100+1):   
        total=total+i

print("sum1=%d" % total)

total=0
for i in range(1,100):   
    if i%2!=0:
        total=total+i
        
print("sum2=%d" % total)

total=0    
for i in range(0,100+1):
    if i%2==0:
        total=total+i

print("sum3=%d" % total)

total=0
for i in range(1,10):
    for j in range(1,10):
        total=i*j
        #print("%d=%d*%d" % (total,i,j),sep="\t\t")
        print("%d*%d=%d" % (i,j,total),end="\t")

print("\n")
total1=0
total2=0
str1=""
str2=""
p=0
for i in range(97,105+1,1):
    if i%2!=0:
        str1+=chr(i) #str1=str1+chr(i)
        p=p+1
        total1=p

p=0
for j in range(97,105+1,1):
    if j%2==0:
        str2+=chr(j) #str=str+chr(j)
        p=p+1
        total2=p

print("偶數字元%s共%d個" % (str2,total2))
print("奇數字元%s共%d個" % (str1,total1))

for i in range(1,5+1):
    print("\t")
    for j in range(1,5+1):
        if j<=i:
            print("A",end="")

print("\n")
for i in range(1,5+1):
    for j in range(0,i):
        print("A",end="")
    print("",end="\n")
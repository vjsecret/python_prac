str1="Hello Python!"
s=""

n=len(str1)
for i in range(0,n):
    if str1[i]=='o':
        s=s+str(i)+' '

print("o位於字串的==>%s" % (s))
print("\n")

str2="Hello Python!"
aa=str2.find('o')
print(aa)
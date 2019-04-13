str1="Java Application"
s=""
p=0

n=len(str1)
for i in range(0,n):
    if str1[i]=='a':
        s=s+str(i)+' '
        p+=1

s=s.rstrip()

print("a共有[%d]個" % p)
print("a位置於[%s]" % (s))
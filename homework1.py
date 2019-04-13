from __future__ import print_function

chi=int(raw_input("輸入國文分數:"))
eng=int(raw_input("輸入英文分數:"))
math=int(raw_input("輸入數學分數:"))

print('國文','英文','數學','總分','平均',sep="\t\t",end="\n")
print(chi,eng,math,(chi+eng+math),round((chi+eng+math)/3.0,2),sep="\t",end="\n")

# import math
# radius=float(raw_input("輸入半徑:"))
# area=math.pi*radius*radius
# data4=2*math.pi*radius
# print("圓面積=%.2f" % area)
# print("圓周長=%.2f" % data4)
import calendar as c
import matplotlib.pyplot as plt
from pyecharts import Bar
data1=['2018-01-03','2018-09-12','2018-02-06','2018-05-18','2018-10-25','2018-11-06','2018-12-13']

result=[]
odd=[]
even=[]

for i in range(0,len(data1)):
    x=data1[i].split("-")
    result.append(int(x[1]))

#print(result)
for jj in range(0,len(result)):
    if (result[jj]%2==1):
        odd.append(int(result[jj]))
    else:
        even.append(int(result[jj]))

list4=sorted(result)
# plt.plot(list4)
# plt.ylabel("y label")
# plt.show()
v1=[2.0,4.9,7.0,23.2,25.6,76.7,135.6]
bar=Bar("圖表","月份資料")
bar.add("參數值",result,v1,mark_line=["average"],mark_point=["max","min"])
bar.render()
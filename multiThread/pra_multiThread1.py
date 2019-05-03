import threading
import time

def setTest(num):
    if num==1:
        return job
    elif (num==2):
        return job1

# 子執行緒的工作函數
def job(num,index):
    global result
    print("job Thread", num)
    time.sleep(1)
    if num >= 3:
        result[index]=True
    else:
        result[index]=False

def job1(num,index):
    global result
    print("job1 Thread", num)
    time.sleep(1)
    if num >= 2:
        result[index]=True
    else:
        result[index]=False
# def job1(num,num2):
#   print("job1 Thread", num)
#   print("job1 Thread", num2)
#   time.sleep(1)
def porj(listDtata,task):
    threads = []
    for i in range(0,len(listDtata)):
        threads.append(threading.Thread(target = task, args = (listDtata[i],i)))
        test=threads[i].start()
    for i in range(0,len(listDtata)):
        threads[i].join()
    print(test)
    #print(threads)
# var1=setTest(1)
# var2=setTest(2)
def testCase(listDtata,joblist):
    global result
    for hh in range(0,len(jobList)):
        var=setTest(jobList[hh])
        porj(listDtata,var)
    for jj in range(0,len(result)):
        print(result[jj])
    #savefile

listDtata=[1,2,3,4,5,6,7]
jobList=[1,2]
result=[]
for kk in range(0,len(listDtata)):
    result.append(-2)
testCase(listDtata,jobList)
# # 建立 5 個子執行緒
# threads = []
# for i in range(5):
#     var=setTest(1)
#     threads.append(threading.Thread(target = var, args = (i,)))
#     threads[i].start()
# threads1 = []
# for j in range(5):
#     var=setTest(2)
#     threads1.append(threading.Thread(target = var, args = (j,5)))
#     threads1[j].start()

# 主執行緒繼續執行自己的工作
# ...

# # 等待所有子執行緒結束
# for i in range(5):
#   threads[i].join()
# for j in range(5):
#   threads1[j].join()

print("Done.")
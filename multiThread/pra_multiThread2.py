import threading
import time


# 子執行緒的工作函數
def job(num,suc):
    threads = []
    result=[]
    for kk in range(0,len(listDtata)):
        result.append(-2)
    print("job Thread", num)
    for i in range(0,len(listDtata)):
        threads.append(threading.Thread(target = caljob, args = (listDtata[i],i,result,suc,)))
        test=threads[i].start()
    for i in range(0,len(listDtata)):
        threads[i].join()
    #time.sleep(1)
    print("task", i)
    print("len(resul)=",len(result))
    for jj in range(0,len(result)):
        print(result[jj])
    print("suc=", suc)
    print("End job\n")
    # if num >= 3:
    #     result[index]=True
    # else:
    #     result[index]=False
def caljob(num,index,result,suc):
    print("caljob on suc=", suc)
    #global result
    print("caljob Thread", num)
    time.sleep(1)
    if num >= 3:
        result[index]=True
        suc=suc+1
        print("suc=", suc)
    else:
        result[index]=False
    
def job1(num,suc):
    threads = []
    result=[]
    for kk in range(0,len(listDtata)):
        result.append(-2)
    print("job1 Thread", num)
    for i in range(0,len(listDtata)-1):
        threads.append(threading.Thread(target = caljob1, args = (listDtata[i],i,result,suc,)))
        test=threads[i].start()
    for i in range(0,len(listDtata)-1):
        threads[i].join()
    time.sleep(1)
    for jj in range(0,len(result)):
        print(result[jj])
    print("suc=", suc)
    print("End job\n")
def caljob1(num,index,result,suc):
    #global result
    print("caljob1 Thread", num)
    time.sleep(1)
    if num >= 2:
        result[index]=True
        suc=suc+1
    else:
        result[index]=False

def porj(listDtata,jobList):
    threads = []
    suc=0
    for i in range(0,len(jobList)):
        task=setTest(jobList[i])
        threads.append(threading.Thread(target = task, args = (listDtata,suc,)))
        test=threads[i].start()
    # for i in range(0,len(listDtata)):
    #     threads[i].join()
    print(test)
    #print(threads)

def testCase(listDtata,jobList):
    threads = []
    for i in range(0,len(listDtata)):
        print("listDtata[i]=", listDtata[i])
        threads.append(threading.Thread(target = porj, args = (listDtata[i],jobList,)))
        threads[i].start()

def test0(listDtata,joblist):
    global result
    for hh in range(0,len(jobList)):
        var=setTest(jobList[hh])
        testCase(listDtata,var)
    for jj in range(0,len(result)):
        print(result[jj])
    #savefile

#有好幾筆list的資料(listDtata1,listDtata2,...)，每筆資料可執行不同的計算任務(job(),job1(),...=>根據jobList填的element的值決定要跑哪個job())
#目標:希望執行multi的計算任務，每個執行計算任務裡也是能針對資料跑multi

def setTest(num):
    if num==1:
        return job
    elif (num==2):
        return job1

def setData(num):
    global jobList
    global listDtata1
    if num==1:
        porj(listDtata1,jobList)
    elif (num==2):
        porj(listDtata2,jobList)

jobList=[1,2]
datanum=[1,2]
listDtata1=[1,2,3,4,5,6,7]
listDtata2=[3,4,5,6,7,8]
# listDtata=[[1,2,3,4,5,6,7], [3,4,5,6,7,8]]
# print(listDtata[1])
listDtata=[1,2,3,4,5,6,7]

#print(len(listDtata))
if __name__ == "__main__":
    print("start:")
    #test0(listDtata,jobList) #=>先實作一筆資料能跑多種任務
    #porj(listDtata,jobList)
    for ii in range(0,len(datanum)):
        setData(datanum[ii])
        print("******************************finish job ", ii)
    
    print("Done.")
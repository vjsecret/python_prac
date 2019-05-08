# import requests
# #import urllib2
# import pandas as pd
# import numpy as np
# import calendar as c
# import datetime
# import csv
# #from pyecharts import Bar
# import os
# import matplotlib.pyplot as plt
import threading
import time
import testM as obCaljob


def job(listDtata,suc):
    threads = []
    result=[]
    for kk in range(0,len(listDtata)):
        result.append(-2)
    print("job Thread", listDtata)
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

#def caljob(num,index,start,max,min,end,targetVar,suc):
def caljob(num,index,result,suc):
    print("caljob on suc=", suc)
    #global result
    print("caljob Thread", num)
    # if num >= 3:
    #     result[index]=True
    #     suc=suc+1
    #     print("suc=", suc)
    # else:
    #     result[index]=False
    aa=obCaljob.cond1(index,num,suc)
    aa.mycondition()
    aa.myconditionSub1()
    aa.myconditionSub2()
    print(aa.Tcase110up)
    return index, aa.Tcase110up, aa.Tcase110ups, aa.Tcase110upf, aa.Tcase110

def job1(listDtata,suc):
    threads = []
    result=[]
    for kk in range(0,len(listDtata)-1):
        result.append(-2)
    print("job1 Thread", listDtata)
    for i in range(0,len(listDtata)):
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
    # if num >= 2:
    #     result[index]=True
    #     suc=suc+1
    #     print("suc=", suc)
    # else:
    #     result[index]=False
    aa=obCaljob.cond2(index,num,suc)
    aa.mycondition()
    aa.myconditionSub1()
    aa.myconditionSub2()
    print(aa.Tcase110up)
    return index, aa.Tcase110up, aa.Tcase110ups, aa.Tcase110upf, aa.Tcase110

def job2(listDtata,suc):
    global filename
    threads = []
    result=[]
    for kk in range(0,len(listDtata)):
        result.append(-2)
    print("job2 Thread", listDtata)
    for i in range(0,len(listDtata)):
        threads.append(threading.Thread(target = caljob2, args = (listDtata[i],i,result,suc,)))
        test=threads[i].start()
    for i in range(0,len(listDtata)):
        threads[i].join()
    #time.sleep(1)
    # print("task", i)
    # print("len(resul)=",len(result))
    # for jj in range(0,len(result)):
    #     print(result[jj])
    print(result)
    print(filename)
    fo = open(filename, "w")
    for ind in range(0,len(result)):
        fo.write(str(result[ind])+" ")
    fo.close()
    print("suc=", suc)
    print("End job\n")
def caljob2(num,index,result,suc):
    #global result
    print("caljob2 Thread", num)
    # if num >= 2:
    #     result[index]=True
    #     suc=suc+1
    #     print("suc=", suc)
    # else:
    #     result[index]=False
    aa=obCaljob.cond3(index,num,suc)
    aa.mycondition()
    # print(index)
    # print(aa.Tcase110up)
    # print("End caljob2 Thread")
    result[index]=aa.Tcase110up
    #return index, aa.Tcase110up

def porj(listDtata,jobList):
    threads = []
    #suc=0.0065
    suc=1001
    for i in range(0,len(jobList)):
        task=setTest(jobList[i])
        threads.append(threading.Thread(target = task, args = (listDtata,suc,)))
        test=threads[i].start()
    # for i in range(0,len(jobList)):
    #     threads[i].join()
    print(test)
    #print(threads)

def setTest(num):
    if num==1:
        return job
    elif (num==2):
        return job1
    elif (num==3):
        return job2
def setData(num):
    global jobList
    global listDtata1
    global listDtata2
    global listDtata3
    if num==1:
        porj(listDtata1,jobList)
    elif (num==2):
        porj(listDtata2,jobList)
    elif (num==3):
        porj(listDtata3,jobList)

jobList=[3]
datanum=[2,3]
listDtata1=[1,2,3,4,5,6,7]
listDtata2=[3,4,5,6,7,8]
listDtata3=[1000,1000,1000,1000,1000,1000,1000]
# listDtata=[[1,2,3,4,5,6,7], [3,4,5,6,7,8]]
# print(listDtata[1])
listDtata=[1,2,3,4,5,6,7]

if __name__ == "__main__":
    print("start:")
    #porj(listDtata,jobList)
    #testCase(listDtata,jobList)
    for ii in range(0,len(datanum)):
        filename=str(datanum[ii]) + "job.txt"
        print(filename)
        setData(datanum[ii])
    
    print("Done.")
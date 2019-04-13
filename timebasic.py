import time as t
import random as r
import datetime
import ntplib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import load_iris
from time import ctime

cs = ntplib.NTPClient()
response = cs.request('uk.pool.ntp.org', version=3)
response.offset
print (ctime(response.tx_time))
print (ntplib.ref_id_to_text(response.ref_id))

x = ntplib.NTPClient()
print ((x.request('ch.pool.ntp.org').tx_time))
print("START")
print(datetime.datetime.now())
exit()

# today = datetime.date.today()
# print(type(today))
# print(today)
today=datetime.date(2018,12,28)
sunday = today + datetime.timedelta(6 - today.weekday())
print(sunday)

tr=t.localtime(t.time())
print(tr.tm_wday)

# tube=[]
# for i in range(0,4):
#     tube.append(r.randint(1,100))

list1=[r.randint(1,100) for i in range(1,5+1)]
tube=tuple(list1)
for i in range(0,len(tube)):
    print(tube[i])
    #t.sleep(2)
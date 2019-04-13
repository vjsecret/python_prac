ch=int(raw_input("請輸入月份:"))

if ch>=1 and ch<=3:
    print("%d 月是春天" % ch)
elif ch>=4 and ch<=6:
    print("%d 月是夏天" % ch)
elif ch>=7 and ch<=9:
    print("%d 月是秋天" % ch)
elif ch>=10 and ch<=12:
    print("%d 月是冬天" % ch)
else:
    print("不在範圍內-請重新輸入")
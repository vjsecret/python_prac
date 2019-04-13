num1=raw_input("請輸入第一個數值:")
num2=raw_input("請輸入第二個數值:")

if num1!="" and num2!="":
    if num1.isdigit() and num2.isdigit():
        start=int(raw_input("請選擇(1)加法(2)減法(3)乘法(4)除法:"))
        total=0
        num1=float(num1)
        num2=float(num2)
        
        if (start==1):
            total=num1+num2
            print(total)
        elif start==2:
            total=num1-num2
            print(total)
        elif start==3:
            total=num1*num2
            print(total)
        elif start==4:
            if num2!=0:
                total=num1/num2
                print(total)
            else:
                print("b值不可為零")
    else:
        print("資料內不可為字母")
else:
    print("無完整資料無法運算")

# import re
# 
# num1=float(raw_input("請輸入第一個數值:"))
# num2=float(raw_input("請輸入第二個數值:"))
# 
# if num1!="" and num2!="":
#     if num1.match(float_number) and num2.match(float_number):
#         start=int(raw_input("請選擇(1)加法(2)減法(3)乘法(4)除法:"))
#         total=0
#         
#         if start==1:
#             total=num1+num2
#             print(total)
#         elif start==2:
#             total=num1-num2
#             print(total)
#         elif start==3:
#             total=num1*num2
#             print(total)
#         elif start==4:
#             if num2!=0:
#                 total=num1/num2
#                 print(total)
#             else:
#                 print("b值不可為零")
#     else:
#         print("資料內不可為字母")
# else:
#     print("無完整資料無法運算")
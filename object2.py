# season=raw_input("請選擇(1)春天(2)夏天(3)秋天(4)冬天:")
# str=""
# m=""
# if season!="":
#     if season.isdigit():
#         if (int(season)>=1 and int(season)<=4):
#             if int(season)==1:
#                 m="春天"
#                 str="櫻花"
#             elif int(season)==2:
#                 m="夏天"
#                 str="金針花"
#             elif int(season)==3:
#                 m="秋天"
#                 str="楓葉"
#             elif int(season)==4:
#                 m="冬天"
#                 str="梅花"
#             
#             print("%s---->%s" % (m,str))
#         else:
#             print("只能輸入1~4之間數值")
#     else:
#         print("請輸入數值")
# else:
#     print("無輸入任何資料")

season=int(raw_input("請選擇(1)春天(2)夏天(3)秋天(4)冬天:"))
str=""
m=""
if season!="":
    if season.isdigit():
        if (season>=1 and season<=4):
            if season==1:
                m="春天"
                str="櫻花"
            elif season==2:
                m="夏天"
                str="金針花"
            elif season==3:
                m="秋天"
                str="楓葉"
            elif season==4:
                m="冬天"
                str="梅花"
            
            print("%s---->%s" % (m,str))
        else:
            print("只能輸入1~4之間數值")
    else:
        print("請輸入數值")
else:
    print("無輸入任何資料")
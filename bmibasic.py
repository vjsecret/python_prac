num1=raw_input("請輸入身高(公分):")
num2=raw_input("請輸入體重(公斤):")

if num1!="" and num2!="":
    #if float(num1)>0 and float(num2)>0:
    if num1.isdigit() and num2.isdigit()
        bmi=float(num2)/((float(num1)/100)**2)
        sum=round(bmi,1)
        print(sum)

        print("你的BMI值為%f" % bmi)
        
        if bmi>=35:
            print("重度肥胖")
        elif bmi>=30 and bmi<35:
            print("中度肥胖")
        elif bmi>=27 and bmi<30:
            print("輕度肥胖")
        elif bmi>=24 and bmi<27:
            print("過重")
        elif bmi>=18.5 and bmi<24:
            print("正常範圍")
        else:
            print("體重過輕")
    else:
        print("資料不可為分母")
else:
    print("資料不足無法計算")
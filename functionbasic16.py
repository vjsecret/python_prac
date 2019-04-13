import calendar as c
def input():
    calendar=calendar.calendar(year, w=2, l=1, c=6, m=3)
    print(calendar)

    num1=raw_input("請輸入一個月費用:")
    num2=raw_input("請輸入年份:")
    num3=raw_input("請輸入月份:")
    tube=c.monthrange(int(num2),int(num3))
    avg,od=calcu(tube,num1)
    display(avg)
    
    #date,od=calcu(int(num1),350)
    #display(date,od)

def calcu(tube,num):
    avg,od=divmod(int(num),tube[1])
    return (avg,od)

def display(num):
    print("一天花費={0}".format(num))

# def calcu(num1,num2):
#     date,od=divmod(num1,num2)
#     return (date,od)
# 
# def display(date,od):
#     print("可維持%d天,剩餘%d" % (date,od))

if __name__ == "__main__":
    input()
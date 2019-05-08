import classbasic0104_3 as obj


class test1:
    def add1(self,x,y):
        sum=x+y;
        return sum
    
if test1.__module__== "__main__":
    tpfun=test1()
    total=tpfun.add1(4,5)
    print(total)
    mylist=[1,2,3,4,5]
    calc=obj.test3(mylist)
    calc.setAdd()
    print(calc._test3__list)
    print(calc.getAdd())
import classa as com

if __name__=="__main__":
    mylist=[1,2,3,4,5]
    calc=com.test3(mylist)
    calc._test3__list[2]=6
    print(calc._test3__list[2])
    calc.setAdd()
    print(calc._test3__list)
    print(calc.getAdd())
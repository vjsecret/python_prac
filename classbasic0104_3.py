class test3:
    def __init__(self,list):
        self.__list=list
        self.__totallist=0
    def setAdd(self):
        self.__totallist=sum(self.__list)
    def getAdd(self):
        return self.__totallist

if test3.__module__=="__main__":
    mylist=[1,2,3,4,5]
    calc=test3(mylist)
    calc.setAdd()
    print(calc._test3__list)
    print(calc.getAdd())
# testlist = [test1,test3] #key
# #value = []
# #=>inputlist={test1:5,test3:3} 
# class unitTest:
#     def __init__(self):
#         print("init unitTest")
#     #private value = "     Awoo~", // 輸入值
#     def setValue(self, value):
#         self.value = value
#     #virtual expected // 預期得到的結果
#     def setExpected(self, expected):
#         self.expected = expected()
#     #obj TestCase: method
#     #obj virtual func(expected, trim(value)); // 經過 trim 後兩者必須相同
#     #obj result = areEqual(input,expected)
#
# class testfunc(unitTest.TestCase):
#     def __init__(self):
#         print("init testfunc")
#     self.value = self.setValue() #var value = "     Awoo~", // 輸入值
#     self.expected = self.setExpected();  # 預期得到的結果 
#     #result = unitTest.func(expected, trim(value)); // 經過 trim 後兩者必須相同 
#     #return result

def expected(func):
    var = func();
    return value

def areEqual(input,expected):
    if input == expected:
        return True
    else:
        return False

class TestMo:
    def __init__(self, index, start, targetVar):
        self.start = start
        # self.max = max
        self.index = index
        self.targetVar = targetVar
        self.Tcase110up=0
        self.Tcase110ups=0
        self.Tcase110upf=0
        self.Tcase110=0
    def mycondition(self):  
    #def mycondition(self, self.__index, self.__start, self.__targetVar):
        print("mycondition")
        print(self.index)
        print(self.start)
        print(self.targetVar)
    def myconditionSub1(self):  
    #def myconditionSub1(self, self.__index, self.__start, self.__targetVar):
        print("myconditionSub1")
        print(self.index)
        print(self.start)
        print(self.targetVar)
    def myconditionSub2(self):  
    #def myconditionSub2(self, self.__index, self.__start, self.__targetVar):   
        print("myconditionSub2")
        print(self.index)
        print(self.start)
        print(self.targetVar)

class cond1(TestMo):
    # def __init__(self,index,start,max,min,end,cal_rocday,targetVar):
    def __init__(self, index, start, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        # self.Tcase110up=Tcase110up00[0]
        # self.Tcase110ups=Tcase110up00[1]
        # self.Tcase110upf=Tcase110up00[2]
        # self.Tcase110=Tcase110up00[3]
    def mycondition(self):
    #def mycondition(self, self.index, self.start, self.targetVar):  
        print("cond1 mycondition")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        # if num >= 2:
        #     result[index]=True
        #     suc=suc+1
        #     print("suc=", suc)
        # else:
        #     result[index]=False
        if self.start >= 3:
            self.Tcase110up=True
            # suc=suc+1
            # print("suc=", suc)
        else:
            self.Tcase110up=False
    def myconditionSub1(self):
    #def myconditionSub1(self, self.index, self.start, self.targetVar):
        print("cond1 myconditionSub1")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        if self.Tcase110up:
            self.Tcase110up=True
            self.Tcase110=True
            self.Tcase110upf=False
        else:
            self.Tcase110upf=True
    def myconditionSub2(self):
    #def myconditionSub2(self, self.index, self.start, self.targetVar):
        print("cond1 myconditionSub2")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        if self.Tcase110up:
            self.Tcase110=True

class cond2(TestMo):
    def __init__(self, index, start, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
    def mycondition(self):
    #def mycondition(self,self.__start,index,Sarray):
        print("cond2 mycondition")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        if self.start >= 2:
            self.Tcase110up=True
            # suc=suc+1
            # print("suc=", suc)
        else:
            self.Tcase110up=False
    def myconditionSub1(self):
    #def myconditionSub1(self,self.__start,index,Sarray):
        print("cond2 myconditionSub1")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
    def myconditionSub2(self):
    #def myconditionSub2(self,self.__start,index,Sarray):
        print("cond2 myconditionSub2")

class cond3(TestMo):
    def __init__(self, index, start, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
    def mycondition(self):
    #def mycondition(self,self.__start,index,Sarray):
        print("cond3 mycondition")
        print(self.Tcase110up)
        print(self.targetVar)
        self.start=self.start+1
        if self.start == self.targetVar:
            self.Tcase110up=True
            # suc=suc+1
            # print("suc=", suc)
        else:
            self.Tcase110up=False

class Testd:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

if __name__ == '__main__':
    # test = Testd('hello')
    # test._Testd__bar()
    # print(test._Testd__foo)
    aa=cond1(2,50,100)
    aa.mycondition()
    aa.myconditionSub1()
    print(aa.Tcase110up)
    print("--------------------------------end Test1")
    bb=cond2(2,1,100)
    bb.mycondition()
    bb.myconditionSub1()
    print(aa.Tcase110up)
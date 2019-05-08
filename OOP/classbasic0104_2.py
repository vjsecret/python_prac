class test2:
    def __init__(self,a,b):
        self.aaa=a
        self.bbb=b
    
    def setAdd(self):
        self.total=self.aaa+self.bbb
    def getAdd(self):
        return self.total

if test2.__module__== "__main__":
    #x=int(input("請輸入值一:"))
    #y=int(input("請輸入值二:"))
    x=1
    y=2
    kcom1=test2(x,y)
    kcom1.aaa=5
    kcom1.bbb=6
    print(kcom1.aaa)
    print(kcom1.bbb)
    kcom1.setAdd()
    print(kcom1.getAdd())
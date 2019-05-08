class test3:
    def __init__(self,list):
        self.__list=list
        self.__totallist=0
    def setAdd(self):
        self.__totallist=sum(self.__list)
    def getAdd(self):
        return self.__totallist
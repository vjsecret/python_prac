class maxcomponet1:
    def __init__(self,mylist1):
        self.__mylist=mylist1
        self.__max=0;
    def setMax(self):
        self.__max=max(self.__mylist)
    def getMax(self):
        return self.__max
class test:
    def __new__(Kind,name):
        if name!='':
            print("物件已建立")
            return object.__new__(Kind)
        else:
            print("物件未建立")
            return None

    def __init__(self,name):
        print(name)
        
dd=test("")
print(test.__module__)
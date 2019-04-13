class Human(object):
    # def __init__(self,h=0,w=0):
    #     self.height=h
    #     self.weight=w
    # def BMI(self):
    #     return self.weight / ((self.height/100)**2)
    # def __add__(self,other):
    #     return self.height + other.height
    # def __iadd__(self,other):
    #     self.height += other.height
    #     self.weight += other.weight
    #     return self
    def __init__(self,h=0,w=0):
        self._height=h
        self._weight=w
    def _BMI(self):
        return self._weight / ((self._height/100)**2)

class Bird:
    def __init__(self):
        print("init") #先執行new 再執行init
    def fly(self):
        print("fly")
    def __new__(self):
        print("new")
        return object.__new__(self) #如果沒有return，這個物件並沒有建立成功
b=Bird()
b.fly()

class FirstClass:
    """My first class in python."""
    str1 = "Apple"
    str2 = "IBM"
    def __init__(self, str1="參數1", str2="參數2"):
        self.str1 = str1
        self.str2 = str2
 
    def fun(self):
        return "Hello world."
 
my_obj = FirstClass()
print(my_obj.str1)
print(my_obj.str2)
print("===分隔線===")
my_obj2 = FirstClass("我是參數1")
print(my_obj2.str1)
print(my_obj2.str2)
print("===分隔線===")
my_obj3 = FirstClass("我是參數1", "我是參數2")
print(my_obj3.str1)
print(my_obj3.str2)

class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        if self.prog_name == '__main__.py':
            self.prog_name = 'python -m django'
        self.settings_exception = None
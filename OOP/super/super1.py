class A:
    def __init__(self, index):
        print("Enter A")
        self.index = index
        self.Tcase110up=0
        self.Tcase110ups=0
        self.Tcase110upf=0
        self.Tcase110=0
        print("Leave A")

class B(A):
    def __init__(self, index):
        print("Enter B")
        A.__init__(self, index)
        print(self.index)
        print(self.Tcase110up)
        self.Tcase110up=1
        print(self.Tcase110up)
        print("Leave B")

class C(A):
    def __init__(self, index):
        print("Enter C")
        A.__init__(self, index)
        print(self.index)
        print(self.Tcase110up)
        self.Tcase110up=2
        print(self.Tcase110up)
        print("Leave C")

class D(A):
    def __init__(self, index):
        print("Enter D")
        A.__init__(self, index)
        print(self.index)
        print(self.Tcase110up)
        self.Tcase110up=3
        print(self.Tcase110up)
        print("Leave D")

class E(B, C, D):
    def __init__(self):
        print("Enter E")
        B.__init__(self, 10)
        C.__init__(self, 3)
        D.__init__(self, 5)
        print("Leave E")
#----------------------------------------------------------------------------------------------------
# class A:
#     def __init__(self):
#         print("Enter A")
#         print("Leave A")
# 
# class B(A):
#     def __init__(self):
#         print("Enter B")
#         A.__init__(self)
#         print("Leave B")
# 
# class C(A):
#     def __init__(self):
#         print("Enter C")
#         A.__init__(self)
#         print("Leave C")
# 
# class D(A):
#     def __init__(self):
#         print("Enter D")
#         A.__init__(self)
#         print("Leave D")
# 
# class E(B, C, D):
#     def __init__(self):
#         print("Enter E")
#         B.__init__(self)
#         C.__init__(self)
#         D.__init__(self)
#         print("Leave E")
#----------------------------------------------------------------------------------------------------
# class A(object):
#     def __init__(self):
#         print("Enter A")
#         print("Leave A")
# 
# class B(A):
#     def __init__(self):
#         print("Enter B")
#         super(B, self).__init__()
#         print("Leave B")
# 
# class C(A):
#     def __init__(self):
#         print("Enter C")
#         super(C, self).__init__()
#         print("Leave C")
# 
# class D(A):
#     def __init__(self):
#         print("Enter D")
#         super(D, self).__init__()
#         print("Leave D")
# 
# class E(B, C, D):
#     def __init__(self):
#         print("Enter E")
#         super(E, self).__init__()
#         print("Leave E")

if __name__ == '__main__':
    E()
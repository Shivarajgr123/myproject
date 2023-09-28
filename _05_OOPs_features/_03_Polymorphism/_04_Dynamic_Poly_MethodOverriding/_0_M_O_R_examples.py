class A:
    def m1(self):
        print("In A : m1() ")

class B(A):
    def m2(self):
        print("In B :m2()")

a = A()
a.m1()
print("-----------")
b = B()
b.m1()
b.m2()
#b.m3()




# super class frameworks flask/djagno

# METHOD OVERRIDING : DYNAMIC POLYMORPHISM
class A:
    def m1(self):
        print("In A : m1() ")
class B(A):
    def m2(self):
        print("In B :m2()")   # 2

    #method overriding
    def m1(self):
        print("In B :m1()")   # 1.2

b = B()
b.m1()  # Python don't know at compilation time which m1() is being called
b.m2()
#b1.m3()

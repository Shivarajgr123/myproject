class A:
    def __init__(self, yy, zz):
        self.yy = yy
        self.zz = zz
        print("A init", self.yy, self.zz)

class B(A):
    def __init__(self, x, y, z):
        self.x = x
        super(B, self).__init__(y, z)  # it can be anywher
        print("B init", self.x)

b = B(10,20,30)

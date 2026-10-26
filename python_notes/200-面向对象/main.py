class A(object):
    var1 = 100
    var2 = 3.14
    var3 = 'hello world'

    @classmethod
    def fun1(cls, agrs):
        print("fun1 %s" % agrs)
        print("var1 % s" % cls.var1)
        cls.var1 = input("修改var1: \n")
        print("var1 % s" % cls.var1)


    def fun2(self, agrs):
        print("fun1 %s" % agrs)
        print("var1 % s" % self.var1)
        self.var1 = input("修改var1: \n")
        print("var1 % s" % self.var1)

# print(A.var1)
# print(A.fun1('aaa'))

a = A()

# a.fun2(23)
#
# print(A.var1)

A.var1 = 0

print(a.var1)



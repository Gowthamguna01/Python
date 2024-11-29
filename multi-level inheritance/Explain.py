class Grandparent:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        self.c=self.a+self.b
        print("addition=",self.c)


class Parent(Grandparent):
    def __init__(self,a,b,o):#
        self.o=o
        Grandparent. __init__(self,a,b) #brow


    def sub(self):
        self.c=self.a+self.b-self.o
        print("substraction",self.c)


class Child(Parent):
    def __init__(self,a,b,o,d):
        Parent.__init__(self,a,b,o)
        self.d=d

    def multi(self):
        self.c=self.a*self.b+self.o*self.d
        print("multiplication", self.c)



a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
d=int(input("enter d="))

o=Child(a,b,c,d)
o.add()
o.sub()
o.multi()

class Arithmatic():#father
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def addition(self):
        self.c=self.a+self.b
        print("addition",self.c)


class Parent(Arithmatic):#mother

    def __init__(self,a,b):
        Arithmatic.__init__(self,a,b)

    def substraction(self):
        self.c=self.a-self.b
        print("substraction",self.c)

    def multiplication(self):
        self.c=self.a*self.b
        print("multiplication",self.c)

    def division(self):
        self.c=self.a/self.b
        print("division=",self.c)


class Child(Parent,Arithmatic):

    def __init__(self,a,b):
        Parent.__init__(self,a,b)
        Arithmatic.__init__(self,a,b)


    def modulus(self):
        self.c=self.a%self.b
        print("modulus=",self.c)



a=int(input("enter a="))
b=int(input("enter b="))

m=Child(a,b)
m.modulus()
m.addition()
m.substraction()
m.multiplication()
m.division()

        

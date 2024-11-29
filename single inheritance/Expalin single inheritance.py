class Parent:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def sub(self):
        self.c=self.a+self.b
        print("subtraction=",self.c)

class Child(Parent):
    def __init__(self,a,b):
        Parent.__init__(self,a,b)
    

    def add(self):
        self.c=self.a+self.b
        print("Add=",self.c)


a=int(input("enter a="))
b=int(input("enter b="))

o=Child(a,b)
o.add()
o.sub()


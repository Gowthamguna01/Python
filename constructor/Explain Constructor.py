class Formula:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def addition(self):
        self.c=self.a+self.b
        print(self.c)

    def sub(self):
        self.c=self.a-self.b
        print(self.c)

a=int(input("enter a"))
b=int(input("enter b"))

x=Formula(a,b)
x.addition()
x.sub()

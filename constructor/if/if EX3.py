class Formula:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def small(self):
        if(self.a<self.b):
            print("A is small")
        if(self.b<self.a):
            print("B is small")


a=int(input("Enter a="))
b=int(input("ENTER b="))

x=Formula(a,b)
x.small()

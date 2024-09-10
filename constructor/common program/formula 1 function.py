import math
class Formula:
    def __init__(self,a,s,b,c):
        self.a=a
        self.s=s
        self.b=b
        self.c=c
    
    def areaoftriangle(self):
        self.v=math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        print(self.v)

a=int(input("Enter a="))
s=int(input("Enter s="))
b=int(input("Enter b="))
c=int(input("Enter c="))

x=Formula(a,s,b,c)
x.areaoftriangle()

import math
class Formula:
    def area_of_triangle(self,a,s,b,c):
        self.a=a
        self.s=s
        self.b=b
        self.c=c
        self.A=math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        return(self.A)


a=int(input("Enter a="))
s=int(input("Enter s="))
b=int(input("Enter b="))
c=int(input("Enter c="))

x=Formula()
v=x.area_of_triangle(a,s,b,c)
print(v)

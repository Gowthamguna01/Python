import math
class Formula:
    def equilateral(self,a):
        self.a=a
        self.b=math.pow(self.a,2)
        self.c=self.b/4
        self.A=math.sqrt(3)*self.c
        return(self.A)

a=int(input("Enter a="))

x=Formula()
v=x.equilateral(a)
print(v)    

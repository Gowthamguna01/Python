import math
class Formula:
    def area_cylinder(self,h,R,r):
        self.h=h
        self.R=R
        self.r=r
        self.u=math.pow(self.R,2)
        self.i=math.pow(self.r,2)
        self.P=2*math.pi*self.r*self.h*(self.u-self.i)
        return(self.P)

h=int(input("enter h="))
R=int(input("enter R="))
r=int(input("enter r="))

x=Formula()
v=x.area_cylinder(h,R,r)
print(v)

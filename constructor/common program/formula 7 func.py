import math
class Formula:
    def __init__(self,h,R,r):
        self.h=h
        self.R=R
        self.r=r
        
    def area_cylinder(self):
        
        self.u=math.pow(self.R,2)
        self.i=math.pow(self.r,2)
        self.P=2*math.pi*self.r*self.h*(self.u-self.i)
        print(self.P)


h=int(input("enter h="))
R=int(input("enter R="))
r=int(input("enter r="))

x=Formula(h,R,r)        
x.area_cylinder()

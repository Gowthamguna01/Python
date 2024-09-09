import math
def area_cylinder(h,R,r):
    
    u=math.pow(R,2)
    i=math.pow(r,2)
    P=2*math.pi*r*h*(u-i)
    print(P)


h=int(input("enter h="))
R=int(input("enter R="))
r=int(input("enter r="))
area_cylinder(h,R,r)

import math
def area_cylinder(h,r,R):
    u=math.pow(R,2)
    i=math.pow(r,2)
    P=2*math.pi*r*h*(u-i)
    return(P)

h=int(input("enter h="))
R=int(input("enter R="))
r=int(input("enter r="))
z=area_cylinder(h,R,r)
print(z)

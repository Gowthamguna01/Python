import math
def area_of_triangle(a,s,b,c):
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return(A)


a=int(input("Enter a="))
s=int(input("Enter s="))
b=int(input("Enter b="))
c=int(input("Enter c="))
z=area_of_triangle(a,s,b,c)
print(z)

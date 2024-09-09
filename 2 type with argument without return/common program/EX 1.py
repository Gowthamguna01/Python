import math
def area_of_triangle(a,b,s,c):
    b=(s-a)*(s-b)*(s-c)
    A=math.sqrt(s)*b
    print(A)
    

a=int(input("Enter a="))
s=int(input("Enter s="))
b=int(input("Enter b="))
c=int(input("Enter c="))
area_of_triangle(a,s,b,c)


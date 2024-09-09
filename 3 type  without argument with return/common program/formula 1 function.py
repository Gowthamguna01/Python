import math
def area_of_triangle():
    a=int(input("Enter a="))
    s=int(input("Enter s="))
    b=int(input("Enter b="))
    c=int(input("Enter c="))
    v=(s-a)*(s-b)*(s-c)
    A=math.sqrt(s)*v
    return(A)


x=area_of_triangle()
print("addition", x)

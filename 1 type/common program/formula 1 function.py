import math
def area_of_triangle():
    a=int(input("Enter a="))
    s=int(input("Enter s="))
    b=int(input("Enter b="))
    c=int(input("Enter c="))
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)
area_of_triangle()

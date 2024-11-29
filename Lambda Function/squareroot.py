import math

s=int(input("Enter s value="))
a=int(input("Enter a value="))
b=int(input("Enter b value="))
c=int(input("Enter c value="))

Area=lambda s,a,b,c: math.sqrt(s*(s-a)*(s-b)*(s-c))
print(Area(s,a,b,c))

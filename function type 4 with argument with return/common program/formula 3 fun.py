import math
def equilateral(a):
    b=math.pow(a,2)
    c=b/4
    A=math.sqrt(3)*c
    return(A)

a=int(input("Enter a="))
z=equilateral(a)
print(z)    

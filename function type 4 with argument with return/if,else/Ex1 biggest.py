def biggest(a,b,c):
    
    if(a>b and a>c):
        return("A is big")
    elif(b>a and b>c):
        return("B is big")
    elif(c>a and c>b):
        return("c is big")


a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
z=biggest(a,b,c)
print(z)       

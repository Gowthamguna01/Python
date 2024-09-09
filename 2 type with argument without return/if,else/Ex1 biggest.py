def biggest(a,b,c):
    if(a>b and a>c):
        print("A is big")
    elif(b>a and b>c):
        print("B is big")
    elif(c>a and c>b):
        print("c is big")


a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
biggest(a,b,c)
        

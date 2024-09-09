def oddeven(n):
    if(n%2==0):
        return("Even number")
    if(n%2==1):
        return("Odd number")

n=int(input("enter n="))
z=oddeven(n)
print(z)

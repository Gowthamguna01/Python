def natural(n):
    b=0
    for i in range(1,n+1,1):
        b=b+i
        i=i+1
    return(b)

n=int(input("Enter number"))
x=natural(n)
print(x)        

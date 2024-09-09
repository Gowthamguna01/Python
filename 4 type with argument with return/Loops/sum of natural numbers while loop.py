def natural(n):
    i=1
    b=0
    while(i<=n):
        b=b+i
        i=i+1
    return(b)

n=int(input("Enter number"))
x=natural(n)
print(x)        

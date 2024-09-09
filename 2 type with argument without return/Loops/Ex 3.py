def factorial(n):
    
    i=1
    j=1
    while(i<=n):
        j=j*i
        print(j)
        i=i+1

n=int(input("enter n number="))
factorial(n)

n=int(input("enter n number="))
i=1
while(i<=n):
    print("*",end="")
    j=i
    while(j<=n):
        if(j==5):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
    print()
        

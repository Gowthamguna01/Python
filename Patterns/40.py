a=int(input("enter a number="))
i=1
while(i<=a):
    j=1
    while(j<=i):
        if(i==3 or j==2):
            print(" ",end="")
        else:
            print(j,end="")
        j=j+1
    i=i+1
    print()

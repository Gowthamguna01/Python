a=int(input("enter a num="))
i=1
while(i<=a):
    j=1
    while(j<=i):
        print(j,end="")
        j=j+1 
    j=i-1
    while(j>=1):
        print(j,end="")
        j=j-1
    i=i+1
    print()

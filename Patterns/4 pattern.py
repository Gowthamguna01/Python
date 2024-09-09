n=int(input("enter a num="))
i=n
while(i>=1):
    j=n
    while(j>=i):
        print(j,end="")
        j=j-1
    i=i-1
    print()

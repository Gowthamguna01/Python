n=str(input("enter n alphabets="))
b=len(n)-1
i=0
while(i<=b):
    j=0
    while(j<=i):
        print(n[i],end="")
        j=j+1
    i=i+1
    print()

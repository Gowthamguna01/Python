a=int(input("enter a  number="))
i=1
while(i<=a):
    k=1
    while(k<=a-i):
        print(" ",end="")
        k=k+1
    j=1
    while(j<=i):
        print(j,end="")
        j=j+1
    i=i+1
    print()

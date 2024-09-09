a=int(input("enter a num="))
i=1
m=1
while(i<=a):
    k=a-i
    while(k>=1):
        print(" ",end="")
        k=k-1
    j=1
    while(j<=m):
        print(j,end="")
        j=j+1
    i=i+1
    m=m+2
    print()

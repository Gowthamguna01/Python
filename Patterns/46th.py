a=int(input("enter a num="))
c=a-1
while(c>=1):
    k=a-c
    while(k>=1):
        print(" ",end="")
        k=k-1
    s=1
    while(s<=c):
        print(s,end="")
        s=s+1
    d=c-1
    while(d>=1):
        print(d,end="")
        d=d-1
    c=c-1
    print()

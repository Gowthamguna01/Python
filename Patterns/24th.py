a=int(input("enter a num="))
c=a
q=1
n=a+3
while(q<=n):
    print("*",end="")
    q=q+1
print()
    
while(c>=1):
    k=a-c
    while(k>=1):
        print(" ",end="")
        k=k-1
    s=1
    while(s<=c):
        if(s==1):
            print("*",end="")
        else:
            print(" ",end="")
        s=s+1
    d=c-1
    while(d>=1):
        if(d==1):
            print("*",end="")
        else:
            print(" ",end="")
        d=d-1
    c=c-1
    print()

a=int(input("enter a number="))
c=a-1
for g in range(1,a+1+4,1):
    print("*",end="")
print()
for c in range(c,0,-1):
    k=a-c
    for k in range(k,0,-1):
        print(" ",end="")
    s=1
    for s in range(s,c+1,1):
        if(s==1):
            print("*",end="")
        else:
            print(" ",end="")
    d=c-1
    for d in range(d,0,-1):
        if(d==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
        

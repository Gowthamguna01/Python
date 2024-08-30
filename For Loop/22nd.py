a=int(input("enter a number="))
g=1
for i in range(1,a+1):
    k=a-g
    for k in range(k,0,-1):
        print(" ",end="")
    j=1
    for j in range(1,g,1):
        if(j==1):
            print("*",end="")
        else:
            print(" ",end="")
    if(g==1):
        print("*",end="")
    else:
        print(" ",end="")
    v=g-1
    for v in range(v,0,-1):
        if(v==1):
            print("*",end="")
        else:
            print(" ",end="")
    g=g+1
    print()
c=a-1
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
        
        
        
        

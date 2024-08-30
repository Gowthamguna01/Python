a=str(input("enter a value="))
b=len(a)-1
g=0
for i in range(0,b+1):
    k=b-1
    for k in range(k,0,-1):
        print(" ",end="")
    for j in range(0,g+1):
        if(j==0):
            print(a[j],end="")
        else:
            print(" ",end="")
    if(g==0):
        print(a[g],end="")
    else:
        print(" ",end="")
    v=g-1
    for  v in range(v,0,-1):
        if(v==0):
            print(a[v],end="")
        else:
            print(" ",end="")
    g=g+1
    print()
c=b-1
for c in range(c,0,-1):
    k=b-c
    for k in range(k,0,-1):
        print(" ",end="")
    s=0
    for s in range(0,c,1):
        if(s==0):
            print(a[s],end="")
        else:
            print(" ",end="")
    d=c-1
    for d in range(d,0,-1):
        if(d==0):
            print(a[d],end="")
        else:
            print(" ",end="")
    print()

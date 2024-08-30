a=int(input("enter a number="))
g=1
for g in range(1,a+1):
    k=a-g
    for k in range(k,0,-1):
        print(" ",end="")
    j=1
    for j  in range(1,g,1):
        print(j,end="")
    print(g,end="")
    v=g-1
    for v in range(v,0,-1):
        print(v,end="")
    g=g+1
    print()
c=a-1
for c in range(c,0,-1):
    k=a-c
    for k in range(k,0,-1):
        print(" ",end="")
    s=1
    for s in range(1,c+1):
        print(s,end="")
        s=s+1
    d=c-1
    for d in range(d,0,-1):
        print(d,end="")
    c=c-1
    print()
        
        
        

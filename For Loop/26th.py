a=int(input("enter a number="))
n=a+3
c=a
for q in range(1,n+1+1,1):
    print("*",end="")
print()

for c in range(a,0,-1):
    k=a-c
    for k in range(k,0,-1):
        print(" ",end="")
    s=1
    for s in range(1,c,1):
        if(s==1):
            print("*",end="")
        else:
            print(" ",end="")
    d=c-1
    for d in range(d+1,0,-1):
        if(d==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

g=1
for g in range(1,a+1,1):
    k=a-g-1
    for k  in range(k+1,0,-1):
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
q=1
y=a+4
for q in range(1,y+1,1):
    print("*",end="")
    
            

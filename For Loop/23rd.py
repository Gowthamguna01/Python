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
for g in range(1,a+1+4,1):
    print("*",end="")
print()

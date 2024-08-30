a=int(input("enter a number="))
g=1
for g in range(1,a+1):
    k=a-g
    for k in range(k,0,-1):
        print(" ",end="")
    for j  in range(1,g,1):
        print(j,end="")
    print(g,end="")
    v=g-1
    for v  in range(v,0,-1):
        print(v,end="")
    g=g+1
    print()
c=a-1
        

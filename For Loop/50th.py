a=int(input("enter a number="))
c=a-1
for c in range(c,0):
    k=a-c
    for k  in range(k,0,-1):
        print(" ",end="")
    s=1
    for s in range(1,c+1,1):
        print("*",end="")
    d=c-1
    for d in range(d,0,-1):
        print("*",end="")
    c=c-1
    print()
        
        

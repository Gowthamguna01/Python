a=int(input("enter a number="))
c=a-1
for c in range(c+1,0,-1):
    k=a-c
    for k in range(k+1,0,-1):
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
        

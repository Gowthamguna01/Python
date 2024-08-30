a=int(input("enter a number="))
i=a
for i in range(a,0):
    if(i>0):
        print("1",end="")
    j=i
    b=1
    for j in range(i,a+1,1):
        if(j==4):
            v=b+1
            print(v,end="")
        else:
            print(" ",end="")
        b=b+1
    i=i-1
    print()
s=1
for s in range(1,a+1,1):
    print(s,end="")
print()
        

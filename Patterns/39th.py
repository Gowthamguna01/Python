a=int(input("enter a number="))
i=a
while(i>1):
    if(i>0):
        print("1",end="")
    j=i
    b=1
    while(j<a):
        if(j==4):
            v=b+1
            print(v,end="")
        else:
            print(" ",end="")
        j=j+1
        b=b+1
    i=i-1
    print()
s=1
while(s<=a):
    print(s,end="")
    s=s+1
print()

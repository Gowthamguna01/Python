a=int(input("enter a number="))
i=1
b=a*2-2
for i in range(1,a+1):
    for k in range(1,b+1,1):
        print("*",end="")
    j=1
    for j in range(1,i+1,1):
        if(j<i):
            print(i,end="*")
        else:
            print(i,end="")
    g=1
    for g in range(1,b+1,1):
        print("*",end="")
    i=i+1
    b=b-1
    print()
        

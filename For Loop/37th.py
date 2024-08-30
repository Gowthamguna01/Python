a=int(input("enter a number="))
for i in range(1,a+1,1):
    for j in range(1,i+1,1):
        if(j==1 or j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
g=1
for g in range(1,a+1+1,1):
    print("*",end="")
    

a=int(input("enter a number="))
for i in range(1,a,1):
    for j in range(0,a,1):
        if(i==0 or i==a-1 or i==1 or j==0 or j==a-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

a=int(input("enter a number="))
for i in range(1,a+1):
    for j in range(1,i+1,1):
        if(i==3 or j==2):
            print(" ",end="")
        else:
            print(j,end="")
    i=i+1
    print()

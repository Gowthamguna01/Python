a=int(input("enter a number="))
for i in range(a,0,-1):
    for j in range(i,a+1,1):
        print(j,end="")
    print()

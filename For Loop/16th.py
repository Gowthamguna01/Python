a=int(input("enter a number="))
for i in range(a+1,0,-1):
    for j in range(a,a+1-i,-1):
        print(j,end="")
    print()

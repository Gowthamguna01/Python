a=int(input("enter a number="))
for i in range(1,a+1):
    for j in range(a+1,i+1,-1):
        print(j,end="")
    i=i+1
    print()

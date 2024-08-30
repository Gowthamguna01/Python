n=int(input("enter a number="))
h=0
for i in range(1,n,1):
    for j in range(1,i+1,1):
        h=h+1
        print(h,end="")
    print()

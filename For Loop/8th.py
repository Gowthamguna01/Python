n=int(input("enter a number="))
i=1
for i in range(1,n+1,1):
    h=1
    for j in range(1,n+1+1,1):
        print(h%2,end="")
        h=h+1
    print()
        

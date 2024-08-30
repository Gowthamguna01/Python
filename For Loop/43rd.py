a=int(input("enter a number="))
for i in range(1,a+1):
    for j in range(1,i+1,1):
        print(j,end="")
    j=i-1
    for j in range(j,0,-1):
        print(j,end="")
    i=i+1
    print()
        
        

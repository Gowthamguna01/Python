a=int(input("enter a number="))
for i in range(1,a+1,1):
    for j in range(a-i,0,-1):
        print(" ",end="")
    for m in range(i,0,-1):
        print(m,end="")
    print()
    

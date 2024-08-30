a=int(input("enter a number="))
i=a
g=1
for g in range(1,a+2,1):
    print("*",end="")
print()

for i in range(a,0,-1):
    j=i
    for j in range(j,1,-1):
        if(j==i):
            print("*",end="")
        else:
            print(" ",end="")
    i=i-1
    print("*",end="")
    print()
    


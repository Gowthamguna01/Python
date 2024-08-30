a=str(input("enter a value="))
b=len(a)-1
for i in range(0,b+1,1):
    for j in range(0,i+1,1):
        print(a[j],end="")
    j=i-1
    for j in range(j+1,0,-1):
        print(a[j-1],end="")
    print()

a=str(input("enter a number="))
b=len(a)-1
for i in range(0,b+1):
    for j in range(0,i+1,1):
        print(a[j],end="")
    i=i+1
    print()

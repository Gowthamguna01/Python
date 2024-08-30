n=str(input("enter n number="))
b=len(n)-1
for i in range(b+1):
    for j in range(b+1-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(n[j],end=" ")
    print()

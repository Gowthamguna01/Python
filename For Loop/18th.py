n=int(input("enter a number="))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")#only space
    for j in range(i+1):
        print("*",end="")
    print()

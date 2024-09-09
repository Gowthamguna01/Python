a=int(input("enter a number="))
i=1
h=1
while(i<=a):
    j=1
    while(j<=a+1):
        print(h%2,end="")
        j=j+1
        h=h+1
    i=i+1
    print()

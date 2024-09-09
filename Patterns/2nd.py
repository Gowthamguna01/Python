a=int(input("enter a number="))
i=1
while(i<=a):
    j=a-i
    while(j>=1):
        print(" ",end="")
        j=j-1
    j=i
    while(j>=1):
        print(j,end="")
        j=j-1
    i=i+1
    print()
    

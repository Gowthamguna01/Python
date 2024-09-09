a=int(input("enter a number="))
i=a
while(i>=1):
    print("*",end="")
    j=i
    while(j<a):
        if(j==4):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i-1
    print()
s=1
while(s<=a+1):
    print("*",end="")
    s=s+1
print()

a=int(input("enter a number="))
i=a
g=1
while(g<=a):
    print("*",end="")
    g=g+1
print()

while(i>=1):
    j=i
    while(j>1):
        if(j==i):
            print("*",end="")
        else:
            print(" ",end="")
        j=j-1
    print("*")
    i=i-1


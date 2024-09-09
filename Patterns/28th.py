a=int(input("enter a number="))
i=0
while(i<a):
    j=0
    while(j<a):
        if(i==0 or i==a-1 or j==0 or j==a-1):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
    print()

    
    
    

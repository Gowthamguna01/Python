a=int(input("enter a number="))
i=0
while(i<=a):
    j=0
    while(j<=i):#first_increment
        if(j==0):
            print("*",end="")
        else:
            print(j,end="")
        j=j+1
    j=i-1
    while(j>=0):#lastu0
        if(j==0):
            print("*",end="")
        else:
            print(j,end="")
        j=j-1
    i=i+1
    print()
n=a-1
g=n
while(g>=0):
    h=0
    while(h<g):
        if(h==0):
            print("*",end="")
        else:
            print(h,end="")
        h=h+1
    f=g
    while(f>=0):
        if(h==0 or f==0):
            print("*",end="")
        else:
            print(f,end="")
        f=f-1
    g=g-1
    print()



    
    
    

    

    
    


           

        
        

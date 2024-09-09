a=int(input("enter a number="))
i=1
b=a*2-2
while(i<=a):#1st column
    k=1
    while(k<=b):#front star increment
        print("*",end="")
        k=k+1
   
    j=1
    while(j<=i): #numbers1 22 333
        if(j<i):
            print(i,end="*")
        else:
            print(i,end="")
        
        j=j+1
        
    g=1#last star increment
    while(g<=b):
        print("*",end="")
        g=g+1
    i=i+1
    b=b-1
    print()
        
    
   
        
        
    
        
        
    
    
        
    
    

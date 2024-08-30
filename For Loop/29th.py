a=str(input("enter a value="))
b=len(a)-1
for i in range(0,b+1):
    for j in range(0,b+1,1):
        print(a[j],end="")
    b=b-1
    print()
        
    

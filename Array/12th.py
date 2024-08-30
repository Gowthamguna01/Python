a=int(input("enter number="))
n=[]
for i in range(a):
    b=int(input("value="))
    n.append(b)
print()

p=len(n)
for i in range(0,p):
    for j in range(i+1,p):
        print(i)
        if(n[i]<n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)

    
    
    
            

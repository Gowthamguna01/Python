a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

p=len(n)#bcoz last to first
for i  in range(0,p):#last to first
    for j in range(i+1,p):#first to last
        if(n[i]==0):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)
        
for i  in range(0,p):#last to first
    for j in range(i+1,p):#first to last
        if(n[j]==1):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)
            
            

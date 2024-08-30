a=int(input("enter number="))
n=[]
for i in range(a):
    b=int(input("value="))
    n.append(b)
print()

p=len(n)
for i in range(0,p):#0,1,2,3,4 p=4 values
    for j in range(i+1,p):#starts from 4(1,2,3,4),end=4
        print(i)
        if(n[i]>n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)




    
    
    
            

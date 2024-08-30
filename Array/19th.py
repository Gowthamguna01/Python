a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

for i in range(a):
    for j in range(i+1,a):
        if(n[i]==n[j]):
            print("duplicate number=",n[i])
       
            
    

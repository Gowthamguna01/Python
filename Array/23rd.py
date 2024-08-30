a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("values="))
    n.append(b)
print(n)

for i in range(a):
    for j in range(i+1,a):
        if(n[i]==n[j]):
            print("duplicate=",n[i])
uni=[]
for i in range(a):
    if n[i] not in uni:
            uni.append(n[i])
            print(uni)

        
            
        

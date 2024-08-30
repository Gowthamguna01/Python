a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("enter values="))
    n.append(b)
print(n)

for i in range(a):
    if(n[i]%2==0):
        print("even numbers=",n[i])
    else:
        print("odd numbers=",n[i])
    

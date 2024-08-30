a=int(input("enter a number="))
n=[]
for i in range(0,a):
    b=int(input("values="))
    n.append(b)
print(n)


p=len(n)
for i in range(0,p):
    for j in range(i+1,p):
        print(i)
        if(n[i]<n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        print(n)

sm=n[1]#anyposition you given just for comparison)
secL=n[3]
for i in range(a):
    if(n[i]<sm):
        secL=sm
        sm=n[i]
    i=i+1
print("second smallest number in array and descending=",secL)




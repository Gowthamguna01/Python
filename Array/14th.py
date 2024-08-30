a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("values="))
    n.append(b)
print(n)

small=max(n)
for i in range(0,len(n)):
    if(n[i]<small):
        small=n[i]
    i=i+1
print("smallest number=",small)

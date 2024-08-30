a=int(input("enter a number="))
n=[]
for i in range(a):
    b=int(input("values="))
    n.append(b)
print(n)

big=min(n)
for i in range(0,len(n)):
    if(n[i]>big):
        big=n[i]
    i=i+1
print("largest number=",big)

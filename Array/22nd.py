a=int(input("enter a number="))
n=[]
d=[]
for i in range(a+1):
    b=str(input("1st array="))
    n.append(b)
print(n)

for j in range(a+1):
    c=str(input("2nd array="))
    d.append(c)
print(d)

#common number
for i in range(a+1):
    for j in range(i+1,a,1):
        if(n[i]==d[j]):
            print("common Element=",n[i])
    

a=int(input("enter a number="))
n=[]
for i in range(0,a):
    b=int(input("values="))
    n.append(b)
print(n)

c=int(input("enter number="))#given
for i in range(a):
    if(c == n[i]):
        print("position:",i)
        break
else:
    print(c)
    
    


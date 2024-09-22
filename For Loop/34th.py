n=int(input("enter n number="))
s=0
for i in range(1,n,1):
    if(n%i==0):
        s=s+i


if(s==n):
    print("Perfect Number")

else:
    print("Not a Perfect Number")
    

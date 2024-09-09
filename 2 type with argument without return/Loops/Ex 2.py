def sumofodd(n):
    
    d=0
    i=1
    while(i<=n):
        if(i%2==1):
            d=d+i
            print(d)
        i=i+1


n=int(input("enter n number="))
sumofodd(n)
    

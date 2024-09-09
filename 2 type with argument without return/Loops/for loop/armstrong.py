def armstrong(n):
    
    p=0
    c=0
    a=n
    for i in range(1,n+1,1):
        n=n//10
        c=c+1
        if(n==0):
            break
        for i in range(1,a):
            d=a%10
            a=a//10
            p=pow(d,c)
            if(a==0):
                break
        if(p==a):
            print("armstrong",p)
        else:
            print("not armstrong",p)

n=int(input("enter n num="))
armstrong(n)

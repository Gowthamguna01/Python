import math
def armstrong(n):
    c=0
    a=n
    d=0
    m=n
    while(n>0):
        n=n//10
        c=c+1  
    while(a>0):
        b=a%10
        d=pow(b,c)+d
        a=a//10
    
    if(d==m):
        return("armstrong",d)
    else:
        return("not armstrong",d)

n=int(input("enter n num="))
x=armstrong(n)
print(x)

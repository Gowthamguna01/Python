import math
def armstrong():
    n=int(input("enter n num="))
    c=len(str(n))
    a=n
    d=0
    for i in range(a,0,-1):
        b=a%10
        d=pow(b,c)+d
        a=a//10 #loop stop
    
    if(d==n):
        return("armstrong",d)
    else:
        return("not armstrong",d)
    
x=armstrong()
print(x)

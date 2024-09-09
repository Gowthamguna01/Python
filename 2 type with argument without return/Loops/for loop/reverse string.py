def reversestring(m):
    
    b=" "
    d=len(m)-1
    for i in range(0,d+1):
        b=b+str(m[d])
        d=d-1
        print(b)

m=str(input("enter m value="))
reversestring(m)
    
    

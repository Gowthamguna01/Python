def sales(a):
    
    if(a<100000):
        if(a<=50000 and a<=100000):
            if(a<=20000 and a<50000):
                if(a<=10000 and a<20000):
                    if(a>=0 and a<10000):
                        b=a*0/100
                        return("b values",b)
                else:
                    b=a*(5/100)
                    return("b value",b)
            else:
                b=a*(10/100)
                return("b value",b)
        else:
            b=a*(15/100)
            return("b values",b)
    else:
        b=a*(20/100)+500
        return("b value=",b)

a=int(input("enter a="))
z=sales(a)
print(z)       
            
                    

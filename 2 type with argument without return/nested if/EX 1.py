def sales(a):
    
    if(a<100000):
        if(a<=50000 and a<=100000):
            if(a<=20000 and a<50000):
                if(a<=10000 and a<20000):
                    if(a>=0 and a<10000):
                        b=a*0/100
                        print("b values",b)
                else:
                    b=a*(5/100)
                    print("b value",b)
            else:
                b=a*(10/100)
                print("b value",b)
        else:
            b=a*(15/100)
            print("b values",b)
    else:
        b=a*(20/100)+500
        print("b value=",b)


a=int(input("enter a="))
sales(a)
        
            
                    

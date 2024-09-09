def gross():
    a=int(input("enter a="))
    if(a<20000):
        if(a<=10000 and a<=20000):
            if(a>=0 and a<10000):
                b=a*(20/100)
                c=a*(80/100)
                gp=a+b+c
                return("gp value=",gp)
        else:
            b=a*(25/100)
            c=a*(90/100)
            gp=a+b+c
            return("gp value=",gp)
    else:
        b=a*(30/100)
        c=a*(95/100)
        gp=a+b+c
        return("gp value=",gp)
x=gross()
print(x)

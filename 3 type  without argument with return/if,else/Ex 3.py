def arithmatic():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=str(input("enter sign"))
    if(c=="1" or c=="+"):
        d=a+b
        return(d)
    elif(c=="2" or c=="-"):
        d=a-b
        return(d)
    elif(c=="3" or c=="*"):
        d=a*b
        return(d)
    elif(c=="4" or c=="/"):
        d=a/b
        return(d)
    elif(c=="5" or c=="%"):
        d=a%b
        return(d)
x=arithmatic()
print(x)

def palindrome():
    a=int(input("enter a number="))
    d=0
    c=a
    while(a>0):
        b=a%10
        a=a//10
        d=d*10+b
        
    if(d==c):
        return("palindrome",d)
    else:
        return("not a palindrome",d)

    return(d)

  
   
x=palindrome()
print(x)

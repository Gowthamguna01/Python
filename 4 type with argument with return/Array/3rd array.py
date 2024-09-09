def second_number(a):
    
    n=[]
    for i in range(0,a):
        b=int(input("values="))
        n.append(b)
    n[1]=50
    return(n)

a=int(input("enter a number="))
x=second_number(a)
print(x)

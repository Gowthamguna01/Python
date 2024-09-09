def first_last(a):
    
    n=[]
    for i in range(0,a):
        b=int(input("values="))
        n.append(b)
    return(n[0],n[4])

a=int(input("enter a number="))
x=first_last(a)
print(x)

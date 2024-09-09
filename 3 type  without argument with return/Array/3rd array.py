def second_number():
    a=int(input("enter a number="))
    n=[]
    for i in range(0,a):
        b=int(input("values="))
        n.append(b)
    n[1]=50
    return(n)
x=second_number()
print(x)

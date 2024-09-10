def third_last(a):
    
    n=[]
    for i in range(a):
        v=int(input("value:"))
        n.append(v)
    return(n[2],n[4])

a=int(input("enter a value="))
x=third_last(a)
print(x)


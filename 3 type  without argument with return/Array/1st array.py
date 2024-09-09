def third_last():
    a=int(input("enter a value="))
    n=[]
    for i in range(a):
        v=int(input("value:"))
        n.append(v)
    return(n[2],n[4])
x=third_last()
print(x)


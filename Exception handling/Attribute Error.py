try:
    t=(2,3,True)
    p=int(input("Enter value"))
    t.append(p)
    print(t)
except AttributeError as a:
    print(a)

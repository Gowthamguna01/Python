a=int(input("enter a num="))
n=[]
for i in range(0,a):#loop run
    b=int(input("values="))
    n.append(b)#b store on n[array]
print(n)

c=int(input("enter value="))
'''if c in n:  (in -> (function)
    print("Array contain value")
else:
    print("Array not contain value")
'''
for i in range(a):#loop running
    if(c == n[i]):#c is normalnum/notcompared onarray[].
        #so compared to n[i]->array position.
        print("Array contain value")
        break
else:
    print("Array not contain value")

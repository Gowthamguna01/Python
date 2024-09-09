def  n_multiplication(tab):
    
    r=16
    for i in range(1,r+1,1):
        b=i*tab
        print(i, "X" ,tab,"=", b)


tab=int(input("enter table="))
n_multiplication(tab)    

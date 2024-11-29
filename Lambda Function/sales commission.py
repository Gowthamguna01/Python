com=lambda sale:print((sale*0)//100)if(sale<10000)else print((sale*5)//100) if(sale<20000)else print((sale*10)//100)if(sale<50000)else print(sale*15)//100)if(sale<100000)else print((sale*20)//100+500)if(sale>100000)else print("invalid")
sale=int(input("Enter sales"))
com(sale)

tax=lambda x:x*0/100 if(x<10000)else((x-10000)*10/100)if(x<20000)else((x-20000)*20//100+(10000*10//100))if(x>=20000)else "invalid"
x=int(input("Enter tax"))
z=tax(x)
print("Tax:", z)

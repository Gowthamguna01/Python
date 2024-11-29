eb=lambda unit:(unit*1.2)if(unit<200)else((unit-199)*1.5+(199*1.2))if(unit<400)else((unit-399)*1.8+(199*1.2)+(200*1.5))if(unit<500)else((unit-599)*2+(199*1.2)+(200*1.5)+(200*1.8))if(unit>599)else "sorry"
unit=int(input("Enter unit"))
z=eb(unit)
if(z>400):
    sur(z*15//100)
    z=sur+z
print(z)

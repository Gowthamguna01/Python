def eligible(a):
    
    if(a>=18):
        return("Eligible for vote")
    if(a<18):
        return("Not Eligible for vote")

a=int(input("enter a num="))
z=eligible(a)
print(z)

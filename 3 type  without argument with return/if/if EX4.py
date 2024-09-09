def eligible():
    a=int(input("enter a num="))
    if(a>=18):
        return("Eligible for vote")
    if(a<18):
        return("Not Eligible for vote")
x=eligible()
print(x)
        

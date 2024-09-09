def positive_negative(a):
    
    if(a>0):
        return("positive")
    elif(a<0):
        return("negative")
    elif(a==0):
        return("netural")

a=int(input("Enter a"))
z=positive_negative(a)
print(z)

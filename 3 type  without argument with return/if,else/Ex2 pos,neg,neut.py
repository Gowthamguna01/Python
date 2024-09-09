def positive_negative():
    a=int(input("Enter a"))
    if(a>0):
        return("positive")
    elif(a<0):
        return("negative")
    elif(a==0):
        return("netural")
x=positive_negative()
print(x)

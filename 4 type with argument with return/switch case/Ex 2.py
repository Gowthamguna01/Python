def calculate(a,b,c):
    
    match c:
        case "+":
            d=a+b
            return("value is=",d)

        case "-":
            d=a-b
            return("value is=",d)

        case "*":
            d=a*b
            return("value is=",d)

        case "/":
            d=a/b
            return("value is=",d)

        case "%":
            d=a%b
            return("value is=",d)

a=int(input("enter a"))
b=int(input("enter b"))
c=str(input("enter value sign:"))
z=calculate(a,b,c)        
print(z)

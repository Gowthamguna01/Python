def calculate():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=str(input("enter value sign:"))
    match c:
        case "+":
            d=a+b
            print("value is=",d)

        case "-":
            d=a-b
            print("value is=",d)

        case "*":
            d=a*b
            print("value is=",d)

        case "/":
            d=a/b
            print("value is=",d)

        case "%":
            d=a%b
            print("value is=",d)
calculate()        

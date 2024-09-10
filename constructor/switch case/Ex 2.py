class Formula:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def calculate(self):
        match self.c:
            case "+":
                self.d=self.a+self.b
                print("value is=",self.d)

            case "-":
                self.d=self.a-self.b
                print("value is=",self.d)

            case "*":
                self.d=self.a*self.b
                print("value is=",self.d)

            case "/":
                self.d=self.a/self.b
                print("value is=",self.d)

            case "%":
                self.d=self.a%self.b
                print("value is=",self.d)

a=int(input("enter a"))
b=int(input("enter b"))
c=str(input("enter value sign:"))                

x=Formula(a,b,c)
x.calculate()        

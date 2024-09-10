class Formula:
    def calculate(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        match c:
            case "+":
                self.d=self.a+self.b
                return("value is=",self.d)

            case "-":
                self.d=self.a-self.b
                return("value is=",self.d)

            case "*":
                self.d=self.a*self.b
                return("value is=",self.d)

            case "/":
                self.d=self.a/self.b
                return("value is=",self.d)

            case "%":
                self.d=self.a%self.b
                return("value is=",self.d)

a=int(input("enter a"))
b=int(input("enter b"))
c=str(input("enter value sign:"))

x=Formula()
v=x.calculate(a,b,c)        
print(v)

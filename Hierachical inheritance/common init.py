class Program:

    def __init__(self,a,b,v):
        self.a=a
        self.b=b
        self.v=v


    def perimeteroftriangle(self):
        self.P=self.a+self.b+self.v/2
        print("ptriangle",self.P)

    
class Child1(Program): #a,b,v

    def __init__(self,a,b,v):
        Program.__init__(self,a,b,v)


    def perimeter(self):
        self.P=3*self.a
        print("perimeter",self.P)


    def pcuboid(self):
        self.P=4*(self.a+self.b+self.v)
        print("pcuboid",self.P)



class Child2(Program):
    def __init__(self,a,b,c):
        Program.__init__(self,a,b,v)
        self.c=c
            
    def calculate(self): #c
    
        match self.c:
            case "+":   
                self.d=self.a+self.b
                print("case value is=",self.d)

            case "-":
                self.d=self.a-self.b
                print("case value is=",self.d)

            case "*":
                self.d=self.a*self.b
                print("case value is=",self.d)

            case "/":
                self.d=self.a/self.b
                print("case value is=",self.d)

            case "%":
                self.d=self.a%self.b
                print("case value is=",self.d)


    def gross(self):
        
        if(self.a<20000):
            if(self.a<=10000 and self.a<=20000):
                if(self.a>=0 and self.a<10000):
                    self.b=self.a*(20/100)
                    self.c=self.a*(80/100)
                    self.gp=self.a+self.b+self.c
                    print("gp value=",self.gp)
            else:
                self.b=self.a*(25/100)
                self.c=self.a*(90/100)
                self.gp=self.a+self.b+self.c
                print("gp value=",self.gp)
        else:
            self.b=self.a*(30/100)
            self.c=self.a*(95/100)
            self.gp=self.a+self.b+self.c
            print("gp value=",self.gp)



a=int(input("enter a"))
b=int(input("enter b"))
v=int(input("enter v="))
c=str(input("enter value sign:"))


G=Child2(a,b,c)
G.perimeteroftriangle()
G.gross()
G.calculate()


m=Child1(a,b,v)
m.perimeteroftriangle()
m.perimeter()
m.pcuboid()
    

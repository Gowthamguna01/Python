class Common:
    def __init__(self,a,b,v,c):
        self.a=a
        self.b=b
        self.v=v
        self.c=c
        


    def perimeteroftriangle(self):
        self.P=self.a+self.b+self.v/2
        print("ptriangle",self.P)


    def perimeter(self):
        self.P=3*self.a
        print("perimeter",self.P)


    def pcuboid(self):
        self.P=4*(self.a+self.b+self.v)
        print("pcuboid",self.P)



class Child(Common):

    def __init__(self,a,b,v,c):
        Common.__init__(self,a,b,v,c)

    
    def calculate(self):
        
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


G=Child(a,b,v,c)
G.perimeteroftriangle()
G.gross()
G.calculate()
G.perimeter()
G.pcuboid()
    

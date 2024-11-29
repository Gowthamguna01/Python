class Parent:

    def __init__(self,a,b,n,c):
        self.a=a
        self.b=b
        self.n=n
        self.c=c
    
    def oddeven(self): #n
        if(self.n%2==0):
            print("Even number")
        if(self.n%2==1):
            print("Odd number")
            
    def biggest(self): #ab
        if(self.a>self.b):
            print("A is BIG")
        if(self.b>self.a):
            print("B is BIG")

    def negative_postive(self): #a
        if(self.a>0):
            print("positive number")
        if(self.a<0):
            print("negative number")

class Child(Parent):
    
    def __init__(self,a,b,n,c,m): #parents variable confirm
        Parent.__init__(self,a,b,n,c)
        self.m=m


    def grasspay(self):  #ab FUNCTION 1
        if(self.a<100000):
            if(self.a<=50000 and self.a<=100000):
                if(self.a<=20000 and self.a<50000):
                    if(self.a<=10000 and self.a<20000):
                        if(self.a>=0 and self.a<10000):
                            self.b=self.a*0/100
                            print("b values",self.b)
                    else:
                        self.b=self.a*(5/100)
                        print("b value",self.b)
                else:
                    self.b=self.a*(10/100)
                    print("b value",self.b)
            else:
                self.b=self.a*(15/100)
                print("b values",self.b)
        else:
            self.b=self.a*(20/100)+500
            print("b value=",self.b)


    def calculate(self): #abc FUNCTION 2
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
       



a=int(input("Enter a="))
b=int(input("Enter b="))
n=int(input("enter n="))
c=str(input("enter value sign:"))
m=67

M=Child(a,b,n,c,m)
M.oddeven()
M.biggest()
M.negative_postive()
M.grasspay()
M.calculate()


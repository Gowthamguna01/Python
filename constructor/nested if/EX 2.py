class Formula:
    def __init__(self,a):
        self.a=a
        
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


a=int(input("enter a="))
x=Formula(a)
x.gross()

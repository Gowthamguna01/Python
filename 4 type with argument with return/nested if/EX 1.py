class Formula:
    def sales(self,a):
        self.a=a
        if(self.a<100000):
            if(self.a<=50000 and self.a<=100000):
                if(self.a<=20000 and self.a<50000):
                    if(self.a<=10000 and self.a<20000):
                        if(self.a>=0 and self.a<10000):
                            self.b=self.a*0/100
                            return("b values",self.b)
                    else:
                        self.b=self.a*(5/100)
                        return("b value",self.b)
                else:
                    self.b=self.a*(10/100)
                    return("b value",self.b)
            else:
                self.b=self.a*(15/100)
                return("b values",self.b)
        else:
            self.b=self.a*(20/100)+500
            return("b value=",self.b)



a=int(input("enter a="))

x=Formula()
v=x.sales(a)
print(v)       
            
                    

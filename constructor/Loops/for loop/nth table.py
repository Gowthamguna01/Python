class Forloops:
    def __init__(self,tab):
        self.tab=tab
        
    def  n_multiplication(self):
        self.r=16
        for i in range(1,self.r+1,1):
            self.b=i*self.tab
            print(i, "X" ,self.tab,"=", self.b)

tab=int(input("enter table="))

x=Forloops(tab)
x.n_multiplication()    

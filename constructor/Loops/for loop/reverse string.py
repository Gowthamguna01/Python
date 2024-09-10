class Forloop:
    def __init__(self,m):
        self.m=m
        
    def reverse(self):
        
        self.b=" "
        self.d=len(self.m)-1
        for i in range(0,self.d+1):
            self.b=self.b+str(self.m[self.d])
            self.d=self.d-1
            print(self.b)

m=str(input("enter m value="))
x=Forloop(m)          
x.reverse()
    
    

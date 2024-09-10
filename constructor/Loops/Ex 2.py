class Loops:
    def __init__(self,n):
        self.n=n
        
    def sumofodd(self):
        self.d=0
        self.i=1
        while(self.i<=self.n):
            if(self.i%2==1):
                self.d=self.d+self.i
                print(self.d)
            self.i=self.i+1

n=int(input("enter n number="))

x=Loops(n)            
x.sumofodd()
    

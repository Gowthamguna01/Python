class Loops:
    def __init__(self,n):
        self.n=n
        
    def natural(self):
        
        self.i=1
        while(self.i<=self.n):
            print(self.i)
            self.i=self.i+1

n=int(input("enter n number="))

x=Loops(n)
x.natural()

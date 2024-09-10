class Loops:

    def __init__(self,n):
        self.n=n
        
    def factorial(self):
        self.i=1
        self.j=1
        while(self.i<=self.n):
            self.j=self.j*self.i
            print(self.j)
            self.i=self.i+1

n=int(input("enter n number="))

x=Loops(n)            
x.factorial()

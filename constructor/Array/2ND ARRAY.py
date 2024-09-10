class Array:
    def __init__(self,a):
        self.a=a
        
    def first_last(self):
        
        self.n=[]
        for i in range(0,self.a):
            self.b=int(input("values="))
            self.n.append(self.b)
        print(self.n[0],self.n[4])

a=int(input("enter a number="))
x=Array(a)    
x.first_last()

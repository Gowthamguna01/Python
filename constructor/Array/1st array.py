class Array:
    def __init__(self,a):
        self.a=a
        
    def third_last(self):
        self.n=[]
        for i in range(self.a):
            self.v=int(input("value:"))
            self.n.append(self.v)
        print(self.n[2],self.n[4])

a=int(input("enter a value="))

x=Array(a)    
x.third_last()


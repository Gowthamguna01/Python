class Array:
    def __init__(self,a):
        self.a=a
        
    def second_number(self):
        
        n=[]
        for i in range(0,self.a):
            b=int(input("values="))
            n.append(b)
        n[1]=50
        print(n)

a=int(input("enter a number="))
x=Array(a)
x.second_number()

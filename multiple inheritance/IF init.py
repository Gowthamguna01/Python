class Mother():
    
     def __init__(self,n):
        self.n=n

     def oddeven(self):
         if(self.n%2==0):
             print("Even number")
         if(self.n%2==1):
             print("Odd number")


class Father():

    def __init__(self,a,b):
       self.a=a
       self.b=b
    
            
    def biggest(self): #ab
        if(self.a>self.b):
            print("A is BIG")
        if(self.b>self.a):
            print("B is BIG")

    def negative_postive(self):
        if(self.a>0):
            print("positive number")
        if(self.a<0):
            print("negative number")



class Child(Mother,Father):
    
    def __init__(self,a,b,c,n):
         Mother.__init__(self,n)
         Father.__init__(self,a,b)
         self.c=c

    

    def calculate(self):
         match self.c:
             case "+":
                  self.d=self.a+self.b
                  print("value is=",self.d)

             case "-":
                  self.d=self.a-self.b
                  print("value is=",self.d)

             case "*":
                  self.d=self.a*self.b
                  print("value is=",self.d)

             case "/":
                  self.d=self.a/self.b
                  print("value is=",self.d)

             case "%":
                  self.d=self.a%self.b
                  print("value is=",self.d)
       



a=int(input("Enter a="))
b=int(input("Enter b="))
n=int(input("enter n="))
c=str(input("enter case sign:"))


M=Child(a,b,c,n)

M.oddeven()
M.calculate()
M.oddeven()
M.biggest()
M.negative_postive()


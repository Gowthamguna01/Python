class Formula:
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def arithmatic(self):
        
        if(self.c=="1" or self.c=="+"):
            self.d=self.a+self.b
            print(self.d)
        elif(self.c=="2" or self.c=="-"):
            self.d=self.a-self.b
            print(self.d)
        elif(self.c=="3" or self.c=="*"):
            self.d=self.a*self.b
            print(self.d)
        elif(self.c=="4" or self.c=="/"):
            self.d=self.a/self.b
            print(self.d)
        elif(self.c=="5" or self.c=="%"):
            self.d=self.a%self.b
            print(self.d)


a=int(input("enter a"))
b=int(input("enter b"))
c=str(input("enter sign"))

x=Formula(a,b,c)            
x.arithmatic()

class Multi:
    def __init__(self,r,c):
        self.r=r
        self.c=c
        
    def multiarray(self):
        
        self.o=[]
        for i in range(0,self.r):
            self.n=[]
            for j in range(0,self.c):
                self.b=int(input("Enter values="))
                self.n.append(self.b)
            self.o.append(self.n)
        print(self.o)
        self.l=[]
        for i in range(0,self.r):
            self.h=[]
            for j in range(0,self.c):
                self.h.append(self.o[j][i])
                print(self.o[j][i],end=" ")
            self.l.append(self.h)
        print()
        for i in range(0,1):
            if(self.o[j][i]== 0 and 1 or 1 and 0):
                print("idetity matrix")
            else:
                print("not identity matrix")


r=int(input("Enter row="))
c=int(input("enter col="))

x=Multi(r,c)
x.multiarray()    
    

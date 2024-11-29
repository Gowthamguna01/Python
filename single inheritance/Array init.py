class Array:

    def __init__(self,a,r,c):
        self.a=a
        self.r=r
        self.c=c
        
    def third_last(self):
        self.n=[]
        for i in range(self.a):
            self.b=int(input("value:"))
            self.n.append(self.b)
        print(self.n[2],self.n[4])



    def first_last(self):
        self.n=[]
        for i in range(0,self.a):
            self.b=int(input("values="))
            self.n.append(self.b)
        print(self.n[0],self.n[4])


class Child(Array):
    
    def __init__(self,a,r,c):
        Array.__init__(self,a,r,c)


    def second_number(self):
        self.n=[]
        for i in range(0,self.a):
            self.b=int(input("values="))
            self.n.append(self.b)
        self.n[1]=50
        print(self.n)

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



a=int(input("enter a number="))
r=int(input("Enter row="))
c=int(input("enter col="))

o=Child(a,r,c)
o.third_last()
o.first_last()
o.second_number()
o.multiarray()

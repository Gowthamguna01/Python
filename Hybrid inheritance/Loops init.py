class Grandparent():#father

    def __init__(self,n):
        self.n=n
        


    def natural(self):
        self.i=1
        while(self.i<=self.n):
            print(self.i)
            self.i=self.i+1



class Loops(Grandparent):#mother

    def __init__(self,n):
        Grandparent.__init__(self,n)#hierachiel
        
        
    def sumofodd(self):
        self.d=0
        self.i=1
        while(self.i<=self.n):
            if(self.i%2==1):
                self.d=self.d+self.i
                print("sumofodd",self.d)
                self.i=self.i+1


    def factorial(self):
        self.i=1
        self.j=1
        while(self.i<=self.n):
            self.j=self.j*self.i
            print("factorial",self.j)
            self.i=self.i+1


class Child(Loops,Grandparent):

    def __init__(self,a,tab,n):
        Loops.__init__(self,n)
        Grandparent.__init__(self,n)
        self.a=a
        self.tab=tab


    def palindrome(self):
        self.n=self.a
        self.b=0
        for i in range(0,self.a+1):
            self.c=self.a%10
            self.a=self.a//10
            self.b=self.b*10+self.c
            print(self.b)
            if(self.a==0):
                break
        if(self.b==self.n):
            print("palindrome",self.b)
        else:
            print("not a palindrome",self.b)



    def  n_multiplication(self):
        self.r=16
        for i in range(1,self.r+1,1):
            self.b=i*self.tab
            print(i, "X" ,self.tab,"=", self.b)


n=int(input("enter n number="))
a=int(input("enter a number="))
tab=int(input("enter table="))



v=Child(n,a,tab)

v.n_multiplication()
v.palindrome()
v.natural()
v.factorial()
v.sumofodd()
v.natural()






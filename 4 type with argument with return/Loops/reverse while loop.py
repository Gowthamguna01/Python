class Formula:
    def reverse(self,a):
        self.a=a
        self.c=0
        while(self.a>0):
            self.b=self.a%10 #rem(reverse pana)
            self.a=self.a//10 #quacent loop stop pana
            self.c=self.c*10+self.b #reverse changing
        return("reverse number=",self.c)


a=int(input("enter n number="))

x=Formula()
v=x.reverse(a)
print(v)


class pattern:
    def star(self):
        self.a=int(input("enter a num"))
        for i in range(1,self.a+1,1):
            for j in range(1,11,1):
                print("*", end="")
            print()

x=pattern()            
x.star()
            

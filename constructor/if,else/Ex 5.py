class Formula:
    
    def __init__(self,b):
        self.b=b
        
    def vowels(self):
        
        if(self.b== "a" or self.b=="e" or self.b=="i" or self.b=="o" or self.b=="u"):
            print("vowels")
        else:
            print("consonants")


b=str(input("Enter VALUE:"))
x=Formula(b)
x.vowels()

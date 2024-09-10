class Formula:
    def vowels(self,b):
        if(b== "a" or b=="e" or b=="i" or b=="o" or b=="u"):
            return("vowels")
        else:
            return("consonants")


b=str(input("Enter VALUE:"))

x=Formula()
v=x.vowels(b)
print(v)

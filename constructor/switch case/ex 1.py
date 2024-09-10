class Formula:
    def __init__(self,c):
        self.c=c
        
    def switch(self):
        
        match self.c:
            case "a" | "e" | "i" | "o" | "u":
                print("vowels")

            case _:
                print("consonants")

c=str(input("enter value:"))

x=Formula(c)
x.switch()

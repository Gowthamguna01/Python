class Formula:
    def switch(self,a):
        self.a=a
        match a:
            case "a" | "e" | "i" | "o" | "u":
                return("vowels")

            case _:
                return("consonants")

a=str(input("enter value:"))

x=Formula()
v=x.switch(a)
print(v)

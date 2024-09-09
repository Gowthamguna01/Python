def switch(a):
    
    match a:
        case "a" | "e" | "i" | "o" | "u":
            return("vowels")

        case _:
            return("consonants")

a=str(input("enter value:"))
z=switch(a)
print(z)

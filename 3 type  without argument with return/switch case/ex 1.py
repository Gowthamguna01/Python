def switch():
    a=str(input("enter value:"))
    match a:
        case "a" | "e" | "i" | "o" | "u":
            return("vowels")

        case _:
            return("consonants")
x=switch()
print(x)

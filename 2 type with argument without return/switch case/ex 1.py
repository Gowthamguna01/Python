def switch(a):
    
    match a:
        case "a" | "e" | "i" | "o" | "u":
            print("vowels")

        case _:
            print("consonants")


a=str(input("enter value:"))
switch(a)

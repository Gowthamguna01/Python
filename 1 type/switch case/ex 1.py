def switch():
    a=str(input("enter value:"))
    match a:
        case "a" | "e" | "i" | "o" | "u":
            print("vowels")

        case _:
            print("consonants")
switch()

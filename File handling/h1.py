import os

class File:
    def write(self):
        self.a = str(input("Enter file name="))
        if os.path.exists(self.a):
            self.f = open(self.a, "w")
            self.c = str(input("Type Here.. "))
            self.f.write(self.c)
            self.f.close()
            print("File Successfully updated :) [visit notepad] ")  # Refresh Everytime
            
            self.f = open(self.a, "r")
            content = self.f.read()
            print("Letters:", len(content))
            self.f.close()
            
            # Initialize vowel counters
            a = e = i = o = u = 0
            
            for char in content:
                match char.lower():  # Use lower() for case-insensitivity
                    case 'a':
                        a += 1
                    case 'e':
                        e += 1
                    case 'i':
                        i += 1
                    case 'o':
                        o += 1
                    case 'u':
                        u += 1
            
            print("Vowel counts:")
            print("a count =", a)
            print("e count =", e)
            print("i count =", i)
            print("o count =", o)
            print("u count =", u)

        else:
            print("File not Available :( ")
            self.g = (input("Do you want to continue: yes/no"))

            if self.g == 'yes':
                self.u = str(input("Do you want create new file: yes/no"))
                if self.u == 'yes':
                    self.q = str(input("Enter File Name:"))
                    self.f = open(self.q, "w")
                    self.h = str(input("Do you want Enter content: yes/no"))

                    if self.h == 'yes':
                        self.b = str(input("Enter Content"))
                        self.f.write(self.b)
                        self.f.close()
                        print("File successfully Updated :)")
                    else:
                        print("Thank you :)")

    # Other methods remain unchanged...
    
    def read(self):
        self.a = str(input("Enter file name="))
        if os.path.exists(self.a):
            self.f = open(self.a, "r")
            print(self.f.read())
            self.f.close()
        else:
            print("File not Available :( ")
            self.g = (input("Do you want to continue: [yes/no]"))
            if self.g == 'yes':
                self.a = str(input("Do you want create new file: yes/no "))
                if self.a == 'yes':
                    self.q = str(input("Enter File Name:"))
                    self.f = open(self.q, "w")
                    self.h = str(input("Do you want Enter content: yes/no"))

                    if self.h == 'yes':
                        self.b = str(input("Enter content"))
                        self.f.write(self.b)
                        self.f.close()
                        print("File successfully updated :) ")
                    else:
                        print("Thank you :)")

    def append(self):
        self.a = str(input("Enter file name="))
        if os.path.exists(self.a):
            self.f = open(self.a, "a")
            self.c = str(input("Type Here..  "))
            self.f.write(self.c)
            self.f.close()
            print("File successfully Updated :)")
        else:
            print("File not Available :( ")
            self.v = (input("Do you want to continue: [yes/no]"))

            if self.v == 'yes':
                self.a = str(input("Do you want to Create new file: yes/no "))
                if self.a == 'yes':
                    self.q = str(input("Enter File Name:"))
                    self.f = open(self.q, "w")
                    self.h = str(input("Do you want Enter content: yes/no"))

                    if self.h == 'yes':
                        self.b = str(input("Enter content"))
                        self.f.write(self.b)
                        self.f.close()
                        print("File successfully Uploaded :)")
                    else:
                        print("Thank you :)")

x = File()

print("1.write")
print("2.read")
print("3.append")

M = 'yes'
while M.lower() == 'yes':
    n = int(input("Enter your option:"))
    if n == 1:
        x.write()
    elif n == 2:
        x.read()
    elif n == 3:
        x.append()
    else:
        print("Not available")

    M = input("Do you want to continue the Page? [yes/no] ")
    
    if M == 'no':
        print("Thank you :) ")

a=int(input("no.of.subjects="))
v=str(input("Enter Name="))
ma=[]
su=[]

for i in range(0,a):
    s=(input("enter subject="))
    su.append(s)

for j in range(0,a):
    m=int(input("enter marks="))
    ma.append(m)

print("student name", end=" ")

for s in su:#space
    print(f"{s:>12}", end=" ")
print()

print(v, end=" ")

for m in ma:#space
    print(f"{m:>13}", end=" ")
print()

g=int(input("Enter again:(press 1)"))

if(g==1):
    a=int(input("no.of.subjects="))
    v=str(input("Enter Name="))
    ma=[]
    su=[]

    for i in range(0,a):
        s=(input("subject name="))
        su.append(s)

    for j in range(0,a):
        m=int(input("enter marks="))
        ma.append(m)

    print(v, end=" ")

    for s in su:#space
        print(f"{s:>10}", end=" ")
    print()

    for m in ma:#space
        print(f"{m:>10}", end=" ")
    print()
    
    




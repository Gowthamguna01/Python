import conn

def insert():
    a=input("Enter Id: ")
    b=input("Enter stName: ")
    c=int(input("Tamil: "))
    d=int(input("English: "))
    e=int(input("Maths: "))
    f=int(input("Science: "))
    g=int(input("Social: "))

    sql="""
    insert into Exam (Id, stName, Tamil, English, Maths, Science, Social, Average) 
    values (%s,%s,%s,%s,%s,%s,%s,(%s+%s+%s+%s+%s)/5)
    """
    
    val=(a,b,c,d,e,f,g,c,d,e,f,g)#cdefg/5 for avg
    conn.mycursor.execute(sql, val)
    conn.mydb.commit()
    print(conn.mycursor.rowcount,"details inserted")

def select():
    print("Id, stName, Tamil, English, Maths, Science, Social, Average:")
    query="select Id, stName, Tamil, English, Maths, Science, Social, Average from Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def update_stName():
    stName=input("Enter Name: ")
    Id=input("Enter Id: ")
    sql="update Exam set stName=%s where Id= %s"
    conn.mycursor.execute(sql,(stName, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount,"details updated")

def update_Tamil():
    Id=input("Enter Id: ")
    Tamil=int(input("Tamil Mark: "))
    sql="update Exam set Tamil=%s, Average=(Tamil+English+Maths+Science+Social)/5 where Id= %s"
    conn.mycursor.execute(sql,(Tamil, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "details updated")

def update_English():
    Id=input("Enter Id: ")
    English=int(input("English Mark: "))
    sql="update Exam set English=%s, Average=(Tamil+English+Maths+Science+Social)/5 where Id= %s"
    conn.mycursor.execute(sql,(English, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "details updated")

def update_Maths():
    Id=input("Enter Id: ")
    Maths=int(input("Maths Mark: "))
    sql="update Exam set Maths=%s, Average=(Tamil+English+Maths+Science+Social)/5 where Id= %s"
    conn.mycursor.execute(sql,(Maths, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "details updated")

def update_Science():
    Id=input("Enter Id: ")
    Science=int(input("Science Mark: "))
    sql="update Exam set Science= %s, Average=(Tamil+English+Maths+Science+Social)/5 where Id= %s"
    conn.mycursor.execute(sql,(Science, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "details updated")

def update_Social():
    Id=input("Enter Id: ")
    Social=int(input("Social Mark: "))
    sql="update Exam set Social = %s, Average=(Tamil+English+Maths+Science+Social)/5 where Id = %s"
    conn.mycursor.execute(sql,(Social, Id))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "details updated")

def update():
    print("1. Update stName")
    print("2. Update Tamil")
    print("3. Update English")
    print("4. Update Maths")
    print("5. Update Science")
    print("6. Update Social")

    u=int(input("Select Update subject: "))

    if u==1:
        update_stName()
    elif u==2:
        update_Tamil()
    elif u==3:
        update_English()
    elif u==4:
        update_Maths()
    elif u==5:
        update_Science()
    elif u==6:
        update_Social()
    else:
        print("Invalid choice")

def delete():
    Id=input("Enter Id: ")
    query="delete from Exam where Id=%s"
    conn.mycursor.execute(query, (Id,))
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "record(s) deleted")

def Tamil():
    query="select Id, stName, Tamil FROM Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def English():
    query="select Id, stName, English FROM Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def Maths():
    query="select Id, stName, Maths FROM Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def Science():
    query="select Id, stName, Science FROM Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def Social():
    query="select Id, stName, Social FROM Exam"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x in myresult:
        print(x)

def marks():
    print("1. Tamil")
    print("2. English")
    print("3. Maths")
    print("4. Science")
    print("5. Social")
    subject=int(input("Enter your subject: "))
    
    if subject==1:
        Tamil()
    elif subject==2:
        English()
    elif subject==3:
        Maths()
    elif subject==4:
        Science()
    elif subject==5:
        Social()
    else:
        print("Invalid choice")

print("1. Insert")
print("2. Select")
print("3. Update")
print("4. Delete")
print("5. Marks")

ch='y'
while ch.lower()=='y':
    x=int(input("Enter choice: "))
    if x==1:
        insert()
    elif x==2:
        select()
    elif x==3:
        update()
    elif x==4:
        delete()
    elif x==5:
        marks()
    else:
        print("Invalid choice")

    ch=input("Do you want to continue? (y/n): ")

conn.mydb.close()

def select():
    print("Displaying Name and Roll coloumns from the student table:")

    #selecting  query
    query="select rollno,stname,city from student"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x  inn myresult:
        print(x)

    print("2.select")
    elif(x==2):
        select()

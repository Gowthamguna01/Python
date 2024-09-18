def update():
    #drop clause
    stname=input("Enter Name: ")
    rollno=(input("Enter Roll:"))
    inputdata=(stname,rollno)
    statement="""update student set stname=%swhere rollno=%s"""
    conn.mycursor.excute(statement,inputdata)
    print(statement)
    conn.mydb.commit()

    print("3.update")
    elif(x==3):
        update()

import  conn
def  insert():
    a=input("Enter rollno: ")
    b=input("Enter Name: ")
    c=input("Enter city: ")
    sql="insert into student(rollno,stname,city)values(%s,%s,%s)"
    val=(a,b,c)
    conn.mycursor.execute(sql,val)
    conn.mydb.commit()
    print(conn.mycursor.rowcount,"details inserted")

def select():
    print("Displaying Name and Roll coloumns from the student table:")

    #selecting  query
    query="select rollno,stname,city from student"
    conn.mycursor.execute(query)
    myresult=conn.mycursor.fetchall()
    for x  in myresult:
        print(x)

def update():
    #drop clause
    stname=input("Enter Name: ")
    rollno=(input("Enter Roll:"))
    inputdata=(stname,rollno)
    statement="""update student set stname=%swhere rollno=%s"""
    conn.mycursor.execute(statement,inputdata)
    print(statement)
    conn.mydb.commit()

    
    
def delete():
    rollno=input("Enter Roll: ")
    query="""delete from student where rollno=%s"""
    conn.mycursor.execute(query,(rollno,))
    conn.mydb.commit()


print("1.insert")
print("2.select")
print("3.update")
print("4.delete")
ch='y'
while(ch=='y'):
    x=int(input("Enter choice"))
    if(x==1):
        insert()
        
    elif(x==2):
        select()

    elif(x==3):
        update()

    elif(x==4):
        delete()
            
    ch=input("Do u want to continue y/n")
conn.mydb.close()
        

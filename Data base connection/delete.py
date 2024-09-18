def delete():
    rollno=input("Enter Roll: "))
    query="""delete from student where rollno=%s"""
    conn.mycursor.excute(query,(rollno,))
    conn.mydb.commit()
    
print("4.delete")
elif(x==4):
    delete()

    

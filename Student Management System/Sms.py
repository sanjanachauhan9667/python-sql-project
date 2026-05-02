import mysql.connector as myconn

mydb = myconn.connect(
    host = 'localhost',
    username = 'root',
    password = 'your_password',
    database = 'student_db',
    auth_plugin = 'mysql_native_password')

# DATABASE CREATED!----------------------------------------------
db_cursor = mydb.cursor()
db_cursor.execute('CREATE DATABASE IF NOT EXISTS student_db')

# TABLE CREATED!-------------------------------------------------
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id  INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50))
""")

# ADD_STUDENT!----------------------------------------------------
def add_student():
    name = input('Enter Name of Student: ')
    age = input('Enter Age of  Student: ')
    course = input('Enter the Course: ')

    query = "INSERT INTO students (name,age,course) VALUES (%s,%s,%s)"
    values = (name,age,course)

    db_cursor.execute(query,values)
    mydb.commit()
    print('Student Added Successfully.')

# VIEW_STUDENTS!------------------------------------------------------
def view_students():
    db_cursor.execute('SELECT * FROM students')
    students = db_cursor.fetchall()
    print("\n Student List")
    for i in students:
        print(f"ID:{i[0]}, NAME:{i[1]}, AGE:{i[2]}, COURSE:{i[3]}")

# UPDATE_STUDENTS!----------------------------------------------------
def update_student():
    new_id = input('Enter the Student ID to update: ')
    new_name = input('Enter the new name to update: ')
    new_age = input('Enter the new age to update: ')
    new_course = input('Enter the new course to update: ')

    query = "UPDATE students SET name=%s,age=%s,course=%s WHERE id=%s"
    db_cursor.execute(query,(new_name,new_age,new_course,new_id))
    mydb.commit()
    print('Student Updated Successfully.')

# DELETE_STUDENTS!----------------------------------------------------
def delete_students():
    student_id = input('Enter the ID of students to delete: ')
    query = " DELETE FROM students WHERE id = %s"
    db_cursor.execute(query,(student_id,))
    mydb.commit()
    print('Student Deleted Successfully')


# MENU!--------------------------------------------------------------
while True:
    print("\n ======== STUDENT MANAGEMENT SYSTEM =========")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3. UPDATE STUDENT")
    print("4. DELETE STUDENT")
    print("5. EXIT STUDENT")

    choice = input('Enter Your Choice:')

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_students()
    elif choice == '5':
        print(' EXITING......')
        break
    else:
        print('Invalid Choice')

# Close Connection
mydb.close()
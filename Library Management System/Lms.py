import mysql.connector as myconn

mydb = myconn.connect(
    host = 'localhost',
    user = 'root',
    password = 'your_password',
    database = 'Library_db',
    auth_plugin = 'mysql_native_password')

# DATABASE CREATED!----------------------------------------------
db_cursor = mydb.cursor()
db_cursor.execute('CREATE DATABASE IF NOT EXISTS Library_db')
db_cursor.execute('USE Library_db ')

# TABLE CREATED! ------------------------------------------------
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    author VARCHAR(100),
    status VARCHAR(50))
""")

## ADD_BOOK!-----------------------------------------------------
def add_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the Author of the book: ')

    query = "INSERT INTO books (name,author,status) Values (%s,%s,%s)"
    db_cursor.execute(query,(name,author,"available"))
    mydb.commit()
    print('Book Added Successfully!')

## VIEW_BOOK!-------------------------------------------------------
def view_books():
    db_cursor.execute("SELECT * FROM books")
    all_books = db_cursor.fetchall()
    print("\n Book List")
    for i in all_books:
        print(f"ID:{i[0]}, Name:{i[1]}, Author:{i[2]}, Status:{i[3]}")

## ISSUE_BOOK!------------------------------------------------------
def issue_book():
    book_id = input('Enter the book id to issue book:')
    query = ('UPDATE books SET status=%s WHERE id=%s')
    db_cursor.execute(query,("issued",book_id))
    mydb.commit()
    print('Book Issued!')

## RETURN_BOOK!-----------------------------------------------------
def return_book():
    book_id = input('Enter the book id to return: ')
    query = "UPDATE books SET status=%s WHERE id=%s"
    db_cursor.execute(query,("available",book_id))
    mydb.commit()
    print('Book Returned!')

## DELETE_BOOK!-----------------------------------------------------
def delete_book():
    book_id = input('Enter the book id to delete: ')
    query = ("DELETE FROM books WHERE id=%s")
    db_cursor.execute(query,(book_id,))
    mydb.commit()
    print('Book Deleted!')

## MENU!------------------------------------------------------------
while True:
    print('=========LIBRARY MANAGEMENT SYSTEM==========')
    print('1. ADD_BOOK ')
    print('2. VIEW_BOOKs ')
    print('3. ISSUE_BOOK ')
    print('4. RETURN_BOOK ')
    print('5. DELETE_BOOK ')
    print('6. EXIT ')


    choice = input('Enter your choice: ')

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print('EXITING.....')
        break
    else:
        print('Invalid Choice...')

## close connection 
mydb.close()
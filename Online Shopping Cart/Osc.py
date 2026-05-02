import pymysql as myconn

mydb = myconn.connect(
    host = 'localhost',
    user = 'root',
    password = 'your_password',
    database = 'Shopkit',
    auth_plugin = 'mysql_native_password'
)

# DATABASE CREATED!-------------------------------------------------
db_cursor = mydb.cursor()
db_cursor.execute("CREATE DATABASE IF NOT EXISTS Shopkit")

## TABLE CREATED!----------------------------------------------------
db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price INT)
""")

# Insert data using this -- to make compartible in different os
# db_cursor.execute("INSERT INTO products VALUES"
#     (1, 'Laptop', 50000),
#     (2, 'Smartphone', 20000),
#     (3, 'Headphones', 2000),
#     (4, 'Keyboard', 1000),
#     (5, 'Mouse', 500),
#     (6, 'Monitor', 12000),
#     (7, 'Printer', 8000),
#     (8, 'USB Drive', 700),
#     (9, 'Power Bank', 1500),
#     (10, 'Smart Watch', 3000))

cart = []

# SHOW_PRODUCT()!------------------------------------------------------
def show_products():
    try:
        db_cursor.execute("SELECT * FROM products")
        products = db_cursor.fetchall()

        print('\nAvailable Products:')
        for p in products:
            print(f"ID:{p[0]}  NAME:{p[1]}  PRICE:{p[2]}")

    except Exception as e:
        print('Error Fetching Products:',e)

# ADD_TO_CART()!-----------------------------------------------------
def add_to_cart():
    try:
        pid = int(input('Enter the Product ID: '))
        db_cursor.execute("SELECT * FROM products WHERE id = %s",(pid,))
        product = db_cursor.fetchone()

        if product:
            cart.append(product)
            print('Product added to cart!')
        else:
            print('Product not Found!')
    except ValueError:
        print('Invalid input! Please enter a number.')
    except Exception as e:
        print("Error:",e)


# VIEW_CART()!---------------------------------------------------------
def view_cart():
    try:
        if len(cart) == 0:
            print("Cart is empty!")
            return
        
        total = 0
        print("\n Items in your cart:")

        for item in cart:
            name = item[1]
            price = item[2]
        
            print(name,"- Rs",price)

            total = total + price
        
        print("Total price =", total)

    except Exception as e:
        print("Error:",e)

# REMOVE_FROM_CART():
def remove_from_cart():
    try:
        if len(cart) == 0:
            print("Cart is empty!")
            return
        
        pid = int(input('Enter Product ID to remove:'))

        for item in cart:
            if item[0] == pid:
                cart.remove(item)
                print("Item removed successfully!")
                return
            
        print("Item not found in cart!")

    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print("Error!",e)

# MENU!----------------------------------------------------------

while True:
    print("======== WELCOME TO SHOPKIT========")
    print(" 1. SHOW PRODUCT ")
    print(" 2. ADD TO CART PRODUCT ")
    print(" 3. VIEW CART ")
    print(" 4. REMOVE PRODUCT ")
    print(" 5. EXIT ")

    try:
        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            show_products()
        elif choice == 2:
            add_to_cart() 
        elif choice == 3:
            view_cart()
        elif choice == 4:
            remove_from_cart()
        elif choice == 5:
            print("Exiting... ThankYou For Shopping.")
            break
        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print("Unexpected Error:",e)

## close connection 
mydb.close()

        





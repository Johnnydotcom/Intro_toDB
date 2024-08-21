import mysql.connector

# Replace with your connection details
try :
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="alx_book_store"
)

    #print(mydb.get_server_info())

    mycursor = mydb.cursor()

    mycursor.execute("""
    CREATE DATABASE IF NOT EXISTS alx_book_store;
    """)

    print("Database 'alx_book_store' created successfully!")
except Exception:
    mysql.connector.Error
finally :
    mycursor.close()
    mydb.close()
    print("Database connection closed.")


import mysql.connector
from mysql.connector import errorcode, MySQLConnection

try:
    # Establishing the database connection
    db_connection = mysql.connector.connect(
        user='admin', 
        password='senai115', 
        host='localhost',  # Add host if not default
        port='3306', 
        database='Borba'
    )
    
    print("Database connection made!")

    # If connection is successful, create a cursor and execute a command
    cursor = db_connection.cursor()
    sql = "SELECT * FROM some_table;"  # Example query - Replace with your SQL command
    cursor.execute(sql)
    
    # Fetch and print results (if any)
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print("Error:", error)

finally:
    # Always close the connection and cursor to prevent memory leaks
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Database connection closed.")

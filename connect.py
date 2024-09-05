import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    connection = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable

    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Host where MySQL is running
            database='scraper_db',  # Name of the database
            user='root',  # Your MySQL username
            password='5trathm0re.'  # Your MySQL password
        )

        if connection.is_connected():
            # Check the connection
            db_info = connection.get_server_info()
            print(f"Connected to MySQL server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()
            print(f"You're connected to the database: {database_name}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if cursor and cursor.is_connected():
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Call the function
connect_to_mysql()

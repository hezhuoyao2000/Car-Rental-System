import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """Creating a Database Connection"""
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except Error as e:
        print(e)
    return connection

def initialize_database(connection):                                     # Initializing the database with the schema.sql file
    """initializing the database with the schema.sql file """
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')  # Dynamic construction of paths
    with open(schema_path, 'r') as f:
        sql_script = f.read()
    try:
        connection.executescript(sql_script)
        print("Database tables initialized.")
    except Error as e:
        print(e)


def test_database():
    #the name of the database file
    db_file = "car_rental.db"

    #create a database connection
    connection = create_connection(db_file)
    if connection is not None:
        # 初始化数据库
        initialize_database(connection)

        #test if the database file is created successfully
        import os
        if os.path.exists(db_file):
            print(f"Database file '{db_file}' created successfully.")
        else:
            print(f"Database file '{db_file}' not found.")

        #test the struture of the database
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        except Error as e:
            print(e)

        #close the database connection
        connection.close()
    else:
        print("Failed to create database connection.")


#run the test function
#test_database()
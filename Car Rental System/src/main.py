from database.database_connections import create_connection, initialize_database
from cli.main_menu import main

if __name__ == "__main__":
    db_file = "database/car_rental.db"
    connection = create_connection(db_file)
    if connection is not None:
        initialize_database(connection)
        main(connection)
        connection.close()
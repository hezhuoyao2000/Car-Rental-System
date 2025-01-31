from database.database_connections import create_connection, initialize_database
from cli.main_menu import main

import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

if __name__ == "__main__":
    db_file = "./car_rental.db"
    connection = create_connection(db_file)
    if connection is not None:
        initialize_database(connection)
        main(connection)
        connection.close()
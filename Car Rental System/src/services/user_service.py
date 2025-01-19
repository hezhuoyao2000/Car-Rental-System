from src.database.database_operations import User_operations
from src.models.user import User

class user_Service:
    @staticmethod
    def login(connection, username, password):
        user_data = User_operations.get_user_by_username(connection, username)
        if user_data and user_data[2] == password:  # user_data[2] is password
            return User(user_data[0], user_data[1], user_data[2], user_data[3])
        return None

    @staticmethod
    def register(connection, username, password, user_role, first_name=None, last_name=None, phone_number=None):
        if User_operations.get_user_by_username(connection, username):
            return False
        user_id = User_operations.add_user(connection, username, password, user_role, first_name, last_name, phone_number)
        return user_id is not None
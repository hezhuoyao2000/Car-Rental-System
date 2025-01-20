class User:
    def __init__(self, user_id, user_name, password, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_role = user_role

class Customer(User):
    def __init__(self, user_id, username, password, first_name, last_name, phone_number):
        super().__init__(user_id, username, password, user_role = "customer")
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class Admin(User):
    def __init__(self, user_id, username, password, admin_name):
        super().__init__(user_id, username, password, user_role = "admin")
        self.admin_name = admin_name

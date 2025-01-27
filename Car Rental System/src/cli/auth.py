from src.services.user_service import user_Service

def login(connection):

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = user_Service.login(connection, username, password)
        if user:
            print("Login successful!")
            #print(f"User role: {user.user_role}")      #for test 

            if user.user_role == "customer":
                from src.cli.customer_menu import customer_menu
                customer_menu(connection)
                break
            elif user.user_role == "admin":
                from src.cli.admin_menu import admin_menu
                admin_menu(connection)
                break
        else:
            print("Invalid username or password.")
            retry = input("Enter 1 to try again or 2 to abort: ").strip()
            if retry == '2':
                print("Login Abandoned.")
                break


def register(connection):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    phone_number = input("Enter phone number: ")

    while True:
        role_input = input("Enter your role (1 for admin, 2 for customer): ")

        if role_input == "1":
            user_role = "admin"
            break
        elif role_input == "2":
            user_role = "customer"
            break
        else:
            print("Invalid input. Please enter 1 for admin or 2 for user.")

    #determine first and last name based on username
    #if username contains underscore, split at the underscore
    if "_" in username:
        first_name, last_name = username.split("_", 1)
    elif " " in username:
        first_name, last_name = username.split(" ", 1)
    else:
        #if no space or underscore in username, assume first name is username and last name is empty
        first_name = username
        last_name = ""

    if user_Service.register(connection, username, password, user_role, first_name, last_name, phone_number):
        print(f"Registration successful! Welcome, {username} ({user_role}).")
    else:
        print("Username already exists. Please try again with a different username.")
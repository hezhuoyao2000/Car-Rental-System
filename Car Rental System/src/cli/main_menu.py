from src.cli.auth import login, register

def display_main_menu(connection):
    print("\n=== Car Rental System ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

def main(connection):
    while True:
        display_main_menu(connection)
        choice = input("Enter your choice: ")
        if choice == "1":                                           # Login
            login(connection)
            print("Logged in the system.")

        elif choice == "2":                                         # Register
            register(connection)

        elif choice == "3":                                         # Exit the system
            print("Logged out the system.")
            break
        else:
            print("Invalid choice. Please try again.")
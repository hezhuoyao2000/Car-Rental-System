from src.services import car_service


def customer_menu(connection):
    while True:
        print("\n=== Customer Menu ===")
        print("1. Browse Available Cars")
        print("2. Book a Car")
        print("3. View Rental Details")
        print("4. Logout")

        choice = input("\nEnter your choice(number 1-4): ")

        if choice == "1":
            pass
            """car_service.()"""

        elif choice == "2":
            car_service.book_car()

        elif choice == "3":
            car_service.view_rental_details()

        elif choice == "4":
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

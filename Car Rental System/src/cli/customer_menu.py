from src.services import car_service


def customer_menu(connection):
    while True:
        print("\n=== Customer Menu ===")
        print("1. Browse Available Cars")
        print("2. Book a Car")
        print("3. View Rental Details")
        print("4. Logout")

        choice = input("\nEnter your choice(number1-4): ")

        if choice == "1":
            car_service.()

        elif choice == "2":
            car_service.book_car()

        elif choice == "3":
            car_service.view_rental_details()

        elif choice == "4":
            break



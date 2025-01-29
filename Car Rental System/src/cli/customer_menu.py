from src.services import car_service
from src.services.booking_service import CustomerService
from datetime import datetime

def customer_menu(connection):
    while True:
        print("\n=== Customer Menu ===")
        print("1. Browse Available Cars")
        print("2. Book a Car")
        print("3. View Rental Details")
        print("4. Logout")

        choice = input("\nEnter your choice(number 1-4): ")

        if choice == "1":
            try:
                available_cars = CustomerService.get_available_cars(connection)

                if available_cars:
                    print("\nAvailable Cars:")
                    print("-" * 60)
                    print(f"{'ID':<5}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Availability':<15}")
                    print("-" * 60)
                    for car in available_cars:
                        car_id, make, model, year, mileage, availability = car
                        print(
                            f"{car_id:<5}{make:<15}{model:<15}{year:<10}{mileage:<10}{'Available' if availability else 'Not Available':<15}")
                    print("-" * 60)
                else:
                    print("\nNo available cars found.")

            except Exception as e:
                print(f"Error fetching available cars: {e}")


        elif choice == "2":
            try:
                car_id = input("Enter the car ID you want to book: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")

                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                if start_date >= end_date:
                    print("Start date must be before end date.")
                    continue

                car = car_service.get_car_details(connection, car_id)
                if not car:
                    print("Car not found.")
                    continue

                make, model, year, mileage, availability, daily_price = car
                if not availability:
                    print("This car is not available.")
                    continue

                total_days = (end_date - start_date).days + 1
                total_cost = total_days * daily_price

                customer_id = 1
                booking_id = CustomerService.book_car(connection, customer_id, car_id, start_date, end_date, total_cost)

                if booking_id:
                    print(f"Booking successful! Your booking ID is {booking_id}.")
                else:
                    print("Booking failed.")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"Error booking car: {e}")


        elif choice == "3":
            CustomerService.view_rental_details()


        elif choice == "4":
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

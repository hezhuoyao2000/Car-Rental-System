from src.services import car_service
from src.services.booking_service import CustomerService
from datetime import datetime
from src.cli.auth import current_user_id

def customer_menu(connection):
    while True:
        print("\n=== Customer Menu ===")
        print("1. Browse Available Cars")
        print("2. Book a Car")
        print("3. View Rental Details")
        print("4. Logout")

        choice = input("\nEnter your choice(number 1-4): ")

        if choice == "1":                       # Browse Available Cars
            try:
                available_cars = CustomerService.get_available_cars(connection)

                if available_cars:              # show the table of available cars
                    print("\nAvailable Cars:")
                    print("-" * 80)
                    print(f"{'ID':<5}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Price/Day':<10}{'Availability':<15}")
                    print("-" * 80)
                    for car in available_cars:
                        car_id, make, model, year, mileage, availability, daily_rent = car
                        print(
                            f"{car_id:<5}{make:<15}{model:<15}{year:<10}{mileage:<10}{daily_rent:<10}{'Available' if availability else 'Not Available':<15}")
                    print("-" * 80)
                else:
                    print("\nNo available cars found.")

            except Exception as e:
                print(f"Error fetching available cars: {e}")


        elif choice == "2":                     # Book a Car
            try:
                car_id = input("Enter the car ID you want to book: ")                # input the target car ID
                start_date = input("Enter start date (YYYY-MM-DD): ")                # choose the start adn end date for the rental
                end_date = input("Enter end date (YYYY-MM-DD): ")

                start_date = datetime.strptime(start_date, "%Y-%m-%d")        # convert the input date to datetime object
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                if start_date >= end_date:
                    print("Start date must be before end date.")
                    continue

                car = car_service.Car_Service.get_car_details(connection, car_id)
                if not car:
                    print("Car not found.")
                    continue

                car_id, make, model, year, mileage, availability, daily_rent = car
                if not availability:
                    print("This car is not available.")
                    continue

                total_days = (end_date - start_date).days + 1
                total_cost = total_days * daily_rent

                customer_id = current_user_id
                booking_id = CustomerService.book_car(connection, customer_id, car_id, start_date, end_date, total_cost, status = "pending")

                if booking_id:
                    print(f"Booking successful! Your booking ID is {booking_id}.")
                else:
                    print("Booking failed.")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"Error booking car: {e}")


        elif choice == "3":
            try:
                rental_details = CustomerService.get_rental_details(connection, current_user_id)
                if rental_details:
                    print("\nYour Rental Details:")
                    print("-" * 140)
                    print(
                        f"{'Booking ID':<12}{'Car ID':<10}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Start Date':<22}{'End Date':<22}{'Total Cost':<15}{'Status':<8}")
                    print("-" * 140)
                    for detail in rental_details:
                        print(
                            f"{detail['booking_id']:<12}{detail['car_id']:<10}{detail['make']:<15}{detail['model']:<15}{detail['year']:<10}{detail['mileage']:<10}{detail['start_time']:<22}{detail['end_time']:<22}{detail['total_cost']:<15}{detail['status']:<8}")
                    print("-" * 140)
                else:
                    print("\nYou have no rental details.")
            except Exception as e:
                print(f"Error fetching rental details: {e}")

        elif choice == "4":
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

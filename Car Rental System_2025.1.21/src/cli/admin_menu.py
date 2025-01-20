from src.services.car_service import Car_Service

def admin_menu(connection):
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add a Cars")
        print("2. Remove a Car")
        print("3. Update car details")
        print("4. Logout")

        choice = input("\nEnter your choice(number1-4): ")

        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            manufacture_year = input("Enter car manufacture year: ")
            mileage = input("Enter car mileage: ")

            if Car_Service.add_car(connection, make, model, manufacture_year, mileage, availability = True):
                print("Car added successfully!")
            else:
                print("Failed to add car.")

        elif choice == "2":
            car_id = input("Enter car id to remove: ")
            if Car_Service.remove_car(connection, car_id):
                print("Car removed successfully!")
            else:
                print("Failed to remove car.")

        elif choice == "3":
            car_id = input("Enter car id to update: ")
            make = input("Enter new make (press enter to keep current): ")
            model = input("Enter new model (press enter to keep current): ")
            manufacture_year = input("Enter new manufacture year (press enter to keep current): ")
            mileage = input("Enter new mileage (press enter to keep current): ")
            availability = input("Enter new availability (True/False): ")

            if Car_Service.update_car_details(connection, car_id, make, model, manufacture_year, mileage, availability):
                print("Car details updated successfully!")
            else:
                print("Failed to update car details.")

        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



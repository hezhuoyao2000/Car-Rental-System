from services.car_service import Car_Service
from services.booking_service import Admin_Service

def admin_menu(connection):
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add a Cars")
        print("2. Remove a Car")
        print("3. Update car details")
        print("4. Browse Orders")
        print("5. Manage Orders")
        print("6. Logout")

        choice = input("\nEnter your choice(number1-6): ")

        if choice == "1":                                                   # Add a Cars
            make = input("Enter car make: ")                                # input all information of car
            model = input("Enter car model: ")
            manufacture_year = input("Enter car manufacture year: ")
            mileage = input("Enter car mileage: ")
            daily_rent = input("Enter car daily rent: ")

            if Car_Service.add_car(connection, make, model, manufacture_year, mileage, daily_rent, availability = True):
                print("Car added successfully!")
            else:
                print("Failed to add car.")

        elif choice == "2":                                                 # Remove a Car
            car_id = input("Enter car id to remove: ")
            if Car_Service.remove_car(connection, car_id):
                print("Car removed successfully!")
            else:
                print("Failed to remove car.")

        elif choice == "3":                                                 # Update car details
            car_id = input("Enter car id to update: ")                      # Selecting the target car using the ID
            current_car = Car_Service.get_car_details(connection, car_id)
            if not current_car:
                print("Car not found.")
                continue

            print("\nCurrent Car Details:")                                 # Displaying the current car details before update
            print(f"Make: {current_car[0]}")
            print(f"Model: {current_car[1]}")
            print(f"Manufacture Year: {current_car[2]}")
            print(f"Mileage: {current_car[3]}")
            print(f"Availability: {current_car[4]}")
            print(f"Daily Rent: {current_car[5]}")

            make = input("Enter new make (press enter to keep current): ")  # Input new details for the car
            model = input("Enter new model (press enter to keep current): ")
            manufacture_year = input("Enter new manufacture year (press enter to keep current): ")
            mileage = input("Enter new mileage (press enter to keep current): ")
            availability_input  = input("Enter new availability (Please enter number 1 or 0 for True/False,press enter to keep current): ")
            daily_rent = input("Enter new daily rent (press enter to keep current): ")

            if not make:                                                   # If no input is given(or if user enters nothing), keep the current value
                make = current_car[0]
            if not model:
                model = current_car[1]
            if not manufacture_year:
                manufacture_year = current_car[2]
            if not mileage:
                mileage = current_car[3]
            if not daily_rent:
                daily_rent = current_car[5]
            if availability_input == "":
                availability = current_car[4]  # 保留原值
            elif availability_input == "1":
                availability = True
            elif availability_input == "0":
                availability = False
            else:
                print("Invalid input for availability. Keeping current value.")
                availability = current_car[4]

            if Car_Service.update_car_details(connection, car_id, make, model, manufacture_year, mileage, availability, daily_rent):
                print("Car details updated successfully!")
            else:
                print("Failed to update car details.")

        elif choice == "4":                                                # Browse Orders
            print("\n=== Browse Orders ===")
            print("1. View All Orders")
            print("2. View Unapproved Orders")
            order_choice = input("Enter your choice (1 or 2): ")

            if order_choice == "1":                                        # View All Orders
                Admin_Service.view_all_orders(connection)
            elif order_choice == "2":                                      # View Unapproved Orders
                Admin_Service.view_unapproved_orders(connection)
            else:
                print("Invalid choice. Please try again.")

        elif choice == "5":                                                # Manage orders, approve or reject orders
            Admin_Service.manage_orders(connection)

        elif choice == "6":                                                # Logout
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")



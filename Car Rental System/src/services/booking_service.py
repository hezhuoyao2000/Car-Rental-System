from database.database_operations import Booking_Operations
from database.database_operations import Car_Operations

class CustomerService:

    @staticmethod
    def display_available_cars(connection):                         # used in customer_menu
        try:
            available_cars = CustomerService.get_available_cars(connection)

            if available_cars:                                      # show the table of available cars
                print("\nAvailable Cars:")
                print("-" * 80)
                print(
                    f"{'ID':<5}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Price/Day':<10}{'Availability':<15}")
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


    @staticmethod
    def get_available_cars(connection):
        return Booking_Operations.get_available_cars(connection)

    @staticmethod
    def book_car(connection, customer_id, car_id, start_time, end_time, total_cost, status):
        return Booking_Operations.create_booking(connection, customer_id, car_id, start_time, end_time, total_cost, status)

    @staticmethod
    def get_user_bookings(connection, customer_id):
        return Booking_Operations.get_user_bookings(connection, customer_id)

    @staticmethod
    def get_rental_details(connection, customer_id):
        user_bookings = Booking_Operations.get_user_bookings(connection, customer_id)
        if not user_bookings:
            return []

        # get car details for each booking
        rental_details = []
        for booking in user_bookings:
            booking_id, customer_id, car_id, start_time, end_time, total_cost, status = booking
            car_details = Car_Operations.get_car_details(connection, car_id)
            if car_details:
                car_id, make, model, year, mileage, availability, daily_rent= car_details

                status_display = {
                    'pending': 'pending',
                    'Approved': 'Approved',
                    'Rejected': 'Rejected'
                }.get(status, 'Unknown')  # 防止未知状态

                rental_details.append({
                    'booking_id': booking_id,
                    'car_id': car_id,
                    'make': make,
                    'model': model,
                    'year': year,
                    'mileage': mileage,
                    'start_time': start_time,
                    'end_time': end_time,
                    'total_cost': total_cost,
                    'status': status_display
                })
        return rental_details



    """used in customer_menu"""
class Admin_Service:
    @staticmethod
    def view_all_orders(connection):
        sql = '''SELECT b.booking_id, b.customer_id, b.car_id, b.start_time, b.end_time, b.total_cost, b.status, c.make, c.model, c.manufacture_year, c.mileage
                 FROM bookings b
                 JOIN cars c ON b.car_id = c.car_id'''
        cur = connection.cursor()
        cur.execute(sql)
        bookings = cur.fetchall()

        if not bookings:
            print("No orders found.")
            return

        print("\nAll Orders:")
        print("-" * 140)
        print(f"{'Booking ID':<12}{'Car ID':<10}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Start Date':<22}{'End Date':<22}{'Total Cost':<15}{'Status':<8}")
        print("-" * 140)
        for booking in bookings:
            booking_id, customer_id, car_id, start_time, end_time, total_cost, status, make, model, year, mileage = booking
            print(f"{booking_id:<12}{car_id:<10}{make:<15}{model:<15}{year:<10}{mileage:<10}{start_time:<22}{end_time:<22}{total_cost:<15}{status:<8}")
        print("-" * 140)

    @staticmethod
    def view_unapproved_orders(connection):
        sql = '''SELECT b.booking_id, b.customer_id, b.car_id, b.start_time, b.end_time, b.total_cost, b.status, c.make, c.model, c.manufacture_year, c.mileage
                 FROM bookings b
                 JOIN cars c ON b.car_id = c.car_id
                 WHERE b.status = 'pending' '''
        cur = connection.cursor()
        cur.execute(sql)
        bookings = cur.fetchall()

        if not bookings:
            print("No unapproved orders found.")
            return False

        print("\nUnapproved Orders:")
        print("-" * 140)
        print(f"{'Booking ID':<12}{'Car ID':<10}{'Make':<15}{'Model':<15}{'Year':<10}{'Mileage':<10}{'Start Date':<22}{'End Date':<22}{'Total Cost':<15}{'Status':<8}")
        print("-" * 140)
        for booking in bookings:
            booking_id, customer_id, car_id, start_time, end_time, total_cost, status, make, model, year, mileage = booking
            print(f"{booking_id:<12}{car_id:<10}{make:<15}{model:<15}{year:<10}{mileage:<10}{start_time:<22}{end_time:<22}{total_cost:<15}{status:<8}")
        print("-" * 140)


    @staticmethod
    def manage_orders(connection):

        if Admin_Service.view_unapproved_orders(connection):
            print("No unapproved orders to process. Returning to Admin Menu.")
            return                             # if no unapproved orders, return to admin menu

        booking_id = input("Enter the booking ID you want to process: ")
        if not booking_id.isdigit():
            print("Invalid booking ID. Please enter a valid number.")
            return

        booking_id = int(booking_id)
        print("\n1. Approve Booking")
        print("2. Reject Booking")
        action_choice = input("Enter your choice (1 or 2): ")

        if action_choice == "1":
            Admin_Service.approve_booking(connection, booking_id)
        elif action_choice == "2":
            Admin_Service.reject_booking(connection, booking_id)
        else:
            print("Invalid choice. Please try again.")


    @staticmethod
    def approve_booking(connection, booking_id):
                                                    # Update booking status
        sql = '''UPDATE bookings                     
                 SET status = 'Approved' 
                 WHERE booking_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (booking_id,))
        connection.commit()
                                                    # Update car availability
        sql = '''UPDATE cars                        
                 SET availability = 0 
                 WHERE car_id IN (SELECT car_id FROM bookings WHERE booking_id = ?)'''
        cur.execute(sql, (booking_id,))
        connection.commit()

        print(f"Booking {booking_id} approved successfully.")


    @staticmethod
    def reject_booking(connection, booking_id):
        # Update booking status
        sql = '''UPDATE bookings 
                 SET status = 'Rejected' 
                 WHERE booking_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (booking_id,))
        connection.commit()

        # Update car availability
        sql = '''UPDATE cars 
                 SET availability = 1 
                 WHERE car_id IN (SELECT car_id FROM bookings WHERE booking_id = ?)'''
        cur.execute(sql, (booking_id,))
        connection.commit()

        print(f"Booking {booking_id} rejected successfully.")

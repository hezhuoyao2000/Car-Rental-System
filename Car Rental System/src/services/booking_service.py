from src.database.database_operations import Booking_Operations

class CustomerService:
    @staticmethod
    def get_available_cars(connection):
        return Booking_Operations.get_available_cars(connection)

    @staticmethod
    def book_car(connection, customer_id, car_id, start_time, end_time, total_cost):
        return Booking_Operations.create_booking(connection, customer_id, car_id, start_time, end_time, total_cost)

    @staticmethod
    def get_user_bookings(connection, customer_id):
        return Booking_Operations.get_user_bookings(connection, customer_id)


    """used in customer_menu"""

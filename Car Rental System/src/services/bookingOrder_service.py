from src.database.database_operations import Booking_Operations

class BookingService:
    @staticmethod
    def book_car(conn, customer_id, car_id, start_time, end_time, total_cost):
        return Booking_Operations.create_booking(conn, customer_id, car_id, start_time, end_time, total_cost)

    @staticmethod
    def get_user_bookings(conn, customer_id):
        return Booking_Operations.get_user_bookings(conn, customer_id)
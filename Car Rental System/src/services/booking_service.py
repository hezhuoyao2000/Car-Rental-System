from src.database.database_operations import Booking_Operations
from src.database.database_operations import Car_Operations

class CustomerService:
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
                    'Pending': 'Pending',
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
    def approve_booking(connection):
        pass

    @staticmethod
    def reject_booking(connection):
        pass
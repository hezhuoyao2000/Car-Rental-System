from datetime import datetime

class bookingOrder:
    def __init__(self, booking_id, customer_id, car_id, start_time, end_time, total_cost, status=False):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_time = start_time
        self.end_time = end_time
        self.total_cost = total_cost
        self.status = status
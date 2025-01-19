from src.database.database_operations import Car_Operations

class Car_Service:
    @staticmethod
    def add_car(connecion, make, model, manufacture_year, milage, availability):
        return Car_Operations.add_car(connecion, make, model, manufacture_year, milage, availability)

    @staticmethod
    def remove_car(connecion, car_id):
        return Car_Operations.remove_car(connecion, car_id)

    @staticmethod
    def update_car_details(connecion, car_id, make, model, manufacture_year, milage, availability):
        return Car_Operations.update_car_details(connecion, car_id, make, model, manufacture_year, milage, availability)

    @staticmethod
    def get_car_details(connecion):
        return Car_Operations.get_car_details(connecion)

    @staticmethod
    def book_car(connecion, car_id, customer_id, start_date, end_date):
        pass

    """@staticmethod
    def view_rental_details():
        pass"""

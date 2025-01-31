from database.database_operations import Car_Operations

class Car_Service:


    """used in admin_menu"""
    @staticmethod
    def add_car(connecion, make, model, manufacture_year, mileage, daily_rent, availability):
        return Car_Operations.add_car(connecion, make, model, manufacture_year, mileage, availability, daily_rent)

    @staticmethod
    def remove_car(connecion, car_id):
        return Car_Operations.remove_car(connecion, car_id)

    @staticmethod
    def update_car_details(connecion, car_id, make, model, manufacture_year, mileage, availability, daily_rent):
        return Car_Operations.update_car_details(connecion, car_id, make, model, manufacture_year, mileage, availability, daily_rent)

    @staticmethod
    def get_car_details(connecion, car_id):
        return Car_Operations.get_car_details(connecion, car_id)

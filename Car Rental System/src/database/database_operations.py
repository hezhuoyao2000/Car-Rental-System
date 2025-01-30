from datetime import datetime

class User_operations:

    @staticmethod
    def add_user(connection, username, password, user_role, first_name=None, last_name=None, phone_number=None):

        sql = '''INSERT INTO users(username, password, user_role, first_name, last_name, phone_number)
                 VALUES(?,?,?,?,?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password, user_role, first_name, last_name, phone_number))
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def get_user_by_username(connection, username):
        sql = '''SELECT * FROM users WHERE username = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (username,))
        return cursor.fetchone()


class Car_Operations:
    @staticmethod
    def add_car(connection, make, model, manufacture_year, mileage, availability, daily_rent):
        sql = '''INSERT INTO cars(make, model, manufacture_year, mileage, availability, daily_rent) VALUES(?,?,?,?,?,?)'''
        cur = connection.cursor()
        cur.execute(sql, (make, model, manufacture_year, mileage, availability, daily_rent))
        connection.commit()
        return cur.lastrowid

    @staticmethod
    def remove_car(connection, car_id):
        sql = '''DELETE FROM cars WHERE car_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (car_id,))
        connection.commit()
        return cur.rowcount

    @staticmethod
    def update_car_details(connection, car_id, make, model, manufacture_year, mileage, availability):
        sql = '''UPDATE cars SET make =?, model =?, manufacture_year =?, mileage =?, availability =? WHERE car_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (make, model, manufacture_year, mileage, availability, car_id))
        connection.commit()
        return cur.rowcount

    @staticmethod
    def get_car_details(connection, car_id):
        sql = '''SELECT car_id, make, model, manufacture_year, mileage, availability , daily_rent 
                 FROM cars 
                 WHERE car_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (car_id,))
        return cur.fetchone()


class Booking_Operations:
    @staticmethod
    def get_available_cars(connection):
        sql = '''SELECT car_id, make, model, manufacture_year, mileage, availability, daily_rent 
                 FROM cars 
                 WHERE availability = 1'''
        cur = connection.cursor()
        cur.execute(sql)
        return cur.fetchall()

    @staticmethod
    def create_booking(connection: object, customer_id: object, car_id: object, start_time: object, end_time: object, total_cost: object, status: object) -> object:
        sql = '''INSERT INTO bookings(customer_id, car_id, start_time, end_time, total_cost, status)
                 VALUES(?,?,?,?,?,?)'''
        cur = connection.cursor()
        cur.execute(sql, (customer_id, car_id, start_time, end_time, total_cost, status))
        connection.commit()
        return cur.lastrowid

    @staticmethod
    def get_user_bookings(connection, customer_id):
        sql = '''SELECT * FROM bookings WHERE customer_id = ?'''
        cur = connection.cursor()
        cur.execute(sql, (customer_id,))
        return cur.fetchall()


"""class admin_Booking_management_Operations:
    @staticmethod
    def approve_booking(connection, booking_id):"""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    user_role TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT
);

CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacture_year INTEGER NOT NULL,
    mileage REAL NOT NULL,
    availability BOOLEAN DEFAULT TRUE,
    daily_rent REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    total_cost REAL NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES users(user_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
);
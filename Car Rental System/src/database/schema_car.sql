

CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacture_year INTEGER NOT NULL,
    mileage REAL NOT NULL,
    availability BOOLEAN DEFAULT TRUE,
    daily_rent REAL NOT NULL
);

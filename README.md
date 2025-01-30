##update 2025.1.28
1. Repair the problem of not being able to return to the main menu when logging out from the customer interface and administrator interface.

  (1)in __auth.py__ file, changed the login(connection) function  
                          and add break after __customer_menu(connection)__ and __admin_menu(connection)__.  
  (2)in admin_menu.py file, changed __admin_menu(connection)__ function, replace break with return in choice == “4”.  
  (3)in __customer_menu.py file, changed __customer_menu(connection)__ function, replace break with return in choice == “4”.  


2. optimize the admin_menu(connection) function in admin_menu.py file.

  (1)choice == “3”.  
  build press enter to keep current function, and use 1 and 0 to select the availability of the car


##update 2025.1.29
3.  built the feature Browse Available Cars

  (1)in __customer_menu__ file, in __customer_menu__ function, added the feature __Browse Available Cars__ .  
  (2)in file __customer_memu.py__, Improved the __customer_menu(connection)__ function under __choice == “1”__.  
  (3)In __database_operation.py__ file, in class __Booking_Operations__, added function __get_available_cars(connection)__.  
  (4)Create a new file __booking_service.py__, and add the functions __get_available_cars(connection)___   
                                                                    and __book_car()__   
                                                                    and __get_user_bookings(connection, customer_id)__ transferred here  


4.  add feature __daily_rent__  
  (1)in __customer_menu()__ file, in __customer_menu()__ function, in __choice = “2”__, build the feature of __Book a Car__  
  (2)add information __daily_rent__ to __car__ table.  
  (3)Modified the content of __customer_menu.py__ file under the __choice == “2”__.  
  (4)Changed __schema.sql__ file to include __daily_rent__ column in __cars__ table.  
  (5)in __database_operations.py__, added __daily_rent__ to __add_car()__ function  


##update 2025.1.30
5. Added the ability to recognize user ids when a user makes a reservation.
(1)in __auth.py__ file , __login(connection)__ function, add __global current_user_id__ and __current_user_id = user.user_id__
(2)in __customer_menu.py__ file, in __choice == "2":__, add __customer_id = current_user_id__

6. fixed the table showing ability in __customer_menu__
(1)in __customer_menu.py__ file, in __choice == "1":__, add __daily_rent__

7. built the ability __View Rental Details__
(1)in __customer_menu.py__ file, in __choice == "3"__, added the code of building a table to show all rental details
(2)changed status of booking from 2 status to 3 status, and showing it in table


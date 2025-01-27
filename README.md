1. Repair the problem of not being able to return to the main menu when logging out from the customer interface and administrator interface.

      (1)Modify the login(connection) function in auth.py file and add break.  
      Add break after customer_menu(connection) and admin_menu(connection).  
      (2)Modify admin_menu(connection)) function in admin_menu.py file  
      Replace break with return in choice == “4”.  
      (3)Modify customer_menu(connection) function in customer_menu.py file.  
      Replace break with return in choice == “4”.  


2. optimize the admin_menu(connection) function in admin_menu.py file.  

      (1)choice == “3”.  
      realize press enter to keep current function, and use 1 and 0 to select the availability of the car  

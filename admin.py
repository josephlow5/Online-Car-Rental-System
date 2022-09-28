#LOW JIA QUAN
#TP063436

#THE FILE HANDLE ALL FUNCTION RELATED TO ADMIN

import file_handling

def login():
    print("===============================================")
    print("========== WELCOME TO THE ADMIN PAGE ==========")
    print("===============================================\n")

    #ASK TO VERIFY IDENTITY
    print("Hi, please verify your identity by entering username and password.")
    

    #LET USER INPUT THE USERNAME AND PASSWORD
    input_username = input("Your username: ")
    input_password = input("Your password: ")

    #ACTION FOR THE INPUT
    print("\n")
    if input_username=="admin" and input_password=="nimda":
        menu()
    else:
        print("Sorry, the username or password is invalid.")

        #ASK THE USER WANTS TO TRY AGAIN OR LEAVE
        input_tryagain = input("Enter T to try again: ").upper()

        #ACTION FOR THE ANSWER
        print()
        if input_tryagain == "T":
            login()
        else:
            print("Good Bye and Have a nice day!")
            exit()


def menu():
    print("====================================================")
    print("========== WELCOME TO THE ADMIN HOME PAGE ==========")
    print("====================================================\n")

    #SHOW ALL ACTION AVAILABLE FOR ADMIN
    print("Welcome, dear admin. Please choose what you want to do from below:\n")
    print("1. Add Car to be rented out")
    print("2. Modify Car Details")
    print("3. Display All records")
    print("4. Search Specific record")
    print("5. Return a Rented Car")
    print("6. Exit\n")
    
    #ASK FOR THE CHOICE
    input_choice = input("I want to (Enter 1/2/3/4/5/6): ")

    #ACTION FOR THE ANSWER
    print()
    if input_choice == "1":
        add_car()
    elif input_choice == "2":
        mod_car()
    elif input_choice == "3":
        display_records()
    elif input_choice == "4":
        search_records()
    elif input_choice == "5":
        return_rented_car()
    elif input_choice == "6":
        print("Good Bye and Have a nice day!")
        exit()
    else:
        print("Invalid input! Please enter again.\n\n")
        menu()


def add_car():
    print('Please enter detail of the car:\n')

    #LET USER INPUT THE CAR DETAILS
    input_car_model = input("Car Model: ")
    input_car_type = input("Car Type: ")
    input_car_transmission = input("Car Transmission (A/M): ").upper()
    while not(input_car_transmission=="A" or input_car_transmission=="M"):
        print("Invalid value! Please enter A or M only.")
        input_car_transmission = input("Car Transmission (A/M): ").upper()
    input_hourly_rate = input("Hourly Rent Rate: RM")
    while not(input_hourly_rate.isdigit()):
        print("Invalid value! Please enter again.")
        input_hourly_rate = input("Hourly Rent Rate: RM")

    #USE FUNCTION IN FILE_HANDLING TO ADD CAR
    file_handling.add_car(input_car_model, input_car_type, input_car_transmission, input_hourly_rate)


    #ASK USER WHETHER WANT TO ADD ANOTHER CAR OR BACK TO MENU
    print()
    input_continue = input("Enter Y to add another car: ").upper()

    #ACTION FOR THE ANSWER
    print("\n")
    if(input_continue=="Y"):
        add_car()
    else:
        print("Successfully added car(s)!\n\n")
        menu()


def mod_car():
    #GET ALL DATA ON CARS.TXT AND PRINT OUT
    cars_data = file_handling.get_cars()
    if not cars_data:
        print("There is car registered yet! Taking you back to menu...\n\n")
        menu()
    else:
        for car_data in cars_data:
            print(car_data.replace(",","\t").replace("\n",""))

    #LET USER INPUT THE CAR ID OF TARGET CAR TO BE MODIFIED
    print()
    input_car_id = input("Please enter a car id of car to be modified (Enter X to back):").upper()

    #CHECK IF ENTERED CAR ID EXIST
    FoundCar = False
    TargetCarDataList = []
    for car_data in cars_data:
        car_data_list = car_data.split(',')
        if(car_data_list[0]==input_car_id):
            FoundCar = True
            TargetCarDataList = car_data_list

    if(FoundCar):
        #LET USER CHOOSE INFORMATION TO MODIFY AND ENTER VALUE
        print("\n\nModifiable Car Information:\n\t1. Car Model\n\t2. Car Type\n\t3. Car Trasmission\n\t4. Hourly Rate")
        accepted_input_mod_type = ["1","2","3","4"]

        #LET USER CHOOSE WHICH INFORMATION TO MODIFY
        input_mod_type = input("\nWhich information you want to modify (Enter 1/2/3/4): ")
        while(input_mod_type not in accepted_input_mod_type):
            print("\nInvalid input! Please try again.\n\n")
            input_mod_type = input("\nWhich information you want to modify (Enter 1/2/3/4): ")

        #LET USER INPUT VALUE, IF IT IS TRANSMISSION CHECK IF IT IS A/M
        input_mod_value = input("What is the new value: ")
        if(input_mod_type=="3"):
                input_mod_value = input_mod_value.upper()
                while not(input_mod_value=="A" or input_mod_value=="M"):
                        print("Invalid value! Please enter A or M only.")
                        input_mod_value = input("What is the new value: ")
        if(input_mod_type=="4"):
            while not (input_mod_value.isdigit()):
                    print("Invalid value! Please enter digits only.")
                    input_mod_value = input("What is the new value: ")

        #MODIFY CAR DETAIL BASED ON CAR ID
        file_handling.mod_car(input_car_id, input_mod_type, input_mod_value)
        print("\nSuccessfully modified car detail!")

    else:
        if(input_car_id.upper()=="X"):
            print("\n\n")
            menu()
        else:
            print("\nCar with this car id not found! Please try again.\n\n")
            mod_car()
            
    
    #ASK USER WHETHER WANT TO MOD ANOTHER CAR OR BACK TO MENU
    print()
    input_continue = input("Enter Y to modify another car's detail: ").upper()

    #ACTION FOR THE ANSWER
    print("\n")
    if(input_continue=="Y"):
        mod_car()
    else:
        menu()


def display_records():
    #SHOW ALL RECORD AVAILABLE
    print("Hi, what record you want to check?")
    print("\ta. Cars available for Rent\n\tb. Customer Payment for a specific time duration\n")

    #LET USER INPUT WHAT RECORD
    input_choice = input("I want to check about (please enter A/B, X to back):").upper()

    #ACTION FOR THE INPUT
    print("\n")
    if(input_choice=="A"):
        
        #GET ALL DATA ON CARS.TXT AND PRINT OUT
        cars_data = file_handling.get_cars(rent_available_only=True)
        if not cars_data:
            print("There is no car available for rent now! Taking you back..\n")
            display_records()
        else:
            for car_data in cars_data:
                print(car_data.replace(",","\t").replace("\n",""))
            print()
            menu()
   
    elif(input_choice=="B"):

        #PROMPT USER ABOUT DURATION AND GET CUSTOMER PAYMENT WITHIN THAT PERIOD
        input_recent_days = input("Display customer payment of recent how many days: ")
        while not(input_recent_days.isdigit()):
            print("Invalid value! Please enter again.")
            input_recent_days = input("Display customer payment of recent how many days: ")
        print("\n")
        orders_data = file_handling.get_orders(customers_payment_in_recent_days=input_recent_days)
        if not orders_data:
            print("No customer payment found in recent "+input_recent_days+" days! Taking you back..\n")
        else:
            print("All customer payment in recent "+input_recent_days+" days")
            print("------------------------------------")
            for order_data in orders_data:
                order_data_list = order_data.split(',')
                print("Order ID:"+order_data_list[0]+" (Username:"+order_data_list[1]+"|Full Name:"+
                      file_handling.get_user_data(order_data_list[1], 2)+")\nCar ID:"+order_data_list[2]+
                      "  Rent Hour:"+order_data_list[3]+"  Total Amount:RM"+order_data_list[4]+
                      "  Status:"+order_data_list[5]+"  Order Expiration:"+order_data_list[6].strip("\n")+"\n")
            print("\n")
        menu()
                
    elif(input_choice=="X"):
        print("\n")
        menu()
    else:
        print("Invalid input! Please enter again.\n\n")
        display_records()


def search_records():
    #SHOW ALL OPTIONS AVAILABLE
    print("Hi, what record you want to search for?")
    print("\ta. Specific Car Booking\n\tb. Specific Customer Payment\n")

    #LET USER INPUT OPTION
    input_choice = input("I want to search about (please enter A/B, X to back):").upper()

    #ACTION FOR THE INPUT
    print("\n")
    if(input_choice=="A"):
        
        #GET ALL DATA ON CARS.TXT AND PRINT OUT
        cars_data = file_handling.get_cars()
        if not cars_data:
            print("There is no car available yet! Taking you back..\n")
            search_records()
        else:
            for car_data in cars_data:
                print(car_data.replace(",","\t").replace("\n",""))
            print()

            #ASK USER WHICH CAR TO BE SEARCHED
            print()
            input_car_id = input("Please enter a car id of rented car to be searched (Enter X to back):").upper()

            #CHECK IF ENTERED CAR ID EXIST
            FoundCar = False
            TargetCarDataList = []
            for car_data in cars_data:
                car_data_list = car_data.split(',')
                if(car_data_list[0]==input_car_id):
                    FoundCar = True
                    TargetCarDataList = car_data_list

            if(FoundCar):
                #GET ALL ORDERS OF THIS CAR
                print("\n")
                orders_data = file_handling.get_orders(specific_car=input_car_id)
                if not orders_data:
                    print("No records of this car found! Taking you back..\n")
                else:
                    print("All record of the car "+input_car_id)
                    print("------------------------------------")
                    for order_data in orders_data:
                        order_data_list = order_data.split(',')
                        print("Order ID:"+order_data_list[0]+" (Username:"+order_data_list[1]+"|Full Name:"+
                              file_handling.get_user_data(order_data_list[1], 2)+")\nCar ID:"+order_data_list[2]+
                              "  Rent Hour:"+order_data_list[3]+"  Total Amount:RM"+order_data_list[4]+
                              "  Status:"+order_data_list[5]+"  Order Expiration:"+order_data_list[6].strip("\n")+
                              "\n")
                    print("\n")
                menu()
        
            else:
                if(input_car_id.upper()=="X"):
                    print("\n\n")
                    menu()
                else:
                    print("\nCar with this car id not found! Please try again.\n\n")
                    search_records()

   
    elif(input_choice=="B"):

        #ASK USER WHICH USERNAME TO BE SEARCHED
        input_user_id = input("Please enter a username of customer to be searched (Enter X to back):")


        #GET ALL ORDERS OF THIS USER
        print("\n")
        orders_data = file_handling.get_orders(specific_customer=input_user_id)
        if not orders_data:
            print("No records of this user found! Taking you back..\n")
        else:
            print("All record of the user "+input_user_id)
            print("------------------------------------")
            for order_data in orders_data:
                order_data_list = order_data.split(',')
                print("Order ID:"+order_data_list[0]+" (Username:"+order_data_list[1]+"|Full Name:"+
                      file_handling.get_user_data(order_data_list[1], 2)+")\nCar ID:"+order_data_list[2]+
                      "  Rent Hour:"+order_data_list[3]+"  Total Amount:RM"+order_data_list[4]+
                      "  Status:"+order_data_list[5]+"  Order Expiration:"+order_data_list[6].strip("\n")+"\n")
            print("\n")
        menu()
                
    elif(input_choice=="X"):
        print("\n")
        menu()
    else:
        print("Invalid input! Please enter again.\n\n")
        search_records()

        
def return_rented_car():
    #GET ALL RENTED CAR ON CARS.TXT AND PRINT OUT
    cars_data = file_handling.get_cars(rented_only=True)
    if not cars_data:
        print("There is no car rented yet! Taking you back to menu...\n\n")
        menu()
    else:
        print("Here is a list of all rented car:")
        for car_data in cars_data:
            print(car_data.replace(",","\t").replace("\n",""))
        print()

    #LET USER INPUT THE CAR ID OF TARGET CAR TO BE RETURNED
    print()
    input_car_id = input("Please enter a car id of rented car to be returned (Enter X to back):").upper()

    #CHECK IF ENTERED CAR ID EXIST
    FoundCar = False
    TargetCarDataList = []
    for car_data in cars_data:
        car_data_list = car_data.split(',')
        if(car_data_list[0]==input_car_id):
            FoundCar = True
            TargetCarDataList = car_data_list

    if(FoundCar):
        #RETURN CAR BASED ON CAR ID
        file_handling.return_rented_car(input_car_id)
        print("\nSuccessfully returned the car!")

    else:
        if(input_car_id.upper()=="X"):
            print("\n\n")
            menu()
        else:
            print("\nCar with this car id not found! Please try again.\n\n")
            return_rented_car()
            
    
    #ASK USER WHETHER WANT TO RETURN ANOTHER CAR OR BACK TO MENU
    print()
    input_continue = input("Enter Y to return another rented car: ").upper()

    #ACTION FOR THE ANSWER
    print("\n")
    if(input_continue=="Y"):
        return_rented_car()
    else:
        menu()

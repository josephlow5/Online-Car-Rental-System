#LOW JIA QUAN
#TP063436

#THE FILE HANDLE ALL FUNCTION RELATED TO REGISTERED CUSTOMER

import file_handling

Logged_In_Username = ""

def login():
    print("===============================================")
    print("=== WELCOME TO THE REGISTERED CUSTOMER PAGE ===")
    print("===============================================\n")

    #ASK TO VERIFY IDENTITY
    print("Hi, please verify your identity by entering username and password.")
    

    #LET USER INPUT THE USERNAME AND PASSWORD
    input_username = input("Your username: ")
    input_password = input("Your password: ")

    #ACTION FOR THE INPUT
    print("\n")
    if file_handling.login_customer(input_username, password=input_password):
        global Logged_In_Username
        Logged_In_Username = input_username
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
    print("=== WELCOME TO THE REGISTERED CUSTOMER HOME PAGE ===")
    print("====================================================\n")

    #SHOW ALL ACTION AVAILABLE FOR ADMIN
    print("Welcome, dear customer. Please choose what you want to do from below:\n")
    print("1. View Personal Rental History")
    print("2. View Detail of Cars to be Rented Out")
    print("3. Select and Book a car for a specific duration")
    print("4. Do payment to confirm Booking")
    print("5. Exit\n")
    
    #ASK FOR THE CHOICE
    input_choice = input("I want to (Enter 1/2/3/4/5): ")

    #ACTION FOR THE ANSWER
    print()
    if input_choice == "1":
        view_personal_rental_history()
    elif input_choice == "2":
        view_cars_available()
    elif input_choice == "3":
        rent_car()
    elif input_choice == "4":
        do_payment()
    elif input_choice == "5":
        print("Good Bye and Have a nice day!")
        exit()
    else:
        print("Invalid input! Please enter again.\n\n")
        menu()


def view_personal_rental_history():
    #GET ALL ORDERS OF THIS USER AND PRINT OUT
    orders_data = file_handling.get_orders(history_username=Logged_In_Username)
    if not orders_data:
        print("You have no rental history! Taking you back..\n")
    else:
        print("All your rental record is/are shown below:")
        for order_data in orders_data:
            order_data_list = order_data.split(',')
            print("Order ID:"+order_data_list[0]+"  Car ID:"+order_data_list[2]+"  Rent Hour(s):"+order_data_list[3]+"  Total Amount:RM"+order_data_list[4]+"  Status:"+order_data_list[5]+"  Expiration:"+order_data_list[6].strip("\n"))
        print("\n")
    menu()

def view_cars_available():
    #GET ALL DATA ON CARS.TXT AND PRINT OUT
    cars_data = file_handling.get_cars(rent_available_only=True)
    if not cars_data:
        print("There is no car available for rent now! Taking you back..\n")
        menu()
    else:
        print("All cars available is/are shown below:")
        for car_data in cars_data:
            print(car_data.replace(",","\t").replace("\n",""))
        print("\n")
        menu()

def rent_car():
    print("All cars available is/are shown below:")
    #GET ALL DATA ON CARS.TXT AND PRINT OUT
    cars_data = file_handling.get_cars(rent_available_only=True)
    if not cars_data:
        print("There is no car available for rent now! Taking you back..\n")
        menu()
    else:
        for car_data in cars_data:
            print(car_data.replace(",","\t").replace("\n",""))
        print("\n")

    #LET USER INPUT THE CAR ID TO BE RENTED
    input_car_id = input("Please enter a car id of car to be rented (Enter X to back):").upper()

    #CHECK IF ENTERED CAR ID EXIST
    FoundCar = False
    TargetCarDataList = []
    for car_data in cars_data:
        car_data_list = car_data.split(',')
        if(car_data_list[0]==input_car_id):
            FoundCar = True
            TargetCarDataList = car_data_list

    if(FoundCar):
        input_rent_hour = input("Please enter number of hours you will rent: ")
        while not(input_rent_hour.isdigit()):
            print("Invalid value! Please enter again.")
            input_rent_hour = input("Please enter number of hours you will rent: ")

        FinalAmount = int(TargetCarDataList[4])*int(input_rent_hour)
        print("Successfully booked the car (ID: "+TargetCarDataList[0]+" ; Model: "+TargetCarDataList[1]+").\n")
        print("Please do your payment (RM"+str(FinalAmount)+") within 24 hours to confirm booking.\n\n")
        file_handling.rent_car(Logged_In_Username, input_car_id, input_rent_hour, str(FinalAmount))
        menu()        
    else:
        if(input_car_id.upper()=="X"):
            print("\n\n")
            menu()
        else:
            print("\nCar with this car id not found! Please try again.\n\n")
            rent_car()

def do_payment():
    #GET ALL UNPAID ORDERS OF THIS USER AND PRINT OUT
    orders_data = file_handling.get_orders(unpaid_username=Logged_In_Username)
    if not orders_data:
        print("You have no unpaid orders now! Note that orders will be terminated if you didn't complete your payment within 24 hours. Taking you back..\n")
        menu()
    else:
        print("All your unpaid order is/are shown below:")
        for order_data in orders_data:
            order_data_list = order_data.split(',')
            print("Order ID: "+order_data_list[0]+"\tAmount to Pay: "+order_data_list[4])
        print("\n")

        #LET USER INPUT THE ORDER ID TO BE RENTED
        input_order_id = input("Please enter an order id of order to be paid (Enter X to back):").upper()

        #CHECK IF ENTERED ORDER ID EXIST
        FoundOrder = False
        TargetOrderDataList = []
        for order_data in orders_data:
            order_data_list = order_data.split(',')
            if(order_data_list[0]==input_order_id):
                FoundOrder = True
                TargetOrderDataList = order_data_list

        if(FoundOrder):
            print("\nPlease provide your card detail to pay RM"+TargetOrderDataList[4])
            input_card_number = input("Please enter your card number: ")
            while not(input_card_number.isdigit()):
                print("Invalid value! Please enter again.")
                input_card_number = input("Please enter your card number: ")
            input_card_valid = input("Please enter your card expiration date (MM/YYYY): ")
            while not(input_card_valid.replace("/","").isdigit()):
                print("Invalid value! Please enter again.")
                input_card_valid = input("Please enter your card expiration date (MM/YYYY): ")
            input_card_cvc = input("Please enter your card cvc: ")
            while not(input_card_cvc.isdigit()):
                print("Invalid value! Please enter again.")
                input_card_cvc = input("Please enter your card cvc: ")

            file_handling.pay_order(input_order_id)
            print("\n\nSuccessfully confirmed the order (ID: "+TargetOrderDataList[0]+").\n")
            print("Please return the car by "+TargetOrderDataList[6]+"\n")
            menu()        
        else:
            if(input_order_id.upper()=="X"):
                print("\n\n")
                menu()
            else:
                print("Order with this order id not found! Please try again.\n\n")
                do_payment()

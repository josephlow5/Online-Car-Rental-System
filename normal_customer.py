#LOW JIA QUAN
#TP063436

#THE FILE HANDLE ALL FUNCTION RELATED TO NOT REGISTERED CUSTOMERS


import file_handling

def menu():
    print("====================================================")
    print("======== WELCOME TO THE CUSTOMER HOME PAGE =========")
    print("====================================================\n")

    #SHOW ALL ACTION AVAILABLE FOR CUSTOMER
    print("Welcome, dear customers. Please choose what you want to do from below:\n")
    print("1. View all cars available for rent")
    print("2. Register as New customer to access other details")
    print("3. Exit\n")
    
    #ASK FOR THE CHOICE
    input_choice = input("I want to (Enter 1/2/3): ")

    #ACTION FOR THE ANSWER
    print()
    if input_choice == "1":
        view_cars_available()
    elif input_choice == "2":
        register_new_customer()
    elif input_choice == "3":
        print("Good Bye and Have a nice day!")
        exit()
    else:
        print("Invalid input! Please enter again.\n\n")
        menu()



def view_cars_available():
    #GET ALL DATA ON CARS.TXT AND PRINT OUT
    cars_data = file_handling.get_cars(rent_available_only=True)
    if not cars_data:
        print("There is no car available for rent now! Taking you back..\n")
        menu()
    else:
        for car_data in cars_data:
            print(car_data.replace(",","\t").replace("\n",""))
        print("\n")
        menu()

def register_new_customer():
    print('Please enter your info to register:\n')
    
    #LET USER INPUT THEIR INFO
    input_username = input("Your Username: ")
    input_password = input("Your Password: ")
    input_fullname = input("Your Full Name: ")
    input_gender = input("Your Gender (M/F): ").upper()
    while not(input_gender=="F" or input_gender=="M"):
        print("Invalid value! Please enter M or F only.")
        input_gender = input("Your Gender (M/F): ").upper()
    input_phone_numer = input("Your Phone Number: ")
    while not(input_phone_numer.isdigit()):
        print("Invalid value! Please enter again.")
        input_phone_numer = input("Your Phone Number: ")
    input_email = input("Your Email Address: ")

    print()
    if(file_handling.register_new_customer(input_username, input_password, input_fullname, input_gender, input_phone_numer, input_email)):
        print("Successfully registered as New Customer!\n\n")
        menu()
    else:
        print("Sorry, the username you used already exist. Please try again.!\n\n")
        register_new_customer()

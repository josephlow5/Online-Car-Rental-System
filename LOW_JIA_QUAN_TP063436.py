#LOW JIA QUAN
#TP063436

#THIS IS MAIN BODY OF THIS ASSIGNMENT, THE PROGRAM STARTS HERE


import admin
import normal_customer
import registered_customer

def home():
    print ("========== WELCOME TO ONLINE CAR RENTAL SYSTEM (OCRS) ==========\n")

    #SHOW ALL ROLES AVAILABLE
    print("Hi, who is using the system?")
    print("\t1. Admin\n\t2. Customers (Whether Registered or Not)\n\t3. Registered Customers\n")
    

    #LET USER INPUT THE ROLE
    input_choice = input("I am a/an (please enter 1/2/3):")

    #ACTION FOR THE INPUT
    print("\n")
    if(input_choice=="1"):
        admin.login()
    elif(input_choice=="2"):
        normal_customer.menu()
    elif(input_choice=="3"):
        registered_customer.login()
    else:
        print("Invalid input! Please enter again.\n\n")
        home()
        
home()

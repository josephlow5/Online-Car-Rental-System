#LOW JIA QUAN
#TP063436

#THE FILE HANDLE ALL FUNCTION RELATED TO FILE HANDLING


import random, string
from datetime import datetime, timedelta

#GENERATE UNUSED CAR_ID
def get_new_car_id():
    random_car_id = ''.join((random.choice(string.ascii_uppercase) for x in range(3)))  #RANDOMLY GENERATE 3 UPPERCASE CHARACTER
    random_car_id += ''.join((random.choice(string.digits) for x in range(3)))          #RANDOMLY GENERATE 3 DIGITS

    random_car_id_list = list(random_car_id)
    random.shuffle(random_car_id_list)
    final_car_id = ''.join(random_car_id_list)  #JOIN 3 UPPERCASE CHARACTER AND 3 DIGITS, THEN SHUFFLE THE POSITION

    car_file = open("cars.txt","r")

    FoundSimilar = False                        #CHECK IF THE ID GENERATED ALREADY EXISTED
    for car_file_line in car_file:
        car_file_line_list = car_file_line.split(',')
        if(car_file_line_list[0]==final_car_id):
            FoundSimilar = True

    while(FoundSimilar):                        #IF THE ID ALREADY EXIST, RANDOM AGAIN UNTIL IT IS UNIQUE
        random_car_id = ''.join((random.choice(string.ascii_uppercase) for x in range(3)))
        random_car_id += ''.join((random.choice(string.digits) for x in range(3)))

        random_car_id_list = list(random_car_id)
        random.shuffle(random_car_id_list)
        final_car_id = ''.join(random_car_id_list)

        FoundSimilar = False
        for car_file_line in car_file:
            car_file_line_list = car_file_line.split(',')
            if(car_file_line_list[0]==final_car_id):
                FoundSimilar = True

    car_file.close()
    return final_car_id  

  
#ADD NEW CAR INTO CARS.TXT
def add_car(car_model, car_type, car_transmission, hourly_rate):
    car_file = open('cars.txt','a')
    car_file.write(get_new_car_id()+','+car_model+','+car_type+','+car_transmission+','+hourly_rate+','+
                   datetime.now().strftime("%d/%m/%Y|%H")+'\n')
    car_file.close()


#RETURN ALL LINES IN CARS.TXT (RENTED TRUE=RETURN CARS AVAILABLE FOR RENT ONLY)
def get_cars(rent_available_only=False, rented_only=False):

    car_file = open("cars.txt","r")
    if not (rent_available_only or rented_only):
        car_file_lines = car_file.readlines()
    else:
        car_file_lines = []
        for car_file_line in car_file:
            car_file_line_list = car_file_line.split(',')
            if(rent_available_only):
                if(datetime.strptime(car_file_line_list[5].strip("\n"), "%d/%m/%Y|%H") <= datetime.now()):  #COMPARE THE CAR AVAILABLE TIME TO CURRENT TIME, SMALLER THEN SHOW CARS AVAILABLE TO BE RENT
                    car_file_lines.append(",".join(car_file_line_list))
            else:
                if(datetime.strptime(car_file_line_list[5].strip("\n"), "%d/%m/%Y|%H") >= datetime.now()):  #COMPARE THE CAR AVAILABLE TIME TO CURRENT TIME, GREATER THEN SHOW CARS RENTED ONLY
                    car_file_lines.append(",".join(car_file_line_list))
    car_file.close()
    return car_file_lines


#MODIFY CAR DETAIL
def mod_car(target_car_id, mod_type, new_value):
    new_car_file = ""

    #READ AND MODIFY CAR DETAIL, AND STORE INTO NEW_CAR_FILE
    car_file = open("cars.txt","r")
    for car_file_line in car_file:
        car_file_line_list = car_file_line.split(',')
        if(car_file_line_list[0]==target_car_id):
            car_file_line_list[int(mod_type)] = new_value
        new_car_file += ",".join(car_file_line_list)
    car_file.close()

    #WRITE NEW_CAR_FILE TO CARS.TXT
    car_file = open("cars.txt","w")
    car_file.write(new_car_file)
    car_file.close()


#RETURN RENTED CAR WITH CAR_ID
def return_rented_car(target_car_id):
    new_car_file = ""

    #READ AND MODIFY CAR DETAIL, AND STORE INTO NEW_CAR_FILE
    car_file = open("cars.txt","r")
    for car_file_line in car_file:
        car_file_line_list = car_file_line.split(',')
        if(car_file_line_list[0]==target_car_id):
            car_file_line_list[5] = datetime.now().strftime("%d/%m/%Y|%H")+'\n'
        new_car_file += ",".join(car_file_line_list)
    car_file.close()

    #WRITE NEW_CAR_FILE TO CARS.TXT
    car_file = open("cars.txt","w")
    car_file.write(new_car_file)
    car_file.close()


#REGISTER A NEW CUSTOMER
def register_new_customer(username, password, fullname, gender, phone_number, email):
    if (login_customer(username=username, CheckUsernameExist=True)):     #CANCEL REGISTRATION IF THE GIVEN USERNAME ALREADY EXIST
        return False
    else:
        user_file = open('users.txt','a')
        user_file.write(username+','+password+','+fullname+','+gender+','+phone_number+','+email+'\n')
        user_file.close()
        return True


#REGISTERED_CUSTOMER LOGIN/CHECK WHETHER AN CUSTOMER USERNAME EXISTED
def login_customer(username, password="", CheckUsernameExist=False):

    #CUSTOMER LOGIN (READ ALL USERS EXISTED AND CHECK WHETHER THE GIVEN USERNAME EXIST AND THE PASSWORD IS CORRECT)
    if not CheckUsernameExist:
        LoginResult = False
        user_file = open("users.txt","r")
        for user_file_line in user_file:
            user_file_line_list = user_file_line.split(',')
            if(user_file_line_list[0]==username):
                if(user_file_line_list[1]==password):
                    LoginResult = True
        user_file.close()
        return LoginResult

    #CHECK IF THE USERNAME EXIST (FOR REGISTRATION PURPOSE)
    else:
        CheckResult = False
        user_file = open("users.txt","r")
        for user_file_line in user_file:
            user_file_line_list = user_file_line.split(',')
            if(user_file_line_list[0]==username):
                    CheckResult = True
        user_file.close()
        return CheckResult


#GET USER DATA BASED ON USERNAME
def get_user_data(username, data_index):
    return_data = ""
    user_file = open("users.txt","r")
    for user_file_line in user_file:
        user_file_line_list = user_file_line.split(',')
        if(user_file_line_list[0]==username):
             return_data = user_file_line_list[data_index]
    user_file.close()
    return return_data
    
#GENERATE UNUSED ORDER_ID
def get_new_order_id():
    random_order_id = ''.join((random.choice(string.ascii_uppercase) for x in range(3)))  #RANDOMLY GENERATE 3 UPPERCASE CHARACTER
    random_order_id += ''.join((random.choice(string.digits) for x in range(3)))          #RANDOMLY GENERATE 3 DIGITS

    random_order_id_list = list(random_order_id)
    random.shuffle(random_order_id_list)
    final_order_id = ''.join(random_order_id_list)  #JOIN 3 UPPERCASE CHARACTER AND 3 DIGITS, THEN SHUFFLE THE POSITION

    order_file = open("orders.txt","r")

    FoundSimilar = False                        #CHECK IF THE ID GENERATED ALREADY EXISTED
    for order_file_line in order_file:
        order_file_line_list = order_file_line.split(',')
        if(order_file_line_list[0]==final_order_id):
            FoundSimilar = True

    while(FoundSimilar):                        #IF THE ID ALREADY EXIST, RANDOM AGAIN UNTIL IT IS UNIQUE
        random_order_id = ''.join((random.choice(string.ascii_uppercase) for x in range(3)))
        random_order_id += ''.join((random.choice(string.digits) for x in range(3))) 

        random_order_id_list = list(random_order_id)
        random.shuffle(random_order_id_list)
        final_order_id = ''.join(random_order_id_list)

        FoundSimilar = False
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[0]==final_order_id):
                FoundSimilar = True

    order_file.close()
    return final_order_id


#REGISTERED CUSTOMER ORDER TO RENT A CAR
def rent_car(username, car_id, rent_hour, final_amount):
    
    #ADD A RECORD TO ORDERS
    date_after_24hours = datetime.now()+ timedelta(days=1)       #CUSTOMERS HAS ONE DAY TO COMPLETE THE PAYMENT
    order_file = open('orders.txt','a')
    order_file.write(get_new_order_id()+','+username+','+car_id+','+rent_hour+','+
                     final_amount+',UNPAID,'+date_after_24hours.strftime("%d/%m/%Y|%H")+'\n')
    order_file.close()

    #MAKE THE ORDERED CAR NOT AVAILABLE FOR 1 DAY
    mod_car(car_id, 5, date_after_24hours.strftime("%d/%m/%Y|%H")+"\n")


#COMPLETE ONE ORDER
def pay_order(order_id):
    
    #MODIFY THE RECORD OF ORDER TO PAID AND GET RENT HOUR, CAR_ID
    new_order_file = ""
    rent_hours = ""
    car_id = ""
    
    #READ AND MODIFY CAR DETAIL, AND STORE INTO NEW_CAR_FILE
    order_file = open('orders.txt','r')
    for order_file_line in order_file:
        order_file_line_list = order_file_line.split(',')
        if(order_file_line_list[0]==order_id):
            order_file_line_list[5] = "PAID"
            rent_hours = order_file_line_list[3]
            car_id = order_file_line_list[2]
        new_order_file += ",".join(order_file_line_list)
    order_file.close()

    #WRITE NEW_CAR_FILE TO CARS.TXT
    order_file = open("orders.txt","w")
    order_file.write(new_order_file)
    order_file.close()


    #MODIFY CAR DATA ACCORDING TO RENT HOUR
    date_end_of_rent = datetime.now()+ timedelta(hours=int(rent_hours))       #CALCULATE DATE END OF RENT
    mod_car(car_id, 5, date_end_of_rent.strftime("%d/%m/%Y|%H")+"\n")

    
#RETREIVE ORDERS BASED ON CRITERIA
def get_orders(unpaid_username="", history_username="", customers_payment_in_recent_days="", specific_car="", specific_customer=""):
    order_file = open("orders.txt","r")
    
    #GET UNPAID ORDER OF AN USER
    if not unpaid_username=="":
        order_file_lines = []
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[1]==unpaid_username and order_file_line_list[5]=="UNPAID"):   #IF THE ORDER BELONGS TO THIS USER
                if(datetime.strptime(order_file_line_list[6].strip("\n"), "%d/%m/%Y|%H") >= datetime.now()):  #COMPARE THE CAR AVAILABLE TIME TO CURRENT TIME, BIGGER MEANS THE ORDER IS STILL AVAILABLE
                    order_file_lines.append(",".join(order_file_line_list))

    #GET ORDER HISTORY OF AN USER
    if not history_username=="":
        order_file_lines = []
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[1]==history_username):   #IF THE ORDER BELONGS TO THIS USER
                    order_file_lines.append(",".join(order_file_line_list))

    #GET ALL CUSTOMER PAYMENT IN THE SPECIFIC RECENT DAYS
    if not customers_payment_in_recent_days=="":
        order_file_lines = []
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[5]=="PAID"):   #IF THE PAYMENT OF ORDER HAS BEEN MADE
                date_days_before = datetime.now()- timedelta(days=int(customers_payment_in_recent_days))  
                if(datetime.strptime(order_file_line_list[6].strip("\n"), "%d/%m/%Y|%H") >= date_days_before):
                    order_file_lines.append(",".join(order_file_line_list))

    #GET ALL ORDER HISTORY OF A SPECIFIC CAR
    if not specific_car=="":
        order_file_lines = []
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[2]==specific_car):   #IF THE ORDER BELONGS TO THIS USER
                    order_file_lines.append(",".join(order_file_line_list))

    #GET ALL ORDER HISTORY OF A SPECIFIC CUSTOMER
    if not specific_customer=="":
        order_file_lines = []
        for order_file_line in order_file:
            order_file_line_list = order_file_line.split(',')
            if(order_file_line_list[1]==specific_customer):   #IF THE ORDER BELONGS TO THIS USER
                    order_file_lines.append(",".join(order_file_line_list))
                    
    order_file.close()
    return order_file_lines

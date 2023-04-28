import mysql.connector

#setting up the database in python
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="01202008",
        database="bank",
        autocommit = True

    )

#view the customers table 
if __name__ == "__main__":
    connect_to_db()
    connection = connect_to_db()
    cursor=connection.cursor()
    connection.cursor()

balance = 0
def option_1 ():
                    id_q =print ('Creating a new account*remember your account information*, Enter a id number.')
                    user_idcustomer = input()
                    if user_idcustomer.isdigit():
                        user_firstname = (input('Input a firstname.'))

                        if user_firstname.isalpha():
                            user_lastname = (input('Input a lastname.')) 

                            if user_lastname.isalpha():
                                user_pin = (input('Enter a pin number.'))
                                if user_pin.isdigit():
                                    verify = (input(f'verify this information:\n ID-{user_idcustomer}\n Firstname-{user_firstname}\n Lastname-{user_lastname}\n Pin-{user_pin} (y/n)'))
                                #insert user option 1 inputs into table customers
                                    if verify == ('y'):
                                            connect_to_db()
                                            cursor=connection.cursor()
                                            query = f"INSERT INTO customer (idcustomer,firstname,lastname,pin,balance) VALUES ('{user_idcustomer}','{user_firstname}','{user_lastname}','{user_pin}','{balance}')"
                                            cursor.execute(query)
                                            print("Inserted",cursor.rowcount,"row(s) of data.")
                                            
                                            
                                            # see if the account was added
                                            if __name__ == "__main__":
                                                    connect_to_db()
                                                    cursor=connection.cursor()
                                                    connection.cursor()
                                                    cursor.execute("SELECT * FROM CUSTOMER")
                                                    for x in cursor:
                                                        print(x)
                                                        print('Showing info in table')
                                                        
                                    else:
                                        return id_q
                                else:
                                    print('Please enter an integer.')
                                    return user_pin   
                            else:
                                print("Letters only please.")
                                return user_firstname

                        else:
                            print("Letters only please.")
                            return user_firstname

                    else:
                        print('Please enter an integer.')
                        return id_q
        # view balance
def option_2(user_pin):
            pin_verify = input(("Please enter your pin:"))
            if pin_verify == user_pin:
                print ("your balance is ${balance}.") 
            else:
                print ("invalid pin. Please try again") 
                return pin_verify
        #Deleting account
def option_3(user_idcustomer):
            verify_delete = input (("deleting an account. Please enter your ID number:"))
            if verify_delete == user_idcustomer:
                delete = input (("Are you sure you want to delete this account?"))
                if delete == ('y'):
                    connect_to_db()
                    cursor=connection.cursor()
                    query = f'DELETE FROM customers WHERE idcustomer = {user_idcustomer}'
                    cursor.execute(query)
                    print("Account Removed",cursor.rowcount,"row(s) of data.")  
            else:
                print("Invalid ID. Please enter your ID number.")
#create an account
def main_menu():
    user_pin = None
    user_idcustomer = None
    running = True
    
    while running:
 # Display menu
 # Get input from user
        print ("Select an option.\n 1. Create account\n 2. view balance\n 3. Remove account\n 4. exit program")
        options = input()
        if options == "1":
            option_1()    
        if options == "2":
            option_2(user_pin)
        if options == "3":
            option_3(user_idcustomer)
        if options == "4":
                    print ('exit')
                    exit()  

main_menu()

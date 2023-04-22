
import mysql.connector

#setting up the database in python
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="01202008",
        database="bank"
    )

#view the customers table test if option 1 is working
if __name__ == "__main__":
    connect_to_db()
    connection = connect_to_db()
    cursor=connection.cursor()
    connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    for x in cursor:
        print(x)
        print('Showing info in table')
        # adding data into table(creating a new account)
        #need a way to print out the main menu to test properly 
balance = 0
running = True

options = print ("Select an option.\n 1. Create account\n 2. view balance\n 3. Remove account\n 4. exit program")
option=input()

def main_menu(options):
    print (options)


while running:
    main_menu(options)    
    if option == "1":
            #id customer
            user_idcustomer =(input('Creating a new account*remember you account information*, Enter a id number.'))
            if user_idcustomer == int:
                user_firstname = (input('Input a firstname.'))

                if user_firstname.isalpha():
                   user_lastname = (input('Input a lastname.')) 

                   if user_lastname.isalpha():
                      user_pin = (input('Enter a pin number.'))
                      if user_pin == int:
                        verify = (input('verify this information:\n ID-{user_idcustomer}\n,Firstname-{user_firstname}\n Lastname-{user_lastname}\n Pin-{user_pin} (y/n)'))
                        #insert user option 1 inputs into table customers
                        if verify == ('y'):
                                    connect_to_db()
                                    user_option_1 = "INSERT INTO customers(idcustomers,firstname,lastname,pin,balance) VALUES (%s,%s,%s,%s,%s)"
                                    op_1 = ({user_idcustomer},{user_firstname},{user_lastname},{user_pin},{balance})
                                    cursor.execute(user_option_1, op_1)
                                    for x in cursor:
                                        print('account created')
                                        print(x)
                                    # see if the account was added
                                        if __name__ == "__main__":
                                            connect_to_db()
                                            connection = connect_to_db()
                                            cursor=connection.cursor()
                                            connection.cursor()
                                            cursor.execute("SELECT * FROM CUSTOMER")
                                            for x in cursor:
                                                print(x)
                                                print('Showing info in table')
                      else:
                          print('Please enter an integer.')
                          #return user_pin   
                   else:
                       print("Letters only please.")
                       #return user_firstname

                else:
                    print("Letters only please.")
                    #return user_firstname

            else:
                print('Please enter an integer.')
                #return user_idcustomer

    if option =="4":
        running = False


import mysql.connector
#setting up the database in python
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="01202008",
        database="bank"
    )
balance = 0
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

def menu() : 
    print ("Select an option.\n 1. Create account\n 2. view balance\n 3. Remove account\n 4. exit program")
    option=input()
    
        # adding data into table(creating a new account)
        #need a way to print out the main menu to test properly     
    if option == "1":
        try:
            user_idcustomer = int(input('Creating a new account*remember you account information*, Enter a id number.'))
                
        except ValueError:
            print('Please enter an integer.')
            return user_idcustomer
            #need a way to check if the id is not already in the data base
            # firstname
        try:
            user_firstname = (input('Input a firstname.'))
        except:    
            if not user_firstname.isalpha():
                print("Only letters are allowed!")
                return user_firstname
        try:
            #lastname
            user_lastname = (input('Input a lastname.'))
        except:
            if not user_lastname.isalpha():
                print("Only letters are allowed!")
                return user_lastname
        try:
            user_pin = int(input('Enter a pin number.'))
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
            return_to_menu = (input('return to menu? (y/n)'))
            if return_to_menu == ("y"):
                return menu
        except ValueError:
            print('Please enter an integer.')
            return user_pin
    if option == "4":
        exit()
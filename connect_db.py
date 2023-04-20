
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
        print('Showing info in table')
        print(x)
balance="0"
#user options
#create account 
#view balance 
#remove account
#exit
print ("Select an option.\n 1. Create account\n 2. view balance\n 3. Remove account\n 4. exit program")
option=input()
# adding data into table(creating a new account)
while True:
    if option == "1":
        try:
            user_idcustomer = int(input('Creating a new account*remember you account information*, Enter a id number.'))
            
        except ValueError:
            print('Please enter an integer.')
            
        #need a way to check if the id is not already in the data base
        # firstname
        try:
            user_firstname = (input('Input a firstname.'))
        except:    
            if not user_firstname.isalpha():
                print("Only letters are allowed!")
                
        try:
            #lastname
            user_lastname = (input('Input a lastname.'))
        except:
            if not user_lastname.isalpha():
                print("Only letters are allowed!")
        try:
            user_pin = int(input('Enter a pin number.'))
            print('verify this information')#need to print out user variables
        except ValueError:
            print('Please enter an integer.')
            #import option 1 data into customers table
            
    
        
    # print ('Creating a new account, Enter a firstname.')
    # firstname = input()
    # print('enter a lastname')
    # lastname = input()
    # print('Enter a pin number')
    



    # print ('Adding an account, to create a new account type in the info like so, ("firstname", "lastname", pin, balance)')
    # query = "INSERT INTO customers(firstname, lastname, pin, balance) VALUES (%s,%s,%s,%s)"
    # query_vals = input()
    # #not working
    # cursor.execute(query,query_vals)

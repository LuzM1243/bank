from dbm import Database
import mysql.connector
#setting up the database in python
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="01202008",
        database="bank"
    )
command_handler = Database.cursor()
connection = connect_to_db()
cursor=connection.cursor()
#view the customers table
if __name__ == "__main__":
    connect_to_db()
    connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    for x in cursor:
        print('Showing info in table')
        print(x)

#user options
#create account 
#view balance 
#remove account
#exit
print ("Select an option.\n 1. Create account\n 2. view balance\n 3. Remove account\n 4. exit program")
option=input()
# adding data into table(creating a new account)
if option == "1":
    print ('Adding an account, to create a new account type in the info like so, ("firstname", "lastname", pin, balance)')
    query = "INSERT INTO customers(firstname, lastname, pin, balance) VALUES (%s,%s,%s,%s)"
    query_vals = input()
    command_handler.execute(query,query_vals)
    connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    for x in cursor:
        print('Showing info in table')
        print(x)
   

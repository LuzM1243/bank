import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="01202008",
        database="bank"
    )
if __name__ == "__main__":
    connection = connect_to_db()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    for x in cursor:
        print(x)
# adding data into table
#query = "INSERT INTO customers"
# Importing dependencies
import mysql.connector as SQLconnector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Getting env variables for database connection
db_config = dotenv_values(".env")

# Try to connect to DB using credentials
def connect_to_sql():
    try:
        connection = SQLconnector.connect(user=db_config["DB_USER"], password=db_config["DB_PASS"], host=db_config["DB_HOST"])
        print("🛜 -> Connection Successful!")
        return connection
    # If the mysql class returns an error, treat this way...
    except SQLconnector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    connect_to_sql()

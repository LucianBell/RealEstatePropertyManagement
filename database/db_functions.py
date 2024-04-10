import os
import mysql.connector as connector
from mysql.connector import errorcode
from connection import connect_to_sql
from dotenv import dotenv_values
import pandas as pd

# Getting env variables for database connection
db_config = dotenv_values(".env")

def create_tables(sql_file, connec):
    cursor = connec.cursor();
    cursor.execute("USE {}".format(db_config["DB_NAME"]))

    try:
        with open(sql_file, 'r') as file:
            sql_statements = file.read()

        # Split SQL statements by semicolon
        statements = sql_statements.split(';')
        
        number = 0
        for statement in statements:
            cursor.execute(statement)
            number += 1
            print(f"⚒️ -> Table #{number} Created successfully!")

    except FileNotFoundError:
        print(f"File {sql_file} not found")
    except connector.Error as err:
        print("Failed to create table: {}".format(err))
        exit(1)

def drop_tables(table_name, connec):
    cursor =  connec.cursor();
    cursor.execute("USE {}".format(db_config["DB_NAME"]))

    try:
        cursor.execute(
            "DROP TABLE {}".format(table_name)
        )
        print("💣 -> Table Drop successful!")
    except connector.Error as err:
        print("Failed to drop table: {}".format(err))
        exit(1)

def table_manipulation(sql_file, connec, intention):
    available_options = ['w', 'd', 'u']
    cursor = connec.cursor();
    cursor.execute("USE {}".format(db_config["DB_NAME"]))

    if intention in available_options:
        try:
            with open(sql_file, 'r') as file:
                sql_statements = file.read()

            cursor.execute(sql_statements)
            if intention == 'w':
                print("⚒️ -> Value inserted successfully!")
            elif intention == 'd':
                print("⚒️ -> Value deleted successfully!")
            elif intention == 'u':
                print("⚒️ -> Value updated successfully!")
            exit(0)
        except connector.IntegrityError as err:
            print("🛑 -- INTEGRITY ERROR -- 🛑")
            print("Check your SQL Command! It may have duplicated keys or invalid data!")
            print("Error code {}\n".format(err.errno))
            print("SQLSTATE Value {}\n".format(err.sqlstate))
            exit(1)
        except connector.Error as err:
            print("🛑 -- ERROR -- 🛑")
            print("Error code {}\n".format(err.errno))
            print("SQLSTATE Value {}\n".format(err.sqlstate))

            if err.errno == errorcode.ER_SYNTAX_ERROR:
                print("SQL Command has a syntax error!")
                print("Check your syntax")
            else:
                print("Failed to insert data: {}\n".format(err.msg))
            exit(1)
    else:
        print("ERROR! Declared manipulation intention is unavailable!\n")
        print("Please choose between inserting values (w), deleting values (d) or updating values (u).")

def consult_db(sql_file, connec):
    cursor = connec.cursor();
    cursor.execute("USE {}".format(db_config["DB_NAME"]))

    try:
        with open(sql_file, 'r') as file:
            sql_statements = file.read()

        cursor.execute(sql_statements)

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        # Get the column names
        columns = [desc[0] for desc in cursor.description]

        # Convert the result set into a DataFrame
        df = pd.DataFrame(rows, columns=columns)
        
        print(df)
        
        print("💾-Would you like to save the result set?\n")
        response = 'w'

        while response.capitalize() != 'Y' or response.capitalize() != 'N':
            response =  input("Enter Y or N: ")

        if response.capitalize() == 'Y':
            save_path = r"C:\\Users\\Lucian\\Desktop\\Code\\Pessoal\\SQL\\DataModelling-CDB\\results"
            filename = 'results.xlsx'
            save_file = os.path.join(save_path, filename)
            df.to_excel(save_file, index=False)
            print(f"Saving result set at {save_path}\n")

        elif response.capitalize() == 'N':
            print("Thank you for the awnser!\n")


    except:
        pass

if __name__ == "__main__":
    # drop_tables(table_name='properties', connec=connect_to_sql())
    # print("\n")
    # drop_tables(table_name='tenants', connec=connect_to_sql())
    create_tables(sql_file=r'C:\Users\Lucian\Desktop\Code\Pessoal\SQL\DataModelling-CDB\database\sql\schema.sql', connec=connect_to_sql())

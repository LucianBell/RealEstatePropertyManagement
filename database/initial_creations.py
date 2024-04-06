import mysql.connector as connector
from connection import connect_to_sql
from dotenv import dotenv_values

# Getting env variables for database connection
db_config = dotenv_values(".env")

def create_database(connec):
    cursor =  connec.cursor();

    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_config["DB_NAME"])
        )
        print("⚒️ -> Database Creation successful!")
    except connector.Error as err:
        print("Failed to create database: {}".format(err))
        exit(1)

def drop_database(connec):
    cursor =  connec.cursor();

    try:
        cursor.execute(
            "DROP DATABASE {}".format(db_config["DB_NAME"])
        )
        print("💣 -> Table Drop successful!")
    except connector.Error as err:
        print("Failed to drop database: {}".format(err))
        exit(1)


def create_tables(sql_file, connec):
    cursor =  connec.cursor();
    cursor.execute("USE {}".format(db_config["DB_NAME"]))

    try:
        with open(sql_file, 'r') as file:
            sql_statements = file.read()

        cursor.execute(sql_statements)
        print("⚒️ -> Table Creation successful!")
    except connector.Error as err:
        print("Failed to create table: {}".format(err))
        exit(1)

if __name__ == "__main__":
    # create_database(connec=connect_to_sql())
    create_tables(sql_file='database\sql\schema.sql', connec=connect_to_sql())

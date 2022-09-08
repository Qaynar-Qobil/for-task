import mysql.connector
import os 

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "salom777",
#     database = "Foundation"
# )

# my_cursor = mydb.cursor()





os.system("cls")

class Database:
    def __init__(self, db_name):
        self.connection = mysql.connector.connect(
          host="localhost",
          user="root",
          password="salom777",
          database="foundation_60"
        )
        
        self.cursor = self.connection.cursor()
        self.db_name = db_name

        print("DATABASE INFO:")
        self.__createDB()
        self.__createTables()
        print("---------------------------------------", '\n' * 2)
        
    
    def __createDB(self):
        self.cursor.execute(f"""
            CREATE DATABASE IF NOT EXISTS {self.db_name};
        """)
        print(f"\"{self.db_name}\" database is created.")

        self.cursor.execute(f"USE {self.db_name}")
        print(f"connected from \"{self.db_name}\" database.")

    def __createTables(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS users (
              ID INT PRIMARY KEY AUTO_INCREMENT,
              NAME VARCHAR(30) NOT NULL, 
              USERNAME VARCHAR(30) UNIQUE
            );
        """)
        print("users table created.")
    
    def get_users(self, limit = -1):
        self.cursor.execute(f"""
            SELECT * FROM users;
        """)

        if limit < 0:
            users = self.cursor.fetchall()
        else:
            users = self.cursor.fetchmany(limit)
    
        self.connection.commit()
        return users
        

    def get_user(self, user_id = 1):
        self.cursor.execute(f"""
            SELECT * FROM users WHERE ID = {user_id};  
        """)

        user = self.cursor.fetchone()
        return user
database = Database("foundation_60")
    # users = database.get_users(10)
users = database.get_user(4)

print(users)
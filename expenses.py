import mysql.connector

#connection to MySQL database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "obie9090",
    database = "expenses"
)
mycursor = db.cursor()

#create table
mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS expenses(
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 category VARCHAR(255), 
                 description VARCHAR(255), 
                 amount FLOAT, date DATE)
                 """)
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

#The main class for tracking expenses
class Expenses:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date
        self.categories = ["🍔 Food", "🛒 Shopping", "🏠 Home", "🎉 Entertainment, 🚕 Transport"]




#create the main script
def main():
        while True:
            print("📈 Welcome to the expenses tracker! \n")
            print("👉 Please select an option:")
            print("1. Add new expense")
            print("2. View all expenses")
            print("3. View total expenses")
            print("4. View expenses by category")
            print("5. View remaining budget")
            print("6. Exit")
            option = input("Enter your option: ")
import mysql.connector
from datetime import datetime
import calendar

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
    def __init__(self):
        pass

    def add_expenses(self, category, description, amount):
        date = datetime.now().strftime('%Y-%m-%d')
        sql = "INSERT INTO expenses (category, description, amount, date) VALUES (%s, %s, %s, %s)"
        val = (category, description, amount, date)
        mycursor.execute(sql, val)
        db.commit()

    def view_all_expenses(self):
        mycursor.execute("SELECT * FROM expenses")
        result = mycursor.fetchall()
        return result

    def total_expenses(self):
        mycursor.execute("SELECT SUM(amount) FROM expenses")
        result = mycursor.fetchone()
        return result[0] if result[0] is not None else 0

    def expenses_of_category(self):
        mycursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        result = mycursor.fetchall()
        return result

    def remaining_budget(self, budget=4000):
        total_expenses = self.total_expenses()
        remaining_budget = budget - total_expenses
        return remaining_budget

    def daily_budget(self, budget=4000):
        today = datetime.now()
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        remaining_days = days_in_month - today.day
        daily_budget = self.remaining_budget(budget) / remaining_days
        return daily_budget

#create the main script
def main():
    categories = ["🍔 Food", "🛒 Shopping", "🏠 Home", "🎉 Entertainment", "🚕 Transport"]
    expenses = Expenses()
    print("📈 Welcome to the expenses tracker!")
    while True:
        print("\n👉 Please select an option:")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. View expenses by category")
        print("5. View remaining budget")
        print("6. Exit")
        option = input("Enter your option: ")
        if option == '1':
            # display the valid categories to choose from
            print("\n👉 Please select a category:")
            for i, category in enumerate(categories):
                print(f"{i+1}. {category}")
            category = categories[int(input("Enter your category: ")) - 1]
            description = input("Enter your description: ")
            amount = float(input("Enter your amount: "))
            # add the expense to the database
            expenses.add_expenses(category, description, amount)
            print("✔️  Your expense has been added successfully")

        elif option == '2':
            # display all expenses
            expenses_list = expenses.view_all_expenses()
            print("\n📝 All expenses:")
            for expense in expenses_list:
                print(f"{expense[1]} - {expense[2]} - {expense[3]}💲 - {expense[4]}")

        elif option == '3':
            # display total expenses
            total_expenses = expenses.total_expenses()
            print(f"\n📊 Total expenses: {total_expenses:.2f}💲")

        elif option == '4':
            # display expenses of each category
            category_totals = expenses.expenses_of_category()
            print("\n📊 Expenses by category")
            for category, total_amount in category_totals:
                print(f"{category}:💲{total_amount:.2f}")

        elif option == '5':
            # display remaining budget
            remaining_budget = expenses.remaining_budget()
            print("\n💵 Budget")
            print(f"You have💲{remaining_budget:.2f} left to spend this month")
            print(f"That’s💲{expenses.daily_budget():.2f} per day")

        elif option == '6':
            # exit the program
            print("\n👋 Thank you for using the expenses tracker! Have a great day!\n")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
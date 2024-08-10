# Expenses-Tracker
Welcome to the Expenses Tracker! This simple command-line application allows you to track your expenses, categorize them, and manage your monthly budget effectively.

## Table of Contents
●Introduction

●Features

●Installation

●How to Use

●Dependencies

●Contributing

●License

## Introduction
The Expenses Tracker is a Python-based application that connects to a MySQL database to store and retrieve your expenses data. You can use this tool to log daily expenses, view total expenditures, categorize spending, and see how much budget you have left for the month.

## Features
●Add new expenses with categories, descriptions, and amounts.
●View all logged expenses.
●Calculate and display the total amount of expenses.
●Summarize expenses by category.
●Calculate remaining budget based on a predefined monthly budget.
●Estimate daily budget needed to stay within your monthly budget.

## Installation
#### 1) Clone the Repository:
###### git clone https://github.com/yourusername/expenses-tracker.git
###### cd expenses-tracker
#### 2) Set Up the MySQL Database:
Make sure you have MySQL installed and running.
Create a database named expenses.
#### 3) Run the Program

## How to Use
●Launch the program using the command above.
●Choose an option from the menu:
●Add new expense: Log a new expense with category, description, and amount.
●View all expenses: List all expenses logged in the database.
●View total expenses: See the sum of all expenses.
●View expenses by category: Breakdown of expenses per category.
●View remaining budget: See how much money is left in your monthly budget and your daily spending allowance.
●Exit: Close the tracker.

## Dependencies
Python 3.x
MySQL Connector for Python: Install via pip:
###### pip install mysql-connector-python

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

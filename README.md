Expense Tracker
A simple command-line expense tracker application built in Python. This application allows users to register, log in, add, view, edit, and delete their daily expenses. User data and expense records are stored in JSON files.

Features
User Authentication:

Sign Up: Create a new user account with a unique username and a password (hashed using bcrypt for security).

Log In: Authenticate existing users to access their expense records.

Expense Management:

Add Expense: Record new expenses with details like date, category (FOOD, TRAVEL, Others), and amount.

View Transactions: Display all recorded expenses for the logged-in user.

Edit Transactions: Modify existing expense entries based on category and date.

Delete Transactions: Remove specific expense entries.

Data Persistence:

User credentials are saved in users.json.

Each user's expenses are saved in a separate JSON file named [username]_expenses.json.

Technologies Used
Python 3

json module for data storage

bcrypt library for password hashing

Getting Started
Prerequisites
Python 3.x installed on your system.

bcrypt library: You can install it using pip:

pip install bcrypt

Installation
Clone the repository:

git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

(Replace your-username and expense-tracker with your actual GitHub username and repository name.)

Install dependencies:

pip install -r requirements.txt

(You might need to create a requirements.txt file first if you haven't already. It should contain bcrypt.)

To create requirements.txt:

pip freeze > requirements.txt

How to Run
Navigate to the project directory in your terminal.

Run the main script:

python Expenses.py

Usage
Upon running the application, you will be presented with a main menu:

Welcome to the Expense Tracker
Please select a valid number :
1.Sign Up
2.Log In
3.Exit

Sign Up:

Select 1 to create a new account.

Enter a unique username and a password (must be at least 8 characters long).

Your account will be registered, and you will be automatically logged in.

Log In:

Select 2 to log in with an existing account.

Enter your username and password.

If successful, you will be logged in to your expense manager.

Expense Manager Menu:
Once logged in, you will see the expense manager options:

Please select from the following
1.Add an expense
2.View all Transactions
3.Edit Transactions
4.Delete Transactions
5.Exit

1. Add an expense: Enter the date (DD-MM-YY), category (FOOD/TRAVEL/Others), and amount.

2. View all Transactions: See a list of all your recorded expenses.

3. Edit Transactions: Specify the category and date of the transaction you wish to edit, then choose to change the amount, date, or category.

4. Delete Transactions: Provide the category and date of the transaction you want to remove.

5. Exit: Exit the expense manager and return to the main menu (or exit the program if you were already in the main menu).

File Structure
Expenses.py: The main Python script containing the Login and Expenses classes, and the application's logic.

users.json: (Generated upon first sign-up) Stores user credentials (username and hashed password).

[username]_expenses.json: (Generated upon first expense entry for a user) Stores the expense records for a specific user.

Contributing
Feel free to fork this repository, open issues, or submit pull requests to improve the project.

License
This project is open source and available under the MIT License.

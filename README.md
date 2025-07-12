📊 Expense Tracker (Python CLI)
A simple, interactive command-line expense tracker built with Python.
Tracks expenses by user, stores data locally in JSON files, and provides secure password hashing with bcrypt.

✨ Features
✅ Sign up & login with password hashing (bcrypt)
✅ Add, view, edit, and delete expenses
✅ Expenses saved in user-specific JSON files
✅ Supports categories & dates
✅ Simple command-line interface

📦 Requirements
Python 3.x

bcrypt

Install dependencies:

bash
Copy
Edit
pip install bcrypt
▶️ How to run
Clone the repository and run the script:

bash
Copy
Edit
python Expenses.py
🛠 Project structure
pgsql
Copy
Edit
Expenses.py          # Main script containing login & expense tracker classes
users.json           # Auto-generated: stores registered users with hashed passwords
<username>_expenses.json   # Auto-generated: stores each user's expenses
🧰 How it works
Sign up / login

New users register with a username and password (min. 8 characters)

Passwords are hashed and saved securely

Expense management

Add new expenses with date, category, and amount

View all saved transactions

Edit or delete specific expenses by category & date

Data storage

All data saved in JSON files for simplicity

⚙️ Modules & concepts used
json – for data storage

bcrypt – secure password hashing

OOP – with Login and Expenses classes

CLI inputs & menus

📌 Note
This is a beginner-friendly local project – data is not encrypted beyond password hashes.

Intended as a learning project to practice Python, file handling, and basic security.




import json
import os 
import bcrypt






class Login :

    def __init__(self) :
        self.details()

    def details(self) :
        self.info = []
        self.loadusers()

    def saveusers(self) :
        try :  
            with open("users.json","w") as file :
                json.dump(self.info,file,indent = 4)
        except IOError as e:
            print(f"Error saving user data {e}")

    def loadusers(self) : 
        try :
            with open("users.json","r") as file :
                reader = json.load(file)
                self.info = reader
        except FileNotFoundError : 
            self.info = []
            print("File not found starting with an empty user list")
            

        except json.JSONDecodeError :
            self.info = []
            print(f"File might be corrupted starting with a new file")
            
        
    def signup(self) :
        while True :  
            found = False
            username = input("Enter a username : ")
            for record in self.info : 
                if record["Username"] == username :
                    found = True
                    print("Please select another username")
                    continue
            if not found :
                break
            break
        while True : 
            self.password = input("Enter a password : ")
            if len(self.password) < 8 : 
                print("Your password must be 8 characters long")
                continue
            hashed = bcrypt.hashpw(self.password.encode('utf-8') , bcrypt.gensalt())
            self.password = hashed.decode('utf-8')
            dict1 = {
                "Username" : username,
                "Password" : self.password
            }
            self.info.append(dict1)
            self.saveusers()
            print("New user has now been registered successfully")
            return username
            break

    def login(self) :
        try :
            while True : 
                username = input("Enter a username please : ")
                found = False
                if not self.info :
                    print('No user has been registered yet Please signup first')
                    return self.signup()
                for user in self.info :
                    if user["Username"] == username :
                        found = True
                        break
                if not found :
                    print("Please enter a valid username")
                    continue

                password = input("Enter a password please : ")
                found = False
                for user in self.info : 
                    if bcrypt.checkpw(password.encode('utf-8') , user["Password"].encode('utf-8') ) :
                        print("Congrats you have logged in successfully")
                        found = True
                        return username
                        break
                if not found :  
                    print("You have entered an incorrect password")
                    continue
                break
        except FileNotFoundError :
            print("Yo haven't registered yet Please signup first")
            self.signup()




class Expenses :

    def __init__(self,username) : 
            self.username = username
            self.filename = f"{username}_expenses.json"
            self.expenses = []
            self.loadexpenses()
    
    def saveexpenses(self) : 
        try :
            with open(self.filename,"w") as file :
                json.dump(self.expenses , file , indent = 4)
        except IOError as e :
            print(f"Error saving user's data {e}")

    def loadexpenses(self) :
        try :
            with open(self.filename,"r") as file : 
                reader = json.load(file)
                self.expenses = reader
        except FileNotFoundError :
            self.expenses = []
            print("No data recorded please enter some first")
        except json.JSONDecodeError :
            self.expenses = []
            print(f"The data might be corrupted removing all the data")

    def addexpense(self) : 
        date = input("Please enter the date (DD-MM-YY) : ")
        category = input("Please enter the category (FOOD/TRAVEL/Others)")
        amount = int(input("Enter the amount youn spent : "))
        dict1 = {
            "Date" : date,
            "Category" : category,
            "Amount" : amount
        }

        self.expenses.append(dict1)
        self.saveexpenses()

    def viewexpenses(self) : 
        try :
            for expense in self.expenses :
                print("----Expenses Report----")
                print(expense)
        except FileNotFoundError :
            print("No records found")

    def editexpense(self) : 
        edit = input("Enter the category you want to edit : ")
        for expense in self.expenses : 
            if expense["Category"] == edit :
                print(f"Category : {expense["Category"]},Date : {expense["Date"]},Amount : {expense["Amount"]}")
                edit_d = input("Enter the date of the transaction : ")
                
                if expense["Date"] == edit_d : 
                    edited = input("Enter what do you want to change (a/d/c) : ")
                    if edited == "a" : 
                        edit_a = input("Enter the new amount : ")
                        expense["Amount"] = edit_a
                    elif edited == "d" : 
                        edit_m = input("Enter the new date (DD-MM-YY) : ")
                        expense["Date"] = edit_m
                    elif edited == "c" :
                        edit_c = input("Please enter the new category (FOOD/TRAVEL/OTHER) : ")
                        expense["Category"] = edit_c
                    else :
                        print("Please select a valid input")

    def deleteexpense(self) : 
        for expenses in self.expenses :
            print(expenses)
        delete = input("Enter the category of the transaction you want to delete : ")
        for expense in self.expenses :
            while True : 
                if expense["Category"] == delete : 
                    date = input("Enter the date of the transaction you want to delete : ")
                    if expense["Date"] == date : 
                        self.expenses.remove(expense)
                        break
                else :
                    print("Please enter a valid category")
                    continue
def repeat(run_expenses) :
        while True :
            ask = input("Do yo want to perform another task (y/n) : ").lower()
            if ask == "y" : 
                expense_manager(run_expenses)
                break
            elif ask == "n" :
                print("Thanks for using this programme")
                break
            else :
                print("Please select a valid input")
                continue


def execute() :
    while True :

        print("Welcome to the Expense Tracker")
        opt1 = int(input("""Please select a valid number :
                            1.Sign Up
                            2.Log In
                            3.Exit
                                """))
        login1 = Login()
 
        if opt1 == 1 : 
            login_user = login1.signup()
            if login_user :
                print(f"Welcome {login_user} You are now logged in")
                user_expenses = Expenses(login_user)
                expense_manager(user_expenses)
                break
            else :
                print("Sign Up Failed . Please try again later")
                continue
            break

        elif opt1 == 2 : 
            login_user = login1.login()
            if login_user :
                print(f"Welcome{login_user} you have logged in successfully")
                user_expenses = Expenses(login_user)
                expense_manager(user_expenses)
                break
            else :
                print("Login Failed")
                continue

        elif opt1 == 3 :
            print("Exitting the main menu") 
            exit()
            break
    
        else : 
            print("Please select a valid number ")
            continue
    

def expense_manager(run_expenses) :
    while True : 
        opt2 = int(input("""Please select from the following
                            1.Add an expense
                            2.View all Transactions
                            3.Edit Transactions
                            4.Delete Transactions
                            5.Exit
                                """))
        try :
            opt2
        except ValueError :
            print("Please enter a number only")
            continue
        if opt2 == 1 :
            run_expenses.addexpense()
            run_expenses.saveexpenses()
            if not repeat(run_expenses) :
                break
            break
        elif opt2 == 2 :
            run_expenses.viewexpenses()
            if not repeat(run_expenses) :
                break
            break
        elif opt2 == 3 :
            run_expenses.editexpense()
            run_expenses.saveexpenses()
            if not repeat(run_expenses) :
                break
            break
        elif opt2 == 4 :
            run_expenses.deleteexpense()
            run_expenses.saveexpenses()
            if not repeat(run_expenses) :
                break
            break
        elif opt2 == 5 :
            print("Thanks for using this programme")
            exit()
        else :
            print("Please enter a valid number")
            continue
    

execute()


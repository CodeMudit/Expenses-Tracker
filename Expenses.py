import csv
import os 





class Expenses :
    
    def __init__(self) :
        self.amount = 0
        self.category = ""
        self.date = ""
        self.budget = None
        self.LoadBudget()
        
        
    
    
    def AddExpenses(self) :
        amount = int(input("Enter the amount you spent : "))
        category = input("Enter the thing you spent your money on : ")
        date = input("Enter the date in (DD-MM-YY) format : ")
        file_exists = os.path.exists("Expenses.csv")
        with open("Expenses.csv","a",newline="") as file :
            dict1 = {
                "Date" : date,
                "Category" : category,
                "Amount" : amount
            }
            fieldnames = ["Date" , "Category" , "Amount"]
            csv_writer = csv.DictWriter(file,fieldnames = fieldnames , delimiter = "|" )
            file.seek(0)
            if not file_exists :
                csv_writer.writeheader()

            csv_writer.writerow(dict1)
            


    
    def ViewAllExpenses(self) :
        try :
            with open("Expenses.csv","r") as f :
                content = csv.reader(f,delimiter = "|")
                print("\n---All expenses---")
                for row in content :
                    print(row)
            
        except FileNotFoundError :
            print("No expenses recorded yet")
        
    
    def SearchExpenses(self) :
        self.search_term = input("Enter the Date,category or amount you spent to find expenses : ").lower()

        try :
            found = False
            with open("Expenses.csv","r") as f :
                lines = csv.reader(f)

                for line in lines : 
                    if self.search_term in line :
                        print(" | ".join(line))

                        found = True
            if not found :
                print("No matching Expense found")

        except FileNotFoundError :
            print(f"Please add some expenses first '{self.search_term}'")
        
    def exit(self) :
        print("thanks for using this programme.GoodBye!")
        exit

    def CheckBudget(self) :
        if self.budget is None :
            print("Please set a budget amount first : ")
            repeat()
            return
        total = 0
        try : 
            with open("Expenses.csv","r") as file :
                reader = csv.DictReader(file,delimiter="|")
                for row in reader :
                    try :
                        total += int(row["Amount"])
                    except ValueError :
                        continue

        except FileNotFoundError :
            print("No expenses to calculate") 
            return 
        
        print(f"The total Amount spent this month is : {total}")
        print(f"Your Monthly spending limit is : {self.budget}")

        if total>self.budget :
            print("Warning ! You have exceeded your monthly spending limit ")
        else : 
            print("You are within your monthly spending limits ")

    def UpdateBudget(self) :
        
        budget = int(input("Enter your Monthly spending limit : "))
        self.budget = budget
        try :
            with open("Budget.csv","w") as file :
                writer = csv.writer(file)
                writer.writerow([budget])
            print(f"Your new Monthly spending limit is : {budget} ")
        except ValueError :
            print("Please enter a valid value")
            return 
        
    def LoadBudget(self) :
        try :
            with open("Budget.csv","r") as file :
                new_file = csv.reader(file)
                self.budget = next(new_file)

        except :
            self.budget = None











    
        
        
Expense1 = Expenses()
def repeat() :
    ask = input("Do you want to run this programme again (y/n) : ").lower()
    if ask == "y" :
        execute()
    elif ask == "n" :
        print("Thanks for running this programme.Remember to come back soon")
    else : 
        print("Please select a valid character ")
        repeat()

def execute() :
    operation = int(input("""Enter the task you want to perform : 
                                1.Add an expense
                                2.View all Expenses
                                3.Search an expense 
                                4.Check Budget
                                5.Update Budget
                                6.Exit
                                """))
    if operation == 1 :
        Expense1.AddExpenses()
        repeat()

    elif operation == 2 :
        Expense1.ViewAllExpenses()
        repeat()

    elif operation == 3 :
        Expense1.SearchExpenses()
        repeat()

    elif operation == 4 :
        Expense1.CheckBudget()

    elif operation == 5:
        Expense1.UpdateBudget()

    elif operation == 6:
        Expense1.exit()
        
    else : 
        print("Please select a valid number ")
        execute()


execute()




            
            

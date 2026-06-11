from datetime import datetime
from database import (
    save_expense,
    load_expenses,
    rewrite_expenses
)
expenses = load_expenses()    

def add_expense():
    date =datetime.now().strftime(
        "%Y-%m-%d"
    )
    category = input("Enter Category :")
    amount = float(input("Enter Amount : "))

    expense ={
        "date": date,
        "category" : category,
        "amount": amount
    }
    expenses.append(expense)

    save_expense(
        date,
        category,
        amount
    )
    print("Expense Added Successfully")

def view_expenses():
    global expenses
    expenses = load_expenses()

    if len(expenses) ==0:
        print("\nNo expense Found\n ")
        return 

    print("\n -----All Expenses-----")

    for index,expense in enumerate(
        expenses,
        start=1

    ):
        date_val =expense.get("date", "No Date")
        cat_val =expense.get("category","N/A")
        amt_val = expense.get("amount",0)
        print(
            
            f"{index}. Date: {date_val} | Category :{cat_val} | Amount : ₹{amt_val}"
            
        )  
    print()      

def total_expense():
    
    total = 0

    for expense in expenses :
        total += expense["amount"]

    return total 

def search_expense():

    category = input(
        "Enter Category To Search : "
    )
    found = False

    for expense in expenses :
        if expense["category"].lower() == category.lower():

            print(
                f"Category : {expense['category']} | Amount : ₹{expense['amount']}"
            )

            found =True
        if not found:
            print("No Record Found")   

def delete_expense():

    if len(expenses) ==0:
        print("No Expenses Found ")
        return 

    view_expenses()

    number =int(
        input(
            "Enter Record  Number To delete :"
        )
    )            

    if 1 <= number <= len(expenses):
        expenses.pop(
            number - 1
        )
        print(
            "Expense Deleted Successfully"
        )

    else:
        print(
            "Invalid record Number "
        )
def update_expense():

    if len(expenses) == 0:
        print("No Expenses Found")
        return

    view_expenses()

    number = int(
        input(
            "Enter Record Number To Update: "
        )
    )

    if 1 <= number <= len(expenses):

        new_category = input(
            "Enter New Category: "
        )

        new_amount = float(
            input(
                "Enter New Amount: "
            )
        )

        expenses[number - 1][
            "category"
        ] = new_category

        expenses[number - 1][
            "amount"
        ] = new_amount

        rewrite_expenses(
            expenses
        )

        print(
            "Expense Updated Successfully"
        )

    else:

        print(
            "Invalid Record Number"
        )        

def add_expense_gui(
    category,
    amount
):
    
    today_date = datetime.today().strftime('%Y-%m-%d')
    expense = {

        "date": today_date,

        "category": category,

        "amount": float(amount)

    }

    expenses.append(
        expense
    )

    rewrite_expenses(
        expenses
    )        

def get_all_expenses():

    return load_expenses()

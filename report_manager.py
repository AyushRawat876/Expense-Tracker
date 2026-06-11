import matplotlib.pyplot as plt

from income_manager import total_income
from expense_manager import total_expense ,expenses

def get_balance():
    return (
        total_income()
        -
        total_expense()

    )
def show_balance():

    income = total_income()
    expense = total_expense()

    balance = income - expense

    print("\n===== FINANCIAL REPORT =====")

    print(f"Total Income  : ₹{income}")
    print(f"Total Expense : ₹{expense}")
    print(f"Balance       : ₹{balance}")

def monthly_report():

    month = input(
        "Enter Month (MM) : "
    )    

    year = input(
        "Enter Year(YYYY) :"
    )

    category_totals ={}

    total = 0

    for expense in expenses:
        expense_date = expense["date"]

        exp_year  = expense_date[:4]
        exp_month = expense_date[5:7]

        if exp_month == month and exp_year == year:

            category = expense["category"]

            amount = expense["amount"]

            if category not in category_totals:
                category_totals[category] =0

            category_totals[category] += amount     
            total += amount

    print("\n ====Monthly Report ====")

    for category, amount in category_totals.items():

        print(
            f"{category} : ₹{amount}"
        ) 
    print(
        f"\n Total Expense = ₹{total}"
    )     

def expense_pie_chart():
    from expense_manager import get_all_expenses
    expenses = get_all_expenses()
    if len(expenses)==0:
        print("No Expense Data Found to display in pie chart!")
        return 
    category_totals ={}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals :
            category_totals[category] =0

        category_totals[category] +=amount

    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct="%1.1f%%"
    )  
    plt.title(
        "Expense Distribution"
    )     
    plt.show()

def expense_bar_chart():

    from expense_manager import get_all_expenses
    expenses = get_all_expenses()

    if len(expenses) ==0:
        print("No Expense Data Found")
        return 

    category_totals ={}

    for expense in expenses :

        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] =0

        category_totals[category] +=amount

    plt.figure(figsize=(8,5))

    plt.bar(
        category_totals.keys(),
        category_totals.values()
    )        

    plt.title("Category Wise Expenses ")
    
    plt.xlabel("Category")

    plt.ylabel("Amount")
    plt.show()

def monthly_trend_chart():

    monthly_totals ={}

    for expense in expenses:

        date =expense["date"]

        month =date[:7]

        amount =expense["amount"]

        if month not in monthly_totals:
            monthly_totals[month] =0

        monthly_totals[month]+=amount

    if len(monthly_totals) ==0:

        print("No Data Found")
        return 

    months =list(
        monthly_totals.keys()
    )

    totals =list(
        monthly_totals.values()
    )

    plt.figure(
        figsize =(8,5)
    ) 

    plt.plot(
        months,
        totals,
        marker ="o"
    )

    plt.title(
        "Monthly Expense Trend"
    )

    plt.xlabel(
        "Month"
    )       

    plt.ylabel(
        "Expense Amount"
    )

    plt.grid(True)

    plt.show()
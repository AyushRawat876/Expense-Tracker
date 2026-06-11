import tkinter as tk
from datetime import datetime
from tkinter import ttk

from expense_manager import(
    get_all_expenses,
    add_expense_gui,
    expenses
)

from income_manager import(
    add_income_gui,
    get_all_incomes
)

from report_manager import(
    expense_pie_chart,
    expense_bar_chart,
    monthly_trend_chart,
    get_balance
)
from budget_manager import get_budget_report    
from database import save_expense,save_income


def open_add_expense():

    top = tk.Toplevel()

    top.title(
        "Add Expense"
    )

    tk.Label(
        top,
        text="Category"
    ).pack()

    category_entry = tk.Entry(
        top
    )

    category_entry.pack()

    tk.Label(
        top,
        text="Amount"
    ).pack()

    amount_entry = tk.Entry(
        top
    )

    amount_entry.pack()

    def save():

        category = (
            category_entry.get()
        )

        amount = (
            amount_entry.get()
        )

        add_expense_gui(
            category,
            amount
        )

        top.destroy()

    tk.Button(
        top,
        text="Save",
        command=save
    ).pack(
        pady=10
    )

def view_expense_table():

    top =tk.Toplevel()

    top.title(
        "All Expenses"
    )
    top.geometry(
        "700x400"
    )

    tree = ttk.Treeview(
        top
    )
    tree["columns"] = (
        "Date",
        "Category",
        "Amount"
    )
    tree.column(
        "#0",
        width=0,
        stretch=False
    )
    tree.column(
        "Date",
        width=150
    )
    tree.column(
        "Category",
        width=200
    )
    tree.column(
        "Amount",
        width=150
    )
    tree.heading(
        "Date",
        text="Date"
    )
    tree.heading(
        "Category",
        text = "Category"
    )
    tree.heading(
        "Amount",
        text ="Amount"
    )

    for expense in get_all_expenses():

        tree.insert(
            "",
            "end",
            values=(
                expense["date"],
                expense["category"],
                expense["amount"]
            )
        )
        tree.pack(
            fill="both",
            expand=True
        )

def open_add_income():

    top = tk.Toplevel()

    top.title(
        "Add Income"
    )

    tk.Label(
        top,
        text="Income Source"
    ).pack()

    source_entry = tk.Entry(
        top
    )

    source_entry.pack()

    tk.Label(
        top,
        text="Amount"
    ).pack()

    amount_entry = tk.Entry(
        top
    )

    amount_entry.pack()

    def save():

        source = (
            source_entry.get()
        )

        amount = (
            amount_entry.get()
        )

        add_income_gui(
            date,
            source,
            amount
        )

        top.destroy()

    tk.Button(
        top,
        text="Save",
        command=save
    ).pack(
        pady=10
    )


def view_income_table():

    top = tk.Toplevel()

    top.title(
        "All Incomes"
    )

    top.geometry(
        "600x400"
    )

    tree = ttk.Treeview(
        top
    )

    tree["columns"] = (
        "Source",
        "Amount"
    )

    tree.column(
        "#0",
        width=0,
        stretch=False
    )

    tree.column(
        "Source",
        width=250
    )

    tree.column(
        "Amount",
        width=150
    )

    tree.heading(
        "Source",
        text="Source"
    )

    tree.heading(
        "Amount",
        text="Amount"
    )

    for income in get_all_incomes():

        tree.insert(
            "",
            "end",
            values=(
                income["source"],
                income["amount"]
            )
        )

    tree.pack(
        fill="both",
        expand=True
    )
def show_balance_gui():

    top = tk.Toplevel()

    top.title(
        "Balance Report"
    )

    balance = (
        get_balance()
    )

    tk.Label(

        top,

        text=f"Current Balance : ₹{balance}",

        font=(
            "Arial",
            16
        )

    ).pack(
        pady=20
    )



window = tk.Tk()

window.title(
    "Expense Tracker "
)
window.geometry(
    "700x500"
)

heading = tk.Label(
    window,
    text="Expense Tracker Dashboard",
    font =("Arial", 20)
)
heading.pack(pady=20)

frame =tk.Frame(window)
frame.pack(pady=20)

btn1 = tk.Button(
    frame,
    text ="Add Expense",
    width = 20,
    command= open_add_expense
)
btn1.pack(pady=5)

btn2 =tk.Button(
    frame,
    text ="View Expenses",
    width=20,
    command = view_expense_table
)
btn2.pack(pady=5)


def add_income_gui():
    
    income_window =tk.Toplevel(window)
    income_window.title("Add Income")
    income_window.geometry("300x200")

    tk.Label(income_window,text ="Income Source :").pack(pady=5)
    source_entry =tk.Entry(income_window)
    source_entry.pack(pady=5)

    tk.Label(income_window,text="Amount :").pack(pady=5)
    amount_entry = tk.Entry(income_window)
    amount_entry.pack(pady=5)

    def save():
        from datetime import datetime
        date = datetime.now().strftime("%y-%m-%d")

        source =source_entry.get()
        amount = amount_entry.get()

        if source and amount:
           save_income(date,source,amount)
           print("Income Saved !")
           income_window.destroy()
        else:
            print("Please fill all Fields")

    tk.Button(income_window,text="Save",command=save).pack(pady=10)


btn3 = tk.Button(
    frame,
    text ="Add Income",
    width =20,
    command = add_income_gui
)

btn3.pack(pady=5)

btn4 =tk.Button(
    frame,
    text ="View Income",
    width =20,
    command=view_income_table
)
btn4.pack(pady=5)

btn5 =tk.Button(
    frame,
    text="Show Balance",
    width=20,
    command=show_balance_gui
)
btn5.pack(
    pady=5
)

btn6 =tk.Button(
    frame,
    text = "Expense Pie Chart",
    width =20,
    command=expense_pie_chart
)
btn6.pack(pady=5)


def show_budget_report():

    top =tk.Toplevel()

    top.title("Budget Report")

    budget,spent,remaining = get_budget_report()

    tk.Label(
        top,
        text=f"Budget : ₹{budget}",
        font =("Arial",14)
    ).pack(pady=10)

    tk.Label(
        top,
        text=f"Spent : ₹{spent}",
        font=("Arial",14)
    ).pack(pady=10)

    tk.Label(
        top,
        text=f"Remaining :₹{remaining}",
        font =("Arial",14)
    ).pack(pady=10)

btn7 =tk.Button(
    frame,
    text="Budget Report",
    width =20,
    command=show_budget_report
)    

btn7.pack(pady=5)

btn8 = tk.Button(
    frame,
    text="Expense Bar Chart",
    width =20,
    command=expense_bar_chart
)
btn8.pack(pady=5)


btn9 = tk.Button(
    frame,
    text="Exit",
    width=20,
    command=window.destroy
)

btn9.pack(pady=5)

btn10 =tk.Button(
    frame,
    text="Monthly Trend Chart ",

    width=20,
    command=monthly_trend_chart
)

btn10.pack(
    pady=5
)
window.mainloop()


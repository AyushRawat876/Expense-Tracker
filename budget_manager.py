from database import(
    save_budget,
    load_budget
)
from expense_manager import total_expense
budget = load_budget()
def set_budget():
    global budget

    budget =float(
        input(
            "Enter Monthly Budget :"
        )
    )
    save_budget(
        budget
    )

    print(
        "Budget Saved Successfully "
    ) 
def check_budget():

    spent = total_expense()
    remaining = budget - spent
    print(
        "\n ==== BUDGET REPORT ======"
    )
    print(
        f"Buddget = ₹{budget}" 
    )
    print(
        f"Spent =₹{spent}"
    )
    print(
        f"Remaining = ₹{remaining}"
    )
    if remaining < 0:
        print (
            "Budget Exceeded"
        )

    elif remaining <= budget * 0.2:
        print(
            "\n Only 20% Budget Left"
        )
    else:
        print(
            "\n Budget Healthy"
        )         

def get_budget_report():

    spent =total_expense()

    remaining = budget - spent 

    return budget,spent,remaining       
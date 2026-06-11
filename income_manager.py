from database import (
    save_income,
    load_incomes
)

incomes = load_incomes()


def add_income():

    source = input("Enter Income Source: ")
    amount = float(input("Enter Amount: "))

    income = {
        "source": source,
        "amount": amount
    }

    incomes.append(income)

    save_income(
        source,
        amount
    )

    print("Income Added Successfully")


def add_income_gui(
    source,
    amount
):

    income = {

        "source": source,

        "amount": float(amount)
    }

    incomes.append(
        income
    )

    save_income(
        source,
        amount
    )


def view_incomes():

    if len(incomes) == 0:
        print("No Income Records Found")
        return

    print("\nAll Incomes")

    for income in incomes:
        print(
            f"Source: {income['source']} | Amount: ₹{income['amount']}"
        )


def total_income():

    total = 0

    for income in incomes:
        total += income["amount"]

    return total 

def get_all_incomes():
    return load_incomes()


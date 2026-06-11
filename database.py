import csv

def save_expense(date,category, amount):

    with open(
        "expenses.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [date,category, amount]
        )


def load_expenses():

    expenses = []

    try:

        with open(
            "expenses.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file,skipinitialspace=True)
            
            if reader.fieldnames:
                reader.fieldnames =[field.strip() for field in reader.fieldnames]
            for row in reader:
              if row and len(row) >= 3 :  

                expenses.append(
                    {
                        "date":row["date"],
                        "category": row["category"],
                        "amount": float(row["amount"])
                        
                    }
                )

    except FileNotFoundError:
        pass

    return expenses

def save_income(date,source, amount):
    with open("incomes.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date,source, amount])    

def load_incomes():

    incomes = []

    try:

        with open(
            "incomes.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
              if row and len(row) >=3 :  

                incomes.append(
                    {   
                        "date" : row["date"],
                        "source": row["source"],
                        "amount": float(row["amount"])
                    }
                    
                )

    except FileNotFoundError:
        pass

    return incomes

def rewrite_expenses(expenses):

    import csv
    with open(
        "expenses.csv",
        "w",
        newline=""
    ) as file:
        
        writer = csv.writer(file)

        writer.writerow(
            ["date ","category","amount"]
                
        )
        for expense in expenses:
            writer.writerow(
                [   
                    expense["date"],
                    expense["category"],
                    expense["amount"]
                ]
            )

def save_budget(budget):

    with open(
        "budget.csv",
        "w",
        newline=""       
    ) as file:
        
        writer = csv.writer(file)

        writer.writerow(
            ["budget"]
        )

        writer.writerow(
            [budget]
        )

def load_budget():

    try:
        with open(
            "budget.csv",
            "r"    
        ) as file :

           reader =csv.DictReader(
               file
           )
           for row in reader:
               return float(
                   row["budget"]
               )
    except:
        return 0
    return 0       
from expense_manager import *
from income_manager import *
from report_manager import ( 
    show_balance,
    monthly_report,
    expense_pie_chart,
    expense_bar_chart
)    
from budget_manager import(
  set_budget,
  check_budget
) 
while True:

    print("\n====EXPENSE TRACKER =====")
    print("1.Add Expense")
    print("2.View Expense")
    print("3. Total Expense")

    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Update Expense")
    print("7. Add Income ")
    print("8 . View Expense ")
    print("9. Total Income")
    print("10. Show Balance")
    print("11. Monthly Report")
    print("12. Set Budget")
    print("13. Budget Report")
    print("14 . Expense Pie Chart")
    print("15. Expense_bar_chart")
    print("16. Exit")

    choice = input("Enter Choice :")

    if choice =="1":
     add_expense()
    elif choice =="2":
     view_expenses()
    elif choice =="3":
     print(f"\nTotal Expense = ₹{total_expense()}")
    elif choice =="4":
      search_expense()
    elif choice =="5":
      delete_expense()
    elif choice =="6":
      update_expense()    
    elif choice =="7":
      add_income()
    elif choice =="8":
      view_incomes()
    elif choice =="9":
     print(f"\nTotal Income =₹{total_income()}")  
    elif choice =="10":
      show_balance()
    elif choice =="11":
      monthly_report()  
    elif choice == "12":
      set_budget()
    elif choice =="13":
      check_budget()  
    elif choice =="14":
      expense_pie_chart()
    elif choice =="15":
      expense_bar_chart()      
    elif choice =="16":  
      print("Program Closed")
      break
    else:
     print("Invalid choice")

from decimal import Decimal, InvalidOperation


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        for expense in self.expenses:
            print(f"{expense.category}: €{expense.amount}")

    def total_amount(self):
        total = Decimal("0")
        for expense in self.expenses:
            total += expense.amount
        return total    

class Expense:
    def __init__(self, amount, category):
        self.amount = Decimal(amount)
        self.category = category
        

tracker = ExpenseTracker()

print("Expense Tracker")
print("1. Add an expense")
print("2. List of expenses")
print("3. Show total")
print("4. Exit")


while True:
    choice = input("\nChoose an option: ").strip()


    if choice == "1":
         amount = input("Enter an expense amount: ")
         category = input("Enter a category: ")

         try:
             expense = Expense(amount, category)
         except InvalidOperation:
             print("Enter a valid amount, such as 4.50.")
             continue

         if not expense.amount.is_finite() or expense.amount <=0:
             print("Enter an amount greater than zero.")
             continue
         
         tracker.add_expense(expense)
         print(f"Added €{expense.amount} for {expense.category}.")
    
    elif choice == "2":
         tracker.list_expenses()

    elif choice == "3":
       print(f"Total: €{tracker.total_amount()}")

    elif choice == "4":
       break
    else:
        print("Chose 1, 2, 3, 4.")
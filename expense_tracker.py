class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        


amount = input("Enter an expense amount: ")
category = input("Enter an category: ")
expense = Expense(amount, category)

print(f"Added €{expense.amount} for {expense.category} expenses")


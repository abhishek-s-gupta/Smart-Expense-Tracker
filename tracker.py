import pandas as pd

class Expense:
    def __init__(self, amount, category, desc):
        self.amount = amount
        self.category = category
        self.desc = desc

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, desc):
        exp = Expense(amount, category, desc)
        self.expenses.append(exp)

    def save_to_file(self):
        data = []
        for e in self.expenses:
            data.append([e.amount, e.category, e.desc])

        df = pd.DataFrame(data, columns=["Amount", "Category", "Description"])
        df.to_csv("data.csv", index=False)

    def load_data(self):
        try:
            df = pd.read_csv("data.csv")
            return df
        except:
            return None

    def total_expense(self):
        return sum(e.amount for e in self.expenses)
import tkinter as tk
from tkinter import messagebox
import re
import matplotlib.pyplot as plt
import pandas as pd
from tracker import ExpenseTracker

tracker = ExpenseTracker()

def add_expense():
    amount = entry_amount.get()
    category = entry_category.get()
    desc = entry_desc.get()

    # Regex validation
    if not re.match("^[0-9]+$", amount):
        messagebox.showerror("Error", "Enter valid amount")
        return

    tracker.add_expense(int(amount), category, desc)
    tracker.save_to_file()

    messagebox.showinfo("Success", "Expense Added")

def show_report():
    df = tracker.load_data()
    if df is not None:
        df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Expense Report")
        plt.show()
    else:
        messagebox.showerror("Error", "No data found")

# GUI window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x300")

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="Show Report", command=show_report).pack(pady=10)

root.mainloop()
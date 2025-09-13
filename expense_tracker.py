import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================== DATABASE SETUP ==================
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    note TEXT
)
""")
conn.commit()


# ================== CORE FUNCTIONS ==================
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Transport/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    cursor.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                   (date, category, amount, note))
    conn.commit()
    print("✅ Expense added successfully!\n")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses recorded yet.\n")
        return

    print("\n---- All Expenses ----")
    for row in rows:
        print(f"ID: {row[0]} | Date: {row[1]} | Category: {row[2]} | Amount: ₹{row[3]} | Note: {row[4]}")
    print()


def show_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    if total is None:
        total = 0
    print(f"\n💰 Total Expenses: ₹{total}\n")


def expenses_by_category():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses to analyze.\n")
        return

    print("\n---- Expenses by Category ----")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")
    print()


def export_to_csv():
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_csv("expenses_export.csv", index=False)
    print("📂 Data exported to expenses_export.csv\n")


# ================== VISUALIZATION FUNCTIONS ==================
def visualize_expenses():
    df = pd.read_sql_query("SELECT * FROM expenses", conn)

    if df.empty:
        print("No expenses available for visualization.\n")
        return

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # ---- Pie Chart: Spending by Category ----
    category_sum = df.groupby("category")["amount"].sum()
    category_sum.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
    plt.title("Expenses by Category")
    plt.ylabel("")  # remove default label
    plt.show()

    # ---- Line Chart: Spending Over Time ----
    daily_sum = df.groupby("date")["amount"].sum()
    daily_sum.plot(kind="line", marker="o", figsize=(8, 4))
    plt.title("Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # ---- Bar Plot: Category-wise Comparison ----
    plt.figure(figsize=(6, 4))
    sns.barplot(x="category", y="amount", data=df, estimator=sum, ci=None)
    plt.title("Category-wise Expense Comparison")
    plt.ylabel("Total Amount (₹)")
    plt.show()


# ================== MENU ==================
def menu():
    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spent")
        print("4. Expenses by Category")
        print("5. Export to CSV")
        print("6. Visualize Expenses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            expenses_by_category()
        elif choice == "5":
            export_to_csv()
        elif choice == "6":
            visualize_expenses()
        elif choice == "7":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.\n")


# ================== RUN APP ==================
if __name__ == "__main__":
    menu()
    conn.close()


# Expense-Tracker-Python
A personal expense tracker built with Python, SQLite, and data visualization.
Perfect 🚀 A **unique README.md** will make your project look professional and stand out on GitHub.
Here’s a polished one for your **Personal Expense Tracker** (till Phase 3).

---

# 💰 Personal Expense Tracker

A **Python-based Expense Tracker** with **SQLite database, CLI interface, and visualizations**.
Track, analyze, and visualize your daily spending with ease.

---

## 🔥 Features

✅ Add, view, and manage daily expenses
✅ Store data securely in **SQLite database** (persistent storage)
✅ Show total expenses
✅ Category-wise spending analysis
✅ Export all data to **CSV** (Excel/Google Sheets friendly)
✅ Beautiful **data visualizations** with Matplotlib & Seaborn:

* 📊 Pie chart → Spending by category
* 📈 Line chart → Spending over time
* 📉 Bar chart → Category comparison

---

## 🖥️ How It Works

1. Run the program in terminal:

   ```bash
   python expense_tracker.py
   ```
2. Choose from the interactive menu:

   ```
   ====== Personal Expense Tracker ======
   1. Add Expense
   2. View Expenses
   3. Show Total Spent
   4. Expenses by Category
   5. Export to CSV
   6. Visualize Expenses
   7. Exit
   ```
3. Data is saved in `expenses.db` (SQLite).
4. Exported CSV: `expenses_export.csv`.
5. Graphs pop up in new windows when you choose **Visualize Expenses**.

---

## 📂 Project Structure

```
ExpenseTracker/
│── expense_tracker.py    # Main Python script
│── expenses.db           # SQLite database (auto-created)
│── expenses_export.csv   # Exported data (on demand)
│── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2. Install Dependencies

```bash
pip install pandas matplotlib seaborn
```

### 3. Run Program

```bash
python expense_tracker.py
```

---

## 📊 Sample Visualizations

*(Generated from your expense data)*

**Pie Chart – Spending by Category**
![Pie Chart Example](images/chart.png)

**Line Chart – Spending Over Time**
![Line Chart Example](images/line.png)

**Bar Chart – Category Comparison**
![Bar Chart Example](images/bargraph.png)

---

## 🚀 Future Enhancements

* Add **GUI (Tkinter / Streamlit)** for a user-friendly interface
* Predict monthly spending with **Machine Learning**
* Set spending limits and get alerts
* Multi-user support with login system

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and improve this project.

---

## 📜 License

This project is open-source under the **MIT License**.

---

✨ Made with Python, SQLite, Matplotlib, and a pinch of ☕

---

👉 Do you want me to also prepare a **Phase 4: Streamlit GUI Web App version** of this project? (would look super cool for your AIML society demo!)

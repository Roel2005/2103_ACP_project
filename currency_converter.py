import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Load currency data from CSV
def load_currency_data():
    try:
        # Read CSV and strip spaces from column names
        currency_data = pd.read_csv("currency_rates.csv").rename(columns=lambda x: x.strip())
        print(currency_data.columns)  # Print column names to debug
        return currency_data
    except FileNotFoundError:
        messagebox.showerror("Error", "CSV file not found.")
        return pd.DataFrame()

# Convert currency
def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()

    if not amount.replace(".", "", 1).isdigit():
        messagebox.showwarning("Invalid Input", "Enter a valid number.")
        return

    amount = float(amount)

    try:
        # Fetch the exchange rates for the selected currencies
        from_rate = currency_data.loc[currency_data['Currency Name'] == from_currency, 'Exchange Rate (USD)'].values[0]
        to_rate = currency_data.loc[currency_data['Currency Name'] == to_currency, 'Exchange Rate (USD)'].values[0]
        
        converted_amount = amount * (to_rate / from_rate)
        result_var.set(f"{converted_amount:.2f} {to_currency}")
    except IndexError:
        messagebox.showerror("Error", "Currency not found.")

# Initialize GUI
root = tk.Tk()
root.title("Currency Converter")

currency_data = load_currency_data()
if currency_data.empty:
    root.quit()  # Quit if data wasn't loaded correctly

currency_names = list(currency_data['Currency Name'])

# Widgets
tk.Label(root, text="From:").grid(row=0, column=0, padx=10, pady=10)
from_currency_var = tk.StringVar(value=currency_names[0])
from_currency_combo = ttk.Combobox(root, textvariable=from_currency_var, values=currency_names, state="readonly")
from_currency_combo.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="To:").grid(row=1, column=0, padx=10, pady=10)
to_currency_var = tk.StringVar(value=currency_names[1])
to_currency_combo = ttk.Combobox(root, textvariable=to_currency_var, values=currency_names, state="readonly")
to_currency_combo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
amount_var = tk.StringVar()
tk.Entry(root, textvariable=amount_var).grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Convert", command=convert_currency).grid(row=3, column=0, columnspan=2, pady=20)

result_var = tk.StringVar(value="Result")
tk.Label(root, textvariable=result_var, font=("Arial", 16)).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

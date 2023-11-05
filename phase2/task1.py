# -*- coding: utf-8 -*-
import pandas as pd
import os

# Function for  expenses
def record_expense():
    date = input("Enter date (MM/DD/YYYY): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    data = {'Date': [date], 'Category': [category], 'Amount': [amount], 'Description': [description]}
    df = pd.DataFrame(data)
    df.to_csv('expenses.csv', mode='a', index=False, header=not os.path.exists('expenses.csv'))

# Function to generate monthly expense 
def generate_report():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    df = pd.read_csv('expenses.csv')
    filtered_df = df[(pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.month == int(month)) & (pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.year == int(year))]
    total_expenses = filtered_df['Amount'].sum()
    print(filtered_df)
    print(f"Total Expenses for {month}/{year}: ${total_expenses}")

record_expense()
generate_report()

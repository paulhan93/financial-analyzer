"""
Project Name: Financial Analyzer
Description : This application will output the confidence level of investments by conducting ratio analysis of a given company.
Author      : Paul (Ki Tae) Han
License     : MIT license
""" 

# import modules
import sqlite3
import numpy as np
import pandas as pd
from yahoofinancials import YahooFinancials
from Company import Company

# functions
def write_to_database():
    # connect to the database
    conn = sqlite3.connect('financial_data.db')

    # read the financial_data.xlsx file as a pandas dataframe
    df = pd.read_excel("financial_data.xlsx")

    # write data stored in df into a table named 'aapl' in the database (financial_data.db)
    df.to_sql('aapl', conn, if_exists='replace')

    # commit to save the changes and close connection to database
    conn.commit()
    conn.close()

def print_table_from_database(table: str):
    # connect to the database
    conn = sqlite3.connect('financial_data.db')

    # create a cursor object to execute SQL commands
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(table))

    # fetch all the rows from the result of a query
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # commit to save the changes and close connection to database
    conn.commit()
    conn.close()

def main():
    # copy the table in financial_data.xlsx into financial_data.db
    #write_to_database()

    # create a Company object
    #apple = Company('aapl')

    #tickers = ['AAPL', 'GOOG', 'C']
    tickers = 'AAPL'
    yahoo_financials = YahooFinancials(tickers, concurrent=True, max_workers=8, country="US")
    balance_sheet_data = yahoo_financials.get_financial_stmts('quarterly', 'balance')
    print(balance_sheet_data)
    

if __name__ == "__main__":
    main()
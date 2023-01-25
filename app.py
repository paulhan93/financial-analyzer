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
import pdb
from yahoofinancials import YahooFinancials
from Company import Company

#pdb.set_trace()

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
    # my investments
    # tickers = ['SPY', 'SPGP', 'GOOGL', 'MSFT', 'META', 'AAPL', 'TSLA', 'KO', 'INTC', 'HOOD', 'F', 'GM', 'NFLX', 'AMZN', 'RBLX', 'DIS', 'COTY', 'RF']

    # prompt user
    ticker = input("Enter ticker: ").upper()

    # create a Company object
    company = Company(ticker)

    # Valuation Ratios
    print(f"PE RATIO: {company.get_pe_ratio()}")
    print(f"PB RATIO: {company.get_pb_ratio()}")
    print(f"PS RATIO: {company.get_ps_ratio()}")
    print(f"EARNINGS YILED: {company.get_earnings_yield()}")
    print(f"EV-TO-EBITDA RATIO: {company.get_ev_to_ebitda()}")
    print(f"FCF YIELD: {company.get_fcf_yield()}")
    print(f"ROE: {company.get_roe()}")
    print(f"ROA: {company.get_roa()}")


if __name__ == "__main__":
    main()
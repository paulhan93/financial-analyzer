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
from Company import Company

# functions
def connect_to_database():
    # connect to the database
    conn = sqlite3.connect('financial_data.db')

    df = pd.read_excel("financial_data.xlsx")
    df.to_sql('aapl', conn, if_exists='replace')

    # create a cursor object to execute SQL commands
    cursor = conn.cursor()
    #cursor.execute('''CREATE TABLE aapl (year INTEGER PRIMARY KEY, currentAssets REAL, currentLiabilities REAL, inventory REAL)''')
    #cursor.execute("INSERT INTO aapl (year, currentAssets, currentLiabilities, inventory) VALUES (2022, 135405, 153982, 4946)")
    cursor.execute("SELECT * FROM aapl")

    # fetch all the rows from the result of a query
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # commit to save the changes and close connection to database
    conn.commit()
    conn.close()


def main():
    # connect to the sqlite database
    connect_to_database()

    #company = Company("AAPL", 135405, 153982, 4946)
    #print(company)

    #df = pd.read_excel("financial_data.xlsx")
    #print(df.head())

if __name__ == "__main__":
    main()
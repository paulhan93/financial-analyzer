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

# classes
class Company:
    def __init__(self, name, current_assets, current_liabilities, inventory):
        # constructor, initialize class variables
        self.name = name
        self.current_assets = current_assets
        self.current_liabilities = current_liabilities
        self.inventory = inventory

    def current_ratio(self):
        """
        Calculate the current ratio; current assets / current liabilities \n
        Current ratio is a measure of a company's ability to meet short-term obligations. 
        A ratio of 1 or higher is generally considered healthy.
        """
        return self.current_assets / self.current_liabilities
        
    def quick_ratio(self):
        """
        Calculate the quick ratio; (current assets - inventory) / current liabilities \n
        Quick ratio is considered to be a more conservative measure of a company's liquidity 
        than the current ratio. A ratio of 1 or higher is generally considered healthy.
        """
        return (self.current_assets - self.inventory) / self.current_liabilities

    def __str__(self):
        # return string representation of the class
        return f"""
                Company object with... 
                Name            : {self.name}
                Current ratio   : {self.current_ratio()}
                Quick ratio     : {self.quick_ratio()}
                """

# functions
def connect_to_database():
    # connect to the database
    conn = sqlite3.connect('financial_analyzer.db')

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
    company = Company("AAPL", 135405, 153982, 4946)
    print(company)

if __name__ == "__main__":
    main()
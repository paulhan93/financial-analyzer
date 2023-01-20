import sqlite3
import pandas as pd

class Company:
    def __init__(self, name):
        self.name = name
        self.df = self.read_sql()

    def read_sql(self) -> pd.DataFrame:
        # connect to the database
        conn = sqlite3.connect('financial_data.db')

        # define the SQL query
        query = 'SELECT * FROM {}'.format(self.name)
        
        # read the data into a dataframe
        df = pd.read_sql(query, conn)

        # commit to save the changes and close connection to database
        conn.commit()
        conn.close()

        return df

    def print_dataframe(self):
        print(self.df)

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

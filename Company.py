import sqlite3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials

#yahoo_financials = YahooFinancials(tickers, concurrent=True, max_workers=8, country="US")
#balance_sheet_data = yahoo_financials.get_financial_stmts('quarterly', 'balance')
#print(balance_sheet_data)

class Company:
    def __init__(self, name):
        self.name = name
        self.company = YahooFinancials(name, concurrent=True, max_workers=8, country="US")

    def __str__(self):
        # return string representation of the class
        return f"Company object ({self.name})"

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

    def plot(self):
        # Generate some data
        x = self.df["Year"].to_list()
        y = self.df["Share Price"].to_list()
        df = pd.DataFrame({'Year': x, 'Share Price': y})

        # Create a scatter plot
        sns.lineplot(data=df, x='Year', y='Share Price')

        # Show the plot
        plt.show()

    def get_pe_ratio(self):
        """Return the Price-to-Earnings (P/E) Ratio."""
        pe_ratio = self.company.get_pe_ratio()
        return pe_ratio
    
    def get_pb_ratio(self):
        """Return the Price-to-Book (P/B) Ratio."""
        market_cap = self.company.get_market_cap()
        book_value = self.company.get_book_value()
        pb_ratio = market_cap/book_value
        return pb_ratio

    def get_ps_ratio(self):
        """Return the Price-to-Sales (P/S) Ratio."""
        market_cap = self.company.get_market_cap()
        revenue = self.company.get_total_revenue()
        ps_ratio = market_cap/revenue
        return ps_ratio

    def get_earnings_yield(self):
        """Return the Earnings Yield Ratio."""
        pe_ratio = self.company.get_pe_ratio()
        earnings_yield = (pe_ratio**-1)*100
        return earnings_yield

    

    
    def calculate_current_ratio(self) -> pd.DataFrame:
        """
        Calculate the current ratio; current assets / current liabilities \n
        Current ratio is a measure of a company's ability to meet short-term obligations. 
        A ratio of 1 or higher is generally considered healthy.
        """
        x = self.df['Year']
        y = self.df['Current Assets'] / self.df['Current Liabilities']
        df = pd.DataFrame({'Year': x, 'Current Ratio': y})

        # plot
        sns.lineplot(data=df, x='Year', y='Current Ratio')
        plt.show()

        return df
        
    def calculate_quick_ratio(self) -> pd.DataFrame:
        """
        Calculate the quick ratio; (current assets - inventory) / current liabilities \n
        Quick ratio is considered to be a more conservative measure of a company's liquidity 
        than the current ratio. A ratio of 1 or higher is generally considered healthy.
        """
        x = self.df['Year']
        y = (self.df['Current Assets']-self.df['Inventory']) / self.df['Current Liabilities']
        df = pd.DataFrame({'Year': x, 'Quick Ratio': y})

        # plot
        sns.lineplot(data=df, x='Year', y='Quick Ratio')
        plt.show()

        return df

    def calculate_gross_profit_margin(self) -> pd.DataFrame:
        """
        Calculate the gross profit margin
        """
        x = self.df['Year']
        y = (self.df['Revenue']-self.df['COGS']) / self.df['Revenue']
        df = pd.DataFrame({'Year': x, 'Gross Profit Margin': y})

        # plot
        sns.lineplot(data=df, x='Year', y='Gross Profit Margin')
        plt.show()

        return df

    def calculate_net_profit_margin(self) -> pd.DataFrame:
        """
        Calculate the net profit margin
        """
        x = self.df['Year']
        y = (self.df['Revenue']-self.df['Expenses']) / self.df['Revenue']
        df = pd.DataFrame({'Year': x, 'Net Profit Margin': y})

        # plot
        sns.lineplot(data=df, x='Year', y='Net Profit Margin')
        plt.show()

        return df

    def calculate_roa(self) -> pd.DataFrame:
        """
        Calculate the return on assets
        """
        x = self.df['Year']
        y = (self.df['Revenue']-self.df['Expenses']) / self.df['Total Assets']
        df = pd.DataFrame({'Year': x, 'ROA': y})

        # plot
        sns.lineplot(data=df, x='Year', y='ROA')
        plt.show()

        return df

    def calculate_roe(self) -> pd.DataFrame:
        """
        Calculate the return on equity
        """
        x = self.df['Year']
        y = (self.df['Revenue']-self.df['Expenses']) / self.df['Shareholder\'s Equity']
        df = pd.DataFrame({'Year': x, 'ROE': y})

        # plot
        sns.lineplot(data=df, x='Year', y='ROE')
        plt.show()

        return df

    def calculate_eps(self) -> pd.DataFrame:
        """
        Calculate the earnings per share
        """
        x = self.df['Year']
        y = self.df['EPS']
        df = pd.DataFrame({'Year': x, 'EPS': y})

        # plot
        sns.lineplot(data=df, x='Year', y='EPS')
        plt.show()

        return df

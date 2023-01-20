import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

    def plot(self):
        # Generate some data
        x = self.df["Year"].to_list()
        y = self.df["Share Price"].to_list()
        df = pd.DataFrame({'Year': x, 'Share Price': y})

        # Create a scatter plot
        sns.lineplot(data=df, x='Year', y='Share Price')

        # Show the plot
        plt.show()

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

    def __str__(self):
        # return string representation of the class
        return f"""
                Company object with... 
                Name            : {self.name}
                """

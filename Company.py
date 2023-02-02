import sqlite3
import pdb
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

    ## The following methods are VALUATION RATIOS
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
        """Return the Earnings Yield."""
        pe_ratio = self.company.get_pe_ratio()
        earnings_yield = (pe_ratio**-1)*100
        return earnings_yield

    def get_ev_to_ebitda(self):
        """Return the Enterprise-to-EBITDA (Earnings before interest, taxes, depreciation, 
        and amortization) Ratio."""
        key_data = self.company.get_key_statistics_data()
        ev_to_ebitda = key_data[self.name]['enterpriseToEbitda']
        return ev_to_ebitda

    def get_fcf_yield(self):
        """Return the Free-Cash-Flow Yield."""
        financial_data = self.company.get_financial_data()
        free_cash_flow = financial_data[self.name]['freeCashflow']
        if type(free_cash_flow) != int:
            free_cash_flow = 0
        market_cap = self.company.get_market_cap()
        fcf_yield = (free_cash_flow/market_cap)*100
        return fcf_yield


    ## The following methods are PROFITABILITY RATIOS
    def get_roe(self):
        """Return the Return on Equity."""
        financial_data = self.company.get_financial_data()
        return_on_equity = financial_data[self.name]['returnOnEquity']*100
        return return_on_equity

    def get_roa(self):
        """Return the Return on Assets."""
        financial_data = self.company.get_financial_data()
        return_on_assets = financial_data[self.name]['returnOnAssets']*100
        return return_on_assets

    def get_roce(self):
        """Return the Return on Capital Employed."""
        ebit = self.company.get_ebit()
        balance_sheet = self.company.get_financial_stmts('quarterly', 'balance')

        a = list(balance_sheet)[0]
        b = list(balance_sheet[a])[0]
        c = list(balance_sheet[a][b])[0]
        d = list(c)[0]
        balance_sheet = c[d]

        total_assets = balance_sheet['totalAssets']
        current_liabilities = balance_sheet['totalCurrentLiabilities']
        return_on_capital_employed = ebit/(total_assets-current_liabilities)*100
        return return_on_capital_employed


    ## The following methods are SOLVENCY RATIOS
    #def get_debt_to_equity(self):
    #"""Return the Debt-to-Equity Ratio."""
    #de_ratio = total_liabilities/equity
    #return de_ratio

    ## The following methods are LIQUIDITY RATIOS
    #def get_current_ratio(self):
    #"""Return the Current Ratio."""
    #current_ratio = current_assets/current_liabilities
    #return current_ratio

    #def get_quick_ratio(self):
    #"""Return the Quick Ratio."""
    #quick_ratio = (current_assets-inventory)/current_liabilities
    #return quick_ratio

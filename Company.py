# Company Class File 

class Company:
    def __init__(self):
        # constructor, initialize class variables
        pass

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
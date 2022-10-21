



class Company : 
    """
    class data Company and finance indicators
    """

    
    name: str
    marketCap: float
    earnings: float
    revenue: float
    cashFlow: float
    equity: float
    liabilities: float
    assets: float



    def __init__(self, name: str, marketCap: float, earnings: float, revenue: float, cashFlow: float, equity: float, liabilities: float, assets: float):
        self.name = name
        self.marketCap =  marketCap
        self.earnings = earnings
        self.revenue = revenue
        self.cashFlow = cashFlow
        self.equity = equity
        self.liabilities = liabilities
        self.assets = assets
    
    def get_price_to_earnings(self) -> float:
        return self.marketCap / self.earnings

    def get_price_to_sales_ratio(self) -> float:
        return self.marketCap / self.revenue

    def get_price_to_cash_flow(self) -> float:
        return self.marketCap / self.cashFlow
    
    def get_price_to_book_value(self) -> float:
        return self.marketCap / self.equity
    
    def get_debt_to_equity_ratio(self) -> float:
        return self.liabilities / self.equity

    def get_return_on_shareholders_equity(self) -> float:
        return self.earnings / self.equity

    def get_return_on_assets(self) -> float:
        return self.earnings / self.assets * 100
    

    


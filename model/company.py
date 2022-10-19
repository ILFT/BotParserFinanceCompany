



class company : 
    """
    class data company and finance indicators
    """
    name: str
    marketCap: float
    earnings: float
    revenue: float
    cashFlow: float
    equity: float
    liabilities: float
    assets: float
    bookValueOfNetAssets: float
    earningsGrowRate: float



    def __init__(self, name: str, marketCap: float, earnings: float, revenue: float, cashFlow: float, equity: float, liabilities: float, assets: float, bookValueOfNetAssets: float, earningsGrowRate: float):
        self.name = name
        self.marketCap =  marketCap
        self.earnings = earnings
        self.revenue = revenue
        self.cashFlow = cashFlow
        self.equity = equity
        self.liabilities = liabilities
        self.assets = assets
        self.bookValueOfNetAssets = bookValueOfNetAssets
        self.earningsGrowRate = earningsGrowRate
    
    def getPriceToEarnings(self) -> float:
        return self.marketCap / self.earnings

    def getPriceEarningsGrowthRatio(self) -> float:
        return self.marketCap / self.earnings / self.earningsGrowRate

    def getPriceToSalesRatio(self) -> float:
        return self.marketCap / self.revenue

    def getPriceToCashFlow(self) -> float:
        return self.marketCap / self.cashFlow
    
    def getPriceToBookValue(self) -> float:
        return self.marketCap / self.bookValueOfNetAssets
    
    def getDebtToEquityRatio(self) -> float:
        return self.liabilities / self.equity

    def getReturnOnShareholdersEquity(self) -> float:
        return self.earnings / self.equity

    def getReturnOnAssets(self) -> float:
        return self.earnings / self.assets * 100
    

    


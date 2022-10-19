


class company : 
    """
    class data company and finance indicators
    """
    name: str
    priceToEarnings: float
    priceEarningsGrowthRatio: float
    priceToSalesRatio: float
    priceToCashFlow: float
    priceToBookValue: float
    debtToEquityRatio: float
    returnOnShareholdersEquity: float
    returnOnAssets: float

    def __init__(self, name: str, priceToEarnings: float, priceEarningsGrowthRatio: float, priceToSalesRatio: float, priceToCashFlow: float, priceToBookValue: float, debtToEquityRatio: float, returnOnShareholdersEquity: float, returnOnAssets: float) -> None:
        self.name = name
        self.priceToEarnings = priceToEarnings
        self.priceEarningsGrowthRatio = priceEarningsGrowthRatio
        self.priceToSalesRatio = priceToSalesRatio
        self.priceToCashFlow = priceToCashFlow
        self.priceToBookValue = priceToBookValue
        self.debtToEquityRatio = debtToEquityRatio
        self.returnOnShareholdersEquity = returnOnShareholdersEquity
        self.returnOnAssets = returnOnAssets


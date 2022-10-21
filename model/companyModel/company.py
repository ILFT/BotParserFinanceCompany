from indicatorEnum import IndicatorEnum



class Company : 
    """
    class data Company and finance indicators
    """

    
    name: str
    indicators: IndicatorEnum
    """
    marketCap: float | None
    earnings: float | None
    revenue: float | None
    equity: float | None
    liabilities: float | None
    assets: float | None
    """


    def __init__(self, name: str, indicators: IndicatorEnum):
        self.name = name
        self.indicators = indicators
       
    def get_price_to_earnings(self) -> float | str:
        if self.indicators.marketCap.get_value_indicator() == None | self.earnings == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.marketCap / self.earnings

    """
    def __init__(self, name: str, marketCap: float | None, earnings: float | None, revenue: float | None, equity: float | None, liabilities: float | None, assets: float | None):
        self.name = name
        self.marketCap =  marketCap
        self.earnings = earnings
        self.revenue = revenue
        self.equity = equity
        self.liabilities = liabilities
        self.assets = assets
    
    def get_price_to_earnings(self) -> float | str:
        if self.marketCap == None | self.earnings == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.marketCap / self.earnings

    def get_price_to_sales_ratio(self) -> float | str:
        if self.marketCap == None | self.revenue == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.marketCap / self.revenue
    
    def get_price_to_book_value(self) -> float | str:
        if self.marketCap == None | self.equity == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.marketCap / self.equity
    
    def get_debt_to_equity_ratio(self) -> float | str:
        if self.liabilities == None | self.equity == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.liabilities / self.equity

    def get_return_on_shareholders_equity(self) -> float | str:
        if self.earnings == None | self.equity == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.earnings / self.equity

    def get_return_on_assets(self) -> float | str:
        if self.earnings == None | self.assets == None:
            return 'Одного из показателей для рассчета нет'
        else:
            return self.earnings / self.assets * 100
    """

    


from pickle import FALSE
from indicatorEnum import IndicatorEnum



class Company : 
    """
    class data Company and finance indicators
    """

    
    name: str
    info: str
    #indicators: IndicatorEnum
    
    marketCap: float | None
    earnings: float | None
    revenue: float | None
    equity: float | None
    liabilities: float | None
    assets: float | None
    


    def __init__(self, name: str, info: str, indicators: IndicatorEnum):
        self.name = name
        self.info = name
        self.__set_indicator(indicators)
        #self.indicators = indicators
       

    """
    def __init__(self, name: str, marketCap: float | None, earnings: float | None, revenue: float | None, equity: float | None, liabilities: float | None, assets: float | None):
        self.name = name
        self.marketCap =  marketCap
        self.earnings = earnings
        self.revenue = revenue
        self.equity = equity
        self.liabilities = liabilities
        self.assets = assets
    """

    def update_indicator(self, indicators: IndicatorEnum):
        self.__set_indicator(indicators)


    def __set_indicator(self, indicators: IndicatorEnum):

        self.marketCap =  indicators.marketCap.value.get_value_indicator()
        self.earnings = indicators.earnings.value.get_value_indicator()
        self.revenue = indicators.revenue.value.get_value_indicator()
        self.equity = indicators.equity.value.get_value_indicator()
        self.liabilities = indicators.liabilities.value.get_value_indicator()
        self.assets = indicators.assets.value.get_value_indicator()


    def get_info_company(self) -> str:
        return self.info

    def get_price_to_earnings(self) -> float | None:
        if self.__check_indicator(self.marketCap, self.earnings):
            return self.marketCap / self.earnings
        else:
            return None

    def get_price_to_sales_ratio(self) -> float | None:
        if self.__check_indicator(self.marketCap, self.revenue):
            return self.marketCap / self.revenue
        else:
            return None
    
    def get_price_to_book_value(self) -> float | None:
        if self.__check_indicator(self.marketCap, self.equity):
            return self.marketCap / self.equity
        else:
            return None
    
    def get_debt_to_equity_ratio(self) -> float | None:
        if self.__check_indicator(self.liabilities, self.equity):
            return self.liabilities / self.equity
        else:
            return None

    def get_return_on_shareholders_equity(self) -> float | None:
        if self.__check_indicator(self.earnings, self.equity):
            return self.earnings / self.equity
        else:
            return None

    def get_return_on_assets(self) -> float | None:
        if self.__check_indicator(self.earnings, self.assets):
            return self.earnings / self.assets * 100
        else:
            return None

    def __check_indicator(*arg) -> bool:
        for indicator in arg:
            if indicator == None:
                return False
        return True
    

    def get_all_indicators(self) -> str:
        return f'P/E = {self.get_price_to_earnings():.2f} \nP/S = {self.get_price_to_sales_ratio():.2f}\nP/B = {self.get_price_to_book_value():.2f}\nD/E = {self.get_debt_to_equity_ratio():.2f}\nROE = {self.get_return_on_shareholders_equity():.2f}\nROA = {self.get_return_on_assets():.2f}'

    

    


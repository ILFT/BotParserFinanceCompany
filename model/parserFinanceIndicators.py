
from model.company import Company


FIRST_STOCK_MARKET = "https://www.moex.com"
SECOND_STOCK_MARKET = "https://tradingview.com"

class ParserFinanceIndicators :
    """
    class parsing finance indicators of company
    """


    def parsing(cls, nameCompany: str):
        """
        the main function for parsing the company
        """
        pass

    def __parsing_with_moex(cls, nameCompany: str) -> Company:
        """
        the function parsing from the site https://www.moex.com
        """
        pass

    def __parsing_with_trading_view(cls, nameCompany: str) -> Company:
        """
        the function parsing from the site https://tradingview.com
        """
        pass

    def __create_company(cls, textIndicator: str) -> Company:
        """
        the function of create new object class company
        """
        pass

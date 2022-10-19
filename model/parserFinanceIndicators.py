
from model.company import Company


FIRST_STOCK_MARKET = "https://www.moex.com"
SECOND_STOCK_MARKET = "https://tradingview.com"

class ParserFinanceIndicators :
    """
    class parsing finance indicators of company
    """


    def parsing(nameCompany: str):
        """
        the main function for parsing the company
        """
        pass

    def __parsing_with_moex(nameCompany: str) -> Company:
        """
        the function parsing from the site https://www.moex.com
        """
        pass

    def __parsing_with_trading_view(nameCompany: str) -> Company:
        """
        the function parsing from the site https://tradingview.com
        """
        pass

    def __create_company(textIndicator: str) -> Company:
        """
        the function of create new object class company
        """
        pass

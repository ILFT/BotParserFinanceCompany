
from model.company import company


FIRST_STOCK_MARKET = "https://www.moex.com"
SECOND_STOCK_MARKET = "https://tradingview.com"

class parserFinanceIndicators :
    """
    class parsing finance indicators of company
    """
    def parsing(nameCompany: str):
        """
        the main function for parsing the company
        """
        pass

    def __parsingWithMoex(nameCompany: str) -> company:
        """
        the function parsing from the site https://www.moex.com
        """
        pass

    def __parsingWithTradingview(nameCompany: str) -> company:
        """
        the function parsing from the site https://tradingview.com
        """
        pass

    def __createCompany(textIndicator: str) -> company:
        """
        the function of create new object class company
        """
        pass

from urllib import request
from bs4 import BeautifulSoup 
import re 
import requests

from companyModel.company import Company
from companyModel.indicatorEnum import IndicatorEnum


FIRST_STOCK_MARKET = "https://www.moex.com"
SECOND_STOCK_MARKET = "https://tradingview.com"
THRID_STOCK_MARKET = "https://smart-lab.ru"
#/q/GAZP/f/y

class ParserFinanceIndicators :
    """
    class parsing finance indicators of company
    """

    @classmethod
    def parsing(cls, nameCompany: str) -> Company | None:
        """
        the main function for parsing the company
        """

        
        return cls.__parsing_with_smart_lab(nameCompany)

    @classmethod
    def __parsing_with_moex(cls, nameCompany: str) -> Company:
        """
        the function parsing from the site https://www.moex.com
        """
        pass

    @classmethod
    def __parsing_with_trading_view(cls, nameCompany: str) -> Company:
        """
        the function parsing from the site https://tradingview.com
        """
        pass
    
    @classmethod
    def __parsing_with_smart_lab(cls, nameCompany: str) -> Company | None:
        response = requests.get(f'https://smart-lab.ru/q/{nameCompany}/f')
        if response.status_code == 200:
            return Company(nameCompany, nameCompany, cls.__get_indicator_enum(response))
        else:
            return None

    @classmethod
    def __get_indicator_enum(cls, response: requests.Response) -> IndicatorEnum:
        for indicators  in IndicatorEnum:
                indicators.value.set_value_indicator(cls.__get_indicator_concrete(indicators.value.get_name_for_parsing(), response))
        return IndicatorEnum

    @classmethod
    def __get_indicator_concrete(cls, nameIndicator: re.Pattern, response: requests.Response) -> float | None:
        try:
            return float(BeautifulSoup(response.text, 'html.parser').find('tr', field = nameIndicator).findChildren('td')[5].text.replace(' ', ''))
        except:
            return None



    @classmethod
    def __create_company(cls, textIndicator: str) -> Company:
        """
        the function of create new object class company
        """
        pass



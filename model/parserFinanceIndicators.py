from urllib import request
from bs4 import BeautifulSoup 
import re 
import requests

from model.companyModel.company import Company
from model.companyModel.indicatorEnum import IndicatorEnum


#FIRST_STOCK_MARKET = "https://www.moex.com"
#SECOND_STOCK_MARKET = "https://tradingview.com"
#THRID_STOCK_MARKET = "https://smart-lab.ru"

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


    """
    def __parsing_with_moex(cls, nameCompany: str) -> Company:
        pass

    def __parsing_with_trading_view(cls, nameCompany: str) -> Company:
        pass

    def __create_company(cls, textIndicator: str) -> Company:
        pass
    """


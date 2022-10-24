
from bs4 import BeautifulSoup 
import re 
import requests


if __name__ == "__main__":

    nameCompany = 'tcsg'
    response  = requests.get(f'https://smart-lab.ru/q/{nameCompany}/f')
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    marketCap = soup.find('tr', field = re.compile('\S*market_cap')).findChildren('td')[5].text
    print(marketCap)

    earnings = soup.find('tr', field = re.compile('\S*net_income')).findChildren('td')[5].text
    print(earnings)

    revenue = soup.find('tr', field = re.compile('\S*revenue|net_operating_income')).findChildren('td')[5].text
    print(revenue)

    equity = soup.find('tr', field = re.compile('\S*cash')).findChildren('td')[5].text
    print(equity)

    liabilities = soup.find('tr', field = re.compile('\S*debt')).findChildren('td')[5].text
    print(liabilities)

    assets = soup.find('tr', field = re.compile('\S*assets')).findChildren('td')[5].text
    print(assets)
    
    k = None
    t = None
    if k == None or t == None:
        print('ssss')
    

    #kkk = IndicatorEnum
    #print(kkk)
    #kkk.marketCap.value.set_value_indicator(123)
    #print(kkk.marketCap.value.get_name_for_parsing())
    #print(kkk.marketCap.value.get_value_indicator())
    #indOneEnum = IndicatorCompany(re.compile('\S*assets'), None)
    #print(indOneEnum.get_name_for_parsing())
    #print(indOneEnum.get_value_indicator())


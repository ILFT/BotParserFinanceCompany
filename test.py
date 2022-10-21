
from bs4 import BeautifulSoup 
import re 
import requests


if __name__ == "__main__":

    response  = requests.get("https://smart-lab.ru/q/tcsg/f")
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    marketCap = soup.find('tr', field = re.compile('\S*market_cap')).findChildren('td')[5].text
    print(marketCap)

    earnings = soup.find('tr', field = re.compile('\S*net_income')).findChildren('td')[5].text
    print(earnings)

    #revenue = soup.find('tr', field = re.compile('\S*revenue')).findChildren('td')[5].text
    #print(revenue)

    #cashFlow = soup.find('tr', field = re.compile('\S*ocf')).findChildren('td')[5].text
    #print(cashFlow)

    equity = soup.find('tr', field = re.compile('\S*cash')).findChildren('td')[5].text
    print(equity)

    liabilities = soup.find('tr', field = re.compile('\S*debt')).findChildren('td')[5].text
    print(liabilities)

    assets = soup.find('tr', field = re.compile('\S*assets')).findChildren('td')[5].text
    print(assets)

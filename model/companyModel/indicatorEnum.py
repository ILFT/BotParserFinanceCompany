from enum import Enum
from indicator import IndicatorCompany
import re 

class IndicatorEnum(Enum):
    marketCap  = IndicatorCompany(re.compile('\S*market_cap'), None)
    earnings = IndicatorCompany(re.compile('\S*net_income'), None)
    revenue = IndicatorCompany(re.compile('\S*revenue|net_operating_income'), None)
    equity = IndicatorCompany(re.compile('\S*cash'), None)
    liabilities = IndicatorCompany(re.compile('\S*debt'), None)
    assets = IndicatorCompany(re.compile('\S*assets'), None)

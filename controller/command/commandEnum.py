from enum import Enum
from indicatorsViewCommand import IndicatorsViewCommand
from searchCompanyCommand import SearchCompanyCommand


class CommandEnum(Enum):
    search = SearchCompanyCommand()
    showIndicator = IndicatorsViewCommand()
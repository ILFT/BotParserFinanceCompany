import re 

class IndicatorCompany:


    nameForParsing: re.Pattern
    """
    name regex on website for parsing
    """
    valueIndicator: float | None

    def __init__(self, nameForParsing: re.Pattern, valueIndicator: float | None):
        self.nameForParsing = nameForParsing
        self.valueIndicator = valueIndicator

    def set_name_for_parsing(self, nameForParsing: re.Pattern):
        self.nameForParsing = nameForParsing

    def get_name_for_parsing(self) -> re.Pattern:
        return self.nameForParsing

    def set_value_indicator(self, valueIndicator: float | None):
        self.valueIndicator = valueIndicator

    def get_value_indicator(self) -> float | None:
        return self.valueIndicator

from model.companyModel.company import Company
from model.parserFinanceIndicators import ParserFinanceIndicators


class ModelApp :
    """
    pattern mvc model 
    """


    nowCompany: Company

    def __init__(self):
        self.nowCompany = None

    def set_company(self, nameCompany: Company):
        self.nowCompany = ParserFinanceIndicators.parsing(nameCompany)

    def indicators_view(self):
        pass
        
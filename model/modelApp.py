
from companyModel.company import Company
from parserFinanceIndicators import ParserFinanceIndicators
from view.observerModel import ObserverModelApp


class ModelApp :
    """
    pattern mvc model 
    """


    nowCompany: Company | None
    observer: ObserverModelApp

    def __init__(self, observer: ObserverModelApp):
        self.nowCompany = None
        self.observer = observer

    def search_company(self, nameCompany: str):
        self.nowCompany = ParserFinanceIndicators.parsing(nameCompany)
        if self.nowCompany  == None:
            self.observer.show_company_serched('company not found')
        else:
            self.observer.show_company_serched(self.nowCompany.get_info_company())

    def indicators_view(self):
        indicator = self.nowCompany.get_price_to_earnings()
        if indicator == None:
            self.observer.show_company_indicator('one or more indicators are missing')
        else:
            self.observer.show_company_indicator(indicator)
        
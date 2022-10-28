from command.ICommand import ICommand
from model. modelApp import ModelApp


class SearchCompanyCommand(ICommand) :
    
    
    def execute(self, modelConcrete: ModelApp, *arg) -> str:
        return modelConcrete.search_company(*arg)
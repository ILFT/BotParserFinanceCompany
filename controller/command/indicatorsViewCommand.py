from command.ICommand import ICommand
from model. modelApp import ModelApp


class IndicatorsViewCommand(ICommand) :
    
    
    def execute(self, modelConcrete: ModelApp, *arg):
        modelConcrete.indicators_view()
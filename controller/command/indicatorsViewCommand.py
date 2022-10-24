from command.ICommand import ICommand
from model. modelApp import ModelApp


class IndicatorsViewCommand(ICommand) :
    
    
    def execute(cls, modelConcrete: ModelApp):
        modelConcrete.indicators_view()
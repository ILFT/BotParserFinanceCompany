from command.commandEnum import CommandEnum
from model.modelApp import ModelApp
from view.observerModel import ObserverModel


class ControllerApp :
    """
    pattern mvc Controller 
    """

    model: ModelApp

    def __init__(self, observerModel: ObserverModel):
        self.model = ModelApp(observerModel)
    
    def execute_command(self, nameCommand: str, *arg):
        CommandEnum[nameCommand].value.execute(self.model, arg)
    #.execute()

from command.commandEnum import CommandEnum
from model.modelApp import ModelApp
#from view.observerModel import ObserverModel


class ControllerApp :
    """
    pattern mvc Controller 
    """

    model: ModelApp

    """
    def __init__(self, observerModel: ObserverModel):
        self.model = ModelApp(observerModel)
    """
    def __init__(self):
        self.model = ModelApp()
    
    def execute_command(self, nameCommand: str, *arg) -> str:
        return CommandEnum[nameCommand].value.execute(self.model, *arg)

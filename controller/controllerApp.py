from command.commandEnum import CommandEnum
from model.modelApp import ModelApp


class ControllerApp :
    """
    pattern mvc Controller 
    """

    model: ModelApp

    def __init__(self):
        self.model = ModelApp()
    
    def execute_command(self, nameCommand: str, *arg) -> str:
        return CommandEnum[nameCommand].value.execute(self.model, *arg)

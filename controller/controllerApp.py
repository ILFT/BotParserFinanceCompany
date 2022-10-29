from command.commandEnum import CommandEnum
from model import modelApp


class ControllerApp :
    """
    pattern mvc Controller 
    """

    model: modelApp

    
    def execute_command(self, nameCommand: str, *arg) -> str:
        return CommandEnum[nameCommand].value.execute(self.model, arg)
    #.execute()

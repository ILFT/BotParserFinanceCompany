from command.commandEnum import CommandEnum
from model import modelApp


class Controller :
    """
    pattern mvc Controller 
    """

    model: modelApp

    
    def execute_command(self, message: str, *arg):
        CommandEnum[message].value.execute(self.model, arg)
    #.execute()

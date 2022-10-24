
from model import modelApp

from controller.command.ICommand import ICommand


class Controller :
    """
    pattern mvc Controller 
    """

    model: modelApp
    
    def execute_command(self, command: ICommand):
        command.execute()

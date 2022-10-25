
from model import modelApp

from controller.command.ICommand import ICommand


class Controller :
    """
    pattern mvc Controller 
    """

    model: modelApp


    #TODO create normal controller  pattern command not perfect need pattern mb states
    
    def execute_command(self, command: ICommand):
        command.execute()

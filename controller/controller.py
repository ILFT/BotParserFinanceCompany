


from controller.command.ICommand import ICommand


class Controller :
    """
    pattern mvc Controller 
    """

    
    def execute_command(command: ICommand):
        command.execute()

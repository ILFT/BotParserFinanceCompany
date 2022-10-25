from model. modelApp import ModelApp


class ICommand :
   """
   pattern command interface
   """

   
   def execute(self, modelConcrete: ModelApp, *arg):
    pass 

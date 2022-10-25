from model. modelApp import ModelApp


class ICommand :
   """
   pattern command interface
   """

   
   def execute(cls, modelConcrete: ModelApp):
    pass 

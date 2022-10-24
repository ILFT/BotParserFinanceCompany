from model. modelApp import ModelApp


class ICommand :
   """
   pattern command interface
   """

   """
   Надопрпрдумать как сделать команды и привязать  события о  подписка должна быть через контророллер необходим универсальный метод для подпискии на события

   а вот как лучше сджлеать команды если нужны параметры типа  именид ак  их передавать в модель через контроллер 
   """

   
   def execute(cls, modelConcrete: ModelApp):
    pass 

from asyncore import dispatcher
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.builtin import Command


from controllerApp import ControllerApp
from view.observerModel import ObserverModel


class ControllerTelegram:

    bot: Bot
    dispatcher: Dispatcher
    controller: ControllerApp
    

    def __init__(self, tokenApi: str, observerModel: ObserverModel):
        self.bot = Bot(token=tokenApi)
        self.dispatcher = Dispatcher(self.bot)
        self.controller = ControllerApp(observerModel)
        self.__set_handler_dispatcher()

    def start_bot(self):
        executor.start_polling(self.dispatcher, skip_updates=True)

    def stop_bot(self):
        self.bot.stop_poll()

    def __set_handler_dispatcher(self):
        self.dispatcher.register_message_handler(self.search_comppny_finance, commands = ['search'])



    async def search_comppny_finance(self, message: types.Message, command: Command.CommandObj):
        await self.controller.execute_command(command.command, command.args)
        

from controller.controllerApp import ControllerApp
from discord.ext.commands import Bot
from discord.ext.commands import Context
from discord.ext import commands
from discord import Intents


from view.viewDiscord import ViewDiscord



class ControllerDiscord():


    controller: ControllerApp
    bot: Bot
    observer: ViewDiscord

    def __init__(self, prefix: str):
        #super().__init__(command_prefix = prefix, intents = Intents.all())
        self.controller = ControllerApp()
        self.bot = Bot(command_prefix = prefix, intents = Intents.all())
        self.observer = ViewDiscord()
        self.__set_handler_bot()

    """
    @bot.event
    async def on_ready():
        print('BOT connected')
    """

    
    def search(self):
        @self.bot.command(name = 'search')
        async def search(ctx: Context, name: str):
            print(ctx.author)
            print(ctx.message.content)
            print(name)
            await ctx.send('fff')
            #await self.observer.send_search_company(ctx, self.controller.execute_command(ctx.command, name))


    def start_bot(self, token: str):
        self.bot.run(token)

    def stop_bot(self):
        self.bot.close()
    
    def __set_handler_bot(self):
        self.search()
    
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
        self.controller = ControllerApp()
        self.bot = Bot(command_prefix = prefix, intents = Intents.all())
        self.observer = ViewDiscord()
        self.__set_handler_bot()


    """
    @bot.event
    async def on_ready():
        print('BOT connected')
    """
    

    @commands.command()
    #@self.bot.command()
    async def search(ctx: Context, arg):
        #print(ctx.author)
        #print(ctx.message.content)
        print(arg)
        await ctx.send(arg)
        #await self.observer.send_search_company(ctx, self.controller.execute_command(ctx.command, arg))

    
    def start_bot(self, token: str):
        self.bot.run(token)

    def stop_bot(self):
        self.bot.close()
    
    def __set_handler_bot(self):
        self.bot.add_command(self.search)
    
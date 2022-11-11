from discord.ext.commands import Cog
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import Context



class CogDiscord(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    
    @commands.command()
    #@self.bot.command()
    async def search(self, ctx: Context, *arg):
        #print(ctx.author)
        #print(ctx.message.content)
        print(arg)
        #await ctx.send(ctx.command.name)
        await self.observer.send_search_company(ctx, self.controller.execute_command(ctx.command, arg))

def setup(bot: Bot) -> None:
    bot.add_cog(CogDiscord(bot))
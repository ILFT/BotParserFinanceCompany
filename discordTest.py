import discord

from discord.ext.commands import Bot
from discord.ext.commands import Context
from discord.ext import commands

bot = Bot(command_prefix = '!', intents = discord.Intents.all())


@bot.event
async def on_ready():
    print('BOT connected')

class ff():
    
    @commands.command(name = 'search')
    async def search_company(self, ctx: Context, arg):
        await ctx.send(arg)

bot.add_command(ff().search_company)
bot.run('')


 
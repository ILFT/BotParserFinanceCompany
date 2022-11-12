from discord.ext.commands import Context



class ViewDiscord:

    async def send_search_company(self, ctx: Context, message):
        await ctx.send(message)
import random, discord, random, json
from discord.ext import commands
from datetime import datetime as date
from colorama import Fore, Style


class Moderator(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.warningLocation = "misc/warns.json"
    
    def __printTerminal(self, ctx: commands.Context, command: str) -> None:
        print(f'{Fore.LIGHTMAGENTA_EX}{date.now().strftime("%x")} {date.now().strftime("%X")} \
            {Fore.BLUE}{ctx.message.author.name} {Style.RESET_ALL} \t \
            {Fore.GREEN} {command} {Style.RESET_ALL}')
    
    @commands.command(name="clear", help="Clear a number of messages from the chat", hidden=True)
    @commands.has_role('Manager')
    async def clear(self, ctx, amount:int=None): # Set default value as None
        self.__printTerminal(ctx, "clear")
        if amount == None:
            await ctx.channel.purge(limit=50)
        else:
            await ctx.channel.purge(limit=amount)
    
    
async def setup(bot):
    await bot.add_cog(Moderator(bot))

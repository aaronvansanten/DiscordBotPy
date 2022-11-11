import multiprocessing, os
from discord.ext import commands
from datetime import datetime as date

from colorama import Fore, Style

class store(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    def __printTerminal(self, ctx: commands.Context, command: str) -> None:
        print(f'{Fore.LIGHTMAGENTA_EX}{date.now().strftime("%x")}-{date.now().strftime("%X")}\t\t{Fore.BLUE}{ctx.message.author.name} {Style.RESET_ALL} \
            {Fore.GREEN}{command} {Style.RESET_ALL}')

    @commands.command(name = "karen", help="I WANT TO SPEAK TO A MANAGER")
    async def karen(self, ctx):
        self.__printTerminal(ctx, "karen")
        # Call the manager for the user
        await ctx.send(f"{ctx.author.name} wants to see the <@&974027415493935194>")


async def setup(bot: commands.bot):
    await bot.add_cog(store(bot))

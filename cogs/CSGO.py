import random
from discord.ext import commands
from datetime import datetime as date

from colorama import Fore, Style

class CSGO(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    def __printTerminal(self, ctx: commands.Context, command: str) -> None:
        print(f'{Fore.LIGHTMAGENTA_EX}{date.now().strftime("%x")} {date.now().strftime("%X")} \
            {Fore.BLUE}{ctx.message.author.name} {Style.RESET_ALL} \t \
            {Fore.GREEN} {command} {Style.RESET_ALL}')

    
    @commands.command(name="IGL", help="chooses a random IGL from a given list")
    async def IGL(self, ctx, message, *args):
        print(f"{message.author.name} has invoked ")
        await ctx.send(f"{message.author.name} chose: {random.choice(args)} as the In Game Leader")


async def setup(bot):
    await bot.add_cog(CSGO(bot))

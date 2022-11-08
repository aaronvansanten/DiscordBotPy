import multiprocessing, os
from discord.ext import commands
from datetime import datetime as date

from colorama import Fore, Style

class misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    def __printTerminal(self, ctx: commands.Context, command: str) -> None:
        print(f'{Fore.LIGHTMAGENTA_EX}{date.now().strftime("%x")}-{date.now().strftime("%X")}\t\t{Fore.BLUE}{ctx.message.author.name} {Style.RESET_ALL} \
            {Fore.GREEN}{command} {Style.RESET_ALL}')

    @commands.command(name="ping", help="returns Pong on succes", aliases=['p'])
    async def ping(self, ctx: commands.Context):
        self.__printTerminal(ctx, "ping")
        await ctx.send("pong")

    @commands.command(name="serverusage", help="Show the server usage")
    async def serverusage(self, ctx) -> None:
        self.__printTerminal(ctx, "serverusage")
        cpu_count = multiprocessing.cpu_count()
        one, five, fifteen = os.getloadavg()
        load_percentage = int(five / cpu_count * 100)
        await ctx.send(f'Server load is at {load_percentage}%')


async def setup(bot: commands.bot):
    await bot.add_cog(misc(bot))

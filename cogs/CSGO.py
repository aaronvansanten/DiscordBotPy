import random, discord, sys
from discord.ext import commands
from datetime import datetime as date
from colorama import Fore, Style

from misc.gangpaden import gangpaden


class CSGO(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    def __printTerminal(self, ctx: commands.Context, command: str) -> None:
        print(f'{Fore.LIGHTMAGENTA_EX}{date.now().strftime("%x")} {date.now().strftime("%X")} \
            {Fore.BLUE}{ctx.message.author.name} {Style.RESET_ALL} \t \
            {Fore.GREEN} {command} {Style.RESET_ALL}')

    
    @commands.command(name="igl", 
                      help="chooses a random IGL from a given list", 
                      aliases=["IGL"])
    async def IGL(self, ctx, *args):
        self.__printTerminal(ctx, "IGL")
        await ctx.send(f"{ctx.message.author.name} chose: {random.choice(args)} as the In Game Leader")
    
    @commands.command(name="jumbo", help="Get the enhanced jumbo logos for your game")
    async def jumbo(self, ctx, colour="default"):
        base_dir = './misc/Images/'
        self.__printTerminal(ctx, "Jumbo")
        if (colour == "blue" or colour == "b"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Blue.jpg'))
        elif (colour == "green" or colour == "g"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Green.jpg'))
        elif (colour == "orange" or colour == "o"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Orange.jpg'))
        elif (colour == "purple" or colour == "p"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Purple.jpg'))
        elif (colour == "yellow" or colour == "y"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Yellow.jpg'))
        elif (colour == "default"):
            await ctx.channel.send(file=discord.File(base_dir + 'Jumbo Original.jpg'))

    @commands.command(name="gangpad", help="Get a random gangpad for your game")
    async def gangpad(self, ctx):
        await ctx.send(random.choice(gangpaden))

async def setup(bot):
    await bot.add_cog(CSGO(bot))

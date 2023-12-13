import random, discord, random, json
from discord.ext import commands
from datetime import datetime as date
from colorama import Fore, Style
 
class Warns(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.warningLocation = "misc/warns.json"

    """ Warning system"""
    @commands.command(name="warn", help="Warn a player for some reason", aliases=["w"])
    @commands.has_role('Manager')
    async def warn(self, ctx, player: discord.Member = None, reason:str = "no reason"):
        self.__printTerminal(ctx, "warn")
        if (player == None): 
            await ctx.send("Who do you want to warn?")
            return

        if (player.name == "Larry2.1"):
            await ctx.send("How dare you assume the bot can get a warning!")
            await ctx.send(f"Larry has warned {ctx.author.mention} for treason")
            return

        with open(self.warningLocation, 'r') as warns:
            warnings = json.load(warns)
            num_of_warnings = warnings.get(str(player.name), 0) + 1
            await ctx.send(f"{ctx.author.mention} has warned {player.mention} for {reason}.")
            await ctx.send(f"{player.mention} now has {num_of_warnings} warnings.")
        
        with open(self.warningLocation, 'w') as warns:
            json.dump(warnings, warns)

    @commands.command(name="remove_warn", help="Remove a warning from a player", aliases=["rw"])
    @commands.has_role('Manager')
    async def remove_warn(self, ctx, player: discord.Member = None):
        self.__printTerminal(ctx, "remove warning")
        if (player == None): 
            await ctx.send("Who do you want to remove a warn from?")
            return

        with open(self.warningLocation, 'r') as warns:
            warnings = json.load(warns)
            num_of_warnings = warnings.get(str(player.name), 0) - 1
            await ctx.send(f"{ctx.author.mention} has removed a warning from {player.mention}.")
            await ctx.send(f"{player.mention} now has {num_of_warnings} warnings.")
        
        with open(self.warningLocation, 'w') as warns:
            json.dump(warnings, warns)

    @commands.command(name="check_warning", help="Check the numbers of warnings a player has", aliases=["cw"])
    async def warns_check(self, ctx, player: discord.Member = None):
        if (player == None): player = ctx.author
        self.__printTerminal(ctx, "check warnings")
        if (player.name == "Larry2.1"):
            await ctx.send("How dare you assume the bot can get a warning!")
            return

        with open(self.warningLocation, 'r') as warns:
            warnings = json.load(warns)
            num_of_warns = warnings.get(str(player.mention), 0)
            await ctx.send(f"{player.mention} has {num_of_warns} warnings now")
import os,  discord
from dotenv import load_dotenv
from discord.ext import commands

from Moderator.badWords import words, check_words

# Retrieve the token from the .env file
load_dotenv()
TOKEN = os.getenv('discord-token')

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)


# Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(intents= intents, command_prefix='!')

""" Define the on_ready event. This event is triggered when the bot is first ready """
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

""" Event handeler for not havind the correct permissions."""
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

# Define the command for the bots
# ---------------------------------------------------------------
@bot.command(name="ping", help=": returns Pong on succes")
# @commands.has_role('admin')
async def ping(ctx, message) -> None:
    print(f"user {message.author.name} issued the command: ping")
    await ctx.send("Pong")



# Run the bot
bot.run(TOKEN)
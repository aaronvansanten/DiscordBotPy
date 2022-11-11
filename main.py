import os,  discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands

from colorama import Fore, Style
from misc.badWords import badWords

# Retrieve the token from the .env file
load_dotenv()
TOKEN = os.getenv('discord-token')

# Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(intents= intents, command_prefix='!')

""" Define the on_ready event. This event is triggered when the bot is first ready """
@bot.event
async def on_ready():
    print(f'{Fore.BLUE}{bot.user.name}{Style.RESET_ALL} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.channel.send(f"Welcome {member.mention} to the discord server.")

# @bot.event
# async def on_message(message):
#     print("A message has been sent" + message.content)
#     for word in badWords:
#         if (message.content.lower() == word):
#             await message.delete()  
#             await message.channel.send("Please dont use that word here!")

""" Event handeler for not havind the correct permissions."""
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

async def main():
    # Initialize all the modules
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    
    # Start the bot
    await bot.start(TOKEN, reconnect=True)
    

if __name__ == '__main__':
    asyncio.run(main())
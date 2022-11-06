import os, random, discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('discord-token')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
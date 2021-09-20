#!/usr/bin/env python3
from os import getenv
from dotenv import load_dotenv

import discord

load_dotenv()

TOKEN = getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is ready !')

client.run(TOKEN)


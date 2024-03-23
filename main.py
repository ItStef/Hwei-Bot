import discord
from discord.ext import commands

import asyncio

import os
from dotenv import load_dotenv

load_dotenv() #Load the .env file

#Create the bot
bot = commands.Bot(command_prefix='.', intents = discord.Intents.all(), help_command=None)

#Event for when the bot is ready
@bot.event
async def on_ready():
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='You int...'))
    except Exception as e:
        print(e)
    print('Hwei online')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

#Starts the bot and runs the load function
async def main():
    await load()
    await bot.start(os.getenv('BOT_TOKEN'))


asyncio.run(main())
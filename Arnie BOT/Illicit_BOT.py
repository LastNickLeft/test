import discord
from discord.ext import commands
from discord.ext.commands import Bot
from config import bot_version, bot_author, bot_author_id, bot_info_prefix, arnie_command_array, random_status, banned_words, local_ip, allowed_roles, bot_token, starting_status
from colorama import Fore, Back, Style
import glob, io, sys
import os
import asyncio  
import time 
import datetime
import asyncio
import random
import subprocess
import sqlite3
bot = commands.Bot(command_prefix=bot_info_prefix)
bot.remove_command('help')
start_time = time.time()    
@bot.event
async def on_ready():
    print (Fore.GREEN + "OK: Arnie BOT Release 1 - Bailey#7708") 
    print (Fore.GREEN + "OK: I am running on " + bot.user.name)
    print (Fore.GREEN + "OK: With the ID: " + bot.user.id)
    print (Fore.GREEN + "OK: Discord Version: " + discord.__version__)
    print (Fore.GREEN + "OK: Cog Setting Up") 
    print (Fore.GREEN + "OK: Cog Connected") 
    print (Fore.GREEN + "OK: BOT Started")
    print (Fore.GREEN + "OK: Commands setting up")
    print (Fore.GREEN + "OK: Commands setup")
    await bot.change_presence(game=discord.Game(name=starting_status, status=discord.Status("online"))) 
    print (Fore.GREEN + "OK: Starting status has been set to " + starting_status)
    print (Fore.GREEN + "OK: Resetting print colours")
    print (Fore.GREEN + "OK: All Done, BOT Online.")
    print (Style.RESET_ALL)
    extensions = ["data.cogs.basescript"]
    for cog in extensions:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(Fore.GREEN + str(e))

bot.run(bot_token)


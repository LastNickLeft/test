import discord
from discord.ext import commands
import os

class ping():
    def __init___(self, bot):
        self.client = bot

    @commands.command(pass_context = True, no_pm = True)
    async def ping(self, ctx, address:str):
        if address == "127.0.0.1":
            await bot.say ("You cannot ping the server's local IP address.")
        elif address == "localhost":
            await bot.say("You cannot ping the server's local IP address.")
        else:
            response = os.system("ping -c 1 " + address)
            if response == 0:
                print(address + " is Online!")
                await bot.say("IP is Online!")
            else:
                print(address + " is Offline!")
                await bot.say("IP is Offline")
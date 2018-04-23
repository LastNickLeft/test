import discord
from discord.ext import commands
import asyncio
import random
import datetime
import time
from config import bot_version
from config import bot_author
from config import bot_master
from config import bot_author_id
from config import bot_info_prefix
from config import arnie_command_array
from config import random_status
from config import banned_words
from colorama import Fore, Back, Style
import os
leaveroom = [] #discord.utils.get(discord.server.channels, name='bot-spam', type=ChannelType.text)
try:
    class verify:
            def __init__(self, bot):
                self.bot = bot
        
            async def on_message(self, message):
                if message.content.startswith('Nigger'):
                    await self.bot.purge_from(message.channel, limit=2)
                    await self.bot.add_roles(message.author, discord.utils.get(message.server.roles, name="MUTED"))
                    
            async def on_message(self, message):
                if message.content.startswith('-invite'):
                    invite = await self.bot.create_invite(destination = message.channel, max_uses = 1)
                    await self.bot.send_message(message.channel, invite)

            @commands.command(pass_context=True)
            async def example(self):
                await self.bot.send_message(discord.Object(id = "436948795641561101"), "Test")

            @commands.command(pass_context=True)
            async def addrole(self, ctx, user: discord.Member, *, role):
                roles1 = [role.name.replace('@', '@\u200b') for role in user.roles]

                if role in roles1:
                    embed = discord.Embed(description = "You already have this role!", color = 0xFF0000)
                    return await self.bot.say(embed = embed)
                    
                if role in allowed_roles:
                    await self.bot.add_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
                    embed = discord.Embed(description = ("Added %s to  **%s** " % (user.mention, role)), color= 0xFF0000)
                    await self.bot.say(embed = embed)

            @commands.command(pass_context=True, no_pm=True)
            async def echo(self, ctx, message:str):
                if "Cool Kids" in [role.name for role in ctx.message.author.roles]:
                    if message in banned_words:
                        embed = discord.Embed(description = "You cannot use language like that!", color = 0xF00000)
                        await self.bot.say(embed = embed)
                    else: 
                        embed = discord.Embed(description = " " + message, color = 0xF00000)
                        await self.bot.say(embed = embed)
                else:
                    embed = discord.Embed(description = "You are not a BOT Master.", color = 0xF00000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context=True, no_pm=True, aliases=['remrl'])
            async def removerole(self, ctx, user: discord.Member, *, role):
                GNHRole = discord.utils.get(ctx.message.server.roles, name = "Mods")
                if any(i in [role.name for role in ctx.message.author.roles] for i in ("Management", "Developer", "Head of Staff")):
                    await self.bot.remove_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
                    embed = discord.Embed(description = ("Removed %s from **%s**" % (user.mention, role)), color = 0xFF0000)
                    await self.bot.say(embed = embed)
                else:
                    embed = discord.Embed(description = ":x:  You are not part of the cool guys!", color = 0xFF0000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context = True, no_pm = True, aliases=['b'])
            async def ban(self, ctx, *, member : discord.Member = None):
                if any(i in [role.name for role in ctx.message.author.roles] for i in ("Cool Kids", "Perms")):
                    if not member:
                        embed = discord.Embed(description = ctx.message.author.mention + ", you did not specify a user to ban! :x:", color = 0xF00000)
                        return await self.bot.say(embed = embed)
                    else:
                        await self.bot.ban(member)

                    embed = discord.Embed(description = "**%s** has been banned."%member.name, color = 0xF00000)
                    print (Fore.GREEN + "OK: Member banned: " + member.name)
                    return await self.bot.say(embed = embed)
                else:
                    embed = discord.Embed(description = "You are not part of the cool guys!", color = 0xF00000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context=True)
            async def reboot(self, ctx):
                if "Cool Kids" in [role.name for role in ctx.message.author.roles]:
                    await self.bot.change_presence(game=discord.Game(name="Rebooting"), status=discord.Status("offline")) 
                    embed = discord.Embed(description = "BOT is shutting down and rebooting.", color = 0xF00000)
                    await self.bot.say(embed = embed)
                    print (Fore.GREEN + "OK: BOT Rebooting")
                    File = "reboot.sh"
                    os.system("./" + File)
                else:
                    embed = discord.Embed(description = "You are not a BOT Master", color = 0xFF0000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context=True)
            async def status(self, ctx, presence:str, status:str):
                if "Cool Kids" in [role.name for role in ctx.message.author.roles]:
                    if status == "Online":
                        status = "online"
                    if status == "Idle":
                        status = "idle"
                    if status == "Offline":
                        status = "offline"
                    if status in banned_words:
                        embed = discord.Embed(description= "Please do not use that kind of language for our BOT status.", color = 0xF00000)
                    await self.bot.change_presence(game=discord.Game(name="" + presence), status=discord.Status("" + status)) 
                    embed = discord.Embed(description = "The BOT's Presence has been changed to " + presence + " - The BOT's Status has been changed to " + status, color = 0xF00000)
                    print (Fore.GREEN + "OK: BOT Status changed to: " + presence)
                    await self.bot.say(embed=embed)
                else:
                    embed = discord.Embed(description = "You are not a BOT Master.", color = 0xF00000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context=True)
            async def randomstatus(self, ctx):
                await self.bot.change_presence(game=discord.Game(name="" + random.choice (random_status)), status= discord.Status("online")) 
                embed = discord.Embed(description= "The BOT's Status has been randomized.", color = 0xF00000)
                print (Fore.GREEN + "OK: BOT Status randomised")
                await self.bot.say(embed=embed)

            @commands.command(pass_context = True)
            async def arnie(self, ctx):
                embed = discord.Embed(color = 0xFF0000)
                embed.set_image (url = random.choice (arnie_command_array))
                embed.set_footer(text="OMG ARNIE!!! 2018")
                await self.bot.say(":heart: :cat: OMG HERE YOU GO THIS IS <33333" + ctx.message.author.mention)
                await self.bot.say(embed=embed)
 

            @commands.command(pass_context=True)
            async def banlist(self, ctx):
                if any(i in [role.name for role in ctx.message.author.roles] for i in ("Cool Kids", "Perms")):
                    x = await self.bot.get_bans(ctx.message.server)
                    x = '\n'.join([y.name for y in x])
                    embed = discord.Embed(title = "Banned Members", description = x, color = 0xFF0000)
                    return await self.bot.say(embed = embed)
                else:
                    embed = discord.Embed(description = "You are not part of the cool guys!", color = 0xFF0000)
                    return await self.bot.say(embed = embed)

            @commands.command(pass_context = True)
            async def send(self, ctx, member : discord.Member, *, message):
                        return await self.bot.send_message(member, embed=discord.Embed(description="Message from **" + ctx.message.author.mention + "**: " + message, color = 0xFF0000))

            @commands.command(pass_context=True)
            async def kick(self, ctx, *, member : discord.Member = None):
                if any (i in [role.name for role in ctx.message.author.roles] for i in ("Cool Kids", "Perms")):
                    if not member:
                        return await self.bot.say(ctx.message.author.mention + "Specify a user to kick!")
                    else:
                        await self.bot.kick(member)
                        embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
                        return await self.bot.say(embed = embed)
                        print (Fore.GREEN + "OK: Member kicked: " + member.name)
                else:
                        embed = discord.Embed(description = "You are not part of the cool guys!", color = 0xF00000)
                        return await self.bot.say(embed = embed)

            @commands.command(pass_context = True, no_pm = True)
            async def mute(self, ctx, *, member : discord.Member):
                if not ctx.message.author.server_permissions.mute_members:
                    embed = discord.Embed(description = ":x: You are not part of the cool guys!", color = 0xF00000)
                else:
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = False
                    await self.bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
                    await self.bot.say("**%s** has been muted!"%member.mention)

            @commands.command(pass_context = True, description='Unmutes the muted members.', no_pm = True)
            async def unmute(self, ctx, *, member : discord.Member):
                if not ctx.message.author.server_permissions.mute_members:
                    embed = discord.Embed(description = ":x: You are not part of the cool guys!", color = 0xF00000)
                else:
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = True
                    await self.bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
                    await self.bot.say("**%s** has been unmuted!"%member.mention)

            @commands.command(pass_context = True)
            async def time(self, ctx):
                date = datetime.datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M %p")
                embed = discord.Embed(color = 0xFF0000)
                embed.add_field(name="Bot's System Date & Time", value=date, inline=False)
                await self.bot.say(embed=embed)
                
            @commands.command(pass_context=True)
            async def mika(self, ctx):
                embed = discord.Embed(description = "Well then i am Arnie BOT but jems has a cute dog aswell, here is his website, http://www.mika.org.uk " + ctx.message.author.mention, color = 0xFF0000)
                await self.bot.say(embed = embed)

            @commands.command(pass_context=True)
            async def kill(self, ctx):
                #if any(i in [role.name for role in ctx.message.author.roles] for i in ("BOT Master")):
                if "Cool Kids" in [role.name for role in ctx.message.author.roles]:
                    await self.bot.change_presence(game=discord.Game(name="Shutting Down"), status=discord.Status("offline")) 
                    await self.bot.say("Bed time for arnie :cat:, goodnight, 'BOT SHUTTING DOWN' " + ctx.message.author.mention )
                    await self.bot.logout()
                else: 
                    await self.bot.say("You are not a BOT Master, " + ctx.message.author.mention)

            @commands.command(pass_context=True)
            async def info(self, ctx, user: discord.Member):
                embed = discord.Embed(title="{}'s info ".format(user.name), description="Statistics", color=0x00c7ff)
                embed.add_field(name="Name", value=user.name)
                embed.add_field(name="Role", value= user.top_role)
                embed.set_thumbnail(url=user.avatar_url)
                await self.bot.say(embed=embed)

            @commands.command(pass_context=True)
            async def help(self, ctx):
                embed = discord.Embed(title="Commands", description="All commands for the Illicit BOT", color=0x00c7ff)
                embed.add_field(name="Command List", value="\n -website\n-help\n-kill\n-embed\n-info @Fred#0001\n-setrole\n-ping\n-delete\n-kick\n-ban\n-addrole\n-removerole\n-connect\n-time\n-author\n-reboot", inline=True)
                embed.set_footer(text="ARNIEEEE 2018", icon_url="")
                await self.bot.send_message(ctx.message.author, embed = embed)
                embed = discord.Embed(title="Commands", description="I just PM'd you.", color=0x00c7ff)
                await self.bot.say(embed=embed)

            @commands.command()
            async def serverinfotest(self):
                embed = discord.Embed(description="Statistics", color=0x00ff00)
                embed.set_author(name="Bailey")
                embed.add_field(name="Server name", value=message.server)
                embed.add_field(name="ID", value= server.id)
                embed.add_field(name="Roles", value=len(server.roles))
                embed.add_field(name="Members", value=len(server.members))  
                embed.add_field(name="Server Region", value=get_region_string(discord.ServerRegion))
                await self.bot.say(embed=embed)

            @commands.command(pass_context = True, no_pm = True)
            async def author(self, ctx):
                embed = discord.Embed(title = "WHO MADE ME?:", description = "Arnie Master: **\n" + bot_master + "Arnie BOT Author: **" + bot_author + "** \nSay **!help** for commands.", color = 0xF00000)
                return await self.bot.say(embed = embed)

            @commands.command(pass_context = True, no_pm = True)
            async def botinfo(self, ctx):
                embed = discord.Embed(title = "Illicit BOT Info:", description = "Author Name: **{}**\n BOT ID: **{}**\n BOT Prefix **{}**\n Time when BOT started: **{}**".format(bot_author,bot_author_id,bot_info_prefix,start_time), color = 0xF00000)
                return await self.bot.say(embed = embed)

            @commands.command(pass_context=True)
            async def delete(self, ctx, number):
                if "Cool Kids" in [role.name for role in ctx.message.author.roles]:
                    mgs = []
                    number = int(number) 
                    async for x in self.bot.logs_from(ctx.message.channel, limit = number):
                        mgs.append(x)
                    await self.bot.delete_messages(mgs)
                    embed = discord.Embed(description = "You have successfully deleted {} messages".format(msg), color = 0x58368)
                else:
                    embed = discord.Embed(description = "You are not a BOT Master", color = 0xF00000)
                    await self.bot.say(embed=embed)

            @commands.command(pass_context=True)
            async def embed(self, ctx):
                embed = discord.Embed(title="Test", description="Lolwot", color=0x00ff00)
                embed.set_footer(text="Illicit Gaming 2018", icon_url="https://i.gyazo.com/f34816e2f9bae52cd7f015b50c2c7390.png")
                embed.set_author(name="Bailey")
                await self.bot.say(embed=embed)

            @commands.command(pass_context=True, no_pm = True)
            async def connect(self, ctx):
                if self.bot.is_voice_connected(ctx.message.server):
                    return await self.bot.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
                else:   
                    author = ctx.message.author
                    voice_channel = author.voice_channel
                    vc = await self.bot.join_voice_channel(voice_channel)

            @commands.command(pass_context = True, no_pm = True)
            async def disconnect(self, ctx):
                for x in self.bot.voice_clients:
                    if(x.server == ctx.message.server):
                        return await self.bot.disconnect()

    def setup(bot):
        bot.add_cog(verify(bot))

except TypeError:
    print ("Test")
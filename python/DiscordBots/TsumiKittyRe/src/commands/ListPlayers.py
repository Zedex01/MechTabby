""" List Players Command
 - Lists the # of players on the server
"""

import discord, os, subprocess
from discord.ext import commands
from util.Server import Server
from util.Config import Config

class ListPlayers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cfg = Config()
        self.srv = Server()
               
    @commands.command(name="list_players", description="List the # of players currently on the server")
    async def stopServer(self, ctx):
        
        #Sends plaintext output of command as a normal message
        await ctx.send(self.srv.sendCmd("list"))
                   
async def setup(bot):
    await bot.add_cog(ListPlayers(bot))
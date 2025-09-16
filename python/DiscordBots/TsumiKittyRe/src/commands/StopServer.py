""" Stop Server Command """
import discord
from discord.ext import commands
from util.Config import Config
from util.Server import Server

import os, subprocess

class StopServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cfg = Config()
        self.srv = Server()
               
    @commands.command(name="stop_server", description="Stops the server")
    @commands.is_owner()
    async def stopServer(self, ctx):
        
        await ctx.send(self.srv.sendCmd("stop"))

                   
async def setup(bot):
    await bot.add_cog(StopServer(bot))
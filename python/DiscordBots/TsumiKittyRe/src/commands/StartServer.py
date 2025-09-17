""" Start Server Command """
import discord, logging
from discord.ext import commands
from util.Config import Config

import os, subprocess

logger = logging.getLogger(__name__)


class StartServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cfg = Config()
               
    @commands.command(name="start_server", description="Boots the server")
    async def startServer(self, ctx):
        logger.info(f"{ctx.author} requested server startup")
        
        
        # === Configs ===   
        self.start_path = self.cfg.get_str("Setup", "start_path")
        
        if not os.path.isfile(self.start_path):
            raise FileNotFoundError(f"{self.start_path} does not exist!")
            
        try:
            await ctx.send("Starting server now, please be patient.")
            process = subprocess.Popen([self.start_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

        except subprocess.CalledProcessError as e:
            await ctx.send("ERR: Server Launch Failed")
            print(f"Error running BAT file: {e}")
        
                   
async def setup(bot):
    await bot.add_cog(StartServer(bot))
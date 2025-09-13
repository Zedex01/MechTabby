""" Check Server Status Commads """
import discord, subprocess, os
from discord.ext import commands
import configparser as cp

class GetServerStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        #config reader setup
        CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "resources", "config", "config.ini")
        config = cp.ConfigParser()
        config.read(CONFIG_FILE)
        self.SERVER_NAME = config['Setup']['server_name']
        
    @commands.command(name="server", description="Checks if the server is currently online.")
    async def getServerStatus(self, ctx):
        #Get Server data:
        cur_IP = subprocess.check_output("curl ifconfig.me", shell = True, universal_newlines=True)

        try:
            StatReturn = subprocess.check_output('tasklist | find "javaw"', shell=True, universal_newlines=True)
        except:
            StatReturn = ''
        

        if StatReturn == '':
            Status = "OFFLINE"
            color = discord.Color.red()

        else:
            Status = "ONLINE"
            color = discord.Color.green()

        embed = discord.Embed(title='Server Details', description=None, color=color)
        embed.add_field(name='Name', value=self.SERVER_NAME, inline=True)
        embed.add_field(name='IP', value= cur_IP, inline=True)
        embed.add_field(name='Status', value= Status, inline=True)
        await ctx.send(embed=embed)
        

async def setup(bot):
    await bot.add_cog(GetServerStatus(bot))
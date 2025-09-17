""" Locate """
import discord, logging
from discord.ext import commands
from util.Linker import Linker
from util.Server import Server

logger = logging.getLogger(__name__)

class Locate(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.lnkr = Linker()
        self.srv = Server()
        
    @commands.command(name="locate", description="locates a player in world")
    @commands.guild_only()
    async def Locate(self, ctx, member: discord.Member = None) -> None:
        
        #Can be used on either self or another member of the discord
        player = member or ctx.author
        
        #Get the players ID from the json file
        playerName = self.lnkr.getMinecraftName(player.id)
        
        #Catch if it is not a linked account
        if playerName == None:
            await ctx.send(f"{player.display_name}'s account is not linked.")
            return
     
        """
        #Check if the server is online
        if not self.srv.isRunning():
            await ctx.send("The server is currently offline, unable to locate.")
            return
            
            
        #check if player is online:
        if not self.srv.isPlayerOnline():
            await ctx.send(f"Currently {player.display_name} is not online.")
            return
            
        """    
        
        #Send a request for players coords to the server
        #coords = self.srv.sendCmd(f"data get entity {playerName} Pos")
        
       
        coords = [100, 45, 678]
        
        embed = discord.Embed(
            title=f"📍 **{playerName}**",
             color=discord.Color.blue()
        )
        embed.add_field(name="Coordinates: ",value=coords, inline=True)

        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Locate(bot))
        
            